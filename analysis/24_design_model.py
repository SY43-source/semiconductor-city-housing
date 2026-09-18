"""[EN] Age-inflow-to-housing-design prediction chain (SS IV.7).
#P2 — 연령기반 주거설계 예측모델(사슬 구현). §4.8.
연령유입 nₐ(고덕) → 가구화 Hₕ=Σₐ nₐ·ρₐ·P(h|a) → 규격/방수/점유 수요 + 1인율 → 공급대비 gap.
P1 데이터: 고덕 5세별(DT_1B04005N), 헤드십(pyeongtaek_headship_2024), P(h|a)(pyeongtaek_head_age_hhsize_2024),
 점유 T(godeok_tenure_by_size), 공급 방수·면적(sqlite).
규격/방수 매핑 M은 문헌·상식 가정(민감도 후속). 점유 T·가구화는 실측.
"""
import os as _os; REPO = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
DATA_ROOT = _os.environ.get('DATA_ROOT', '/Users/Shared/seoyeon_research')
INVENTORY_DB = _os.environ.get('INVENTORY_DB', '/Users/Shared/seoyeon_inventory_master.sqlite')
import os,sys,csv,sqlite3
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='AppleGothic'; plt.rcParams['axes.unicode_minus']=False
sys.path.insert(0, os.path.join(os.path.dirname(__file__),'..','src'))
from kosis_client import kosis_get
EMP=DATA_ROOT + '/employment'; DB=INVENTORY_DB
HH=['1인','2인','3인','4인','5인+']

# ── 1) 고덕 연령유입 nₐ (2018→2025 순증), 가구주연령 밴드(20-24..85+) ──
BANDS=[('20~24세','20 - 24세'),('25~29세','25 - 29세'),('30~34세','30 - 34세'),('35~39세','35 - 39세'),
       ('40~44세','40 - 44세'),('45~49세','45 - 49세'),('50~54세','50 - 54세'),('55~59세','55 - 59세'),
       ('60~64세','60 - 64세'),('65~69세','65 - 69세'),('70~74세','70 - 74세'),('75~79세','75 - 79세'),
       ('80~84세','80 - 84세'),('85+','85세이상')]
def godeok_pop(year):
    p={}
    for code in ['4122033000','4122066000']:  # 고덕면+고덕동(신도시 이후 신설 → 초기 연도 미존재 가능)
        d=kosis_get({'method':'getList','orgId':'101','tblId':'DT_1B04005N',
            'objL1':code,'objL2':'ALL','itmId':'T2','prdSe':'Y','startPrdDe':str(year),'endPrdDe':str(year)})
        if not isinstance(d,list): continue   # err dict(미존재 동) 스킵
        for x in d:
            if x.get('DT') is not None: p[x['C2_NM']]=p.get(x['C2_NM'],0)+int(x['DT'])
    return p
p18,p25=godeok_pop(2018),godeok_pop(2025)
inflow={b:(p25.get(pl,0)-p18.get(pl,0)) for b,pl in BANDS}

# ── 2) 헤드십 ρₐ, P(h|a) ──
rho={r['age_band']:float(r['headship']) for r in csv.DictReader(open(f'{EMP}/pyeongtaek_headship_2024.csv'))}
rho['85+']=rho.get('85+',0) or 0.56   # 85+ pop라벨 불일치 보정(이웃값)
Pha={}
for r in csv.DictReader(open(f'{EMP}/pyeongtaek_head_age_hhsize_2024.csv')):
    a=r['age'].replace(' ',''); vec=np.array([float(r[h]) for h in HH]); s=vec.sum()
    if s>0: Pha[a]=vec/s

# ── 3) 가구화: new_heads_a = nₐ·ρₐ ; Hₕ=Σ new_heads·P(h|a) ──
H=np.zeros(len(HH)); new_heads_total=0
for b,_ in BANDS:
    key=b.replace(' ','')
    if key not in Pha: continue
    nh=inflow[b]*rho.get(b,0); new_heads_total+=nh
    H+=nh*Pha[key]
H=np.maximum(H,0); Hsum=H.sum(); Hp=H/Hsum
one_ratio=Hp[0]*100
print("=== 연령유입 기반 신규가구 구성 (고덕 2018→2025) ===")
print(f"신규 가구주 추정 {new_heads_total:,.0f} · 신규가구 {Hsum:,.0f}")
for i,h in enumerate(HH): print(f"  {h}: {Hp[i]*100:.1f}%")
print(f"★ 1인가구 비율(신규 유입) = {one_ratio:.1f}%")

# ── 4) 규격수요 (M^size, 가정) vs 공급(고덕 실측) ──
Msize={'1인':[.85,.15,0],'2인':[.50,.45,.05],'3인':[.10,.75,.15],'4인':[.03,.62,.35],'5인+':[0,.45,.55]}
Dsize=np.zeros(3)
for i,h in enumerate(HH): Dsize+=H[i]*np.array(Msize[h])
Dsize=Dsize/Dsize.sum()*100
con=sqlite3.connect(DB)
def supply_size():
    q="""SELECT CASE WHEN p.exclusive_area_m2<60 THEN 0 WHEN p.exclusive_area_m2<85 THEN 1 ELSE 2 END b,SUM(p.units_of_same_area)
     FROM complexes c JOIN pyeong_types p ON c.complex_number=p.complex_number
     WHERE c.bjd_code LIKE '41220%' AND (c.sector LIKE '%고덕%' OR c.road_name LIKE '%고덕%') AND p.units_of_same_area>0 GROUP BY b"""
    s=np.zeros(3)
    for b,u in con.execute(q): s[b]=u
    return s/s.sum()*100
