"""[EN] Consolidated mismatch figure — Fig. 3 (SS IV.4). Four panels in one exhibit.
#§IV.4 통합 그림 — 재캘리브레이션과 그 결과 미스매치를 한 장으로 함축.

배경: v10 까지 §IV.4 는 그림을 3장(공급구조 2패널 + 재캘리브레이션 3패널 + 분포형태 3패널 = 8패널)으로
      쪼개 같은 이야기를 반복했다. 세부를 여러 장으로 나누지 말고 **한 장으로 함축**하라는 지시에 따라
      다음 4패널 1장으로 통합한다(스토리 = 왜 보정하나 → 무엇이 바뀌나 → 두 축이 어떻게 다르나 → 공급은 왜 극단인가).

  ① 가구원수 분포: 시 전체 모수(기각) vs 고덕 특화 보정 밴드 — 왜 보정이 필요한가
  ② 면적 축: 수요(보정 후 밴드) vs 공급 → 대형만 shortage한 단방향
  ③ 방수 축: 수요(보정 후 밴드) vs 공급 → 3방 surplus·양끝 shortage의 양극(barbell)
  ④ 공급 규격군 파레토: 84~85㎡ 한 규격군에 55.3% — 공급 측 극단성

대체 대상(원고에서 제외): 28_supply_structure(표 2와 중복) · 32_godeok_recalibration · 34_barbell_distribution
데이터: 전부 로컬 실측/파생. KOSIS API 미호출.
출력: analysis/37_gap_consolidated.png
"""
import os as _os; REPO = _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__)))
DATA_ROOT = _os.environ.get('DATA_ROOT', '/Users/Shared/seoyeon_research')
INVENTORY_DB = _os.environ.get('INVENTORY_DB', '/Users/Shared/seoyeon_inventory_master.sqlite')
import os, csv, sqlite3
import numpy as np
from scipy.optimize import brentq
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.rcParams['font.family']='Helvetica'
plt.rcParams['axes.unicode_minus'] = False

BASE = REPO
EMP = DATA_ROOT + '/employment'
HH = ['1', '2', '3', '4', '5+']
SZ = np.array([1, 2, 3, 4, 5.5])

# ── 수요 재추정 (32_godeok_recalibration 과 동일 사양) ──
Q = np.array([0.393, 0.236, 0.186, 0.146, 0.039]); Q = Q / Q.sum()          # 고덕 연령기반 사전분포
PT = np.array([0.3754, 0.2745, 0.1862, 0.1340, 0.0300]); PT = PT / PT.sum()  # 평택 실측(기각된 모수)
POP_GD, APT, POP_BASE = 77337, 22368, 10382
m_up, m_lo = POP_GD / APT, (POP_GD - POP_BASE) / APT
m_mid = (m_up + m_lo) / 2

MA = {'1': [.85, .15, 0], '2': [.50, .45, .05], '3': [.10, .75, .15], '4': [.03, .62, .35], '5+': [0, .45, .55]}
MR = {'1': [.90, .10, 0], '2': [.60, .38, .02], '3': [.10, .82, .08], '4': [.03, .72, .25], '5+': [0, .45, .55]}
SUP_A = np.array([30.1, 59.0, 11.0])
SUP_R = np.array([7.0, 78.4, 14.6])

def tilt(q, mbar):
    f = lambda lam: ((q * np.exp(lam * SZ)) / (q * np.exp(lam * SZ)).sum() * SZ).sum() - mbar
    lam = brentq(f, -5, 5, xtol=1e-12)
    w = q * np.exp(lam * SZ)
    return w / w.sum()

def demand(p, M):
    d = np.zeros(3)
    for i, h in enumerate(HH):
        d += p[i] * np.array(M[h])
    return d / d.sum() * 100

P_band = [tilt(Q, m) for m in (m_lo, m_mid, m_up)]
A_band = np.array([demand(p, MA) for p in P_band])   # (3 앵커, 3 밴드)
R_band = np.array([demand(p, MR) for p in P_band])

