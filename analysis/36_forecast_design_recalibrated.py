"""[EN] Planning-horizon trajectory recomputed after Godeok recalibration (SS IV.7-(5)).
#§IV.7-(5) 후속과제 — 계획기간 궤적의 고덕 특화 보정 후 재산출.

문제(v9~v10 §V.4-(5) 로 등록됐던 잔여 결손):
  27_forecast_design.py 는 평택시 전체 모수(ρ, P(h|a))만 사용하는 **보정 전** 사슬이어서
  1인율 39→34% 같은 궤적의 '수준(level)' 이 §IV.4 의 고덕 특화 재추정(1인율 16.1%)과 정합하지 않았다.
  → 변화의 방향·폭만 읽어야 한다는 단서를 달아 두었을 뿐 재산출은 미착수 상태였다.

본 스크립트의 보정 방식:
  ① 시나리오 A(유입지속, 현 연령 프로파일) / B(코호트 성숙, 연령 프로파일 +1밴드 이동) 각각에 대해
     보정 전 사슬로 사전분포 q_h 를 만든다.                    (27 과 동일)
  ② **구조적 편의는 λ 로 이전한다.** 32_godeok_recalibration.py 의 최대엔트로피 지수 기울기
     p_h ∝ q_h·exp(λh) 를 쓰되, λ 는 **A(2025 관측 시점)를 m̄ 앵커에 맞춰 1회만 구하고**,
     같은 λ 를 B 에 그대로 적용한다.
     근거: ρ·P(h|a) 가 평택 전체 모수라는 편의는 연령 프로파일이 이동해도 남는 **구조적** 편의이므로
           보정계수(λ)를 고정하는 것이 옳고, B 의 m̄ 는 그 결과로 '움직이게' 두어야 한다.
           (B 에 m̄=3.23 을 다시 강제하면 코호트 성숙의 효과를 정의상 지워버린다.)
  ③ m̄ 앵커는 §IV.2 관측 밴드(보수 2.99 / 기준 3.23 / 상한 3.46)로 두어 결과를 밴드로 낸다.

데이터: 전부 로컬 캐시 사용(KOSIS API 재호출 없음).
  population/godeok_age_year_matrix.csv   고덕 5세별 인구 2013–2025 (실측)
  employment/pyeongtaek_headship_2024.csv          ρ_a
  employment/pyeongtaek_head_age_hhsize_2024.csv   P(h|a)
  employment/godeok_tenure_by_size.csv             T_(s,k)
출력: employment/godeok_forecast_recalibrated.csv  (원고 §IV.7-(5) 수치의 근거)
"""
import os, csv
import numpy as np
from scipy.optimize import brentq

BASE = '/Users/Shared/seoyeon_research'
EMP, POP = f'{BASE}/employment', f'{BASE}/population'
HH = ['1인', '2인', '3인', '4인', '5인+']
SZ = np.array([1, 2, 3, 4, 5.5])                      # 5인+ 대표값 5.5 (32 와 동일)

# 연령밴드: (ρ·P(h|a) 키, 고덕 인구 CSV 컬럼들) — 85+ 는 CSV 상 4개 컬럼 합
BANDS = [('20~24세', ['20 - 24세']), ('25~29세', ['25 - 29세']), ('30~34세', ['30 - 34세']),
         ('35~39세', ['35 - 39세']), ('40~44세', ['40 - 44세']), ('45~49세', ['45 - 49세']),
         ('50~54세', ['50 - 54세']), ('55~59세', ['55 - 59세']), ('60~64세', ['60 - 64세']),
         ('65~69세', ['65 - 69세']), ('70~74세', ['70 - 74세']), ('75~79세', ['75 - 79세']),
         ('80~84세', ['80 - 84세']), ('85+', ['85 - 89세', '90 - 94세', '95 - 99세', '100+'])]

# ── 모수 적재 (전부 실측) ──
rho = {r['age_band']: float(r['headship']) for r in csv.DictReader(open(f'{EMP}/pyeongtaek_headship_2024.csv'))}
rho['85+'] = rho.get('85+', 0) or 0.56                # CSV 상 0 → 80~84 수준으로 대체(27 과 동일)

Pha = {}
for r in csv.DictReader(open(f'{EMP}/pyeongtaek_head_age_hhsize_2024.csv')):
    a = (r['age'] or '').replace(' ', '')
    if not a:
        continue
    v = np.array([float(r[h]) for h in HH])
    Pha[a] = v / v.sum() if v.sum() else v
Pha['85+'] = Pha.get('85+', Pha['80~84세'])           # 85+ 조건분포는 80~84 로 대체

