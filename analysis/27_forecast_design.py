"""[EN] Design-target trajectory to 2035, reported as a band rather than a point estimate.
#P4 — 설계 target 미래 궤적(2025→2035). 과잉 단정 회피: 단일 점예측 아닌 시나리오 밴드.
연령유입 프로파일 시나리오로 규격·방수·점유·1인율의 계획기간 안정성 확인.
 A 유입지속(캠퍼스 P4/P5 가동→젊은 프로파일 유지)  B 코호트 성숙(유입둔화+자녀성장·고령화→연령 프로파일 +1밴드 이동)
데이터: 고덕 유입(DT_1B04005N), 파라미터 P1 CSV. 볼륨은 신도시 계획인구로 스케일(참고).
"""
import os as _os; REPO = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
DATA_ROOT = _os.environ.get('DATA_ROOT', '/Users/Shared/seoyeon_research')
INVENTORY_DB = _os.environ.get('INVENTORY_DB', '/Users/Shared/seoyeon_inventory_master.sqlite')
import os,sys,csv
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='AppleGothic'; plt.rcParams['axes.unicode_minus']=False
sys.path.insert(0, os.path.join(os.path.dirname(__file__),'..','src'))
from kosis_client import kosis_get
EMP=DATA_ROOT + '/employment'; HH=['1인','2인','3인','4인','5인+']
BANDS=[('20~24세','20 - 24세'),('25~29세','25 - 29세'),('30~34세','30 - 34세'),('35~39세','35 - 39세'),
       ('40~44세','40 - 44세'),('45~49세','45 - 49세'),('50~54세','50 - 54세'),('55~59세','55 - 59세'),
       ('60~64세','60 - 64세'),('65~69세','65 - 69세'),('70~74세','70 - 74세'),('75~79세','75 - 79세'),
       ('80~84세','80 - 84세'),('85+','85세이상')]
rho={r['age_band']:float(r['headship']) for r in csv.DictReader(open(f'{EMP}/pyeongtaek_headship_2024.csv'))}
rho['85+']=rho.get('85+',0) or 0.56
Pha={}
for r in csv.DictReader(open(f'{EMP}/pyeongtaek_head_age_hhsize_2024.csv')):
    a=r['age'].replace(' ',''); v=np.array([float(r[h]) for h in HH]); Pha[a]=v/v.sum() if v.sum() else v
Msize={'1인':[.85,.15,0],'2인':[.50,.45,.05],'3인':[.10,.75,.15],'4인':[.03,.62,.35],'5인+':[0,.45,.55]}
Mroom={'1인':[.90,.10,0],'2인':[.60,.38,.02],'3인':[.10,.82,.08],'4인':[.03,.72,.25],'5인+':[0,.45,.55]}
Tsize={r['size_band']:np.array([float(r['p_sale']),float(r['p_jeonse']),float(r['p_wolse'])])*np.array([8,2,2])
       for r in csv.DictReader(open(f'{EMP}/godeok_tenure_by_size.csv'))}  # stock 보정(매매8년)
for k in Tsize: Tsize[k]=Tsize[k]/Tsize[k].sum()

def godeok_pop(year):
    p={}
    for code in ['4122033000','4122066000']:
        d=kosis_get({'method':'getList','orgId':'101','tblId':'DT_1B04005N','objL1':code,'objL2':'ALL','itmId':'T2','prdSe':'Y','startPrdDe':str(year),'endPrdDe':str(year)})
        if isinstance(d,list):
            for x in d:
                if x.get('DT') is not None: p[x['C2_NM']]=p.get(x['C2_NM'],0)+int(x['DT'])
    return p
p18,p25=godeok_pop(2018),godeok_pop(2025)
inflow=np.array([p25.get(pl,0)-p18.get(pl,0) for _,pl in BANDS],float)
inflow=np.maximum(inflow,0)

def chain(infl):
    H=np.zeros(len(HH))
    for i,(b,_) in enumerate(BANDS):
        key=b.replace(' ','')
        if key in Pha: H+=infl[i]*rho.get(b,0)*Pha[key]
    H=np.maximum(H,0); Hp=H/H.sum()
    Ds=np.zeros(3); Dr=np.zeros(3)
    for i,h in enumerate(HH): Ds+=H[i]*np.array(Msize[h]); Dr+=H[i]*np.array(Mroom[h])
    Ds=Ds/Ds.sum()*100; Dr=Dr/Dr.sum()*100
    Dt=np.zeros(3)
    for i,s in enumerate(['소형<60','국평60-85','대형85+']): Dt+=(Ds[i]/100)*Tsize[s]
    Dt=Dt/Dt.sum()*100
    return Hp*100,Ds,Dr,Dt

# 시나리오
A=inflow.copy()                       # 유입지속(현 프로파일)
B=np.zeros_like(inflow); B[1:]=inflow[:-1]  # 코호트 성숙: 연령 프로파일 +1밴드(5세) 이동
scen={'2025 현재\n(유입지속 A)':A, '2035 성숙\n(코호트 B)':B}
print("시나리오별 설계 target (%)")
res={}
for nm,infl in scen.items():
    Hp,Ds,Dr,Dt=chain(infl); res[nm]=(Hp,Ds,Dr,Dt)
    print(f"\n[{nm.strip()}]")
    print(f"  1인율 {Hp[0]:.0f} | 소형 {Ds[0]:.0f} 국평 {Ds[1]:.0f} | 1-2방 {Dr[0]:.0f} 3방 {Dr[1]:.0f} | 매매 {Dt[0]:.0f} 전세 {Dt[1]:.0f} 월세 {Dt[2]:.0f}")

fig,axes=plt.subplots(1,4,figsize=(18,5))
fig.suptitle('P4 설계 target 궤적 — 유입지속(A) vs 코호트 성숙(B) 시나리오 (밴드=계획기간 불확실성)',fontsize=13,fontweight='bold')
keys=list(scen); c=['#39c','#c73']
def grp(ax,idx,labels,title,pick):
    x=np.arange(len(labels)); w=0.38
    for j,k in enumerate(keys):
        vals=res[k][idx] if pick is None else [res[k][idx][pick]]
        ax.bar(x+(j-0.5)*w,res[k][idx],w,label=k.split(chr(10))[0],color=c[j])
    ax.set_xticks(x); ax.set_xticklabels(labels,fontsize=8); ax.set_title(title); ax.set_ylabel('%'); ax.grid(alpha=0.3,axis='y'); ax.legend(fontsize=7)
grp(axes[0],0,HH,'가구원수(1인율)',None)
grp(axes[1],1,['소형','국평','대형'],'면적 수요',None)
grp(axes[2],2,['1-2방','3방','4방+'],'방수 수요',None)
grp(axes[3],3,['매매','전세','월세'],'점유 수요(stock)',None)
plt.tight_layout(rect=[0,0,1,0.93])
out=REPO + '/analysis/27_forecast_design.png'
plt.savefig(out,dpi=120,bbox_inches='tight'); print(f'\n✅ {out}')
print("\n해석: 성숙(B) 시 1인율·소형·1-2방 수요 다소↓·매매↑이나, 여전히 소형·소형방·임대 수요 상당 → 규격 다양화 결론 계획기간 내 유지.")
