"""[EN] Annual housing-design roadmap derived from the age-inflow chain.
#P1~P3 (v7 §IV.9) — 연도별 설계 로드맵. 연령유입 예측 → 가구화 → 평형·방수·점유별 필요 세대수.
유입 예측: 선형(최근 3년 기울기, backcast MAPE 5.6% — 로지스틱 33.8%보다 우수), 계획 K=144,173 상한 clip.
가구화: 고덕 특화 재캘리브레이션(32) — 지수기울기로 평균 가구원수 m̄ 밴드(2.99~3.46) 반영.
출력: employment/godeok_design_roadmap.csv + 그림 33
"""
import os as _os; REPO = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import os,sys,csv
import numpy as np
from scipy.optimize import brentq
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Helvetica'; plt.rcParams['axes.unicode_minus']=False
POP='/Users/Shared/seoyeon_research/population'; EMP='/Users/Shared/seoyeon_research/employment'
HH=['1','2','3','4','5+']; SZ=np.array([1,2,3,4,5.5])
K_POP=144173.0; PLAN_HH=58300; BUILT=22368
# ── 연령군 모수(실측) ──
GRP={'Children 0-14':(0.0,[0,0,0,0,0]),'Youth 15-24':(0.0922,[.8378,.1362,.0198,.0051,.0011]),
     'Core 25-39':(0.5065,[.5059,.2169,.1580,.0977,.0215]),'Mid 40-54':(0.5701,[.2755,.1892,.2204,.2434,.0714]),
     'Senior 55-64':(0.5859,[.2934,.3390,.2265,.1154,.0257]),'65+':(0.5698,[.3667,.4447,.1367,.0374,.0145])}
PROF={'Children 0-14':13717,'Youth 15-24':3825,'Core 25-39':24986,'Mid 40-54':15902,'Senior 55-64':5075,'65+':3152}
W={k:v/sum(PROF.values()) for k,v in PROF.items()}     # 유입 연령 프로파일(실측 고정)
MA={'1':[.85,.15,0],'2':[.50,.45,.05],'3':[.10,.75,.15],'4':[.03,.62,.35],'5+':[0,.45,.55]}
MR={'1':[.90,.10,0],'2':[.60,.38,.02],'3':[.10,.82,.08],'4':[.03,.72,.25],'5+':[0,.45,.55]}
T=[[.21,.11,.68],[.41,.27,.32],[.36,.25,.39]]
SUP_A=np.array([30.1,59.0,11.0])/100; SUP_R=np.array([7.0,78.4,14.6])/100

# ── 유입 예측: 선형(최근 3년) + K clip ──
rows=list(csv.DictReader(open(f'{POP}/godeok_age_year_matrix.csv')))
yr=np.array([int(r['year']) for r in rows]); tot=np.array([int(r['계']) for r in rows],float)
slope=(tot[-1]-tot[-3])/2.0
print(f"최근 3년 기울기 = {slope:,.0f}명/년 (2023→2025) · 2025 실측 {tot[-1]:,.0f} · 계획 K {K_POP:,.0f}")
FUT=np.arange(2026,2036); P=[]; cur=tot[-1]
for _ in FUT: cur=min(cur+slope,K_POP); P.append(cur)
P=np.array(P); infl=np.diff(np.concatenate([[tot[-1]],P]))     # 연도별 순유입
print(f"예측 2030 {P[4]:,.0f}명({P[4]/K_POP*100:.0f}%) · 2035 {P[-1]:,.0f}명({P[-1]/K_POP*100:.0f}%) · 포화 도달 {FUT[np.argmax(P>=K_POP-1)] if (P>=K_POP-1).any() else '미도달'}")

def tilt(q,m):
    """p_h ∝ q_h·exp(λh) s.t. Σp·h=m. log-sum-exp 안정화."""
    def norm(l):
        z=l*SZ; z=z-z.max(); w=q*np.exp(z); return w/w.sum()
    l=brentq(lambda l:(norm(l)*SZ).sum()-m,-6,6,xtol=1e-12); return norm(l)
def chain(n_total,m):
    if n_total<=0:      # 계획 수용인구 포화 후 순유입 소멸 → 신규 수요 0
        return 0.0,np.zeros(5),np.zeros(3),np.zeros(3),np.zeros(3)
    q=np.zeros(5)
    for k,(rho,pha) in GRP.items(): q+=n_total*W[k]*rho*np.array(pha)
    q=q/q.sum(); p=tilt(q,m); H=n_total/m
    dA=np.zeros(3); dR=np.zeros(3)
    for i,h in enumerate(HH): dA+=p[i]*np.array(MA[h]); dR+=p[i]*np.array(MR[h])
    pA=dA/dA.sum(); pR=dR/dR.sum()
    ten=np.zeros(3)
    for s in range(3): ten+=pA[s]*np.array(T[s])
    return H,p,pA,pR,ten

