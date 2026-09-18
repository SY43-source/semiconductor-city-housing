"""[EN] Dose-response using manufacturing employment as a continuous treatment.
#dose 강화 — 평택 제조업 고용(연속 처치) vs 고덕 국지효과.

라인수(단조증가, 시간교란)보다 나은 연속 dose = 평택 광업·제조업 종사자(KOSIS 118 MONA49, 반기→연간).
고덕 인접/외곽 가격배율·고덕 신규개발과 상관. 2018~2025.
"""
import os as _os; REPO = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import os,sys,csv,statistics,sqlite3
from collections import defaultdict
import numpy as np
from scipy import stats
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='AppleGothic'; plt.rcParams['axes.unicode_minus']=False
sys.path.insert(0, os.path.join(os.path.dirname(__file__),'..','src'))
from kosis_client import kosis_get  # 분당 200건 제한 자동 스로틀+백오프
RP='/Users/Shared/seoyeon_research/realprice'; DB='/Users/Shared/seoyeon_inventory_master.sqlite'
EMP_CSV='/Users/Shared/seoyeon_research/employment/pyeongtaek_mfg_2018_2025.csv'
os.makedirs(os.path.dirname(EMP_CSV),exist_ok=True)

# 1) 평택 제조업 고용 (반기→연간 평균), 저장
def fetch_emp():
    d=kosis_get({'method':'getList','orgId':'118','tblId':'DT_118N_MONA49',
      'objL1':'ZONE2017A313107','objL2':'IND201701','itmId':'16118z1','prdSe':'H','newEstPrdCnt':'16'})
    byyr=defaultdict(list)
    for x in d: byyr[x['PRD_DE'][:4]].append(int(x['DT']))
    return {int(y):sum(v)//len(v) for y,v in byyr.items()}
emp=fetch_emp()
with open(EMP_CSV,'w',newline='',encoding='utf-8-sig') as f:
    w=csv.writer(f); w.writerow(['year','pyeongtaek_mfg_employees'])
    for y in sorted(emp): w.writerow([y,emp[y]])
print("평택 제조업 고용:",{y:emp[y] for y in sorted(emp)})

YEARS=[y for y in range(2018,2026) if y in emp]
# 2) 고덕 인접/외곽 가격배율
pt=[r for r in csv.DictReader(open(f'{RP}/realprice_apt_trade.csv',encoding='utf-8-sig')) if r['region']=='평택시']
def ppm2(keys):
    by=defaultdict(list)
    for r in pt:
        if any(k in r['umdNm'] for k in keys):
            try:
                a=float(str(r['dealAmount']).replace(',','')); ar=float(r['excluUseAr']); y=int(r['dealYear'])
                if ar>0: by[y].append(a/ar)
            except: pass
    return {y:(statistics.median(by[y]) if by[y] else np.nan) for y in range(2015,2026)}
near=ppm2(['고덕','서정동','지제동','동삭동','신촌']); far=ppm2(['안중읍','포승읍','팽성읍','청북읍','현덕면','오성면'])
prem={y:near[y]/far[y] for y in near}
# 3) 고덕 신규개발
con=sqlite3.connect(DB); dev={}
for yr,n in con.execute("""SELECT approval_year,SUM(total_households) FROM complexes WHERE bjd_code LIKE '41220%'
 AND (sector LIKE '%고덕%' OR road_name LIKE '%고덕%' OR sector LIKE '%서정%' OR sector LIKE '%지제%')
 AND approval_year BETWEEN 2018 AND 2025 GROUP BY approval_year"""): dev[yr]=n or 0
con.close()

x=np.array([emp[y] for y in YEARS])/1000
yp=np.array([prem[y] for y in YEARS]); yd=np.array([dev.get(y,0) for y in YEARS])/1000
rp=stats.pearsonr(x,yp); rd=stats.pearsonr(x,yd)
fig,(a1,a2)=plt.subplots(1,2,figsize=(15.5,6))
fig.suptitle('용량반응 강화 — 평택 제조업 고용(연속 dose) vs 고덕 국지효과 (2018~2025)',fontsize=13.5,fontweight='bold')
# 시계열 겹침
a1.bar(YEARS,[emp[y]/1000 for y in YEARS],color='#ddd',label='평택 제조업 고용(천명)')
a1.set_ylabel('제조업 고용(천명)'); a1.set_ylim(70,105); a1.set_xlabel('연도')
ab=a1.twinx(); ab.plot(YEARS,yp,'D-',color='#a2d',lw=2.3,label='고덕/외곽 가격배율'); ab.set_ylabel('가격배율')
a1.set_title('시계열: 제조업 고용 ↑ 와 고덕 프리미엄 ↑')
l1,la1=a1.get_legend_handles_labels(); l2,la2=ab.get_legend_handles_labels(); a1.legend(l1+l2,la1+la2,fontsize=8,loc='upper left'); a1.grid(alpha=0.2)
# 산점도
a2.scatter(x,yp,color='#a2d',s=70,zorder=3)
for i,y in enumerate(YEARS): a2.annotate(str(y)[2:],(x[i],yp[i]),fontsize=8,ha='center',va='bottom')
b=np.polyfit(x,yp,1); xf=np.linspace(x.min(),x.max(),20); a2.plot(xf,b[0]*xf+b[1],color='#a2d',alpha=0.5)
a2.set_xlabel('평택 제조업 고용(천명)'); a2.set_ylabel('고덕/외곽 가격배율')
a2.set_title(f'용량반응: 고용 ↔ 가격배율\nPearson r={rp.statistic:.2f} (p={rp.pvalue:.3f}) / 개발 r={rd.statistic:.2f}')
a2.grid(alpha=0.3)
plt.tight_layout(rect=[0,0,1,0.93])
out=REPO + '/analysis/15_dose_employment.png'
plt.savefig(out,dpi=120,bbox_inches='tight'); print(f'✅ {out}')
print(f"고용 vs 가격배율 r={rp.statistic:.2f} p={rp.pvalue:.4f} / 고용 vs 개발 r={rd.statistic:.2f} p={rd.pvalue:.4f}")
