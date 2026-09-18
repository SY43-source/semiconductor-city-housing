"""[EN] Data audit with a local LLM (Ollama Gemma) over NAVER complex records (SS III.2).
#§3.2 자료 교차검증 — 로컬 LLM(Ollama Gemma) 으로 네이버 JSON 단지 레코드를 감사.

배경: 본 연구는 세 차례 '명목 분류' 오류를 겪었다(임대 판별·지역 판별·공급주체 판별).
      단지명 같은 이름 필드를 실측 필드의 대용으로 쓴 것이 원인이었다.
      사람이 22,368세대·29,014 평형 레코드를 일일이 볼 수 없으므로, 규칙으로 잡히지 않는
      '이름과 수치의 불일치'를 로컬 LLM 에 감사시킨다.

과제 A — 규격 정합성: 평형 레코드의 (전용면적, 방수, 단지명)이 서로 모순되는 건 탐지.
과제 B — 공급주체 판별: 단지명만 보고 공공/민간 공급 여부를 판정하게 한 뒤,
         LH·GH 입주자모집공고로 확인한 정답과 대조하여 '이름 기반 판별'의 실제 정확도를 측정.

실행 요건: 로컬 Ollama + Gemma 계열 모델. 큐 클라이언트 경로는 GEMMA_CLIENT_DIR,
          모델 태그는 OLLAMA_MODEL 환경변수로 지정한다(아래 참조).
출력: analysis/38_llm_crosscheck.json  (본문 §3.2 에 인용)
"""
import os as _os; REPO = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import json, sqlite3, sys, re
# 로컬 Ollama 큐 클라이언트(gemma_queue_client.py)가 있는 디렉터리
_client_dir = _os.environ.get('GEMMA_CLIENT_DIR')
if not _client_dir:
    sys.exit('GEMMA_CLIENT_DIR 환경변수에 gemma_queue_client.py 경로를 지정하세요.')
sys.path.insert(0, _client_dir)
from gemma_queue_client import GemmaQueueClient

# 원 분석은 로컬 Ollama 의 Gemma 계열 모델로 수행했다.
MODEL = _os.environ.get('OLLAMA_MODEL', 'gemma3:latest')
DB = _os.environ.get('INVENTORY_DB', '/Users/Shared/seoyeon_inventory_master.sqlite')
cli = GemmaQueueClient(caller='seoyeon_38_llm_crosscheck', priority=3)

def ask(system, user, timeout=180):
    r = cli.submit({'model': MODEL, 'stream': False,
                    'messages': [{'role':'system','content':system},
                                 {'role':'user','content':user}],
                    'options': {'temperature': 0}}, timeout=timeout)
    if not r.get('success'): return None
    return r['result']['message']['content']

def jparse(t):
    if not t: return None
    m = re.search(r'\{.*\}|\[.*\]', t, re.S)
    try: return json.loads(m.group(0)) if m else None
    except Exception: return None

con = sqlite3.connect(DB)

# ── 과제 A: 규격 정합성 감사 ──
rows = con.execute("""SELECT c.name, p.exclusive_area_m2, p.room_count, p.units_of_same_area
                      FROM complexes c JOIN pyeong_types p ON c.complex_number=p.complex_number
                      WHERE c.bjd_code LIKE '41220%' AND p.units_of_same_area>0
                        AND p.exclusive_area_m2 IS NOT NULL AND p.room_count IS NOT NULL""").fetchall()
SYS_A = ("You audit Korean apartment unit records. For each record you get the complex name, "
         "exclusive floor area in m2, and the number of bedrooms. Flag a record as inconsistent "
         "only if the area and bedroom count cannot plausibly coexist in Korean apartment practice "
         "(e.g. under 30 m2 with 3+ bedrooms, or over 100 m2 with 1 bedroom). "
         "Answer strictly as JSON: {\"flagged\":[{\"i\":<index>,\"why\":\"<short>\"}]} with no prose.")
flagged, checked = [], 0
for s in range(0, len(rows), 60):
    chunk = rows[s:s+60]
    lines = [f"{i}. area={r[1]}m2 rooms={r[2]} name={r[0]}" for i, r in enumerate(chunk)]
    out = jparse(ask(SYS_A, "\n".join(lines)))
    checked += len(chunk)
    if out and isinstance(out.get('flagged'), list):
        for f in out['flagged']:
            try: rec = chunk[int(f['i'])]
            except Exception: continue
            flagged.append({'name': rec[0], 'area': rec[1], 'rooms': rec[2],
                            'units': rec[3], 'why': str(f.get('why',''))[:120]})
    print(f"  [A] {checked}/{len(rows)} 검사 · 지적 {len(flagged)}건", flush=True)

# ── 과제 B: 이름만으로 공급주체 판별 → 공고 확인 정답과 대조 ──
TRUTH = {  # LH·GH 입주자모집공고/준공자료로 확인한 정답
 '평택고덕신동아파밀리에엔에이치에프7단지':'public', '고덕국제신도시르플로랑':'public',
 '고덕국제신도시헤스티블':'public', '고덕국제신도시양우내안애':'public',
 '어울림스퀘어(민간임대)':'private', '다해브':'unknown',
 '고덕하늘채시그니처':'private', '고덕국제신도시금호어울림':'private',
 '고덕국제신도시제일풍경채':'private', '고덕국제신도시파라곤':'private',
 '고덕국제신도시포레스트자이':'private', '힐스테이트고덕스카이시티':'private',
 '고덕국제신도시아너스':'private', '신안인스빌시그니처':'private',
}
SYS_B = ("You classify Korean apartment complexes by who supplied them, using ONLY the complex name. "
         "Answer 'public' if the name indicates public rental supply (LH, GH, happy housing, national/permanent rental, "
         "public rental REIT), otherwise 'private'. "
         "Answer strictly as JSON: {\"answers\":{\"<name>\":\"public|private\"}} with no prose.")
names = [n for n, v in TRUTH.items() if v != 'unknown']
out = jparse(ask(SYS_B, "\n".join(names)))
ans = (out or {}).get('answers', {})
hit = [n for n in names if ans.get(n) == TRUTH[n]]
miss = [{'name': n, 'llm': ans.get(n), 'truth': TRUTH[n]} for n in names if ans.get(n) != TRUTH[n]]

res = {'task_A': {'records_checked': checked, 'flagged': len(flagged), 'examples': flagged[:10]},
       'task_B': {'n': len(names), 'correct': len(hit),
                  'accuracy_pct': round(len(hit)/len(names)*100, 1) if names else None,
                  'errors': miss},
       'model': MODEL, 'via': 'gemma_queue_daemon'}
out_path = REPO + '/analysis/38_llm_crosscheck.json'
json.dump(res, open(out_path, 'w'), ensure_ascii=False, indent=2)
print(json.dumps(res['task_A'] | {'examples': '...'}, ensure_ascii=False))
print(json.dumps(res['task_B'], ensure_ascii=False))
print("✅", out_path)
con.close()
