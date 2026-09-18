"""[EN] Barbell shape of the room-count mismatch (SS IV.4).
#v7 §IV.4 보강 — 분포 형태로 본 수급 미스매치.
① 공급(면적) = 고덕 아파트 전용면적 **실측** 분포(세대수 가중) → 84~85㎡ 한 규격에 절반 집중
② 수요(면적) = 가구원수별 선호면적 N(μ_h,σ_h)를 재캘리브 p_h로 가중한 혼합분포
   ⚠️ μ_h·σ_h는 논문 규격매핑 M^A의 밴드확률을 재현하도록 격자탐색으로 캘리브(오차 ≤0.02) → 임의 가정 아님
③ 방수(이산) = 수요 vs 공급 → **양극(barbell): 1-2방·4방+ 부족, 3방 과잉**
★ 검증 결과: barbell은 **방수 축**의 현상이며, 면적 축은 '대형 부족' 단방향(수요는 가족쪽 단봉).
"""
import os as _os; REPO = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
DATA_ROOT = _os.environ.get('DATA_ROOT', '/Users/Shared/seoyeon_research')
INVENTORY_DB = _os.environ.get('INVENTORY_DB', '/Users/Shared/seoyeon_inventory_master.sqlite')
import os,sqlite3
import numpy as np
from scipy.stats import norm, gaussian_kde
from scipy.optimize import brentq
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='AppleGothic'; plt.rcParams['axes.unicode_minus']=False
DB=INVENTORY_DB
HH=['1인','2인','3인','4인','5인+']; SZ=np.array([1,2,3,4,5.5])
PREF={'1인':(42,18),'2인':(60,15),'3인':(74,11),'4인':(81,11),'5인+':(86,8)}   # M^A 정합 캘리브
MA={'1인':[.85,.15,0],'2인':[.50,.45,.05],'3인':[.10,.75,.15],'4인':[.03,.62,.35],'5인+':[0,.45,.55]}
MR={'1인':[.90,.10,0],'2인':[.60,.38,.02],'3인':[.10,.82,.08],'4인':[.03,.72,.25],'5인+':[0,.45,.55]}
SUP_R=np.array([7.0,78.4,14.6])
print("PREF 정합 점검 (밴드확률 vs M^A)")
for h,(mu,sg) in PREF.items():
    p=[norm.cdf(60,mu,sg),norm.cdf(85,mu,sg)-norm.cdf(60,mu,sg),1-norm.cdf(85,mu,sg)]
    print(f"  {h:<5} [{p[0]:.2f} {p[1]:.2f} {p[2]:.2f}] vs {MA[h]}")

# 공급 실측(면적)
con=sqlite3.connect(DB)
rows=con.execute("""SELECT p.exclusive_area_m2,p.units_of_same_area FROM complexes c
 JOIN pyeong_types p ON c.complex_number=p.complex_number
 WHERE c.bjd_code LIKE '41220%' AND (c.sector LIKE '%고덕%' OR c.road_name LIKE '%고덕%')
   AND p.units_of_same_area>0 AND p.exclusive_area_m2 IS NOT NULL""").fetchall()
con.close()
A=np.array([r[0] for r in rows]); U=np.array([r[1] for r in rows],float); TOT=U.sum()
# 1㎡ 버킷 집계(같은 면적 여러 단지 합산)
bins=np.arange(np.floor(A.min()),np.ceil(A.max())+2,1.0)
hist,_=np.histogram(A,bins=bins,weights=U); ctr=(bins[:-1]+bins[1:])/2
imax=int(np.argmax(hist)); print(f"\n공급 최다 규격 {ctr[imax]:.0f}㎡ = {hist[imax]:,.0f}세대 ({hist[imax]/TOT*100:.1f}%)")
m84=hist[(ctr>=83.5)&(ctr<=85.5)].sum(); print(f"84~85㎡ 합계 {m84:,.0f}세대 ({m84/TOT*100:.1f}%)")

# 규격군: 1㎡ 버킷을 연속 정수구간(run)으로 병합 = 실무 규격군
_b={}
for a_,u_ in zip(A,U): _b[int(round(a_))]=_b.get(int(round(a_)),0)+u_
_ks=sorted(_b); _runs=[]; _cur=[_ks[0]]
for _k in _ks[1:]:
    if _k-_cur[-1]<=1: _cur.append(_k)
    else: _runs.append(_cur); _cur=[_k]
