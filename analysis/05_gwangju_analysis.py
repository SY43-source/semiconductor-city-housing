"""[EN] Gwangju unit-composition and mismatch analysis (framework transfer).
#1 광주 규격·미스매치 분석 — 평택 분석틀 이식 + 군공항구(광산) vs 광주 전역.

광주=반도체 신도시(군공항 부지, 광산구) 배후. 현재 규격 baseline을 진단해 §13.5 예측 근거로.
데이터: realprice_apt_trade_gwangju.csv(228,649) + 1인가구(광주광역시) + 평택(참조).
패널1: 광주 전역 면적대 거래비중 추이. 패널2: 광산구(군공항) vs 광주전역 국평비중.
패널3: 광주 1인가구 vs 국평/소형 (미스매치 진단).
"""
import os as _os; REPO = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
DATA_ROOT = _os.environ.get('DATA_ROOT', '/Users/Shared/seoyeon_research')
INVENTORY_DB = _os.environ.get('INVENTORY_DB', '/Users/Shared/seoyeon_inventory_master.sqlite')
import csv
from collections import defaultdict
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'AppleGothic'
plt.rcParams['axes.unicode_minus'] = False
RP = DATA_ROOT + '/realprice'
POP = DATA_ROOT + '/population/city_1person_household_2015_2024.csv'
YEARS = list(range(2015, 2026))
AIRPORT_DONG = {'송정동','도산동','신촌동','우산동','신가동','운남동','도호동','황룡동','비아동','신창동','수완동','장덕동'}

def load(path, region=None):
    return [r for r in csv.DictReader(open(path, encoding='utf-8-sig'))
            if (not region or r['region'] == region) and r['excluUseAr'] and r['dealYear']]

gj = load(f'{RP}/realprice_apt_trade_gwangju.csv')
pt = load(f'{RP}/realprice_apt_trade.csv', '평택시')

def share(rows, lo, hi, yrs=YEARS):
    tot = defaultdict(int); sel = defaultdict(int)
    for r in rows:
        y = int(r['dealYear'])
        if 2015 <= y <= 2025:
            tot[y] += 1
            if lo <= float(r['excluUseAr']) < hi: sel[y] += 1
    return {y: (sel[y]/tot[y]*100 if tot[y] else np.nan) for y in yrs}

gj_small, gj_guk, gj_big = share(gj,0,60), share(gj,60,85), share(gj,85,999)
pt_guk = share(pt,60,85)
gwangsan = [r for r in gj if r['region']=='광산구']
airport = [r for r in gwangsan if r['umdNm'] in AIRPORT_DONG]
gs_guk = share(gwangsan,60,85); ap_guk = share(airport,60,85)

single = {}
for r in csv.DictReader(open(POP, encoding='utf-8-sig')):
    if r['region']=='광주광역시' and r['single_ratio']:
        single[int(r['year'])] = float(r['single_ratio'])

fig, axes = plt.subplots(1, 3, figsize=(18, 5.6))
fig.suptitle('광주(전남광주통합특별시) 아파트 규격·미스매치 — 반도체 군공항 부지 배후 baseline',
             fontsize=14, fontweight='bold')

# 패널1: 광주 전역 면적대 추이
ax = axes[0]
ax.plot(YEARS, [gj_small[y] for y in YEARS], '^-', color='#2a8', lw=2, label='소형(~60㎡)')
ax.plot(YEARS, [gj_guk[y] for y in YEARS], 's-', color='#37a', lw=2, label='국평(60-85㎡)')
ax.plot(YEARS, [gj_big[y] for y in YEARS], 'o-', color='#c63', lw=2, label='대형(85㎡+)')
ax.set_title('[광주 전역] 면적대 거래비중 추이'); ax.set_xlabel('연도'); ax.set_ylabel('거래비중(%)')
ax.legend(fontsize=9); ax.grid(alpha=0.3)

# 패널2: 군공항(광산) vs 전역 국평
ax = axes[1]
ax.plot(YEARS, [gj_guk[y] for y in YEARS], 's-', color='#888', lw=2, label='광주 전역')
ax.plot(YEARS, [gs_guk[y] for y in YEARS], 'o-', color='#d33', lw=2.3, label='광산구(군공항 구)')
ax.plot(YEARS, [ap_guk[y] for y in YEARS], 'D--', color='#e88', lw=2, label='군공항 인근 동')
ax.set_title('[군공항 배후] 국평(60-85㎡) 거래비중\n광산구·인근동 vs 전역'); ax.set_xlabel('연도'); ax.set_ylabel('국평 비중(%)')
ax.legend(fontsize=9); ax.grid(alpha=0.3)

# 패널3: 광주 1인가구 vs 공급
ax = axes[2]
yrs2 = [y for y in YEARS if y in single]
ax.plot(yrs2, [single[y] for y in yrs2], 'o-', color='#d33', lw=2.4, label='1인가구 비율')
ax.plot(yrs2, [gj_guk[y] for y in yrs2], 's--', color='#37a', lw=2, label='국평(가족형) 비중')
ax.plot(yrs2, [gj_small[y] for y in yrs2], '^:', color='#2a8', lw=2, label='소형(1인적합) 비중')
ax.set_title('[광주 미스매치 진단]\n1인가구 vs 공급 규격'); ax.set_xlabel('연도'); ax.set_ylabel('비율(%)')
ax.legend(fontsize=9); ax.grid(alpha=0.3)

plt.tight_layout(rect=[0,0,1,0.92])
out = REPO + '/analysis/05_gwangju_analysis.png'
plt.savefig(out, dpi=120, bbox_inches='tight')
print(f'✅ {out}')
print(f"\n광주 전역 국평비중: {gj_guk[2015]:.1f}→{gj_guk[2025]:.1f}% / 소형: {gj_small[2015]:.1f}→{gj_small[2025]:.1f}%")
print(f"광산구(군공항) 국평: {gs_guk[2015]:.1f}→{gs_guk[2025]:.1f}% / 군공항인근동: {ap_guk[2015]:.1f}→{ap_guk[2025]:.1f}%")
print(f"광주 1인가구: {single.get(2015)}→{single.get(2024)}%")
print(f"참조 평택 국평 2025: {pt_guk[2025]:.1f}%")
