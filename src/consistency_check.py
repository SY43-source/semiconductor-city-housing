"""[EN] Checks that documents derived from the manuscript still agree with it.

정본 = paper/source/MANUSCRIPT_v12.md (+ _EN). 나머지(README·EVIDENCE_MAP·LIMITATIONS·
figures/README)는 파생물이다. 원고가 개정될 때 파생물 갱신이 누락되는 사고가 반복돼
(부록의 v10 참조 · 영문판 한계 (5) · 근거지도의 철회 수치) 기계로 잡는다.

종료 코드
  0  통과
  1  불일치 발견 — 고쳐야 한다
  2  **검사 불가** (정본에서 기준값을 못 뽑음 등). 통과 아님.

사용
  python3.11 src/consistency_check.py          # 검사
  python3.11 src/consistency_check.py --self-test   # 고장주입 자가검증
"""
import os, re, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KO   = 'paper/source/MANUSCRIPT_v12.md'
EN   = 'paper/source/MANUSCRIPT_v12_EN.md'
DERIVED = ['README.md', 'EVIDENCE_MAP.md', 'LIMITATIONS.md', 'REPRODUCE.md', 'figures/README.md']

# 정본에 반드시 있어야 하는 핵심 사실. 정본에서 못 찾으면 검사 불가(exit 2).
FACTS = [
    ('public_rental_units', r'7,720',  '공공임대 세대수'),
    ('public_rental_share', r'25\.7%', '공공임대 비중'),
    ('total_stock',         r'30,088', '총 재고'),
    ('rental_total',        r'8,380',  '임대 계'),
    ('supply_units',        r'22,368', '민간 분양 재고'),
    ('pir',                 r'16\.1',  'PIR'),
    ('rent_share',          r'73\.4%', '월세 비중'),
    ('size_band_share',     r'55\.3%', '단일 규격군 집중'),
    ('sales_records',       r'253,255','매매 실거래'),
    ('lease_records',       r'156,330','전월세 실거래'),
]

# 철회된 값 — 현행 문서에 나오면 안 된다. 다만 '기각/철회/참고' 맥락은 허용.
WITHDRAWN = [
    (r'4,640',   '공공임대 구값(v9~v10)'),
    (r'28,597',  '총 재고 구값'),
    (r'30,078',  '총 재고 구값(v11)'),
    (r'7,321',   '공공임대 구값(v11)'),
    (r'2,249',   '민간임대 구값'),
]
ALLOW = re.compile(r'기각|철회|withdrawn|rejected|superseded|구값|\(참고\)|archive')

# 현행 문서가 가리키면 안 되는 구판 링크
STALE_LINK = re.compile(r'MANUSCRIPT_v(?:[1-9]|10|11)[._]|APPENDIX_v(?:[1-9]|10|11)[._]')

def read(rel):
    p = os.path.join(REPO, rel)
    return open(p, encoding='utf-8').read() if os.path.exists(p) else None