SCEN={'low m=2.99':2.99,'base m=3.23':3.23,'high m=3.46':3.46}
out={}
for nm,m in SCEN.items():
    rec=[]
    for y,n in zip(FUT,infl):
        H,p,pA,pR,ten=chain(n,m)
        rec.append(dict(year=y,inflow=n,H=H,small=pA[0]*H,std=pA[1]*H,large=pA[2]*H,
                        r12=pR[0]*H,r3=pR[1]*H,r4=pR[2]*H,wolse=ten[2]*H,one=p[0]))
    out[nm]=rec
base=out['base m=3.23']
print(f"\n{'연도':<6}{'유입':>8}{'신규가구':>9} | {'Small':>7}{'Standard':>7}{'Large':>7} | {'1-2방':>7}{'3방':>7}{'4방+':>7} | {'월세':>7}")
for r in base:
    print(f"{r['year']:<6}{r['inflow']:>8,.0f}{r['H']:>9,.0f} | {r['small']:>7,.0f}{r['std']:>7,.0f}{r['large']:>7,.0f} | {r['r12']:>7,.0f}{r['r3']:>7,.0f}{r['r4']:>7,.0f} | {r['wolse']:>7,.0f}")
cum={k:sum(r['H'] for r in v) for k,v in out.items()}
print(f"\n10년 누적 신규가구: 보수 {cum['low m=2.99']:,.0f} / 기준 {cum['base m=3.23']:,.0f} / 상한 {cum['high m=3.46']:,.0f} 세대")
print(f"계획 잔여 {PLAN_HH-BUILT:,}세대 대비 기준 시나리오 {cum['base m=3.23']/(PLAN_HH-BUILT)*100:.0f}%")
cumA={k:[sum(r[c] for r in v) for c in ['small','std','large']] for k,v in out.items()}
print(f"누적 면적 배합(기준): 소형 {cumA['base m=3.23'][0]:,.0f} / 국평 {cumA['base m=3.23'][1]:,.0f} / 대형 {cumA['base m=3.23'][2]:,.0f} 세대")

with open(f'{EMP}/godeok_design_roadmap.csv','w',newline='') as f:
    w=csv.writer(f); w.writerow(['scenario','year','inflow','new_hh','small','std','large','r12','r3','r4plus','wolse','one_ratio'])
    for nm,rec in out.items():
        for r in rec: w.writerow([nm,r['year'],f"{r['inflow']:.0f}",f"{r['H']:.0f}",f"{r['small']:.0f}",f"{r['std']:.0f}",
                                  f"{r['large']:.0f}",f"{r['r12']:.0f}",f"{r['r3']:.0f}",f"{r['r4']:.0f}",f"{r['wolse']:.0f}",f"{r['one']:.4f}"])
print(f"✅ {EMP}/godeok_design_roadmap.csv")

# ── 그림 ──
fig,ax=plt.subplots(1,3,figsize=(17,5.4))
fig.suptitle('Annual design roadmap: age-inflow forecast (linear, backcast MAPE 5.6%) x Godeok-specific household formation',fontsize=13,fontweight='bold')
Y=[r['year'] for r in base]
# (1) 인구 궤적
ax[0].plot(yr,tot/1000,'o-',color='#c33',lw=2,label='observed')
ax[0].plot(FUT,P/1000,'s--',color='#37a',label='forecast (linear)')
ax[0].axhline(K_POP/1000,color='gray',ls=':'); ax[0].text(2014,K_POP/1000+3,'Planned capacity 144k',fontsize=8,color='gray')
ax[0].set_xlabel('Year'); ax[0].set_ylabel('Population (thousands)'); ax[0].set_title('(1) Population trajectory and forecast'); ax[0].legend(fontsize=9); ax[0].grid(alpha=0.3)
# (2) 연도별 면적 배합 스택
sm=[r['small'] for r in base]; st=[r['std'] for r in base]; lg=[r['large'] for r in base]
ax[1].bar(Y,sm,color='#4a7fb5',label='Small <60m2')
ax[1].bar(Y,st,bottom=sm,color='#7aa95c',label='Standard 60-85m2')
ax[1].bar(Y,lg,bottom=np.array(sm)+np.array(st),color='#c58b3d',label='Large 85+m2')
ax[1].set_xlabel('Year'); ax[1].set_ylabel('New units required'); ax[1].set_title('(2) Required units by size and year (base m=3.23)')
ax[1].legend(fontsize=8); ax[1].grid(alpha=0.3,axis='y')
# (3) 시나리오 밴드(누적)
labels=['Small','Standard','Large']; x=np.arange(3); w=0.26
for j,(nm,v) in enumerate(cumA.items()):
    ax[2].bar(x+(j-1)*w,v,w,label=nm)
for i in x: ax[2].text(i,max(v[i] for v in cumA.values())*1.03,'',ha='center')
ax[2].set_xticks(x); ax[2].set_xticklabels(labels); ax[2].set_ylabel('Cumulative units, 10 years')
ax[2].set_title('(3) Cumulative mix by scenario (uncertainty band)'); ax[2].legend(fontsize=8); ax[2].grid(alpha=0.3,axis='y')
plt.tight_layout(rect=[0,0,1,0.92])
o=REPO + '/analysis/33_annual_design_roadmap.png'
plt.savefig(o,dpi=120,bbox_inches='tight'); print(f'✅ {o}')
