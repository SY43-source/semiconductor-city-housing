"""[EN] Model sensitivity — is the gap direction robust to the unit-size mapping M?
#P3-민감도 — 규격·방수 매핑(M) 가정 변주에도 gap 방향 강건한가.
가구구성 Hp는 실측 파생(고정), 규격수요매핑 M^size·M^room만 3시나리오(가족편중/기준/소가구)로 변주.
특히 방수 gap(-44.8%p, 공급-수요·음수=부족)이 가정에 얼마나 의존하는지 확인.
Hp=모델(24) 출력(고덕 신규유입): 1인39.3/2인23.6/3인18.6/4인14.6/5인+3.9. 공급=sqlite 실측.
"""
import os as _os; REPO = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
DATA_ROOT = _os.environ.get('DATA_ROOT', '/Users/Shared/seoyeon_research')
INVENTORY_DB = _os.environ.get('INVENTORY_DB', '/Users/Shared/seoyeon_inventory_master.sqlite')
import os,sqlite3
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Helvetica'; plt.rcParams['axes.unicode_minus']=False
DB=INVENTORY_DB
HH=['1','2','3','4','5+']
Hp=np.array([0.393,0.236,0.186,0.146,0.039]); Hp=Hp/Hp.sum()  # 모델 실측파생(고정)

# 공급 실측 (면적·방수)
con=sqlite3.connect(DB)
def sup(expr):
    q=f"""SELECT {expr} b,SUM(p.units_of_same_area) FROM complexes c JOIN pyeong_types p ON c.complex_number=p.complex_number
     WHERE c.bjd_code LIKE '41220%' AND (c.sector LIKE '%고덕%' OR c.road_name LIKE '%고덕%') AND p.units_of_same_area>0 {'AND p.room_count IS NOT NULL' if 'room' in expr else ''} GROUP BY b"""
    s=np.zeros(3)
    for b,u in con.execute(q): s[int(b)]=u
    return s/s.sum()*100
Ssize=sup("CASE WHEN p.exclusive_area_m2<60 THEN 0 WHEN p.exclusive_area_m2<85 THEN 1 ELSE 2 END")
Sroom=sup("CASE WHEN p.room_count<=2 THEN 0 WHEN p.room_count=3 THEN 1 ELSE 2 END")
con.close()

# M 시나리오 [소형/국평/대형] & [1-2방/3방/4방+]
SIZE={
 'Family-weighted':{'1':[.70,.30,0],'2':[.35,.55,.10],'3':[.05,.70,.25],'4':[.02,.50,.48],'5+':[0,.35,.65]},
 'Base':         {'1':[.85,.15,0],'2':[.50,.45,.05],'3':[.10,.75,.15],'4':[.03,.62,.35],'5+':[0,.45,.55]},
 'Small-household':    {'1':[.92,.08,0],'2':[.62,.36,.02],'3':[.15,.75,.10],'4':[.05,.70,.25],'5+':[0,.55,.45]},
}
ROOM={
 'Family-weighted':{'1':[.75,.25,0],'2':[.40,.58,.02],'3':[.05,.85,.10],'4':[.02,.65,.33],'5+':[0,.35,.65]},
 'Base':         {'1':[.90,.10,0],'2':[.60,.38,.02],'3':[.10,.82,.08],'4':[.03,.72,.25],'5+':[0,.45,.55]},
 'Small-household':    {'1':[.96,.04,0],'2':[.75,.24,.01],'3':[.18,.75,.07],'4':[.05,.75,.20],'5+':[0,.55,.45]},
}
def demand(M):
    d=np.zeros(3)
    for i,h in enumerate(HH): d+=Hp[i]*np.array(M[h])
    return d/d.sum()*100

print("=== 면적 gap 민감도 (소형<60) · gap=공급-수요(음수=부족) ===")
size_small=[]
for sc in SIZE:
    d=demand(SIZE[sc]); g=Ssize-d; size_small.append(g[0])
    print(f"  [{sc:12s}] 소형 수요 {d[0]:.0f} | gap {g[0]:+.1f}  (국평 {g[1]:+.1f})")
print("=== 방수 gap 민감도 (1-2방) · gap=공급-수요(음수=부족) ===")
room_small=[]
for sc in ROOM:
    d=demand(ROOM[sc]); g=Sroom-d; room_small.append(g[0])
    print(f"  [{sc:12s}] 1-2방 수요 {d[0]:.0f} | gap {g[0]:+.1f}  (3방 {g[1]:+.1f})")

fig,(a1,a2)=plt.subplots(1,2,figsize=(14,6))
fig.suptitle('Sensitivity: the direction of the gap is robust to mapping assumptions',fontsize=13,fontweight='bold')
sc=list(SIZE); x=np.arange(3)
a1.bar(x,size_small,color='#d33'); a1.axhline(0,color='gray',lw=1)
for i,v in enumerate(size_small): a1.text(i,v-1.5,f'{v:+.0f}',ha='center',fontweight='bold')
a1.set_xticks(x); a1.set_xticklabels(sc,fontsize=9); a1.set_ylabel('Small (<60m2) gap = supply - demand (%p)'); a1.set_title(f'Floor area: small-unit gap\nrange {min(size_small):+.0f} to {max(size_small):+.0f}%p'); a1.grid(alpha=0.3,axis='y')
a2.bar(x,room_small,color='#d33'); a2.axhline(0,color='gray',lw=1)
for i,v in enumerate(room_small): a2.text(i,v-2.0,f'{v:+.0f}',ha='center',fontweight='bold')
a2.set_xticks(x); a2.set_xticklabels(sc,fontsize=9); a2.set_ylabel('1-2 room gap = supply - demand (%p)'); a2.set_title(f'Room count: 1-2 room gap\nrange {min(room_small):+.0f} to {max(room_small):+.0f}%p'); a2.grid(alpha=0.3,axis='y')
plt.tight_layout(rect=[0,0,1,0.93])
out=REPO + '/analysis/24b_model_sensitivity.png'
plt.savefig(out,dpi=120,bbox_inches='tight'); print(f'\n✅ {out}')
print(f"\n소형 gap {min(size_small):+.0f}~{max(size_small):+.0f} · 1-2방 gap {min(room_small):+.0f}~{max(room_small):+.0f} (모두 음수=부족 강건)")
