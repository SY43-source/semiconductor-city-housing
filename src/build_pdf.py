"""[EN] Manuscript Markdown to PDF (journal-style layout) via markdown + WeasyPrint.
#원고 MD → PDF (「국토계획」 양식 근사). python3.11 markdown → HTML → weasyprint CLI.
한글판: AppleMyungjo(본문 명조)+Apple SD Gothic Neo(제목·표). 영문판: Georgia+Helvetica.
사용: python3.11 src/build_pdf.py [v12|v12en|appendix|appendixen|v11|v11en|v10|v10en|v9|v9en|v8|v8en|v7|v7en|all]
     (기본 all = 현행 정본 v12 한/영 + 부록 한/영)
영문판은 JAABE(Journal of Asian Architecture and Building Engineering) 2단 조판 준용(lang='en2').
⚠️ 미게재 원고이므로 러닝 푸터에 실제 저널명·권호·페이지를 넣지 않는다(중립 표기).
"""
import os, re, sys, subprocess, markdown
import os as _os
BASE=_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
ANALYSIS=f'{BASE}/analysis'
# 정본 = v12 (+ APPENDIX_v12). v7~v11 은 롤백점으로 유지(명시 지정 시에만 빌드).
# lang: 'ko'=국토계획 준용 1단 / 'en2'=JAABE 준용 2단 / 'en'=기존 1단 영문(구판용)
JOBS={'v12':('MANUSCRIPT_v12','ko'),'v12en':('MANUSCRIPT_v12_EN','en2'),
      'appendix':('APPENDIX_v12','ko'),'appendixen':('APPENDIX_v12_EN','en2'),
      'v11':('MANUSCRIPT_v11','ko'),'v11en':('MANUSCRIPT_v11_EN','en'),
      'v10':('MANUSCRIPT_v10','ko'),'v10en':('MANUSCRIPT_v10_EN','en'),
      'v9':('MANUSCRIPT_v9','ko'),'v9en':('MANUSCRIPT_v9_EN','en'),
      'v8':('MANUSCRIPT_v8','ko'),'v8en':('MANUSCRIPT_v8_EN','en'),
      'v7':('MANUSCRIPT_v7','ko'),'v7en':('MANUSCRIPT_v7_EN','en'),
      'en':('MANUSCRIPT_v12_EN','en2')}
# 정본은 안정 파일명으로 출력한다(원서·인용 링크가 판올림에 깨지지 않도록)
OUT={'MANUSCRIPT_v12':'Semiconductor-City-Housing-KO','MANUSCRIPT_v12_EN':'Semiconductor-City-Housing-EN',
     'APPENDIX_v12':'Appendix-KO','APPENDIX_v12_EN':'Appendix-EN'}
ALL=['v12','v12en','appendix','appendixen']
TARGET=(sys.argv[1] if len(sys.argv)>1 else 'all')
SEL=[JOBS[k] for k in ALL] if TARGET=='all' else [JOBS[TARGET]]

