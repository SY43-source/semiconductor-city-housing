"""[EN] Dual-axis mismatch chart — single-person household rise vs mid-size supply.
#3 미스매치 이중축 차트 (§6.2 그림2) — 인구 1인화 vs 아파트 공급 규격의 괴리.

핵심: 평택은 1인가구가 급증(26.7→37.3%)하는데 거래·공급은 국평(가족형)으로 이동 = 미스매치.
대조(안성)와 비교하면 1인가구화는 거의 동일한데 국평 shift는 평택만 → 반도체 특정 효과로 확정.

패널1: 평택 이중축 — 1인가구 비율(좌) vs 소형(~60㎡)/국평(60-85㎡) 거래비중(우).
패널2: 평택 vs 안성 — 1인가구화(동일) vs 국평비중(발산) = 미스매치의 인과 격리.
데이터: city_1person_household_2015_2024.csv + realprice(평택/안성).
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

POP = DATA_ROOT + '/population/city_1person_household_2015_2024.csv'
RP = DATA_ROOT + '/realprice'
YEARS = list(range(2015, 2025))  # 1인가구 데이터 범위에 맞춤

# 1인가구 비율
single = defaultdict(dict)
for r in csv.DictReader(open(POP, encoding='utf-8-sig')):
    if r['region'] in ('평택시', '안성시') and r['single_ratio']:
        single[r['region']][int(r['year'])] = float(r['single_ratio'])

# 실거래 면적대별 비중
def load(path, region=None):
    return [r for r in csv.DictReader(open(path, encoding='utf-8-sig'))
            if (not region or r['region'] == region) and r['excluUseAr'] and r['dealYear']]
def share_by_year(rows, lo, hi):
    tot = defaultdict(int); sel = defaultdict(int)
    for r in rows:
        y = int(r['dealYear'])
        if 2015 <= y <= 2024:
            tot[y] += 1
            if lo <= float(r['excluUseAr']) < hi: sel[y] += 1
    return {y: (sel[y]/tot[y]*100 if tot[y] else np.nan) for y in YEARS}

pt = load(f'{RP}/realprice_apt_trade.csv', '평택시')
an = load(f'{RP}/realprice_apt_trade_anseong.csv')
pt_small = share_by_year(pt, 0, 60)     # 소형 ~60㎡ (1인 적합)
pt_guk = share_by_year(pt, 60, 85)      # 국평 60-85㎡ (가족형)
an_guk = share_by_year(an, 60, 85)

fig, (ax1, ax3) = plt.subplots(1, 2, figsize=(16, 6.2))
fig.suptitle('미스매치: 인구는 1인화하는데 아파트 공급은 가족형(국평)에 머문다',
             fontsize=15, fontweight='bold')

# ── 패널1: 평택 이중축 ──
c_red, c_blue, c_green = '#d33', '#37a', '#2a8'
ax1.set_xlabel('연도'); ax1.set_ylabel('1인가구 비율 (%)', color=c_red)
l1 = ax1.plot(YEARS, [single['평택시'][y] for y in YEARS], 'o-', color=c_red, lw=2.6, label='1인가구 비율(좌)')
ax1.tick_params(axis='y', labelcolor=c_red); ax1.set_ylim(20, 42)
ax1.fill_between(YEARS, [single['평택시'][y] for y in YEARS], 20, alpha=0.06, color=c_red)

ax2 = ax1.twinx(); ax2.set_ylabel('거래 비중 (%)', color=c_blue)
l2 = ax2.plot(YEARS, [pt_guk[y] for y in YEARS], 's--', color=c_blue, lw=2.4, label='국평(60-85㎡, 가족형) 거래비중(우)')
l3 = ax2.plot(YEARS, [pt_small[y] for y in YEARS], '^:', color=c_green, lw=2.0, label='소형(~60㎡, 1인적합) 거래비중(우)')
ax2.tick_params(axis='y', labelcolor=c_blue); ax2.set_ylim(20, 60)
ax1.set_title('[평택] 1인가구↑ vs 국평(가족형)↑ / 소형→\n= 1인 수요 느는데 소형 공급 안 늘어 (괴리)')
lines = l1 + l2 + l3
ax1.legend(lines, [l.get_label() for l in lines], loc='upper left', fontsize=8.5)
ax1.grid(alpha=0.25)

# ── 패널2: 평택 vs 안성 (미스매치 인과 격리) ──
ax3.plot(YEARS, [single['평택시'][y] for y in YEARS], 'o-', color=c_red, lw=2.4, label='평택 1인가구비율')
ax3.plot(YEARS, [single['안성시'][y] for y in YEARS], 'o--', color='#e88', lw=2.0, label='안성 1인가구비율')
ax3.plot(YEARS, [pt_guk[y] for y in YEARS], 's-', color=c_blue, lw=2.4, label='평택 국평비중')
ax3.plot(YEARS, [an_guk[y] for y in YEARS], 's--', color='#8ac', lw=2.0, label='안성 국평비중')
ax3.set_xlabel('연도'); ax3.set_ylabel('비율 (%)')
ax3.set_title('[평택 vs 안성] 1인가구화는 거의 동일\n그러나 국평 shift는 평택만 → 반도체 특정 효과')
ax3.legend(fontsize=8.5, loc='center left'); ax3.grid(alpha=0.25)
ax3.annotate('1인가구화: 두 도시 수렴 (~37%)', xy=(2022, 36), fontsize=9, color=c_red)

plt.tight_layout(rect=[0, 0, 1, 0.93])
out = REPO + '/analysis/03_mismatch_dualaxis.png'
plt.savefig(out, dpi=120, bbox_inches='tight')
print(f'✅ {out}')
print('\n=== 요약 (2015→2024) ===')
print(f"평택 1인가구: {single['평택시'][2015]:.1f}→{single['평택시'][2024]:.1f}% / 안성: {single['안성시'][2015]:.1f}→{single['안성시'][2024]:.1f}%")
print(f"평택 국평비중: {pt_guk[2015]:.1f}→{pt_guk[2024]:.1f}% / 안성: {an_guk[2015]:.1f}→{an_guk[2024]:.1f}%")
print(f"평택 소형(~60)비중: {pt_small[2015]:.1f}→{pt_small[2024]:.1f}%")
