"""[EN] Pyeongtaek population projection to 2030/2035 with prediction intervals.
#평택 인구 2030·2035 예측 — 기울기 기반 외삽(시나리오 + 예측구간).

⚠️ 외삽은 취약(Mankiw&Weil 1989 반면교사). 단일 점추정 금지 → 3 시나리오 + 95% 예측구간.
S1 최근가속(2018~2025 OLS): 반도체 확장기 기울기 유지 가정.
S2 보수(2010~2025 OLS): 장기 평균 기울기.
S3 포화(로지스틱 근사): 고덕 물량 소진 시 감속.
데이터: control_regions_pop_2000_2025.csv (평택).
"""
import os as _os; REPO = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import csv
import numpy as np
from scipy import stats
from scipy.optimize import curve_fit
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='AppleGothic'; plt.rcParams['axes.unicode_minus']=False
CSV='/Users/Shared/seoyeon_research/population/control_regions_pop_2000_2025.csv'
pt={int(r['year']):int(r['population'])/1000 for r in csv.DictReader(open(CSV,encoding='utf-8-sig')) if '평택' in r['region']}
YR=np.array(sorted(pt)); POP=np.array([pt[y] for y in YR])
FUT=np.array([2030,2035])

def ols_pred(x,y,xnew):
    lr=stats.linregress(x,y); n=len(x); dof=n-2
    yhat=lr.intercept+lr.slope*xnew
    resid=y-(lr.intercept+lr.slope*x); s=np.sqrt(np.sum(resid**2)/dof)
    Sxx=np.sum((x-x.mean())**2); t=stats.t.ppf(0.975,dof)
    pi=t*s*np.sqrt(1+1/n+(xnew-x.mean())**2/Sxx)
    return lr,yhat,pi

# S1 최근 가속(2018~)
m1=YR>=2018; lr1,f1,pi1=ols_pred(YR[m1],POP[m1],FUT)
# S2 보수(2010~)
m2=YR>=2010; lr2,f2,pi2=ols_pred(YR[m2],POP[m2],FUT)
# 외생 앵커: 도시기본계획 목표 90만(2035). 포화 천장이 아니라 '추세 상회 목표'인지 검증.
KPLAN=900.0
p2025=POP[YR==2025][0]
req_slope=(KPLAN-p2025)/(2035-2025)   # 90만 달성에 필요한 연평균 증가
print(f"S1 최근가속 기울기 {lr1.slope:.1f}천/년: 2030 {f1[0]:.0f}±{pi1[0]:.0f} / 2035 {f1[1]:.0f}±{pi1[1]:.0f}")
print(f"S2 보수 기울기 {lr2.slope:.1f}천/년: 2030 {f2[0]:.0f}±{pi2[0]:.0f} / 2035 {f2[1]:.0f}±{pi2[1]:.0f}")
print(f"도시기본계획 목표 90만(2035): 필요 기울기 {req_slope:.1f}천/년 (현 {lr1.slope:.1f}의 {req_slope/lr1.slope:.1f}배) → 추세({f1[1]:.0f})가 목표(900)에 {900-f1[1]:.0f}천 미달")

fig,ax=plt.subplots(figsize=(12,7))
ax.plot(YR,POP,'o-',color='#333',lw=2,ms=4,label='실측(2000~2025)')
xf=np.linspace(2025,2035,50)
# S1
ax.plot(xf,lr1.intercept+lr1.slope*xf,'--',color='#e33',lw=2,label=f'S1 최근가속 ({lr1.slope:.1f}천/년)')
ax.errorbar(FUT,f1,yerr=pi1,fmt='D',color='#e33',ms=9,capsize=6)
# S2
ax.plot(xf,lr2.intercept+lr2.slope*xf,'--',color='#38a',lw=2,label=f'S2 보수 ({lr2.slope:.1f}천/년)')
ax.errorbar(FUT+0.15,f2,yerr=pi2,fmt='s',color='#38a',ms=8,capsize=5)
# 외생 앵커: 도시기본계획 90만 목표선 + 목표 달성경로
ax.axhline(KPLAN,color='#2a8',ls='-',lw=1,alpha=0.6)
ax.plot([2025,2035],[p2025,KPLAN],':',color='#2a8',lw=2,label=f'도시기본계획 목표경로 (필요 {req_slope:.0f}천/년)')
ax.plot([2035],[KPLAN],'*',color='#2a8',ms=16)
ax.annotate(f'도시기본계획 목표 90만\n(2035, 추세보다 {900-f1[1]:.0f}천↑)',(2035,KPLAN),fontsize=8.5,color='#2a8',ha='right',va='bottom')
for x,l in [(2020,'P2'),(2022,'P3'),(2028,'P5가동')]:
    ax.axvline(x,color='gray',ls=':',lw=1)
    ax.text(x,372,l,fontsize=8,color='gray',ha='center')
for i,y in enumerate(FUT):
    ax.annotate(f'{f1[i]:.0f}',(y,f1[i]),fontsize=9,color='#e33',ha='left',va='bottom')
    ax.annotate(f'{f2[i]:.0f}',(y+0.15,f2[i]),fontsize=9,color='#38a',ha='left',va='top')
ax.set_xlabel('연도'); ax.set_ylabel('평택 총인구(천명)')
ax.set_title('평택 인구 2030·2035 예측 — 기울기 외삽 시나리오 (95% 예측구간)\n(주의) 외삽은 추세 지속 가정, 신뢰구간 넓음',fontsize=13,fontweight='bold')
ax.legend(fontsize=9.5,loc='upper left'); ax.grid(alpha=0.3)
plt.tight_layout()
out=REPO + '/analysis/18_pop_forecast.png'
plt.savefig(out,dpi=120,bbox_inches='tight'); print(f'✅ {out}')