JAABE = """
/* ── JAABE(Journal of Asian Architecture and Building Engineering) 준용 2단 조판 ──
   ⚠️ 미게재 학생 원고이므로 러닝 푸터는 실제 저널명·권호 대신 중립 표기를 쓴다. */
@page { size: A4; margin: 22mm 18mm 20mm 18mm;
  @bottom-left  { content: "Unpublished student manuscript"; font-family:%(head)s; font-size:7.5pt; color:#888; }
  @bottom-right { content: counter(page) " / " counter(pages); font-family:%(head)s; font-size:7.5pt; color:#888; } }
* { box-sizing: border-box; }
body { font-family:%(body)s; font-size:9.2pt; line-height:1.42; color:#111;
       column-count:2; column-gap:7mm; text-align:justify; hyphens:auto; }
/* 표제부·초록은 단 전체 폭 */
h1, h1 + h3, .fullwidth { column-span: all; }
h1 { font-family:%(body)s; font-size:13pt; font-weight:700; text-align:center;
     margin:0 0 6pt; line-height:1.32; }
/* 저자명·소속 블록: 표제 아래 중앙 (JAABE 배치) */
/* 번호 붙은 정렬 수식 + where 정의 (JAABE 배치) */
div.eq { display:table; width:100%%; margin:5pt 0 3pt; text-indent:0; }
div.eq .eqb { display:table-cell; text-align:center; font-family:%(body)s; font-size:9.2pt; }
div.eq .eqn { display:table-cell; text-align:right; width:11%%; vertical-align:middle;
              font-family:%(body)s; font-size:9.2pt; white-space:nowrap; }
div.whr { margin:2pt 0 6pt 3mm; font-size:8.6pt; line-height:1.5; text-indent:0; }
p.author { column-span: all; text-align:center; font-weight:700; font-size:10.2pt;
           margin:10pt 0 2pt; text-indent:0; letter-spacing:.02em; }
p.affil  { column-span: all; text-align:center; font-size:8.4pt; color:#333;
           margin:0 0 2pt; text-indent:0; line-height:1.4; }
h1 + h3 { text-align:center; font-weight:400; color:#222; font-size:10.5pt; margin:0 0 14pt; border:none; }
h2 { font-family:%(body)s; font-size:10pt; font-weight:700; margin:11pt 0 3pt;
     border:none; padding:0; page-break-after:avoid; }
h3 { font-family:%(body)s; font-size:9.4pt; font-weight:700; margin:8pt 0 2pt; page-break-after:avoid; }
p { margin:0; text-indent:4.2mm; }
p + p { margin-top:0; }
h2 + p, h3 + p, blockquote + p, table + p, div + p { text-indent:0; }
strong { font-weight:700; }
/* Abstract·Keywords·저자·각주 블록: 전체 폭 + 위아래 괘선 */
blockquote { column-span: all; background:none; border:none;
     border-top:0.9pt solid #222; border-bottom:0.9pt solid #222;
     padding:7pt 0; margin:8pt 0 12pt; font-size:8.9pt; line-height:1.42; text-align:justify; }
blockquote p { text-indent:4.2mm; } blockquote p:first-child { text-indent:0; }
/* 표·그림은 단을 넘겨 배치(2단 폭에 눌리면 판독 불가) */
div.wide { column-span: all; }
div.figblock { page-break-inside: avoid; margin:7pt 0 5pt; }
div.figcap { font-family:%(body)s; font-size:8.6pt; font-weight:700; text-align:center;
             margin:3pt 0 1pt; line-height:1.35; }
table { border-collapse:collapse; width:100%%; margin:7pt 0 3pt;
        font-family:%(head)s; font-size:8.1pt; page-break-inside:auto; }
thead { display:table-header-group; }
tr { page-break-inside:avoid; }
th,td { border:0.5pt solid #999; padding:2.4pt 4pt; text-align:left; vertical-align:top; }
th { background:#eceef0; font-weight:700; }
img { display:block; margin:6pt auto 2pt; max-width:100%%; page-break-inside:avoid; }
/* 표·그림 캡션만 단 전체 폭. 본문 중 인라인 각주는 흐름 유지(겹침 방지). */
div.cap { column-span: all; display:block; font-size:7.6pt; color:#555; text-align:left;
      margin:0 0 7pt; line-height:1.34; }
div.cap sub { font-size:inherit; vertical-align:baseline; }
sub { font-size:7.8pt; color:#555; vertical-align:baseline; }
pre { font-family:'Menlo','Courier New',monospace; font-size:7.6pt; line-height:1.34;
      white-space:pre-wrap; background:#f5f6f7; border:0.5pt solid #dcdee0; padding:5pt 7pt; }
code { font-family:'Menlo','Courier New',monospace; font-size:8.2pt; }
hr { display:none; }   /* 2단에서 절 구분선은 강제 분단만 만든다 */
sup { font-size:68%%; }
ol,ul { margin:3pt 0 3pt 12pt; } li { margin:1.5pt 0; text-align:justify; }
"""

def css(lang):
    if lang=='en2':
        return JAABE % {'body':"Georgia,'Times New Roman',serif",
                        'head':"'Helvetica Neue',Helvetica,Arial,sans-serif"}
    body_f = "'AppleMyungjo','Apple SD Gothic Neo',serif" if lang=='ko' else "Georgia,'Times New Roman',serif"
    head_f = "'Apple SD Gothic Neo',sans-serif" if lang=='ko' else "'Helvetica Neue',Helvetica,Arial,sans-serif"
    fs     = "10.3pt" if lang=='ko' else "10.1pt"
    return """
@page { size: A4; margin: 20mm 17mm 18mm 17mm;
  @bottom-center { content: counter(page) " / " counter(pages); font-family:%(head)s; font-size:8pt; color:#888; } }
* { box-sizing: border-box; }
body { font-family:%(body)s; font-size:%(fs)s; line-height:1.62; color:#111; }
h1 { font-family:%(head)s; font-size:16.5pt; font-weight:800; text-align:center; margin:2pt 0 0; line-height:1.3; }
h1 + h3 { text-align:center; font-weight:600; color:#333; font-size:11.5pt; margin:1pt 0 10pt; border:none; }
h2 { font-family:%(head)s; font-size:13pt; font-weight:800; margin:18pt 0 7pt; padding-bottom:3pt;
     border-bottom:1.5pt solid #333; page-break-after:avoid; }
h3 { font-family:%(head)s; font-size:11pt; font-weight:700; margin:12pt 0 5pt; page-break-after:avoid; }
p { margin:5pt 0; text-align:justify; }
strong { font-weight:700; }
blockquote { background:#f3f4f6; border:0.7pt solid #d0d3d8; border-radius:3pt; padding:9pt 12pt; margin:9pt 0;
     font-size:9.5pt; line-height:1.55; }
blockquote p:first-child { margin-top:0; } blockquote p:last-child { margin-bottom:0; }
/* 표: 통째로 avoid 하면 긴 표(공공임대 8행·국제비교 등)가 다음 장으로 통째 밀려 공백이 크게 남는다.
   행 단위로만 avoid 하고 표 자체는 분할 허용 + thead 반복 → 공백 회수(v10 조판 정리). */
table { border-collapse:collapse; width:100%%; margin:7pt 0; font-family:%(head)s; font-size:9pt; page-break-inside:auto; }
thead { display:table-header-group; }
tr { page-break-inside:avoid; }
th,td { border:0.6pt solid #999; padding:3pt 5.5pt; text-align:left; vertical-align:top; }
th { background:#e8eaed; font-weight:700; }
img { display:block; margin:6pt auto; max-width:94%%; page-break-inside:avoid; }
pre { background:#f5f6f7; border:0.6pt solid #d8dadd; border-radius:3pt; padding:8pt 10pt;
      font-family:'Menlo','Courier New',monospace; font-size:8.3pt; line-height:1.4; white-space:pre-wrap; page-break-inside:avoid; }
code { font-family:'Menlo','Courier New',monospace; font-size:9pt; background:#f0f1f2; padding:0 2pt; border-radius:2pt; }
sub { font-size:8.2pt; color:#666; }
hr { border:none; border-top:0.6pt solid #ccc; margin:12pt 0; }
sup { font-size:70%%; }
ol,ul { margin:5pt 0 5pt 16pt; } li { margin:2pt 0; }
div[align="right"] { color:#555; font-size:8.5pt; }
""" % {'body':body_f,'head':head_f,'fs':fs}

