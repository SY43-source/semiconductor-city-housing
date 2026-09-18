"""[EN] Annual cohort matrix for Godeok (age x year population).
#P1 — v7 연도별 코호트 데이터 정비. 고덕 연령×연도 인구 행렬 P_{a,t} 및 순증 Δ_{a,t} 추출.
데이터: KOSIS DT_1B04005N(읍면동 5세별), 고덕면(4122033000)+고덕동(4122066000, 2021~신설).
산출: population/godeok_age_year_matrix.csv  (행=연도, 열=5세 연령밴드, 값=인구)
      population/godeok_age_year_delta.csv   (연도별 순증 Δ = P_t - P_{t-1})
용도: v7 §IV.9 연도별 예측(코호트 진행 + 유입 로지스틱)의 입력.
"""
import os,sys,csv
from collections import OrderedDict
sys.path.insert(0, os.path.join(os.path.dirname(__file__),'..','src'))
from kosis_client import kosis_get
OUT='/Users/Shared/seoyeon_research/population'
YEARS=list(range(2013,2026))
CODES=['4122033000','4122066000']   # 고덕면 · 고덕동(2021~)

def godeok_year(y):
    """해당 연도 고덕(면+동) 연령밴드별 인구 dict. 미존재 동은 skip."""
    p={}
    for code in CODES:
        d=kosis_get({'method':'getList','orgId':'101','tblId':'DT_1B04005N','objL1':code,
                     'objL2':'ALL','itmId':'T2','prdSe':'Y','startPrdDe':str(y),'endPrdDe':str(y)})
        if not isinstance(d,list): continue          # err dict = 그 해 미존재 행정동
        for x in d:
            if x.get('DT') is None: continue
            p[x['C2_NM']]=p.get(x['C2_NM'],0)+int(x['DT'])
    return p

mat=OrderedDict()
for y in YEARS:
    mat[y]=godeok_year(y)
    print(f"  {y} 수집 완료 (계 {mat[y].get('계',0):,}명)")

# 연령밴드 순서 정리(계 제외, 원 순서 유지)
bands=[b for b in mat[YEARS[-1]].keys() if b!='계']
os.makedirs(OUT,exist_ok=True)

f1=f'{OUT}/godeok_age_year_matrix.csv'
with open(f1,'w',newline='') as f:
    w=csv.writer(f); w.writerow(['year','계']+bands)
    for y in YEARS: w.writerow([y,mat[y].get('계',0)]+[mat[y].get(b,0) for b in bands])
print(f"✅ {f1}")

f2=f'{OUT}/godeok_age_year_delta.csv'
with open(f2,'w',newline='') as f:
    w=csv.writer(f); w.writerow(['year','계']+bands)
    for i,y in enumerate(YEARS):
        if i==0: continue
        pv,cv=mat[YEARS[i-1]],mat[y]
        w.writerow([y,cv.get('계',0)-pv.get('계',0)]+[cv.get(b,0)-pv.get(b,0) for b in bands])
print(f"✅ {f2}")

# 요약: 성장기(2019~2025) 연평균 순증 및 연령 프로파일 w_a
print("\n=== 성장기(2019→2025) 연령대별 순증 & 유입 프로파일 w_a ===")
tot=0; prof={}
for b in bands:
    d=mat[2025].get(b,0)-mat[2018].get(b,0)
    prof[b]=d; tot+=max(d,0)
for b in bands:
    if prof[b]>0: print(f"  {b:<12} +{prof[b]:>6,}  (w_a={prof[b]/tot*100:5.1f}%)")
print(f"  총 순증 {sum(prof.values()):,}명 · 양(+) 합 {tot:,}명")
print(f"\n계획 수용인구 K_pop=144,173 대비 2025 실측 {mat[2025].get('계',0):,} = {mat[2025].get('계',0)/144173*100:.1f}%")
