"""[EN] Collects headship data (household-head age x household size) for Pyeongtaek.
#P1 — 연령기반 설계모델 링크핀: 가구주 연령 × 가구원수 결합분포 (평택).
KOSIS DT_1JC1511 '가구주의 연령 및 가구원수별 가구(일반가구) - 시군구'.
param: objL1=31070(평택 레거시코드), objL2=가구주연령(020=15-19 … 5세스텝 … 090=85+, 000=합계),
       itmId T100=일반가구계 / T210~T270=가구원수 1~7명이상.
산출:
  employment/pyeongtaek_head_age_hhsize_2024.csv — 행=가구주연령밴드, 열=가구원수 1~5+명 가구수
용도: P(가구원수 h | 가구주연령 a) = 행 정규화. 헤드십 numerator(가구주수 by age)=T100 열.
"""
import os,sys,csv
sys.path.insert(0, os.path.dirname(__file__))
from kosis_client import kosis_get

YEAR='2024'
# 가구주연령 밴드코드 (탐색으로 확정). 015=15세미만은 X라 제외, 020~090.
AGE_CODES=[f'{c:03d}' for c in range(20,91,5)]   # 020,025,...,090
# 가구원수 항목: 1~4명 개별 + 5+명(5·6·7이상 합산)
ITM_SINGLE={'T210':'1인','T220':'2인','T230':'3인','T240':'4인'}
ITM_5PLUS=['T250','T260','T270']  # 5·6·7+명 → 5인+
ITM_TOTAL='T100'

def get(age, itm):
    d=kosis_get({'method':'getList','orgId':'101','tblId':'DT_1JC1511',
        'objL1':'31070','objL2':age,'itmId':itm,'prdSe':'Y','startPrdDe':YEAR,'endPrdDe':YEAR})
    if isinstance(d,list) and d and d[0].get('DT') not in (None,'X'):
        return int(float(d[0]['DT'])), d[0].get('C2_NM','')
    return None, (d[0].get('C2_NM','') if isinstance(d,list) and d else '')

rows=[]
for age in AGE_CODES:
    rec={'age_code':age}
    tot,nm=get(age,ITM_TOTAL); rec['age']=nm; rec['총가구']=tot or 0
    for itm,lab in ITM_SINGLE.items():
        v,_=get(age,itm); rec[lab]=v or 0
    p5=0
    for itm in ITM_5PLUS:
        v,_=get(age,itm); p5+=(v or 0)
    rec['5인+']=p5
    rows.append(rec)

out='/Users/Shared/seoyeon_research/employment/pyeongtaek_head_age_hhsize_2024.csv'
os.makedirs(os.path.dirname(out),exist_ok=True)
cols=['age_code','age','총가구','1인','2인','3인','4인','5인+']
with open(out,'w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=cols); w.writeheader()
    for r in rows: w.writerow({k:r.get(k,'') for k in cols})
print(f'✅ {out}')
# 요약: 젊은 가구주(25-39)의 가구원수 구성 vs 전연령
def band(codes):
    sub=[r for r in rows if r['age_code'] in codes]
    tt=sum(r['총가구'] for r in sub)
    return tt,{h:sum(r[h] for r in sub) for h in ['1인','2인','3인','4인','5인+']}
young_tt,young=band(['030','035','040'])  # 25-39 가구주
all_tt=sum(r['총가구'] for r in rows); allh={h:sum(r[h] for r in rows) for h in ['1인','2인','3인','4인','5인+']}
print(f"\n[가구주 25-39세] 총 {young_tt:,}가구")
for h in ['1인','2인','3인','4인','5인+']: print(f"  {h}: {young[h]/young_tt*100:.1f}%")
print(f"[전 연령] 총 {all_tt:,}가구")
for h in ['1인','2인','3인','4인','5인+']: print(f"  {h}: {allh[h]/all_tt*100:.1f}%")
