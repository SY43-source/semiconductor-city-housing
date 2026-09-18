"""[EN] Unit-price divergence — where the semiconductor effect actually shows.
#핵심 누락 보강 — 가격(단가) 발산: 반도체 효과의 진짜 소재.

규격 비중(%)은 스케일-불변이라 반도체 효과를 못 잡음. 반도체는 '가격·거래량·규모'에 나타남.
평택(처치) vs 안성(대조) vs 광주 중위 실거래 단가(만원/㎡) + 평택/안성 배율(사이클 상쇄 프리미엄).
데이터: realprice 매매(평택·안성·광주).
"""
import os as _os; REPO = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import csv, statistics
from collections import defaultdict
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='AppleGothic'; plt.rcParams['axes.unicode_minus']=False
RP='/Users/Shared/seoyeon_research/realprice'; YEARS=list(range(2015,2026))
def load(p,pred=lambda r:True): return [r for r in csv.DictReader(open(p,encoding='utf-8-sig')) if pred(r)]
def ppm2(rows):
    by=defaultdict(list)
    for r in rows:
        try:
            amt=float(str(r['dealAmount']).replace(',','')); ar=float(r['excluUseAr']); y=int(r['dealYear'])
            if ar>0 and 2015<=y<=2025: by[y].append(amt/ar)
        except: pass
    return {y:statistics.median(by[y]) if by[y] else np.nan for y in YEARS}
pt=ppm2(load(f'{RP}/realprice_apt_trade.csv',lambda r:r['region']=='평택시'))
an=ppm2(load(f'{RP}/realprice_apt_trade_anseong.csv'))
gj=ppm2(load(f'{RP}/realprice_apt_trade_gwangju.csv'))
ratio={y:pt[y]/an[y] for y in YEARS}

fig,(a1,a2)=plt.subplots(1,2,figsize=(15.5,6))
fig.suptitle('반도체 효과의 진짜 소재 = 가격(단가) — 규격 비중이 놓친 것',fontsize=14,fontweight='bold')
a1.plot(YEARS,[pt[y] for y in YEARS],'o-',color='#e33',lw=2.4,label='평택(반도체)')
a1.plot(YEARS,[an[y] for y in YEARS],'s--',color='#38a',lw=2,label='안성(대조)')
a1.plot(YEARS,[gj[y] for y in YEARS],'^:',color='#2a8',lw=2,label='광주')
a1.axvline(2017,color='blue',ls=':',lw=1.5,alpha=0.6); a1.axvspan(2020,2022,alpha=0.08,color='orange')
a1.set_title('중위 실거래 단가 (만원/㎡)'); a1.set_xlabel('연도'); a1.set_ylabel('만원/㎡'); a1.legend(fontsize=9); a1.grid(alpha=0.3)
a2.plot(YEARS,[ratio[y] for y in YEARS],'D-',color='#a2d',lw=2.6)
a2.axhline(ratio[2015],color='gray',ls='--',lw=1,label=f'2015 기준 {ratio[2015]:.2f}')
a2.axvline(2017,color='blue',ls=':',lw=1.5,label='삼성 P1 2017')
a2.set_title(f'평택/안성 단가 배율 = 사이클 상쇄 프리미엄\n1.16(2015) → {ratio[2025]:.2f}(2025)')
a2.set_xlabel('연도'); a2.set_ylabel('평택 ÷ 안성 단가'); a2.legend(fontsize=9); a2.grid(alpha=0.3)
plt.tight_layout(rect=[0,0,1,0.93])
out=REPO + '/analysis/11_price_divergence.png'
plt.savefig(out,dpi=120,bbox_inches='tight'); print(f'✅ {out}')
print(f"평택 단가 ×{pt[2025]/pt[2015]:.2f} / 안성 ×{an[2025]/an[2015]:.2f} / 광주 ×{gj[2025]/gj[2015]:.2f} (2015→25)")
print(f"평택/안성 배율 {ratio[2015]:.2f}→{ratio[2025]:.2f}")