Ssize=supply_size()

# ── 5) 방수수요 (M^room, 가정) vs 공급(room_count 실측) ──
Mroom={'1인':[.90,.10,0],'2인':[.60,.38,.02],'3인':[.10,.82,.08],'4인':[.03,.72,.25],'5인+':[0,.45,.55]}  # [1-2방,3방,4방+]
Droom=np.zeros(3)
for i,h in enumerate(HH): Droom+=H[i]*np.array(Mroom[h])
Droom=Droom/Droom.sum()*100
def supply_room():
    q="""SELECT CASE WHEN p.room_count<=2 THEN 0 WHEN p.room_count=3 THEN 1 ELSE 2 END b,SUM(p.units_of_same_area)
     FROM complexes c JOIN pyeong_types p ON c.complex_number=p.complex_number
     WHERE c.bjd_code LIKE '41220%' AND (c.sector LIKE '%고덕%' OR c.road_name LIKE '%고덕%') AND p.units_of_same_area>0 AND p.room_count IS NOT NULL GROUP BY b"""
    s=np.zeros(3)
    for b,u in con.execute(q): s[b]=u
    return s/s.sum()*100
Sroom=supply_room(); con.close()

# ── 6) 점유수요 D^tenure = Σ_s Dsize_s · T[s] (T 고덕 실측) ──
T={r['size_band']:[float(r['p_sale']),float(r['p_jeonse']),float(r['p_wolse'])]
   for r in csv.DictReader(open(f'{EMP}/godeok_tenure_by_size.csv'))}
order=['소형<60','국평60-85','대형85+']
Dten=np.zeros(3)
for i,s in enumerate(order): Dten+=(Dsize[i]/100)*np.array(T[s])
Dten=Dten/Dten.sum()*100

print("\n=== 규격 수요 vs 공급 (%) · gap=공급-수요(음수=부족) ===")
for i,l in enumerate(['소형<60','국평60-85','대형85+']):
    print(f"  {l:9s} 수요 {Dsize[i]:5.1f} | 공급 {Ssize[i]:5.1f} | gap {Ssize[i]-Dsize[i]:+5.1f}")
print("=== 방수 수요 vs 공급 (%) · gap=공급-수요(음수=부족) ===")
for i,l in enumerate(['1-2방','3방','4방+']):
    print(f"  {l:6s} 수요 {Droom[i]:5.1f} | 공급 {Sroom[i]:5.1f} | gap {Sroom[i]-Droom[i]:+5.1f}")
print("=== 점유 수요 (매매/전세/월세, %) ===")
for i,l in enumerate(['매매','전세','월세']): print(f"  {l} {Dten[i]:.1f}")

# ── 7) 시각화 ──
fig,ax=plt.subplots(2,2,figsize=(15,10))
fig.suptitle(f'연령유입 기반 주거설계 예측모델 — 고덕 (신규 유입 1인가구 {one_ratio:.0f}%)',fontsize=14,fontweight='bold')
def gapbar(a,labels,dem,sup,title):
    x=np.arange(len(labels)); w=0.38
    a.bar(x-w/2,dem,w,label='수요(모델)',color='#2a8'); a.bar(x+w/2,sup,w,label='공급(실측)',color='#c62')
    for i in x:
        a.text(i-w/2,dem[i]+0.8,f'{dem[i]:.0f}',ha='center',fontsize=8.5)
        a.text(i+w/2,sup[i]+0.8,f'{sup[i]:.0f}',ha='center',fontsize=8.5)
    a.set_xticks(x); a.set_xticklabels(labels); a.set_ylabel('%'); a.set_title(title); a.legend(fontsize=9); a.grid(alpha=0.3,axis='y')
gapbar(ax[0,0],['소형<60','국평60-85','대형85+'],Dsize,Ssize,'① 면적 규격 수요 vs 공급')
gapbar(ax[0,1],['1-2방','3방','4방+'],Droom,Sroom,'② 방수 수요 vs 공급')
# 가구구성
ax[1,0].bar(range(len(HH)),Hp*100,color=['#37a','#4a9','#7b6','#c94','#a44'])
for i in range(len(HH)): ax[1,0].text(i,Hp[i]*100+0.6,f'{Hp[i]*100:.0f}',ha='center',fontsize=9)
ax[1,0].set_xticks(range(len(HH))); ax[1,0].set_xticklabels(HH); ax[1,0].set_ylabel('%')
ax[1,0].set_title(f'③ 신규 유입 가구원수 구성 (1인 {one_ratio:.0f}%)'); ax[1,0].grid(alpha=0.3,axis='y')
# 점유
ax[1,1].bar(['매매','전세','월세'],Dten,color=['#c62','#2a8','#39c'])
for i,v in enumerate(Dten): ax[1,1].text(i,v+0.8,f'{v:.0f}%',ha='center',fontsize=10,fontweight='bold')
ax[1,1].set_ylabel('%'); ax[1,1].set_title('④ 점유 형태 수요 (매매/전세/월세)'); ax[1,1].grid(alpha=0.3,axis='y')
plt.tight_layout(rect=[0,0,1,0.95])
out=REPO + '/analysis/24_design_model.png'
plt.savefig(out,dpi=120,bbox_inches='tight'); print(f'\n✅ {out}')