def main():
    problems, blocked = [], []

    ko, en = read(KO), read(EN)
    if ko is None: blocked.append(f'정본 없음: {KO}')
    if en is None: blocked.append(f'영문 정본 없음: {EN}')
    if blocked:
        for b in blocked: print(f'⛔ {b}')
        print('\n검사 불가 — 통과가 아니다.'); return 2

    # ── 1) 정본에서 기준값을 실제로 뽑았는가 (불변식: 0건이면 검사 불가)
    anchored = []
    for key, pat, label in FACTS:
        if re.search(pat, ko): anchored.append((key, pat, label))
        else: blocked.append(f'정본에서 기준값 못 찾음: {label} /{pat}/')
    if blocked:
        for b in blocked: print(f'⛔ {b}')
        print(f'\n검사 불가 — 정본 구조가 바뀌었을 수 있다. FACTS 를 갱신하라.'); return 2
    if not anchored:
        print('⛔ 기준값 0건 — 검사 불가'); return 2

    # ── 2) 한·영 정본이 같은 수치를 말하는가
    for key, pat, label in anchored:
        if not re.search(pat, en):
            problems.append(f'[판 불일치] 영문 정본에 {label} /{pat}/ 없음')

    # ── 3) 파생 문서에 철회된 값이 살아 있는가
    for rel in DERIVED:
        txt = read(rel)
        if txt is None:
            blocked.append(f'파생 문서 없음: {rel}'); continue
        for i, line in enumerate(txt.split('\n'), 1):
            if ALLOW.search(line): continue
            for pat, label in WITHDRAWN:
                if re.search(pat, line):
                    problems.append(f'[철회값] {rel}:{i} — {label} /{pat}/  → {line.strip()[:70]}')
            if STALE_LINK.search(line):
                problems.append(f'[구판 링크] {rel}:{i} — {line.strip()[:70]}')

    # ── 4) 원고가 참조하는 그림이 실제로 있는가
    for rel in (KO, EN):
        base = os.path.dirname(os.path.join(REPO, rel))
        for img in re.findall(r'!\[[^\]]*\]\(([^)]+)\)', read(rel)):
            if not os.path.exists(os.path.join(base, img)):
                problems.append(f'[그림 없음] {rel} → {img}')

    # ── 5) 문서 내 상대 링크가 유효한가
    for rel in DERIVED:
        txt = read(rel)
        if txt is None: continue
        base = os.path.dirname(os.path.join(REPO, rel))
        for link in re.findall(r'\]\(([^)#][^)]*)\)', txt):
            if link.startswith('http'): continue
            if not os.path.exists(os.path.join(base, link)):
                problems.append(f'[깨진 링크] {rel} → {link}')

    if blocked:
        for b in blocked: print(f'⛔ {b}')
        print('\n검사 불가 — 통과가 아니다.'); return 2

    if problems:
        print(f'❌ 불일치 {len(problems)}건\n')
        for p in problems: print('  ' + p)
        return 1

    print(f'✅ 통과 — 기준값 {len(anchored)}개, 파생 문서 {len(DERIVED)}개 대조')
    return 0

def self_test():
    """고장주입 — 일부러 틀린 상태를 만들어 검사기가 잡는지 본다."""
    import tempfile, shutil
    global REPO
    ok = True
    real = REPO
    cases = [
        ('철회값 주입', 'EVIDENCE_MAP.md', lambda s: s + '\n| 공공임대 | 4,640세대 |\n', 1),
        ('구판 링크 주입', 'README.md', lambda s: s + '\n[old](MANUSCRIPT_v10.md)\n', 1),
        ('깨진 링크 주입', 'README.md', lambda s: s + '\n[x](does/not/exist.md)\n', 1),
        ('정본 훼손', 'paper/source/MANUSCRIPT_v12.md', lambda s: s.replace('7,720', 'XXX'), 2),
        ('영문판 수치 누락', 'paper/source/MANUSCRIPT_v12_EN.md', lambda s: s.replace('30,088', 'XXX'), 1),
    ]
    for name, target, mutate, expect in cases:
        tmp = tempfile.mkdtemp()
        dst = os.path.join(tmp, 'repo')
        shutil.copytree(real, dst, ignore=shutil.ignore_patterns('.git', '*.png', '*.pdf', '__pycache__'))
        p = os.path.join(dst, target)
        open(p, 'w', encoding='utf-8').write(mutate(open(p, encoding='utf-8').read()))
        REPO = dst
        import io as _io, contextlib
        buf = _io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = main()
        REPO = real
        shutil.rmtree(tmp)
        mark = '✅' if rc == expect else '❌'
        if rc != expect: ok = False
        print(f'  {mark} {name}: 기대 exit {expect}, 실제 {rc}')
    print('\n✅ 자가검증 통과 — 검사기가 고장을 잡는다' if ok else '\n❌ 자가검증 실패')
    return 0 if ok else 1

if __name__ == '__main__':
    sys.exit(self_test() if '--self-test' in sys.argv else main())
