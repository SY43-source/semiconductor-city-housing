"""[EN] Dose-response: campus scale (treatment intensity) vs Godeok housing effect.
#원인-효과 용량반응 — 캠퍼스 규모(처치강도) vs 고덕 주택효과.

처치강도 = 삼성 평택캠퍼스 누적 가동 라인수 (P1 2017→1, P2 2020→2, P3 2022→3, P4 2024→4).
효과 = 고덕권 신규개발 세대수(sqlite) + 고덕/외곽 가격 배율(실거래).
시계열 겹침 + 용량반응 산점도(상관). '반도체를 날짜on/off'가 아니라 '연속 강도'로.
"""
import os as _os; REPO = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import csv, sqlite3, statistics
from collections import defaultdict
import numpy as np
from scipy import stats
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='AppleGothic'; plt.rcParams['axes.unicode_minus']=False
YEARS=list(range(2015,2026))
# 처치강도: 누적 가동 라인
LINES={2015:0,2016:0,2017:1,2018:1,2019:1,2020:2,2021:2,2022:3,2023:3,2024:4,2025:4}
DB='/Users/Shared/seoyeon_inventory_master.sqlite'; RP='/Users/Shared/seoyeon_research/realprice'
# 고덕 신규개발 세대수
con=sqlite3.connect(DB)
dev={y:0 for y in YEARS}
for yr,n in con.execute("""SELECT approval_year, SUM(total_households) FROM complexes
  WHERE bjd_code LIKE '41220%' AND (sector LIKE '%고덕%' OR road_name LIKE '%고덕%' OR sector LIKE '%서정%' OR sector LIKE '%지제%')
  AND approval_year BETWEEN 2015 AND 2025 GROUP BY approval_year"""):
    if yr in dev: dev[yr]=n or 0
con.close()
# 고덕/외곽 가격 배율
pt=[r for r in csv.DictReader(open(f'{RP}/realprice_apt_trade.csv',encoding='utf-8-sig')) if r['region']=='평택시']
def ppm2(keys):
    by=defaultdict(list)
    for r in pt:
        if any(k in r['umdNm'] for k in keys):
            try:
                a=float(str(r['dealAmount']).replace(',','')); ar=float(r['excluUseAr']); y=int(r['dealYear'])
                if ar>0 and 2015<=y<=2025: by[y].append(a/ar)
            except: pass
    return {y:(statistics.median(by[y]) if by[y] else np.nan) for y in YEARS}
near=ppm2(['고덕','서정동','지제동','동삭동','신촌']); far=ppm2(['안중읍','포승읍','팽성읍','청북읍','현덕면','오성면'])
prem={y:near[y]/far[y] for y in YEARS}

fig,(a1,a2)=plt.subplots(1,2,figsize=(15.5,6))
fig.suptitle('원인-효과 용량반응 — 캠퍼스 라인 ramp vs 고덕 주택효과',fontsize=14,fontweight='bold')
# 패널1: 시계열 겹침
ax=a1
ax.bar(YEARS,[LINES[y] for y in YEARS],color='#ddd',label='캠퍼스 누적 라인(처치강도)')
ax.set_ylabel('누적 가동 라인'); ax.set_ylim(0,6); ax.set_xlabel('연도')
axb=ax.twinx()
axb.plot(YEARS,[dev[y]/1000 for y in YEARS],'o-',color='#e33',lw=2.3,label='고덕 신규개발(천세대)')
axb.plot(YEARS,[prem[y] for y in YEARS],'D--',color='#a2d',lw=2.3,label='고덕/외곽 가격배율')
axb.set_ylabel('개발(천세대) / 가격배율')
ax.set_title('시계열: 라인↑ → 고덕 개발·가격↑');
l1,la1=ax.get_legend_handles_labels(); l2,la2=axb.get_legend_handles_labels()
ax.legend(l1+l2,la1+la2,fontsize=8,loc='upper left'); ax.grid(alpha=0.2)
# 패널2: 용량반응 산점도
ax=a2
x=np.array([LINES[y] for y in YEARS]); yp=np.array([prem[y] for y in YEARS]); yd=np.array([dev[y]/1000 for y in YEARS])
rp=stats.pearsonr(x,yp); rd=stats.pearsonr(x,yd)
ax.scatter(x,yp,color='#a2d',s=60,zorder=3,label=f'가격배율 (r={rp.statistic:.2f})')
for y in YEARS: ax.annotate(str(y)[2:],(LINES[y],prem[y]),fontsize=7,ha='center',va='bottom')
b=np.polyfit(x,yp,1); xf=np.linspace(0,4,20); ax.plot(xf,b[0]*xf+b[1],color='#a2d',alpha=0.5)
ax.set_xlabel('캠퍼스 누적 가동 라인 (처치강도)'); ax.set_ylabel('고덕/외곽 가격배율')
ax.set_title(f'용량반응: 라인수 ↑ → 가격배율 ↑\nPearson r={rp.statistic:.2f} (p={rp.pvalue:.3f}) / 개발 r={rd.statistic:.2f}')
ax.legend(fontsize=9); ax.grid(alpha=0.3)
plt.tight_layout(rect=[0,0,1,0.93])
out=REPO + '/analysis/14_dose_response.png'
plt.savefig(out,dpi=120,bbox_inches='tight'); print(f'✅ {out}')
print(f"라인수 vs 가격배율 r={rp.statistic:.2f} p={rp.pvalue:.4f}")
print(f"라인수 vs 고덕개발 r={rd.statistic:.2f} p={rd.pvalue:.4f}")
print(f"고덕 개발세대: {[dev[y] for y in YEARS]}")
print(f"가격배율: {[round(prem[y],2) for y in YEARS]}")