# ── 공급 규격군 (34_barbell_distribution 과 **동일 쿼리·동일 병합 규칙** 사용) ──
# ⚠️ 근사·대체값을 쓰지 않는다. DB 접근 실패 시 그림을 그리지 않고 즉시 중단한다.
DB = INVENTORY_DB
con = sqlite3.connect(f'file:{DB}?mode=ro', uri=True)
rows = con.execute("""SELECT p.exclusive_area_m2, p.units_of_same_area FROM complexes c
 JOIN pyeong_types p ON c.complex_number = p.complex_number
 WHERE c.bjd_code LIKE '41220%' AND (c.sector LIKE '%고덕%' OR c.road_name LIKE '%고덕%')
   AND p.units_of_same_area > 0 AND p.exclusive_area_m2 IS NOT NULL""").fetchall()
con.close()
if not rows:
    raise SystemExit('❌ 공급 실측 0건 — 쿼리/DB 확인 필요 (근사값으로 대체하지 않는다)')
A = np.array([r[0] for r in rows], float)
U = np.array([r[1] for r in rows], float)
tot = U.sum()

_b = {}
for a_, u_ in zip(A, U):
    _b[int(round(a_))] = _b.get(int(round(a_)), 0) + u_
_ks = sorted(_b); _runs = []; _cur = [_ks[0]]
for _k in _ks[1:]:
    if _k - _cur[-1] <= 1:
        _cur.append(_k)
    else:
        _runs.append(_cur); _cur = [_k]
_runs.append(_cur)
grp = [((f'{r[0]}~{r[-1]}' if len(r) > 1 else f'{r[0]}'), sum(_b[k] for k in r)) for r in _runs]
grp.sort(key=lambda t: -t[1])
share = [v / tot * 100 for _, v in grp]
cum = np.cumsum(share)
labels = [f'{k}m2' for k, _ in grp]

# ── 작도 ──
fig, ax = plt.subplots(1, 4, figsize=(21, 5.2))
fig.suptitle('Demand recalibration and the unit-composition mismatch: (1) why recalibrate  (2) floor-area axis: large units short  (3) room-count axis: barbell  (4) concentration of supply',
             fontsize=13.5, fontweight='bold')
C_SUP, C_DEM, C_REJ = '#c0392b', '#2980b9', '#95a5a6'

# ① 가구원수 분포
x = np.arange(len(HH)); w = 0.2
ax[0].bar(x - 1.5 * w, PT * 100, w, color=C_REJ, label=f'City-wide parameters (mean {(PT*SZ).sum():.2f}, not used)')
for j, (p, nm) in enumerate(zip(P_band, ['low 2.99', 'base 3.23', 'high 3.46'])):
    ax[0].bar(x + (j - 0.5) * w, p * 100, w, label=f'Godeok-corrected, mean {nm}',
              color=plt.cm.Blues(0.45 + 0.2 * j))
ax[0].set_xticks(x); ax[0].set_xticklabels(HH)
ax[0].set_ylabel('Share of households (%)')
ax[0].set_title('(1) Household-size distribution, fitted to the observed mean', fontsize=11)
ax[0].legend(fontsize=7.5); ax[0].grid(alpha=0.3, axis='y')

