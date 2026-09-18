"""[EN] Per-attribute regression (slope + 95% CI) and segmented-regression breakpoint test.
#2 요소별 회귀(기울기+95%CI) + 분절회귀(변곡점 vs P1 2017) — 평택.

§5.3 회귀: 국평(60-85㎡) 거래비중 ~ 연도. slope β1, 95%CI, R², p (scipy.linregress).
§5.4 분절회귀: 2-segment 그리드 탐색으로 변곡점 추정 → P1(2017) 정렬 검정.
데이터: 평택 실거래(realprice_apt_trade.csv). 대조로 안성도 회귀.
"""
import os as _os; REPO = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import csv
from collections import defaultdict
import numpy as np
from scipy import stats
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'AppleGothic'
plt.rcParams['axes.unicode_minus'] = False
RP = '/Users/Shared/seoyeon_research/realprice'
YEARS = np.array(range(2015, 2026))

def load(path, pred): return [r for r in csv.DictReader(open(path, encoding='utf-8-sig'))
    if r['excluUseAr'] and r['dealYear'] and pred(r)]
def guk_series(rows):
    tot=defaultdict(int); sel=defaultdict(int)
    for r in rows:
        y=int(r['dealYear'])
        if 2015<=y<=2025:
            tot[y]+=1
            if 60<=float(r['excluUseAr'])<85: sel[y]+=1
    return np.array([sel[y]/tot[y]*100 for y in YEARS])

pt=load(f'{RP}/realprice_apt_trade.csv', lambda r:r['region']=='평택시')
an=load(f'{RP}/realprice_apt_trade_anseong.csv', lambda r:True)
y_pt=guk_series(pt); y_an=guk_series(an)
x=YEARS.astype(float)

# ── 회귀 + 95% CI ──
def reg(x,y):
    lr=stats.linregress(x,y); n=len(x); tcrit=stats.t.ppf(0.975,n-2)
    ci=tcrit*lr.stderr
    return lr, ci
lr_pt,ci_pt=reg(x,y_pt); lr_an,ci_an=reg(x,y_an)
print(f"[평택 국평~연도] β1={lr_pt.slope:+.2f} ±{ci_pt:.2f} %p/yr (95%CI [{lr_pt.slope-ci_pt:+.2f},{lr_pt.slope+ci_pt:+.2f}]) R²={lr_pt.rvalue**2:.2f} p={lr_pt.pvalue:.4f}")
print(f"[안성 국평~연도] β1={lr_an.slope:+.2f} ±{ci_an:.2f} %p/yr R²={lr_an.rvalue**2:.2f} p={lr_an.pvalue:.4f}")

# ── 분절회귀: 2-segment 그리드 변곡점 ──
def seg_sse(x,y,bp):
    m1=x<=bp; m2=x>=bp; sse=0
    for m in (m1,m2):
        if m.sum()>=2:
            l=stats.linregress(x[m],y[m]); sse+=np.sum((y[m]-(l.intercept+l.slope*x[m]))**2)
    return sse
cands=np.arange(2017,2024)
sses={bp:seg_sse(x,y_pt,float(bp)) for bp in cands}
best_bp=min(sses,key=sses.get)
single_sse=np.sum((y_pt-(lr_pt.intercept+lr_pt.slope*x))**2)
print(f"\n[분절회귀 평택] 최적 변곡점={best_bp} (SSE {sses[best_bp]:.0f} vs 단일선 {single_sse:.0f})")
print(f"  변곡점별 SSE: {{{', '.join(f'{b}:{s:.0f}' for b,s in sses.items())}}}")
# 변곡점 전후 기울기
m1=x<=best_bp; m2=x>=best_bp
s1=stats.linregress(x[m1],y_pt[m1]); s2=stats.linregress(x[m2],y_pt[m2])
print(f"  전({int(x[m1][0])}-{best_bp}) β={s1.slope:+.2f} / 후({best_bp}-{int(x[m2][-1])}) β={s2.slope:+.2f}")

# ── 그림 ──
fig,(ax1,ax2)=plt.subplots(1,2,figsize=(15,6))
fig.suptitle('평택 국평(60-85㎡) 비중 — 회귀 추세 + 분절회귀 변곡점',fontsize=14,fontweight='bold')
# 회귀 + CI 밴드
ax=ax1; xf=np.linspace(2015,2025,50)
yhat=lr_pt.intercept+lr_pt.slope*xf
n=len(x); se_line=np.sqrt(np.sum((y_pt-(lr_pt.intercept+lr_pt.slope*x))**2)/(n-2))*np.sqrt(1/n+(xf-x.mean())**2/np.sum((x-x.mean())**2))
tcrit=stats.t.ppf(0.975,n-2)
ax.scatter(x,y_pt,color='#e33',zorder=3,label='평택 실측')
ax.plot(xf,yhat,color='#e33',lw=2,label=f'회귀 β1={lr_pt.slope:+.2f}%p/yr')
ax.fill_between(xf,yhat-tcrit*se_line,yhat+tcrit*se_line,alpha=0.15,color='#e33',label='95% CI')
ax.scatter(x,y_an,color='#38a',marker='s',zorder=3,label='안성(대조)')
ax.plot(xf,lr_an.intercept+lr_an.slope*xf,'--',color='#38a',lw=1.5)
ax.set_xlabel('연도'); ax.set_ylabel('국평 거래비중(%)')
ax.set_title(f'선형 회귀 (평택 R²={lr_pt.rvalue**2:.2f}, p={lr_pt.pvalue:.3f})'); ax.legend(fontsize=8.5); ax.grid(alpha=0.3)
# 분절회귀
ax=ax2
ax.scatter(x,y_pt,color='#333',zorder=3)
ax.plot(x[m1],s1.intercept+s1.slope*x[m1],color='#2a8',lw=2.5,label=f'~{best_bp} (β={s1.slope:+.1f})')
ax.plot(x[m2],s2.intercept+s2.slope*x[m2],color='#c33',lw=2.5,label=f'{best_bp}~ (β={s2.slope:+.1f})')
ax.axvline(2017,color='blue',ls=':',lw=2,label='삼성 P1 2017')
ax.axvline(best_bp,color='orange',ls='--',lw=2,label=f'추정 변곡점 {best_bp}')
ax.set_xlabel('연도'); ax.set_ylabel('국평 거래비중(%)')
ax.set_title(f'분절회귀 — 변곡점 {best_bp} vs P1(2017)'); ax.legend(fontsize=8.5); ax.grid(alpha=0.3)

plt.tight_layout(rect=[0,0,1,0.93])
out=REPO + '/analysis/07_regression_breakpoint.png'
plt.savefig(out,dpi=120,bbox_inches='tight')
print(f'\n✅ {out}')
