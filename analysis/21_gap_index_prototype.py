"""[EN] Prototype demand-supply gap index by household composition (superseded by 32).
#PROTOTYPE — 가구형태별 규격 수요 gap 지수 (고덕).
수요 = 평택 가구형태 × 규격수요 매핑(가정) / 공급 = 고덕 아파트 규격 비중(NAVER sqlite).
Gap = 공급% - 수요% (음수=부족·공급확대 필요 / 양수=과잉). 가구원수=평택 실측(DT_1JC1516), 규격매핑은 가정(감도분석 21b).
"""
import os as _os; REPO = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
DATA_ROOT = _os.environ.get('DATA_ROOT', '/Users/Shared/seoyeon_research')
INVENTORY_DB = _os.environ.get('INVENTORY_DB', '/Users/Shared/seoyeon_inventory_master.sqlite')
import sqlite3
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='AppleGothic'; plt.rcParams['axes.unicode_minus']=False
DB=DATA_ROOT + '/seoyeon_inventory_master.sqlite'
DB=INVENTORY_DB

# 1) 가구형태 분포 (평택). ★실측: KOSIS DT_1JC1516 세대구성·가구원수별 가구, 평택(objL1=31070) 2024, 정규화(합=258,625)
HH={'1인':0.3754,'2인':0.2745,'3인':0.1862,'4인':0.1340,'5인+':0.0300}
# 2) 규격 수요 매핑(가정): 가구형태→[소형<60, 국평60-85, 대형85+] 확률
MAP={'1인':[0.85,0.15,0.00],'2인':[0.50,0.45,0.05],'3인':[0.10,0.75,0.15],
     '4인':[0.03,0.62,0.35],'5인+':[0.00,0.45,0.55]}
BANDS=['소형<60','국평60-85','대형85+']
demand=np.zeros(3)
for h,share in HH.items(): demand+=share*np.array(MAP[h])
demand=demand/demand.sum()*100

# 3) 공급: 고덕 아파트 규격 비중(세대수, NAVER)
con=sqlite3.connect(DB)
q="""SELECT CASE WHEN p.exclusive_area_m2<60 THEN 0 WHEN p.exclusive_area_m2<85 THEN 1 ELSE 2 END b,
 SUM(p.units_of_same_area) u FROM complexes c JOIN pyeong_types p ON c.complex_number=p.complex_number
 WHERE c.bjd_code LIKE '41220%' AND (c.sector LIKE '%고덕%' OR c.road_name LIKE '%고덕%') AND p.units_of_same_area>0 GROUP BY b"""
sup=np.zeros(3)
for b,u in con.execute(q): sup[b]=u
con.close(); supply=sup/sup.sum()*100
gap=supply-demand   # 공급-수요: 음수=부족, 양수=과잉

print("가구형태(평택 2024 실측 DT_1JC1516):",{k:f'{v*100:.1f}%' for k,v in HH.items()})
print(f"\n{'규격':<12}{'수요%':>8}{'공급%(고덕)':>12}{'Gap(공급-수요)':>14}")
for i,b in enumerate(BANDS):
    print(f"{b:<12}{demand[i]:>8.1f}{supply[i]:>12.1f}{gap[i]:>+13.1f}")
print(f"\n해석: 소형 {gap[0]:+.0f}%p(부족→다양화 우선), 국평 {gap[1]:+.0f}%p(과잉), 대형 {gap[2]:+.0f}%p")

fig,(a1,a2)=plt.subplots(1,2,figsize=(14.5,6))
fig.suptitle('고덕 아파트 규격 수급 gap 지수 (수요=평택 실측 가구원수 DT_1JC1516, 매핑 감도분석 21b)',fontsize=12,fontweight='bold')
x=np.arange(3); w=0.36
a1.bar(x-w/2,demand,w,color='#a2d',label='수요(가구형태 기반)')
a1.bar(x+w/2,supply,w,color='#c63',label='공급(고덕 신축 세대)')
for i in x:
    a1.text(i-w/2,demand[i]+0.5,f'{demand[i]:.0f}',ha='center',fontsize=9)
    a1.text(i+w/2,supply[i]+0.5,f'{supply[i]:.0f}',ha='center',fontsize=9)
a1.set_xticks(x); a1.set_xticklabels(BANDS); a1.set_ylabel('비중(%)'); a1.set_title('수요 vs 공급'); a1.legend(fontsize=9); a1.grid(alpha=0.3,axis='y')
cols=['#d33' if g<0 else '#2a8' for g in gap]   # 부족(-)=적색, 과잉(+)=녹색
a2.bar(x,gap,color=cols); a2.axhline(0,color='gray',lw=1)
for i in x: a2.text(i,gap[i]+(0.6 if gap[i]>=0 else -1.5),f'{gap[i]:+.0f}%p',ha='center',fontsize=10,fontweight='bold')
a2.set_xticks(x); a2.set_xticklabels(BANDS); a2.set_ylabel('Gap = 공급 - 수요 (%p)')
a2.set_title('gap 지수\n(- 부족=공급확대 우선 / + 과잉)'); a2.grid(alpha=0.3,axis='y')
plt.tight_layout(rect=[0,0,1,0.93])
out=REPO + '/analysis/21_gap_index_prototype.png'
plt.savefig(out,dpi=120,bbox_inches='tight'); print(f'\n✅ {out}')
