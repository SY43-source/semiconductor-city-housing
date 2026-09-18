"""[EN] Jeonse/monthly-rent analysis — where small-unit demand is actually realized.
#A 전월세 분석 — 모집단(소형 수요 실재처) + 월세화. 평택·안성·광주.

핵심1: 소형(<60㎡) 수요는 매매보다 전월세에 실재하는가 (모집단 아티팩트).
핵심2: 월세화(전월세 중 월세 비중) — 반도체 특유인가 전국인가.
데이터: realprice_apt_rent_{pt,an,gwangju} + realprice_apt_trade(평택/안성/광주).
"""
import os as _os; REPO = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import csv
from collections import defaultdict
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Helvetica'; plt.rcParams['axes.unicode_minus']=False
RP='/Users/Shared/seoyeon_research/realprice'; YEARS=list(range(2015,2026))
def load(p,pred=lambda r:True): return [r for r in csv.DictReader(open(p,encoding='utf-8-sig')) if pred(r)]
def small(rows):
    t=defaultdict(int); s=defaultdict(int)
    for r in rows:
        y=r.get('dealYear')
        if y and r.get('excluUseAr') and 2015<=int(y)<=2025:
            yi=int(y); t[yi]+=1
            if float(r['excluUseAr'])<60: s[yi]+=1
    return {y:(s[y]/t[y]*100 if t[y] else float('nan')) for y in YEARS}
def wolse(rows):
    t=defaultdict(int); w=defaultdict(int)
    for r in rows:
        y=r.get('dealYear')
        if y and 2015<=int(y)<=2025:
            yi=int(y); t[yi]+=1
            if r.get('rentType')=='monthly' or (r.get('monthly') and r['monthly'] not in ('0','')): w[yi]+=1
    return {y:(w[y]/t[y]*100 if t[y] else float('nan')) for y in YEARS}
pt_rent=load(f'{RP}/realprice_apt_rent_pt.csv'); an_rent=load(f'{RP}/realprice_apt_rent_an.csv'); gj_rent=load(f'{RP}/realprice_apt_rent_gwangju.csv')
pt_sale=load(f'{RP}/realprice_apt_trade.csv',lambda r:r['region']=='평택시'); gj_sale=load(f'{RP}/realprice_apt_trade_gwangju.csv')
pts_sale,pts_rent=small(pt_sale),small(pt_rent); gjs_sale,gjs_rent=small(gj_sale),small(gj_rent)
pt_w,an_w,gj_w=wolse(pt_rent),wolse(an_rent),wolse(gj_rent)

fig,(a1,a2)=plt.subplots(1,2,figsize=(15.5,6))
fig.suptitle('Lease market: where small-unit demand is realized, and the shift to monthly rent',fontsize=13.5,fontweight='bold')
# 패널1: 소형 매매 vs 전월세 (평택·광주)
a1.plot(YEARS,[pts_sale[y] for y in YEARS],'s-',color='#37a',lw=2.2,label='Pyeongtaek small, sale')
a1.plot(YEARS,[pts_rent[y] for y in YEARS],'D-',color='#e33',lw=2.2,label='Pyeongtaek small, lease')
a1.plot(YEARS,[gjs_sale[y] for y in YEARS],'s--',color='#8ac',lw=1.8,label='Gwangju small, sale')
a1.plot(YEARS,[gjs_rent[y] for y in YEARS],'D--',color='#e88',lw=1.8,label='Gwangju small, lease')
a1.set_title('Small-unit (<60m2) share: leases exceed sales\n-> small-household demand is realized through leases')
a1.set_xlabel('Year'); a1.set_ylabel('Small-unit share (%)'); a1.legend(fontsize=8.5); a1.grid(alpha=0.3)
# 패널2: 월세화 3도시
a2.plot(YEARS,[pt_w[y] for y in YEARS],'o-',color='#e33',lw=2.3,label='Pyeongtaek (semiconductor)')
a2.plot(YEARS,[an_w[y] for y in YEARS],'s--',color='#38a',lw=2,label='Anseong (control)')
a2.plot(YEARS,[gj_w[y] for y in YEARS],'^:',color='#2a8',lw=2,label='Gwangju')
a2.axvline(2017,color='blue',ls=':',lw=1.4,label='Samsung P1, 2017')
a2.set_title('Monthly rent as a share of leases\nrising in all three cities: a nationwide trend')
a2.set_xlabel('Year'); a2.set_ylabel('Monthly-rent share (%)'); a2.legend(fontsize=8.5); a2.grid(alpha=0.3)
plt.tight_layout(rect=[0,0,1,0.92])
out=REPO + '/analysis/10_rent_analysis.png'
plt.savefig(out,dpi=120,bbox_inches='tight'); print(f'✅ {out}')
print(f"소형 매매vs전월세 2024 — 평택 {pts_sale[2024]:.0f}/{pts_rent[2024]:.0f} · 광주 {gjs_sale[2024]:.0f}/{gjs_rent[2024]:.0f}")
print(f"월세비중 2015→24 — 평택 {pt_w[2015]:.0f}→{pt_w[2024]:.0f} · 안성 {an_w[2015]:.0f}→{an_w[2024]:.0f} · 광주 {gj_w[2015]:.0f}→{gj_w[2024]:.0f}")