MA = {'1인': [.85, .15, 0], '2인': [.50, .45, .05], '3인': [.10, .75, .15], '4인': [.03, .62, .35], '5인+': [0, .45, .55]}
MR = {'1인': [.90, .10, 0], '2인': [.60, .38, .02], '3인': [.10, .82, .08], '4인': [.03, .72, .25], '5인+': [0, .45, .55]}
SUP_A = np.array([30.1, 59.0, 11.0])                  # 고덕 공급 실측 (면적)
SUP_R = np.array([7.0, 78.4, 14.6])                   # 고덕 공급 실측 (방수)

# 점유성향: 회전율 stock 보정(매매 8년 보유 가정) — 27 과 동일
Tsize = {}
for r in csv.DictReader(open(f'{EMP}/godeok_tenure_by_size.csv')):
    v = np.array([float(r['p_sale']), float(r['p_jeonse']), float(r['p_wolse'])]) * np.array([8, 2, 2])
    Tsize[r['size_band']] = v / v.sum()

# ── 고덕 유입(2018→2025) ──
mat = {int(r['year']): r for r in csv.DictReader(open(f'{POP}/godeok_age_year_matrix.csv'))}
def band_pop(year):
    row = mat[year]
    return np.array([sum(int(row[c]) for c in cols if row.get(c)) for _, cols in BANDS], float)
inflow = np.maximum(band_pop(2025) - band_pop(2018), 0)

# ── 사슬 (보정 전) ──
def prior(infl):
    """연령유입 → 가구원수 분포 q_h (평택 전체 모수 기반, 보정 전)"""
    H = np.zeros(len(HH))
    for i, (key, _) in enumerate(BANDS):
        if key in Pha:
            H += infl[i] * rho.get(key, 0) * Pha[key]
    H = np.maximum(H, 0)
    return H / H.sum()

def tilt_lambda(q, mbar):
    """p_h ∝ q_h·exp(λh), Σp·h = mbar 를 만족하는 λ (최소 KL 발산 해)"""
    def mean_of(lam):
        w = q * np.exp(lam * SZ)
        return ((w / w.sum()) * SZ).sum()
    return brentq(lambda l: mean_of(l) - mbar, -5, 5, xtol=1e-12)

def apply_lambda(q, lam):
    w = q * np.exp(lam * SZ)
    return w / w.sum()

def outcomes(p):
    """가구원수 분포 → 면적·방수·점유 수요(%)"""
    a = np.zeros(3); r = np.zeros(3)
    for i, h in enumerate(HH):
        a += p[i] * np.array(MA[h]); r += p[i] * np.array(MR[h])
    a = a / a.sum() * 100; r = r / r.sum() * 100
    t = np.zeros(3)
    for i, s in enumerate(['소형<60', '국평60-85', '대형85+']):
        t += (a[i] / 100) * Tsize[s]
    return a, r, t / t.sum() * 100

# ── 시나리오 ──
qA = prior(inflow)
infB = np.zeros_like(inflow); infB[1:] = inflow[:-1]   # 코호트 성숙: 연령 프로파일 +1밴드(5세) 이동
qB = prior(infB)

print('=' * 96)
print('§IV.7-(5) 계획기간 궤적 — 고덕 특화 보정 후 재산출')
print('=' * 96)
print(f'\n[보정 전 사전분포]  A(2025 유입지속) 평균 {(qA*SZ).sum():.2f}명 · 1인율 {qA[0]*100:.1f}%'
      f'   |   B(2035 코호트 성숙) 평균 {(qB*SZ).sum():.2f}명 · 1인율 {qB[0]*100:.1f}%')

ANCHORS = [('보수', 2.99), ('기준', 3.23), ('상한', 3.46)]
rows = []
print('\n[보정 후]  λ 는 A 를 m̄ 앵커에 맞춰 1회 결정 → 같은 λ 를 B 에 적용(구조적 편의 이전)')
hdr = (f"{'앵커':<6}{'λ':>7} | {'A 1인율':>8}{'A 평균':>7}{'A 1-2방':>8}{'A 월세':>7}"
       f" | {'B 1인율':>8}{'B 평균':>7}{'B 1-2방':>8}{'B 월세':>7}")
print(hdr); print('-' * len(hdr))
for nm, mbar in ANCHORS:
    lam = tilt_lambda(qA, mbar)
    pA, pB = apply_lambda(qA, lam), apply_lambda(qB, lam)
    aA, rA, tA = outcomes(pA)
    aB, rB, tB = outcomes(pB)
    rows.append((nm, mbar, lam, pA, pB, aA, rA, tA, aB, rB, tB))
    print(f"{nm:<6}{lam:>+7.4f} | {pA[0]*100:>7.1f}%{(pA*SZ).sum():>7.2f}{rA[0]:>7.1f}%{tA[2]:>6.1f}%"
          f" | {pB[0]*100:>7.1f}%{(pB*SZ).sum():>7.2f}{rB[0]:>7.1f}%{tB[2]:>6.1f}%")

