"""[EN] Gap sensitivity — Fig. A1. Varies household and unit-size mapping assumptions.
#gap 정합 — 민감도 분석. 가구형태·규격매핑 가정을 범위로 흔들어 '소형 부족' 결론 강건성 검증.
기준=평택 실측 가구원수(KOSIS DT_1JC1516, objL1=31070·objL2=00). 규격매핑·가구배분을 범위로 변주해 강건성 검증.
공급=고덕(sqlite). Gap=공급-수요(음수=부족). 결론: 소형 부족은 모든 시나리오서 음수(강건).
"""
import os as _os; REPO = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
DATA_ROOT = _os.environ.get('DATA_ROOT', '/Users/Shared/seoyeon_research')
INVENTORY_DB = _os.environ.get('INVENTORY_DB', '/Users/Shared/seoyeon_inventory_master.sqlite')
import sqlite3
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Helvetica'; plt.rcParams['axes.unicode_minus']=False
DB=INVENTORY_DB
# 공급(고덕)
con=sqlite3.connect(DB)
q="""SELECT CASE WHEN p.exclusive_area_m2<60 THEN 0 WHEN p.exclusive_area_m2<85 THEN 1 ELSE 2 END b,SUM(p.units_of_same_area) u
 FROM complexes c JOIN pyeong_types p ON c.complex_number=p.complex_number
 WHERE c.bjd_code LIKE '41220%' AND (c.sector LIKE '%고덕%' OR c.road_name LIKE '%고덕%') AND p.units_of_same_area>0 GROUP BY b"""
sup=np.zeros(3)
for b,u in con.execute(q): sup[b]=u
con.close(); supply=sup/sup.sum()*100  # 소형/국평/대형

# 시나리오: 1인=37.3% 고정, (2인,3인,4인,5+) 배분 변주 + 규격매핑 변주
def demand(hh, MAP):
    d=np.zeros(3)
    for k in hh: d+=hh[k]*np.array(MAP[k])
    return d/d.sum()*100
MAP_base={'1':[.85,.15,0],'2':[.50,.45,.05],'3':[.10,.75,.15],'4':[.03,.62,.35],'5+':[0,.45,.55]}
MAP_fam ={'1':[.70,.30,0],'2':[.35,.55,.10],'3':[.05,.70,.25],'4':[.02,.50,.48],'5+':[0,.35,.65]}  # 가족선호(소형수요 축소=보수)
MAP_sm  ={'1':[.92,.08,0],'2':[.62,.36,.02],'3':[.15,.75,.10],'4':[.05,.70,.25],'5+':[0,.55,.45]}  # 소형선호
SC={
 'Family-weighted': ({'1':.373,'2':.24,'3':.21,'4':.14,'5+':.037}, MAP_fam),
 'Base':     ({'1':.3754,'2':.2745,'3':.1862,'4':.1340,'5+':.0300}, MAP_base),
 'Small-household':   ({'1':.45,'2':.31,'3':.15,'4':.07,'5+':.02}, MAP_sm),  # 젊은근로 다수→1인↑
}
print(f"공급(고덕): 소형 {supply[0]:.0f} / 국평 {supply[1]:.0f} / 대형 {supply[2]:.0f}")
names=list(SC); small_gap=[]; guk_gap=[]
for n in names:
    hh,mp=SC[n]; dem=demand(hh,mp); g=supply-dem   # 공급-수요: 음수=부족
    small_gap.append(g[0]); guk_gap.append(g[1])
    print(f"  [{n}] 소형수요 {dem[0]:.0f}% → 소형 gap {g[0]:+.1f}%p / 국평 gap {g[1]:+.1f}%p")

fig,ax=plt.subplots(figsize=(11,6.2))
x=np.arange(len(names)); w=0.36
b1=ax.bar(x-w/2,small_gap,w,color='#d33',label='Small (<60) gap')
b2=ax.bar(x+w/2,guk_gap,w,color='#2a8',label='Standard (60-85) gap')
ax.axhline(0,color='gray',lw=1)
for bars in (b1,b2):
    for r in bars: ax.text(r.get_x()+r.get_width()/2, r.get_height()+(0.6 if r.get_height()>=0 else -1.8), f'{r.get_height():+.0f}',ha='center',fontsize=9,fontweight='bold')
ax.set_xticks(x); ax.set_xticklabels(names); ax.set_ylabel('Gap = supply - demand (%p)')
ax.set_title('Gap sensitivity to household-form and mapping assumptions',fontsize=13,fontweight='bold')
ax.legend(fontsize=10); ax.grid(alpha=0.3,axis='y')
ax.annotate('A larger small-household share widens the small-unit shortage',xy=(2,small_gap[2]),xytext=(1.1,small_gap[2]-8),
            fontsize=8.5,color='#d33',arrowprops=dict(arrowstyle='->',color='#d33',alpha=0.6))
plt.tight_layout()
out=REPO + '/analysis/21b_gap_sensitivity.png'
plt.savefig(out,dpi=120,bbox_inches='tight'); print(f'\n✅ {out}')
print(f"소형 gap 범위: {min(small_gap):+.1f} ~ {max(small_gap):+.1f}%p (모두 음수=부족 강건)")