# ②③ 면적·방수 수요 vs 공급
for k, (band, sup, labs, ttl) in enumerate([
        (A_band, SUP_A, ['Small\n<60m2', 'Standard\n60-85m2', 'Large\n>=85m2'], '(2) Floor-area axis: only large units are short'),
        (R_band, SUP_R, ['1-2 rooms', '3 rooms', '4+ rooms'], '(3) Room-count axis: a barbell')]):
    a = ax[k + 1]; xx = np.arange(3)
    lo, hi, mid = band.min(0), band.max(0), band[1]
    a.bar(xx - 0.19, mid, 0.36, yerr=[mid - lo, hi - mid], capsize=4,
          color=C_DEM, label='Demand (corrected; band = 3 anchors)')
    a.bar(xx + 0.19, sup, 0.36, color=C_SUP, label='Supply (measured)')
    ymax = max(sup.max(), hi.max()) * 1.30
    for i in range(3):
        gap = sup[i] - mid[i]
        over = gap > 0
        a.annotate(f'{"+" if over else "-"}{abs(gap):.1f}%p\n{"surplus" if over else "shortage"}',
                   (xx[i], max(mid[i], sup[i]) + ymax * 0.035), ha='center', va='bottom',
                   fontsize=9, fontweight='bold', linespacing=1.25,
                   color='white',
                   bbox=dict(boxstyle='round,pad=0.28',
                             fc=('#c0392b' if over else '#1e6091'), ec='none', alpha=0.92))
    a.set_xticks(xx); a.set_xticklabels(labs, fontsize=9)
    a.set_ylabel('Share (%)'); a.set_ylim(0, ymax)
    a.set_title(ttl, fontsize=11); a.legend(fontsize=7.5, loc='upper left'); a.grid(alpha=0.3, axis='y')

# ④ 공급 규격군 파레토 — 막대(비중)와 누적선을 분리해 겹침 제거
n = min(10, len(grp))
a = ax[3]; xx = np.arange(n)
a.bar(xx, share[:n], 0.62, color=C_SUP)
a.set_xticks(xx); a.set_xticklabels(labels[:n], rotation=45, ha='right', fontsize=8)
a.set_ylabel('Share of units (%)'); a.set_ylim(0, share[0] * 1.42)
a.text(0.50, 0.60, f'{labels[0]} alone:\n{grp[0][1]:,.0f} units = {share[0]:.1f}%',
       transform=a.transAxes, ha='center', va='center', fontsize=10, fontweight='bold',
       color='#7b241c',
       bbox=dict(boxstyle='round,pad=0.42', fc='#fdedec', ec='#c0392b', lw=1.1))
a.annotate('', xy=(0.18, share[0] * 0.72), xytext=(2.0, share[0] * 0.90),
           arrowprops=dict(arrowstyle='->', color='#c0392b', lw=1.4))
a2 = a.twinx()
a2.plot(xx, cum[:n], 'o-', color='#2c3e50', lw=1.6, ms=4, label='cumulative share')
a2.axhline(cum[2], ls=':', color='#7f8c8d', lw=1.2)
a2.text(n - 0.4, cum[2] + 3.5, f'Top 3 groups {cum[2]:.1f}%', ha='right', va='bottom',
        fontsize=8.5, color='#555')
a2.set_ylabel('Cumulative (%)'); a2.set_ylim(0, 112)
a.set_title(f'(4) Pareto of supplied unit types ({len(grp)} groups)', fontsize=11)
a.grid(alpha=0.3, axis='y')

plt.tight_layout(rect=[0, 0, 1, 0.91])
out = f'{BASE}/analysis/37_gap_consolidated.png'
plt.savefig(out, dpi=120, bbox_inches='tight')
print(f'✅ {out}')
print(f'\n검증 — 기준 앵커 gap: 소형 {SUP_A[0]-A_band[1][0]:+.1f} · 국평 {SUP_A[1]-A_band[1][1]:+.1f} · '
      f'대형 {SUP_A[2]-A_band[1][2]:+.1f} | 1-2방 {SUP_R[0]-R_band[1][0]:+.1f} · 3방 {SUP_R[1]-R_band[1][1]:+.1f} %p')
print(f'검증 — 최대 규격군 {labels[0]} {grp[0][1]:,.0f}세대 = {share[0]:.1f}% · 상위3 누적 {cum[2]:.1f}% · 규격군 수 {len(grp)} · 총 {tot:,.0f}세대')
