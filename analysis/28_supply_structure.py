"""[EN] Godeok new-build supply structure — Table 2. Room-count and floor-area distribution.
#IV.3 근거 — 고덕 신축 아파트 공급 구조(방수·면적 분포). 세대수 기준.
데이터: master sqlite(complexes+pyeong_types), 고덕 29단지·22,368세대. room_count·exclusive_area_m2.
"""
import os as _os; REPO = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import sqlite3
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='AppleGothic'; plt.rcParams['axes.unicode_minus']=False
DB='/Users/Shared/seoyeon_inventory_master.sqlite'
WHERE="c.bjd_code LIKE '41220%' AND (c.sector LIKE '%고덕%' OR c.road_name LIKE '%고덕%') AND p.units_of_same_area>0"
con=sqlite3.connect(DB)
ncplx,ntot=con.execute(f"SELECT COUNT(DISTINCT c.complex_number),SUM(p.units_of_same_area) FROM complexes c JOIN pyeong_types p ON c.complex_number=p.complex_number WHERE {WHERE}").fetchone()
def dist(expr,cond=''):
    d={}
    for b,u in con.execute(f"SELECT {expr} b,SUM(p.units_of_same_area) FROM complexes c JOIN pyeong_types p ON c.complex_number=p.complex_number WHERE {WHERE} {cond} GROUP BY b"):
        d[b]=u
    return d
room=dist("CASE WHEN p.room_count<=2 THEN '1-2방' WHEN p.room_count=3 THEN '3방' ELSE '4방+' END","AND p.room_count IS NOT NULL")
area=dist("CASE WHEN p.exclusive_area_m2<60 THEN '소형<60' WHEN p.exclusive_area_m2<85 THEN '국평60-85' ELSE '대형85+' END")
con.close()
rlab=['1-2방','3방','4방+']; alab=['소형<60','국평60-85','대형85+']
rv=np.array([room.get(l,0) for l in rlab],float); rtot=rv.sum()
av=np.array([area.get(l,0) for l in alab],float); atot=av.sum()
print(f"고덕 {ncplx}단지 {int(ntot):,}세대")
print("방수:",{l:f'{v:.0f}({v/rtot*100:.1f}%)' for l,v in zip(rlab,rv)})
print("면적:",{l:f'{v:.0f}({v/atot*100:.1f}%)' for l,v in zip(alab,av)})

fig,(a1,a2)=plt.subplots(1,2,figsize=(13,5.6))
fig.suptitle(f'고덕 신축 아파트 공급 구조 — {ncplx}개 단지·{int(ntot):,}세대 (전국 표준 국민평형·3방에 수렴)',fontsize=13,fontweight='bold')
# 방수
cr=['#c33' if l=='3방' else '#9bb' for l in rlab]
b1=a1.bar(rlab,rv,color=cr)
for i,v in enumerate(rv): a1.text(i,v+250,f'{v/rtot*100:.0f}%\n({int(v):,})',ha='center',fontsize=9.5,fontweight='bold')
a1.set_ylabel('세대수'); a1.set_title('방(침실) 수 분포 — 3방 편중'); a1.set_ylim(0,rtot*0.95); a1.grid(alpha=0.3,axis='y')
# 면적
ca=['#37a' if l=='국평60-85' else '#9bb' for l in alab]
a2.bar(alab,av,color=ca)
for i,v in enumerate(av): a2.text(i,v+200,f'{v/atot*100:.0f}%\n({int(v):,})',ha='center',fontsize=9.5,fontweight='bold')
a2.set_ylabel('세대수'); a2.set_title('전용면적 분포 — 국민평형 편중'); a2.set_ylim(0,atot*0.9); a2.grid(alpha=0.3,axis='y')
plt.tight_layout(rect=[0,0,1,0.94])
out=REPO + '/analysis/28_supply_structure.png'
plt.savefig(out,dpi=120,bbox_inches='tight'); print(f'✅ {out}')
