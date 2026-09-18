"""[EN] Collects observed household-size distribution for Pyeongtaek (KOSIS DT_1JC1516).
#평택 실측 가구원수 분포 수집 — KOSIS DT_1JC1516(세대구성 및 가구원수별 가구, 시군구).
발견한 param: objL1=지역(레거시 순번코드, 평택=31070), objL2=세대구성 '00'=계, itmId T10=일반가구/T21~T25=가구원수 1~5명.
출력: employment/pyeongtaek_hhsize_2015_2024.csv
"""
import os as _os
DATA_ROOT = _os.environ.get('DATA_ROOT', '/Users/Shared/seoyeon_research')
INVENTORY_DB = _os.environ.get('INVENTORY_DB', '/Users/Shared/seoyeon_inventory_master.sqlite')
import os,sys,csv
sys.path.insert(0, os.path.dirname(__file__))
from kosis_client import kosis_get  # 분당 200건 제한 자동 스로틀+백오프
ITM={'T10':'일반가구','T21':'1인','T22':'2인','T23':'3인','T24':'4인','T25':'5인+'}
# 참고: DT_1JC1516 T25='5명' 실제로는 '5명 이상'일 수 있음 → 메타 확인
def call(itm):
    return kosis_get({'method':'getList','orgId':'101','tblId':'DT_1JC1516',
       'objL1':'31070','objL2':'00','itmId':itm,'prdSe':'Y','startPrdDe':'2015','endPrdDe':'2024'})
data={}  # year -> {label: val}
for itm,lab in ITM.items():
    for d in call(itm):
        if d.get('DT') is None: continue
        y=int(d['PRD_DE']); data.setdefault(y,{})[lab]=int(d['DT'])
out=DATA_ROOT + '/employment/pyeongtaek_hhsize_2015_2024.csv'
os.makedirs(os.path.dirname(out),exist_ok=True)
cols=['year']+list(ITM.values())
with open(out,'w',newline='') as f:
    w=csv.writer(f); w.writerow(cols)
    for y in sorted(data): w.writerow([y]+[data[y].get(l,'') for l in ITM.values()])
print(f'✅ {out}')
# 최신년도 분포 출력
y=max(data); tot=data[y]['일반가구']
print(f"\n평택 {y} 일반가구 {tot:,}")
for l in ['1인','2인','3인','4인','5인+']:
    v=data[y].get(l,0); print(f"  {l}: {v:,} ({v/tot*100:.1f}%)")
ssum=sum(data[y].get(l,0) for l in ['1인','2인','3인','4인','5인+'])
print(f"  합계검증: {ssum:,} vs 일반가구 {tot:,} (차={tot-ssum:,})")
