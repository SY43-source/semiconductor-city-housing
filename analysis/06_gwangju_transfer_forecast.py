"""[EN] Gwangju transfer forecast via event-time alignment on the Pyeongtaek trajectory.
#3 §13.5 광주 전이 예측 — 평택(+용인·이천) 궤적을 event-time τ 정렬 → 광주 미래 규격.

델타 전이: 광주(τ) = 광주_baseline(2025) + Δ평택(τ) ± k·σ.
  τ=0 = 반도체 가동 (평택 2017 / 광주 ~2030, offset 13년). 광주 2025 = τ-5.
  Δ = donor 도시(평택 P1 前후) 국평비중 변화. σ = donor(평택·용인·이천) 분산.
결과: 광주 국평(가족형)·소형(1인) 비중의 2030/2035 시나리오 + 미스매치 함의.
데이터: realprice(광주 병합 + 평택·용인·이천).
"""
import os as _os; REPO = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import csv
from collections import defaultdict
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'AppleGothic'
plt.rcParams['axes.unicode_minus'] = False
RP = '/Users/Shared/seoyeon_research/realprice'

def load(path, pred=None):
    return [r for r in csv.DictReader(open(path, encoding='utf-8-sig'))
            if r['excluUseAr'] and r['dealYear'] and (pred is None or pred(r))]

def guk_by_year(rows, lo=60, hi=85):
    tot=defaultdict(int); sel=defaultdict(int)
    for r in rows:
        y=int(r['dealYear'])
        if 2015<=y<=2025:
            tot[y]+=1
            if lo<=float(r['excluUseAr'])<hi: sel[y]+=1
    return {y:(sel[y]/tot[y]*100 if tot[y] else np.nan) for y in range(2015,2026)}

gj   = load(f'{RP}/realprice_apt_trade_gwangju.csv')
pt   = load(f'{RP}/realprice_apt_trade.csv', lambda r:r['region']=='평택시')
yong = load(f'{RP}/realprice_apt_trade.csv', lambda r:r['region'].startswith('용인'))
ich  = load(f'{RP}/realprice_apt_trade.csv', lambda r:r['region']=='이천시')

gj_guk, pt_guk = guk_by_year(gj), guk_by_year(pt)
gj_small = guk_by_year(gj,0,60)

# donor Δ(국평): 2015(baseline) → 2024(성숙). 평택 P1=2017 유입효과 포함
def delta(g): return g[2024]-g[2015]
donors={'평택':delta(pt_guk),'용인':delta(guk_by_year(yong)),'이천':delta(guk_by_year(ich))}
dvals=list(donors.values()); dmean=np.mean(dvals); dsig=np.std(dvals)
gj_base=gj_guk[2025]  # 광주 현재 baseline

# 예측: 광주 국평(2035, 가동+5) = baseline + Δmean ± k·σ  (포화 상한 78% 클립)
def clip(v): return min(v,78.0)
pred_pt=clip(gj_base+dmean)
band=(clip(gj_base+dmean-2.5*dsig), clip(gj_base+dmean+2.5*dsig))

# ── event-time 정렬 그림 ──
fig,(ax1,ax2)=plt.subplots(1,2,figsize=(15.5,6))
fig.suptitle('§13.5 광주 반도체 배후 규격 전이 예측 (평택 궤적 이식)',fontsize=14,fontweight='bold')

# 패널1: event-time τ 정렬 (평택 τ=0=2017 / 광주 τ=0=2030)
ax=ax1
tau_pt=[y-2017 for y in range(2015,2026)]
tau_gj=[y-2030 for y in range(2015,2026)]
ax.plot(tau_pt,[pt_guk[y] for y in range(2015,2026)],'s-',color='#e33',lw=2.2,label='평택 (donor, τ=0:2017)')
ax.plot(tau_gj,[gj_guk[y] for y in range(2015,2026)],'o-',color='#37a',lw=2.2,label='광주 실측 (τ=0:2030)')
# 광주 예측 (τ=+5 = 2035)
ax.errorbar([5],[pred_pt],yerr=[[pred_pt-band[0]],[band[1]-pred_pt]],fmt='D',color='#a2d',ms=10,capsize=6,label=f'광주 예측 τ+5(2035)')
ax.axvline(0,color='gray',ls=':',lw=1.5); ax.text(0.1,36,'가동 τ=0',fontsize=8,color='gray')
ax.set_xlabel('event-time τ (반도체 가동 기준 연차)'); ax.set_ylabel('국평(60-85㎡) 거래비중(%)')
ax.set_title('event-time 정렬 — 평택 궤적 → 광주 전이'); ax.legend(fontsize=8.5); ax.grid(alpha=0.3)

# 패널2: 광주 예측 요약 (국평↑ / 소형↓ = 미스매치 심화)
ax=ax2
cats=['국평(가족형)\n현재→예측','소형(1인)\n현재→예측']
cur=[gj_base, gj_small[2025]]
# 소형 예측: 국평 상승분만큼 소형 감소 가정(보수적)
small_pred=max(gj_small[2025]-(pred_pt-gj_base)*0.8, 15)
prd=[pred_pt, small_pred]
x=np.arange(2); w=0.35
ax.bar(x-w/2,cur,w,color=['#37a','#2a8'],alpha=0.5,label='현재(2025)')
ax.bar(x+w/2,prd,w,color=['#37a','#2a8'],label='예측(2035, 가동+5)')
ax.errorbar([x[0]+w/2],[pred_pt],yerr=[[pred_pt-band[0]],[band[1]-pred_pt]],fmt='none',ecolor='#a2d',capsize=5,lw=2)
ax.set_xticks(x); ax.set_xticklabels(cats,fontsize=9)
ax.set_ylabel('거래비중(%)'); ax.set_title(f'광주 예측 (donor Δ={dmean:+.1f}±{dsig:.1f}%p)\n국평↑·소형↓ = 1인 소형 부족 심화')
ax.legend(fontsize=9); ax.grid(alpha=0.3,axis='y')

plt.tight_layout(rect=[0,0,1,0.93])
out=REPO + '/analysis/06_gwangju_transfer_forecast.png'
plt.savefig(out,dpi=120,bbox_inches='tight')
print(f'✅ {out}')
print(f"\ndonor Δ국평(2015→24): {donors} → mean {dmean:+.1f} ±{dsig:.1f}%p")
print(f"광주 baseline 국평(2025): {gj_base:.1f}%")
print(f"광주 예측 국평 τ+5(2035): {pred_pt:.1f}%  밴드[{band[0]:.1f}, {band[1]:.1f}]")
print(f"광주 소형 예측: {gj_small[2025]:.1f}→{small_pred:.1f}% (1인 부족 심화)")
