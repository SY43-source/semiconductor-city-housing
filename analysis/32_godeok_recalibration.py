"""[EN] Godeok-specific demand recalibration — Table 3 (SS IV.4). Max-entropy exponential tilt.
#P0 (v7 핵심) — 고덕 특화 수요 재캘리브레이션. v6 gap 과대추정 교정.
문제: v6는 수요 분포로 평택 전체 가구원수(1인 37.5%)를 사용 → 고덕은 젊은 가족 도시(0-14세 19.4%,
      65+ 6.7%, 평균 가구원수 ~3.0-3.5명)라 부적합. 평택 1인가구율은 구도심 고령 1인가구에서 상당부분 발생.
방법: ① 고덕 연령구조 × 평택 조건분포로 사전분포 q_h 생성(24 사슬)
      ② 관측 제약(고덕 평균 가구원수 m̄)에 맞춰 **최소 KL 발산 지수 기울기**로 보정
         p_h ∝ q_h·exp(λh),  Σ p_h·h = m̄   (최대엔트로피 해)
      ③ m̄ 밴드(2.99 보수 / 3.2 기준 / 3.46 상한)로 gap 밴드 산출
출력: employment/godeok_demand_recalibrated.csv + 그림 32
"""
import os as _os; REPO = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
DATA_ROOT = _os.environ.get('DATA_ROOT', '/Users/Shared/seoyeon_research')
INVENTORY_DB = _os.environ.get('INVENTORY_DB', '/Users/Shared/seoyeon_inventory_master.sqlite')
import os,sys,csv
import numpy as np
from scipy.optimize import brentq
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='AppleGothic'; plt.rcParams['axes.unicode_minus']=False
EMP=DATA_ROOT + '/employment'
HH=['1인','2인','3인','4인','5인+']; SZ=np.array([1,2,3,4,5.5])

# ── 사전분포 q: 고덕 연령구조 기반(24_design_model 산출) ──
Q=np.array([0.393,0.236,0.186,0.146,0.039]); Q=Q/Q.sum()
PT=np.array([0.3754,0.2745,0.1862,0.1340,0.0300]); PT=PT/PT.sum()   # v6가 쓴 평택 실측
print(f"사전분포 q(고덕 연령기반) 평균 = {(Q*SZ).sum():.2f}명")
print(f"v6 사용 분포(평택 실측)  평균 = {(PT*SZ).sum():.2f}명")

# ── 고덕 평균 가구원수 관측 앵커 ──
POP_GD=77337; APT=22368; POP_BASE_2018=10382      # 실측
m_up  = POP_GD/APT                                 # 상한: 전원 아파트 거주 가정
m_lo  = (POP_GD-POP_BASE_2018)/APT                 # 보수: 2018 기저(구 고덕면 비아파트) 제외
m_mid = (m_up+m_lo)/2
print(f"\n고덕 평균 가구원수 관측: 보수 {m_lo:.2f} / 기준 {m_mid:.2f} / 상한 {m_up:.2f} 명 (평택 2.18)")

def tilt(q, mbar):
    """최소 KL 발산(지수 기울기): p_h ∝ q_h·exp(λh), Σp·h=mbar"""
    def mean_of(lam):
        w=q*np.exp(lam*SZ); p=w/w.sum(); return (p*SZ).sum()
    lam=brentq(lambda l: mean_of(l)-mbar, -5, 5, xtol=1e-12)
    w=q*np.exp(lam*SZ); return w/w.sum(), lam

# ── 규격/방수/점유 매핑 (v6와 동일 — 비교 가능성 유지) ──
MA={'1인':[.85,.15,0],'2인':[.50,.45,.05],'3인':[.10,.75,.15],'4인':[.03,.62,.35],'5인+':[0,.45,.55]}
MR={'1인':[.90,.10,0],'2인':[.60,.38,.02],'3인':[.10,.82,.08],'4인':[.03,.72,.25],'5인+':[0,.45,.55]}
SUP_A=np.array([30.1,59.0,11.0]); SUP_R=np.array([7.0,78.4,14.6])   # 고덕 공급 실측
def demand(p,M):
    d=np.zeros(3)
    for i,h in enumerate(HH): d+=p[i]*np.array(M[h])
    return d/d.sum()*100

cases=[('v6 사용(평택 실측)',PT,None),
       ('보수 m=%.2f'%m_lo, None, m_lo),
       ('기준 m=%.2f'%m_mid,None,m_mid),
       ('상한 m=%.2f'%m_up, None,m_up)]
