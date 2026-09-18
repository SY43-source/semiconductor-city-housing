"""[EN] Macro (pandemic) cycle adjustment — Fig. A2. Removes common year effects.
#4 거시(팬데믹) 사이클 보정 — 공통 연도효과 제거 상대지표로 '반도체 순신호' 재검정.

문제: 국평 비중 시계열이 2020 급등(유동성)·2022 급락(금리·거래절벽) = 전국 공통 사이클에 지배됨.
보정: 상대지표 = 평택 국평비중 - 대조 벤치마크(안성, 또는 안성+광주 평균).
      공통 연도효과(팬데믹·금리)가 상쇄 → 평택 고유(반도체 후보) 성분만 남음.
raw 회귀/변곡점 vs 보정 회귀/변곡점 비교로 '거시가 잡은 것인지 반도체인지' 판별.
"""
import os as _os; REPO = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import csv
from collections import defaultdict
import numpy as np
from scipy import stats
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams['font.family']='Helvetica'
plt.rcParams['axes.unicode_minus'] = False
RP='/Users/Shared/seoyeon_research/realprice'
YEARS=np.array(range(2015,2026)); x=YEARS.astype(float)
def load(path,pred): return [r for r in csv.DictReader(open(path,encoding='utf-8-sig')) if r['excluUseAr'] and r['dealYear'] and pred(r)]
def guk(rows):
    t=defaultdict(int); s=defaultdict(int)
    for r in rows:
        y=int(r['dealYear'])
        if 2015<=y<=2025:
            t[y]+=1
            if 60<=float(r['excluUseAr'])<85: s[y]+=1
    return np.array([s[y]/t[y]*100 if t[y] else np.nan for y in YEARS])
pt=guk(load(f'{RP}/realprice_apt_trade.csv',lambda r:r['region']=='평택시'))
an=guk(load(f'{RP}/realprice_apt_trade_anseong.csv',lambda r:True))
gj=guk(load(f'{RP}/realprice_apt_trade_gwangju.csv',lambda r:True))

bench=np.nanmean(np.vstack([an,gj]),axis=0)   # 대조 벤치마크(안성+광주 평균) = 거시 프록시
excess=pt-bench                                # 평택 초과 = 거시 제거분

def reg(x,y):
    m=~np.isnan(y); lr=stats.linregress(x[m],y[m]); n=m.sum(); ci=stats.t.ppf(0.975,n-2)*lr.stderr
    return lr,ci
lr_raw,ci_raw=reg(x,pt); lr_ex,ci_ex=reg(x,excess)
def seg(x,y):
    best=None
    for bp in range(2017,2024):
        m1=x<=bp; m2=x>=bp; sse=0
        for m in (m1,m2):
            if m.sum()>=2: l=stats.linregress(x[m],y[m]); sse+=np.sum((y[m]-(l.intercept+l.slope*x[m]))**2)
        if best is None or sse<best[1]: best=(bp,sse)
    return best[0]
print("=== raw 평택 국평 vs 보정(평택-벤치마크) ===")
print(f" raw   : β1={lr_raw.slope:+.2f} (95%CI±{ci_raw:.2f}) R²={lr_raw.rvalue**2:.2f} p={lr_raw.pvalue:.3f} 변곡점={seg(x,pt)}")
print(f" 보정   : β1={lr_ex.slope:+.2f} (95%CI±{ci_ex:.2f}) R²={lr_ex.rvalue**2:.2f} p={lr_ex.pvalue:.3f} 변곡점={seg(x,excess)}")
print(f" 평택 초과(국평, %p): 2015 {excess[0]:+.1f} → 2025 {excess[-1]:+.1f} (Δ{excess[-1]-excess[0]:+.1f}%p, 거의 평탄이면 반도체 순효과 미미)")

fig,(ax1,ax2)=plt.subplots(1,2,figsize=(15,6))
fig.suptitle('Macro-cycle adjustment: net signal after removing common year effects',fontsize=13.5,fontweight='bold')
# 패널1: raw 세 도시 동조 + 팬데믹 구간 음영
ax=ax1
ax.axvspan(2020,2022,alpha=0.12,color='orange',label='Pandemic liquidity -> rate hikes')
ax.plot(YEARS,pt,'o-',color='#e33',lw=2,label='Pyeongtaek')
ax.plot(YEARS,an,'s--',color='#38a',lw=1.8,label='Anseong')
ax.plot(YEARS,gj,'^:',color='#2a8',lw=1.8,label='Gwangju')
ax.set_title('Raw standard-size share: three cities move together'); ax.set_xlabel('Year'); ax.set_ylabel('Standard-size share of transactions (%)')
ax.legend(fontsize=8.5); ax.grid(alpha=0.3)
# 패널2: 보정(초과) + 회귀
ax=ax2
ax.axvspan(2020,2022,alpha=0.10,color='orange')
ax.axhline(0,color='gray',lw=1)
ax.scatter(x,excess,color='#a2d',zorder=3,label='Pyeongtaek excess (vs control mean)')
xf=np.linspace(2015,2025,50)
ax.plot(xf,lr_ex.intercept+lr_ex.slope*xf,color='#a2d',lw=2,label=f'adjusted trend b1={lr_ex.slope:+.2f}%p/yr (p={lr_ex.pvalue:.2f})')
ax.axvline(2017,color='blue',ls=':',lw=1.8,label='Samsung P1, 2017')
ax.set_title('After adjustment: Pyeongtaek-specific component'); ax.set_xlabel('Year'); ax.set_ylabel('Excess standard-size share, Pyeongtaek (%p)')
ax.legend(fontsize=8.5); ax.grid(alpha=0.3)

plt.tight_layout(rect=[0,0,1,0.93])
out=REPO + '/analysis/08_macro_adjusted.png'
plt.savefig(out,dpi=120,bbox_inches='tight'); print(f'\n✅ {out}')