for name,lang in SEL:
    MD   = f'{BASE}/paper/source/{name}.md'
    PDF  = f'{BASE}/paper/{OUT.get(name, name)}.pdf'
    HTML = f'/private/tmp/_render_{name}.html'
    src=open(MD,encoding='utf-8').read()
    src=re.sub(r'^<!--.*?-->\s*','',src,flags=re.S|re.M)                      # 편집용 주석 제거
    src=re.sub(r'^\*(「국토계획」|Journal-style manuscript).*?\*\s*$','',src,flags=re.M)  # 편집자 노트 제거
    if lang=='en2':
        # ⓪ 저자명·소속 줄에 클래스 부여 (표제부 중앙 배치)
        src=re.sub(r'^\*\*([A-Z][A-Z\s]+)\*\*(<sup>[^<]*</sup>)\s*$',
                   r'<p class="author">\1\2</p>', src, flags=re.M)
        src=re.sub(r'^(<sup>[^<]*</sup> (?:Valor|Corresponding)[^\n]*)$',
                   r'<p class="affil">\1</p>', src, flags=re.M)
        # ① 그림: [캡션 → 이미지 → Source] 를 [이미지 → 캡션 → Source] 한 덩어리로 (JAABE 는 캡션이 그림 아래)
        def _fig(m):
            cap, img, srcline = m.group(1), m.group(2), (m.group(3) or '')
            srchtml = f'<div class="cap"><sub>{srcline}</sub></div>' if srcline else ''
            return (f'<div class="wide figblock"><img src="{img}">'
                    f'<div class="figcap">{cap}</div>{srchtml}</div>')
        src=re.sub(r'^(?:<br>)?\*\*(Fig\.[^*]+)\*\*\s*\n!\[[^\]]*\]\(([^)]+)\)\s*(?:\n<sub>(.*?)</sub>)?\s*$',
                   _fig, src, flags=re.M)
        # ② 남은 표·본문 캡션 줄을 단 전체 폭 블록으로
        src=re.sub(r'^<sub>(.*?)</sub>\s*$', r'<div class="cap"><sub>\1</sub></div>', src, flags=re.M|re.S)
    body=markdown.markdown(src, extensions=['tables','fenced_code','sane_lists','attr_list','md_in_html','nl2br'])
    body=body.replace('src="../../analysis/', f'src="file://{ANALYSIS}/')
    body=body.replace('src="../analysis/', f'src="file://{ANALYSIS}/')        # 이미지 절대경로
    if lang=='en2':   # WeasyPrint 는 table/img 자체에 column-span 을 적용하지 않는다 → 래퍼로 감싼다
        body=re.sub(r'(<table>.*?</table>)', r'<div class="wide">\1</div>', body, flags=re.S)
        body=re.sub(r'(<p>\s*)?(<img[^>]*>)(\s*</p>)?', r'<div class="wide">\2</div>', body)
    html=(f'<!DOCTYPE html><html lang="{"ko" if lang=="ko" else "en"}"><head><meta charset="utf-8">'
          f'<title>{name}</title><style>{css(lang)}</style></head><body>{body}</body></html>')
    open(HTML,'w',encoding='utf-8').write(html)
    r=subprocess.run(['weasyprint',HTML,PDF],capture_output=True,text=True)
    if r.returncode!=0:
        print(f"❌ {name} weasyprint 실패:\n",r.stderr[-1500:]); raise SystemExit(1)
    print(f"✅ {os.path.basename(PDF)} ({os.path.getsize(PDF)/1024/1024:.2f} MB, lang={lang}) ← {name}.md")
    if r.stderr.strip(): print("  경고:",r.stderr.strip()[-300:])