rows=[]
print(f"\n{'시나리오':<20}{'1인율':>7}{'평균':>6} | {'소형gap':>8}{'국평gap':>8}{'대형gap':>8} | {'1-2방gap':>9}{'3방gap':>8}")
for nm,pfix,mbar in cases:
    p = pfix if pfix is not None else tilt(Q,mbar)[0]
    a=demand(p,MA); r=demand(p,MR); ga=SUP_A-a; gr=SUP_R-r
    rows.append((nm,p,a,r,ga,gr))
    print(f"{nm:<20}{p[0]*100:>6.1f}%{(p*SZ).sum():>6.2f} | {ga[0]:>+8.1f}{ga[1]:>+8.1f}{ga[2]:>+8.1f} | {gr[0]:>+9.1f}{gr[1]:>+8.1f}")

# 밴드(보수~상한) 요약
band=rows[1:]
def rng(idx,which):
    v=[r[4][idx] if which=='A' else r[5][idx] for r in band]
    return min(v),max(v)
print("\n★ 고덕 특화 gap 밴드 (보수~상한, 음수=부족)")
for i,l in enumerate(['소형<60','국평60-85','대형85+']):
    lo,hi=rng(i,'A'); print(f"  면적 {l:<10} {lo:+.1f} ~ {hi:+.1f} %p  → {'부족' if hi<0 else ('과잉' if lo>0 else '부호 불확정')}")
for i,l in enumerate(['1-2방','3방','4방+']):
    lo,hi=rng(i,'R'); print(f"  방수 {l:<10} {lo:+.1f} ~ {hi:+.1f} %p  → {'부족' if hi<0 else ('과잉' if lo>0 else '부호 불확정')}")

# ── 저장 ──
os.makedirs(EMP,exist_ok=True)
with open(f'{EMP}/godeok_demand_recalibrated.csv','w',newline='') as f:
    w=csv.writer(f); w.writerow(['scenario','mean_hh']+HH+['dem_small','dem_std','dem_large','gap_small','gap_std','gap_large','gap_12room','gap_3room'])
    for nm,p,a,r,ga,gr in rows:
        w.writerow([nm,f'{(p*SZ).sum():.3f}']+[f'{x:.4f}' for x in p]+[f'{a[0]:.1f}',f'{a[1]:.1f}',f'{a[2]:.1f}',
                    f'{ga[0]:.1f}',f'{ga[1]:.1f}',f'{ga[2]:.1f}',f'{gr[0]:.1f}',f'{gr[1]:.1f}'])
print(f"✅ {EMP}/godeok_demand_recalibrated.csv")

# ── 그림 ──
fig,ax=plt.subplots(1,3,figsize=(16.5,5.4))
fig.suptitle('P0 고덕 특화 수요 재캘리브레이션 — v6(평택 분포) 대비 gap 교정 (Gap=공급-수요, 음수=부족)',fontsize=13,fontweight='bold')
# (1) 가구원수 분포
x=np.arange(len(HH)); w=0.2
for j,(nm,p,*_ ) in enumerate(rows):
    ax[0].bar(x+(j-1.5)*w,p*100,w,label=nm.split('(')[0].strip())
ax[0].set_xticks(x); ax[0].set_xticklabels(HH); ax[0].set_ylabel('가구 비중(%)')
ax[0].set_title('① 가구원수 분포 — v6 vs 고덕 특화'); ax[0].legend(fontsize=7.5); ax[0].grid(alpha=0.3,axis='y')
# (2) 면적 gap
lab=['소형<60','국평60-85','대형85+']
for j,(nm,p,a,r,ga,gr) in enumerate(rows):
    ax[1].bar(np.arange(3)+(j-1.5)*w,ga,w,label=nm.split('(')[0].strip())
ax[1].axhline(0,color='gray',lw=1); ax[1].set_xticks(np.arange(3)); ax[1].set_xticklabels(lab,fontsize=9)
ax[1].set_ylabel('gap (%p)'); ax[1].set_title('② 면적 gap — 소형 부호 반전'); ax[1].grid(alpha=0.3,axis='y'); ax[1].legend(fontsize=7.5)
# (3) 방수 gap
labr=['1-2방','3방','4방+']
for j,(nm,p,a,r,ga,gr) in enumerate(rows):
    ax[2].bar(np.arange(3)+(j-1.5)*w,gr,w,label=nm.split('(')[0].strip())
ax[2].axhline(0,color='gray',lw=1); ax[2].set_xticks(np.arange(3)); ax[2].set_xticklabels(labr,fontsize=9)
ax[2].set_ylabel('gap (%p)'); ax[2].set_title('③ 방수 gap — 1-2방 부족 방향 유지·크기 축소'); ax[2].grid(alpha=0.3,axis='y'); ax[2].legend(fontsize=7.5)
plt.tight_layout(rect=[0,0,1,0.92])
o=REPO + '/analysis/32_godeok_recalibration.png'
plt.savefig(o,dpi=120,bbox_inches='tight'); print(f'✅ {o}')
