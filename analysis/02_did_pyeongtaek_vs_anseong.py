"""[EN] Difference-in-differences: Pyeongtaek (treated) vs Anseong (control).
#1 이중차분(DiD) — 평택(처치) vs 안성(대조): 반도체 → 국평(가족형) shift 인과 추정.

대조군 정당성: 안성·평택은 고속도로 IC(안성IC)·휴게소(안성휴게소)를 공유할 만큼 인접,
반도체 前 유사 발전 → 평행추세(parallel trends) 가정 충족. (Greenstone et al. winner/loser 논리)

결과변수: 국평(전용 60–85㎡, 3방) 거래 비중(%) — "가족형 수요" 대리지표.
DiD = (평택_post - 평택_pre) - (안성_post - 안성_pre).  pre=2015–16, post=2020–24.
데이터: realprice_apt_trade.csv(평택) + realprice_apt_trade_anseong.csv(안성).
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

BASE = '/Users/Shared/seoyeon_research/realprice'
def load(path, region=None):
    rows = []
    for r in csv.DictReader(open(path, encoding='utf-8-sig')):
        if region and r['region'] != region:
            continue
        if r['excluUseAr'] and r['dealYear']:
            rows.append(r)
    return rows

pt = load(f'{BASE}/realprice_apt_trade.csv', region='평택시')
an = load(f'{BASE}/realprice_apt_trade_anseong.csv')
print(f'평택 {len(pt):,}건 / 안성 {len(an):,}건')

YEARS = list(range(2015, 2026))
def gukpyeong_share_by_year(rows):
    """연도별 국평(60-85㎡) 거래비중(%)."""
    tot = defaultdict(int); guk = defaultdict(int)
    for r in rows:
        y = int(r['dealYear'])
        if 2015 <= y <= 2025:
            tot[y] += 1
            if 60 <= float(r['excluUseAr']) < 85:
                guk[y] += 1
    return {y: (guk[y]/tot[y]*100 if tot[y] else np.nan) for y in YEARS}, tot

pt_share, pt_n = gukpyeong_share_by_year(pt)
an_share, an_n = gukpyeong_share_by_year(an)

PRE = [2015, 2016]; POST = [2020, 2021, 2022, 2023, 2024]
def avg(share, yrs): return np.nanmean([share[y] for y in yrs])
pt_pre, pt_post = avg(pt_share, PRE), avg(pt_share, POST)
an_pre, an_post = avg(an_share, PRE), avg(an_share, POST)
did = (pt_post - pt_pre) - (an_post - an_pre)

print('\n=== 국평(60-85㎡) 거래비중 (%) ===')
print(f'{"연도":>6} {"평택":>8} {"안성":>8}')
for y in YEARS:
    print(f'{y:>6} {pt_share[y]:>7.1f} {an_share[y]:>7.1f}')
print(f'\npre(2015-16):  평택 {pt_pre:.1f}  안성 {an_pre:.1f}')
print(f'post(2020-24): 평택 {pt_post:.1f}  안성 {an_post:.1f}')
print(f'Δ평택 = {pt_post-pt_pre:+.1f}%p / Δ안성 = {an_post-an_pre:+.1f}%p')
print(f'★ DiD = {did:+.1f}%p  ("반도체 효과"로 귀속되는 국평 비중 순증)')

# ── 시각화 (2패널) ──
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
fig.suptitle('이중차분(DiD): 반도체 → 국평(60-85㎡, 가족형) 전환 효과\n처치=평택 vs 대조=안성 (인접·IC공유 → 평행추세)',
             fontsize=14, fontweight='bold')

# 패널1: 시계열 + 평행추세 확인
ax1.plot(YEARS, [pt_share[y] for y in YEARS], 'o-', color='#e55', lw=2.2, label='평택 (반도체)')
ax1.plot(YEARS, [an_share[y] for y in YEARS], 's--', color='#48c', lw=2.2, label='안성 (대조)')
ax1.axvline(2017, color='blue', ls=':', lw=2, label='삼성 P1 가동 2017')
ax1.axvspan(2015, 2016, alpha=0.08, color='gray'); ax1.axvspan(2020, 2024, alpha=0.08, color='green')
ax1.set_xlabel('거래연도'); ax1.set_ylabel('국평(60-85㎡) 거래비중 (%)')
ax1.set_title('국평 비중 추이 — pre 유사, post 벌어짐'); ax1.legend(fontsize=9); ax1.grid(alpha=0.3)

# 패널2: DiD bar
labels = ['평택\npre', '평택\npost', '안성\npre', '안성\npost']
vals = [pt_pre, pt_post, an_pre, an_post]
colors = ['#f9b', '#e55', '#9bd', '#48c']
bars = ax2.bar(labels, vals, color=colors)
for b, v in zip(bars, vals):
    ax2.text(b.get_x()+b.get_width()/2, v+0.5, f'{v:.1f}', ha='center', fontsize=10, fontweight='bold')
ax2.set_ylabel('국평 거래비중 (%)')
ax2.set_title(f'DiD = (Δ평택 {pt_post-pt_pre:+.1f}) - (Δ안성 {an_post-an_pre:+.1f})\n= {did:+.1f}%p  (반도체 순효과)')
ax2.grid(alpha=0.3, axis='y')

plt.tight_layout(rect=[0, 0, 1, 0.93])
out = REPO + '/analysis/02_did_pyeongtaek_vs_anseong.png'
plt.savefig(out, dpi=120, bbox_inches='tight')
print(f'\n✅ {out}')