_runs.append(_cur)
GRP=[(f"{r[0]}~{r[-1]}" if len(r)>1 else f"{r[0]}", sum(_b[k] for k in r)) for r in _runs]
GRP.sort(key=lambda t:-t[1])
gs=np.array([u for _,u in GRP]); gcum=np.cumsum(gs)/TOT*100
print(f"규격군 {len(GRP)}개 · 상위1 {gs[0]/TOT*100:.1f}% · 상위2 {gcum[1]:.1f}% · 상위3 {gcum[2]:.1f}%")

# 수요 분포
Q=np.array([0.393,0.236,0.186,0.146,0.039]); Q/=Q.sum()
def tilt(q,m):
    def nrm(l):
        z=l*SZ; z-=z.max(); w=q*np.exp(z); return w/w.sum()
    l=brentq(lambda l:(nrm(l)*SZ).sum()-m,-6,6,xtol=1e-12); return nrm(l)
P7=tilt(Q,3.23); P6=np.array([.3754,.2745,.1862,.1340,.0300]); P6/=P6.sum()
print("수요 p_h (v7 m̄=3.23):"," ".join(f"{h} {v*100:.0f}%" for h,v in zip(HH,P7)))
x=np.linspace(35,125,600)
def mix(p):
    c=np.array([p[i]*norm.pdf(x,*PREF[h]) for i,h in enumerate(HH)]); return c,c.sum(0)
c7,d7=mix(P7); _,d6=mix(P6)
kde=gaussian_kde(A,weights=U,bw_method=0.16); sup=kde(x)
def npk(y): return sum(1 for i in range(1,len(y)-1) if y[i]>y[i-1] and y[i]>=y[i+1] and y[i]>0.10*y.max())
print(f"봉우리 — 수요 {npk(d7)}개 / 공급 {npk(sup)}개  → 면적축 barbell 미성립")
# 방수 수요
dR=np.zeros(3)
for k,h in enumerate(HH): dR+=P7[k]*np.array(MR[h])
dR=dR/dR.sum()*100; gR=SUP_R-dR
print(f"방수 수요 {dR.round(1)} vs 공급 {SUP_R} → gap {gR.round(1)}  (1-2방·4방+ 부족, 3방 과잉 = barbell)")

# ── 그림 ──
fig,ax=plt.subplots(1,3,figsize=(17.5,5.7))
fig.suptitle('분포 형태로 본 수급 미스매치 — 면적축은 "대형 부족", 방수축은 "양극(barbell) 부족"',fontsize=13.5,fontweight='bold')
C=['#3a7ca5','#4f9d69','#c99a3b','#c1553b','#8e4a7d']
ax[1].axvline(60,color='#aaa',ls=':',lw=1); ax[1].axvline(85,color='#aaa',ls=':',lw=1)
ax[1].set_xlim(35,125); ax[1].set_xlabel('전용면적 (㎡)')

# ① 공급 실측 — 파레토(규격군 내림차순 + 누적)
NT=8
lab1=[g[0] for g in GRP[:NT]]+['기타']
val1=list(gs[:NT]/TOT*100)+[gs[NT:].sum()/TOT*100]
xi1=np.arange(len(lab1))
cols=['#a93226' if k==0 else '#aeb6bf' for k in range(len(lab1))]
ax[0].bar(xi1,val1,color=cols,width=0.7)
for k,v in enumerate(val1):
    if v>=1.0: ax[0].text(k,v+1.2,f'{v:.1f}',ha='center',fontsize=8.5,fontweight='bold' if k==0 else 'normal')
ax[0].set_xticks(xi1); ax[0].set_xticklabels(lab1,fontsize=7.5,rotation=38,ha='right')
ax[0].set_ylabel('세대 비중 (%)'); ax[0].set_ylim(0,68)
ax[0].set_xlabel('전용면적 규격군 (㎡, 세대수 내림차순)')
a0b=ax[0].twinx()
a0b.plot(xi1,list(gcum[:NT])+[100.0],'o-',color='#2c3e50',lw=1.6,ms=4,label='누적 비중')
a0b.set_ylim(0,105); a0b.set_ylabel('누적 비중 (%)',fontsize=9); a0b.grid(False)
a0b.axhline(gcum[2],color='#2c3e50',ls=':',lw=1)
a0b.annotate(f'상위 3개 규격군\n= 전체의 {gcum[2]:.1f}%',xy=(2,gcum[2]),xytext=(3.1,58),fontsize=9,color='#2c3e50',
  fontweight='bold',arrowprops=dict(arrowstyle='->',color='#2c3e50'))