# ── 기준 앵커 상세 (원고 §IV.7-(5) 인용 대상) ──
nm, mbar, lam, pA, pB, aA, rA, tA, aB, rB, tB = rows[1]
print(f'\n★ 기준 앵커(m̄={mbar}) 상세 — 2025(A) → 2035(B)')
print(f"  평균 가구원수   {(pA*SZ).sum():.2f} → {(pB*SZ).sum():.2f} 명")
print(f"  1인가구 비율    {pA[0]*100:.1f}% → {pB[0]*100:.1f}%")
print(f"  면적 수요       소형 {aA[0]:.1f}→{aB[0]:.1f} · 국평 {aA[1]:.1f}→{aB[1]:.1f} · 대형 {aA[2]:.1f}→{aB[2]:.1f} %")
print(f"  방수 수요       1-2방 {rA[0]:.1f}→{rB[0]:.1f} · 3방 {rA[1]:.1f}→{rB[1]:.1f} · 4방+ {rA[2]:.1f}→{rB[2]:.1f} %")
print(f"  점유 수요       매매 {tA[0]:.1f}→{tB[0]:.1f} · 전세 {tA[1]:.1f}→{tB[1]:.1f} · 월세 {tA[2]:.1f}→{tB[2]:.1f} %")
print(f"\n  gap (공급−수요, 음수=부족)")
print(f"    2025(A)  소형 {SUP_A[0]-aA[0]:+.1f} · 대형 {SUP_A[2]-aA[2]:+.1f} · 1-2방 {SUP_R[0]-rA[0]:+.1f} · 3방 {SUP_R[1]-rA[1]:+.1f} %p")
print(f"    2035(B)  소형 {SUP_A[0]-aB[0]:+.1f} · 대형 {SUP_A[2]-aB[2]:+.1f} · 1-2방 {SUP_R[0]-rB[0]:+.1f} · 3방 {SUP_R[1]-rB[1]:+.1f} %p")

# ── 밴드 전체에서 부호가 유지되는지 (결론 강건성) ──
print('\n★ 계획기간(2035) 부호 강건성 — 3개 앵커 전체')
for idx, lab, sup, which in [(0, '소형<60㎡', SUP_A[0], 'A'), (2, '대형≥85㎡', SUP_A[2], 'A'),
                             (0, '1–2방', SUP_R[0], 'R'), (1, '3방', SUP_R[1], 'R')]:
    vals = [sup - (r[8][idx] if which == 'A' else r[9][idx]) for r in rows]
    lo, hi = min(vals), max(vals)
    verdict = '부족' if hi < 0 else ('과잉' if lo > 0 else '부호 불확정')
    print(f"  {lab:<10} {lo:+.1f} ~ {hi:+.1f} %p → {verdict}")

# ── 저장 ──
out = f'{EMP}/godeok_forecast_recalibrated.csv'
with open(out, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['anchor', 'm_bar_A', 'lambda', 'scenario', 'mean_hh', 'single_pct',
                'dem_small', 'dem_std', 'dem_large', 'dem_12room', 'dem_3room', 'dem_4room',
                'dem_sale', 'dem_jeonse', 'dem_wolse',
                'gap_small', 'gap_std', 'gap_large', 'gap_12room', 'gap_3room', 'gap_4room'])
    for nm, mbar, lam, pA, pB, aA, rA, tA, aB, rB, tB in rows:
        for sc, p, a, r, t in [('A_2025_inflow_continues', pA, aA, rA, tA),
                               ('B_2035_cohort_maturation', pB, aB, rB, tB)]:
            ga, gr = SUP_A - a, SUP_R - r
            w.writerow([nm, f'{mbar:.2f}', f'{lam:.6f}', sc, f'{(p*SZ).sum():.3f}', f'{p[0]*100:.1f}']
                       + [f'{x:.1f}' for x in a] + [f'{x:.1f}' for x in r] + [f'{x:.1f}' for x in t]
                       + [f'{x:.1f}' for x in ga] + [f'{x:.1f}' for x in gr])
print(f'\n✅ {out}')
print('\n해석: 보정 후에도 코호트 성숙(B)에서 1인율·소형·1–2방 수요가 소폭 감소하고 매매가 증가하나,')
print('      3방 과잉과 1–2방 부족의 부호는 3개 앵커 전체에서 유지 → 규격 다양화 결론은 계획기간 내 유지.')
