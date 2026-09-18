"""[EN] Long-run population trend, Pyeongtaek vs Anseong (1966-2024).
#장기 인구 추세 — 평택 vs 안성 (1966~2024). "언제부터 벌어졌나" 역사적 맥락.

목적: DiD의 기준선 동등성 서사 강화 + 반도체 이전/이후 발산 시점 시각화.
데이터:
  1966~2015 = 통계청 인구총조사(census, 경계재구성). 평택 pre-1995 = 평택군+송탄시+옛평택시 합산.
  2020~2024 = KOSIS 주민등록(DT_1B040A3, 본인 API 실측). ← 최근 tail은 측정기준 다름(주석).
교차검증: census vs 주민등록 <1.5% 차이(평택 2015 457,873 vs 460,532) → 시계열 일관.
CSV 동시 저장: shared_data/population/city_longterm_pop_1966_2024.csv (연도·지역·인구·출처).
"""
import os as _os; REPO = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
import csv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'AppleGothic'
plt.rcParams['axes.unicode_minus'] = False

# (year, 평택, 안성, source)  — 인구총조사 1966~2015, 주민등록 2020·2024
DATA = [
    (1966, 188863, 144274, 'census'),
    (1970, 199700, 132685, 'census'),
    (1975, 225077, 133404, 'census'),
    (1980, 234356, 127891, 'census'),
    (1985, 246870, 121752, 'census'),
    (1990, 271826, 118260, 'census'),
    (1995, 312927, 120023, 'census'),  # 평택 통합시 출범
    (2000, 345306, 132906, 'census'),
    (2005, 378438, 157632, 'census'),
    (2010, 388508, 175824, 'census'),
    (2015, 457873, 183611, 'census'),
    (2020, 537307, 187012, 'resident'),   # KOSIS 주민등록 실측
    (2024, 598556, 193949, 'resident'),   # KOSIS 주민등록 실측
]

# CSV 저장
OUT_CSV = '/Users/Shared/seoyeon_research/population/city_longterm_pop_1966_2024.csv'
with open(OUT_CSV, 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.writer(f); w.writerow(['year', 'region', 'population', 'source'])
    for y, pt, an, src in DATA:
        w.writerow([y, '평택시', pt, src]); w.writerow([y, '안성시', an, src])
print(f'✅ CSV: {OUT_CSV} ({len(DATA)*2} rows)')

yrs = [d[0] for d in DATA]
pt = [d[1] for d in DATA]
an = [d[2] for d in DATA]

fig, ax = plt.subplots(figsize=(13, 7))
ax.plot(yrs, [v/1000 for v in pt], 'o-', color='#e33', lw=2.6, ms=6, label='평택시')
ax.plot(yrs, [v/1000 for v in an], 's-', color='#38a', lw=2.6, ms=6, label='안성시')

# 사건 표기
for x, txt, col in [(1995, '평택시 통합\n(송탄+평택+평택군)', 'gray'),
                    (2017, '삼성 반도체\nP1 가동', 'red'),
                    (1986, '평택역·미군기지·\n평택항 성장기', '#888')]:
    ax.axvline(x, color=col, ls=':', lw=1.5, alpha=0.7)
    ax.text(x, ax.get_ylim()[1]*0.96 if False else 620, txt, fontsize=8, color=col, ha='center', va='top')

# 발산 구간 음영
ax.axvspan(2015, 2024, alpha=0.07, color='red')
ax.annotate('반도체 가속 (평택 급증)', xy=(2019, 500), fontsize=10, color='#c22', fontweight='bold')
ax.annotate('안성: 1970→90 인구 감소\n(농촌 정체)', xy=(1978, 95), fontsize=9, color='#268')

# 배수 주석
ax.annotate(f'평택 {pt[1]/1000:.0f}천→{pt[-1]/1000:.0f}천 (×{pt[-1]/pt[1]:.1f})',
            xy=(2024, pt[-1]/1000), xytext=(2006, 560), fontsize=9, color='#e33',
            arrowprops=dict(arrowstyle='->', color='#e33', alpha=0.6))
ax.annotate(f'안성 {an[1]/1000:.0f}천→{an[-1]/1000:.0f}천 (×{an[-1]/an[1]:.1f})',
            xy=(2024, an[-1]/1000), xytext=(2006, 220), fontsize=9, color='#38a',
            arrowprops=dict(arrowstyle='->', color='#38a', alpha=0.6))

ax.set_xlabel('연도'); ax.set_ylabel('인구 (천 명)')
ax.set_title('평택 vs 안성 장기 인구 추세 (1966–2024)\n인접·유사 출발 → 평택은 철도·산업·반도체로 발산, 안성은 정체',
             fontsize=13, fontweight='bold')
ax.legend(fontsize=11, loc='upper left'); ax.grid(alpha=0.3)
ax.set_ylim(80, 640)
ax.text(0.99, 0.02, '출처: 1966–2015 통계청 인구총조사(경계재구성) / 2020–2024 KOSIS 주민등록',
        transform=ax.transAxes, fontsize=7.5, color='gray', ha='right')

plt.tight_layout()
out = REPO + '/analysis/04_longterm_population_trend.png'
plt.savefig(out, dpi=120, bbox_inches='tight')
print(f'✅ {out}')
print(f'\n평택: {pt[1]:,}(1970) → {pt[-1]:,}(2024), ×{pt[-1]/pt[1]:.2f}')
print(f'안성: {an[1]:,}(1970) → {an[-1]:,}(2024), ×{an[-1]/an[1]:.2f}')
print(f'1970 격차 {pt[1]/an[1]:.2f}배 → 2024 격차 {pt[-1]/an[-1]:.2f}배')