ax[0].annotate(f'{GRP[0][0]}㎡ 한 규격군에\n{gs[0]/TOT*100:.1f}%',xy=(0,val1[0]),xytext=(0.55,val1[0]+4),
  fontsize=9.5,fontweight='bold',color='#a93226',arrowprops=dict(arrowstyle='->',color='#a93226'))
ax[0].set_title(f'① 공급(실측) — {len(GRP)}개 규격군 중 3개가 85%'); a0b.legend(fontsize=8,loc='center right')

# ② 면적: 수요 성분 + 공급 겹침
supn=sup/sup.sum(); d7n=d7/d7.sum(); d6n=d6/d6.sum()
for k,h in enumerate(HH):
    ax[1].fill_between(x,0,c7[k]/d7.sum(),color=C[k],alpha=0.16)
    ax[1].plot(x,c7[k]/d7.sum(),color=C[k],lw=1.1,ls='--',label=f'{h} {P7[k]*100:.0f}%')
ax[1].fill_between(x,0,supn,color='#aeb6bf',alpha=0.5,label='공급(실측)')
ax[1].plot(x,d7n,color='#a93226',lw=2.6,label='수요 합계(v7)')
ax[1].plot(x,d6n,color='#7f8c8d',lw=1.3,ls=':',label='수요(v6 가정)')
ax[1].fill_between(x,supn,d7n,where=(d7n>supn),color='#c0392b',alpha=0.28,interpolate=True)
ax[1].annotate('대형(≥85㎡) 부족',xy=(97,max(d7n[x>92])*0.8),xytext=(100,max(d7n)*0.55),fontsize=9,color='#c0392b',fontweight='bold')
ax[1].set_ylabel('정규화 밀도'); ax[1].set_title('② 면적 — 수요는 가족쪽 단봉, 대형 부족'); ax[1].legend(fontsize=7); ax[1].grid(alpha=0.25,axis='y')

# ③ 방수 — barbell
lab=['1–2방','3방','4방+']; xi=np.arange(3); w=0.36
ax[2].bar(xi-w/2,dR,w,color='#a93226',label='수요(모델)')
ax[2].bar(xi+w/2,SUP_R,w,color='#aeb6bf',label='공급(실측)')
for k in xi:
    ax[2].text(k-w/2,dR[k]+1,f'{dR[k]:.0f}',ha='center',fontsize=9)
    ax[2].text(k+w/2,SUP_R[k]+1,f'{SUP_R[k]:.0f}',ha='center',fontsize=9)
    col='#c0392b' if gR[k]<0 else '#2e7d32'
    ax[2].text(k,max(dR[k],SUP_R[k])+5.5,f'{gR[k]:+.0f}%p',ha='center',fontsize=10.5,fontweight='bold',color=col)
ax[2].set_xticks(xi); ax[2].set_xticklabels(lab); ax[2].set_ylabel('비중 (%)'); ax[2].set_ylim(0,104)
ax[2].set_title('③ 방수 — 양극 부족·중간 과잉 (barbell)'); ax[2].legend(fontsize=8.5); ax[2].grid(alpha=0.25,axis='y')
ax[2].annotate('',xy=(0,95),xytext=(2,95),arrowprops=dict(arrowstyle='<->',color='#c0392b',lw=1.4))
ax[2].text(1,97,'양극 부족 · 중간 과잉',ha='center',fontsize=9.5,color='#c0392b',fontweight='bold')
yl=ax[1].get_ylim()[1]
for xx,t in [(47,'소형'),(72,'국민평형'),(105,'대형')]: ax[1].text(xx,yl*0.965,t,fontsize=8,color='#777',ha='center')
plt.tight_layout(rect=[0,0,1,0.92])
o=REPO + '/analysis/34_barbell_distribution.png'
plt.savefig(o,dpi=120,bbox_inches='tight'); print(f'\n✅ {o}')
