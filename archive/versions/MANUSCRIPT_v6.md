<!-- v6 (2026-07-25): 「국토계획」(대한국토·도시계획학회지) 투고 양식으로 형식 재구성. -->
<!-- 내용·수치는 v6 서술본(→ MANUSCRIPT_v6_preformat_backup.md)과 동일, 형식만 학술지 양식. 이력 _CHANGELOG.md. -->
<!-- ⚠️ 실제 저널 ISSN/DOI/배너는 미기재(미게재 학생 원고를 게재본으로 위장하지 않기 위함). -->

> ## ⚠️ 인용 주의 — 본 판(v6)의 gap 수치는 수요측 가정 오류로 과대추정되었습니다
>
> **2026-07-25 감사 결과**: 본 판은 gap 계산의 수요 분포로 **평택시 전체 가구원수(1인 37.5%)** 를 사용했으나, 이는 고덕에 부적절함이 실측으로 확인되었습니다.
> - 고덕 0–14세 비중 **19.4%**(평택 12.6%·전국 10.3%), 65세+ **6.7%**(평택 14.6%) → 고덕은 **젊은 가족 도시**이며, 평택 전체의 1인가구율은 상당부분 구도심 **고령 1인가구**에서 발생.
> - 고덕 평균 가구원수 **약 3.0–3.5명**(평택 2.18명)인데, 본 판 설계모델이 산출한 분포의 평균은 **2.22명** → 내부 모순.
> - 재계산 시 **소형 gap의 부호가 반전**될 수 있음(−17.8%p 부족 → +3~+13%p 과잉), **대형이 오히려 부족**(−9~−15%p), **1–2방 부족은 방향 유지·크기 축소**(−45.6 → −12~−23%p).
>
> **여전히 유효한 결과**: 공급의 3방 78.4% 편중(실측) · 월세 편중의 고덕 특수성(고덕 73.4% vs 안성 53.5%, 대조 검증 통과) · 캠퍼스 거리 hedonic(−3.7%/km) · 규격추세의 전국성 · **1–2방 부족의 방향**.
>
> → **수정판은 [`MANUSCRIPT_v7.md`](MANUSCRIPT_v7.md)를 인용하십시오.** 본 판은 이력 보존용(롤백점)으로만 유지되며 내용을 수정하지 않습니다.

*「국토계획」 투고 양식 준용 초안 — 미게재 학생 연구원고. 📑 근거 지도 → [`PAPER_GUIDE.md`](PAPER_GUIDE.md) · 이전 서술본 [`v6_preformat_backup`](MANUSCRIPT_v6_preformat_backup.md) · 이력 [`_CHANGELOG.md`](_CHANGELOG.md)*

<br>

# 반도체 클러스터 주변지역 신도시의 주거 규격은 인구 구조를 반영하는가
### : 고덕 사례와 수요–공급 gap 기반 규격 다양화 제언<sup>*</sup>

# Does the Housing Unit Composition of a New Town near a Semiconductor Cluster Reflect Its Population Structure?
### : The Godeok Case and a Demand–Supply Gap-Based Proposal for Unit Diversification

<br>

**전서연**<sup>**</sup>
SEOYEON JEON<sup>**</sup>

---

> **Abstract**
>
> Semiconductor clusters give rise to planned new towns nearby that concentrate a specific age cohort—young workers. Using Godeok New Town, adjacent to Samsung's Pyeongtaek Campus, as a case, this study diagnoses whether the supply of housing unit types reflects the area's demographic structure—drawing on transaction, population, and supply data—and proposes unit diversification grounded in a demand–supply gap framework. A large share of Pyeongtaek's net population growth concentrated in Godeok alone (population ×5.7; share of the city 3.1%→12.7%; virtually all net growth since 2022), and the center of gravity of in-migration was working-age adults 25–39 (2.4× the inflow of teenagers) together with young children. New supply, however, skewed heavily toward three-bedroom units (79%) and the standard 60–85㎡ floor area (59%). A gap index (supply − demand; negative = shortage), contrasting supply with demand estimated from Pyeongtaek's measured household-size distribution (single-person 37.5%; KOSIS DT_1JC1516), shows a **17.8-percentage-point shortage of small units (<60㎡)** and a **17.4-point surplus of standard units**; the shortage direction is robust across a sensitivity range of assumptions (−5.8 to −33.2pp). In practice, demand for small units is realized through leasing (56% small among leases vs. 44% among sales; 76% of leases are monthly-rent) rather than new-build ownership. We further generalize the diagnosis into a **predictive design chain (age inflow → household formation → unit size, room count, and tenure)**, with household formation grounded in measured head-age-by-household-size distributions. The model reveals that the mismatch is far larger in room count than in floor area (1–2-room gap −44.8pp vs. −17.4pp for area), and passes cross-city transferability validation (MAPE 6–11%), mapping-assumption sensitivity, and planning-horizon (2035) stability checks. This is a data-grounded consistency diagnosis and proposal, not a causal or optimal-allocation claim.
>
> **Keywords**: semiconductor-adjacent new town, housing unit-size fit, demand–supply gap, unit diversification, single-person and working households, real transaction data

---

**■ 국문 초록** 반도체 클러스터 주변지역에는 계획 신도시가 조성되고 특정 연령대(젊은 근로자)가 집중된다. 본 연구는 삼성 평택캠퍼스 주변지역 고덕신도시를 사례로, 주거 규격 공급이 그 지역의 인구 구조를 반영하는지를 실거래·인구·공급 데이터로 진단하고, 수요–공급 gap에 기반한 규격 다양화 방향을 제언한다. 평택 인구 순증의 상당부분이 고덕 한 곳에 집중됐고(고덕 ×5.7, 비중 3.1→12.7%, 2022년 이후 순증은 사실상 전부 고덕), 유입 무게중심은 25–39세 근로연령(청소년 유입의 2.4배)과 어린 자녀였다. 그러나 신축 공급은 3방(79%)·국민평형(59%)에 편중됐다. 평택 실측 가구원수(1인 37.5% 등, KOSIS DT_1JC1516)로 추정한 규격 수요를 공급과 대조한 gap 지수(공급−수요, 음수=부족)는 소형(<60㎡) −18%p 부족, 국민평형 +17%p 과잉을 보였고, 규격매핑 가정을 범위로 흔든 민감도 분석에서도 소형 부족 방향은 강건했다(−5.8~−33.2%p). 실제로 소형 수요는 매매(소형 44%)보다 전월세(소형 56%, 월세 비중 76%)로 우회 실현됐다. 나아가 연령유입→가구형성→규격·방수·점유의 예측 사슬(설계모델)을 제시했으며, 미스매치가 면적보다 방수에서 훨씬 큼(1–2방 −45%p vs 소형 −17%p)을 드러냈고, 타 도시 이식 검증(MAPE 6~11%)·매핑 민감도·계획기간(2035) 안정성을 통과했다. 단, 이는 인과·최적량의 단정이 아니라 다층 데이터에 근거한 정합성 진단·제언이다.

**주제어**: 반도체 주변지역 신도시, 주거 규격 정합성, 수요–공급 gap, 규격 다양화, 1인·근로가구, 실거래가

<sub>* 본 연구는 학생 연구과제로 수행되었으며, 국토교통부 실거래가·통계청 KOSIS·NAVER 부동산 공개 데이터를 활용하였다.</sub>
<sub>** Valor International Scholars (제1저자·교신저자). E-mail: seoyeon.jeon@valorschool.org, alisnaea43@gmail.com</sub>

---

## I. 서론

### 1. 연구의 배경

반도체 산업은 주변지역에 계획 신도시를 만들고 젊은 근로 인구를 집중시킨다(Greenstone et al., 2010). 삼성전자 평택캠퍼스(P1 2017·P2 2020·P3 2022)의 가동과 함께 고덕국제신도시가 조성되었고, 인구·개발·주택 가격이 빠르게 재편되었다. 통념은 "가족 유입 → 국민평형(3방) 수요"이지만, 유입의 무게중심이 젊은 근로·소가구라면 통념대로 지어진 공급은 수요와 어긋날 수 있다. 그러나 이러한 신도시에 공급되는 주거 **규격**(면적·방수·점유형태)이 실제 유입 인구의 연령·가구 구조와 정합하는지는 검증된 바 없다.

### 2. 연구의 목적

본 연구의 질문은 다음과 같다. **① 고덕신도시의 주거 공급 규격은 그 지역 인구를 반영하는가? ② 반영하지 못한다면 어떤 규격을 다양화해야 하는가?** 이에 따른 기여는 (1) 인구·공급·거래(매매/전월세) 다층 데이터로 규격 정합성 진단, (2) 가구형태 기반 수요–공급 gap 프레임워크(의사결정 지원) 제시, (3) 연령유입 기반 주거설계 예측모델(가구화 실측·규격/방수/점유 산출·타 도시 이식 검증) 제시, (4) 비판적 검토로 가정·한계를 투명화하는 것이다.

---

## II. 이론 및 선행연구 고찰

### 1. 대형 산업 입지의 지역 효과

대형 산업 입지는 고용·인구·주택시장에 광범위한 지역 효과를 낳는다(Greenstone et al., 2010; Dallas Fed, 2023). 반도체와 같은 첨단산업 클러스터는 특히 젊은 근로 인구를 단기간에 집중시켜, 주변지역 주거의 수요 구조를 통상적 도시와 다르게 만든다.

### 2. 인구 구조와 주택 수요

인구 연령 구조는 주택 수요의 양과 규격을 좌우한다(Mankiw and Weil, 1989). 가구는 인구로부터 형성되며(가구주화·headship), 가구원수 구성이 필요한 주거 규격을 결정한다. 코호트-요인법(cohort-component)은 연령별 인구로부터 가구를 추계하는 표준 방법이다(Zeng et al., 2014). 본 연구의 설계 예측모델은 이 접근을 규격·방수·점유 설계로 확장한다.

### 3. 수요–공급 정합성(격차) 진단

주택 공급이 수요와 얼마나 정합하는지를 격차(gap)로 진단하는 접근이 제안되어 왔다(*Journal of Housing and the Built Environment*, 2025). 한국의 1인가구 증가와 소형주택 수요에 관한 논의도 축적되어 있다(대한국토·도시계획학회, 2024). 본 연구는 이 격차 진단을 반도체 주변지역 신도시의 규격 설계에 적용한다.

### 4. 연구의 차별성

기존 연구가 규격 '추세'(국민평형화 등)를 전국 현상으로 다룬 데 비해, 본 연구는 (1) 특정 신도시(고덕)의 국지 인구 구조와 공급 규격의 정합성을 진단하고, (2) 가구원수·가구주연령별 가구원수를 **실측**으로 사용하며, (3) 연령유입에서 규격·방수·점유를 산출하는 예측모델을 제시하고 타 도시로 이식 검증한다는 점에서 차별적이다.

---

## III. 분석 방법론

### 1. 분석의 범위

공간적 범위는 삼성 평택캠퍼스 주변 고덕신도시(평택시 고덕면·고덕동)와 비교 기준으로서 평택시 전역이며, 대조도시로 안성·화성·광주를 사용한다. 시간적 범위는 실거래 2015–2025년, 인구 2011–2025년이다.

### 2. 분석 데이터

<br>**표 1. 분석 데이터 개요**
**Table 1. Overview of analysis data**

| ID | 자료 | 출처·코드 | 기간 | 파일 |
|---|---|---|---|---|
| D1 | 아파트 매매·전월세 실거래 | 국토교통부 실거래가 | 2015–2025 | `realprice/` |
| D2 | 5세별 인구 | 통계청 KOSIS DT_1B04005N | 2011–2025 | `population/` |
| D3b | 가구원수별 가구(실측) | 통계청 KOSIS DT_1JC1516 | 2015–2024 | `employment/` |
| D3c | 가구주연령×가구원수(실측) | 통계청 KOSIS DT_1JC1511 | 2024 | `employment/` |
| D7 | 단지·평형·방수·좌표 메타 | NAVER 부동산 | ~2026 | master sqlite |

<sub>Source: 국토교통부·통계청·NAVER 부동산 공개 데이터. 상세는 `DATA_SOURCES.md`.</sub>

### 3. 분석 방법

**1) 수요–공급 gap 프레임워크.** 가구형태 분포(실측) × 규격수요 매핑(가정)으로 수요 규격비중을 산출하고, 공급 규격비중과 대조한다. **Gap = 공급 − 수요**로 정의하며, **음수는 부족**(공급확대 필요), **양수는 과잉**을 뜻한다. 규격수요 매핑 가정은 민감도 분석으로 강건성을 검증한다.

**2) 캠퍼스 거리 hedonic.** 실거래를 단지 좌표에 매칭하여, 로그 단가를 캠퍼스로부터의 연속거리(km)·신도시 더미·면적·연식·연도 고정효과에 회귀한다(HC0 robust). '공장 근접'과 '신도시 패키지'를 부분 분리한다.

**3) 연령유입 기반 주거설계 예측모델.** 연령대 `a`별 순유입 `n_a`로부터 다음 사슬로 규격·방수·점유·1인비율을 산출한다(하첨자는 `_`로 표기: `H_h`=가구원수 h인 가구, `Σ_a`=연령 a에 대한 합).
```
가구화       H_h    = Σ_a  n_a · ρ_a · P(h | 가구주연령 a)      (ρ = 헤드십, P = DT_1JC1511 실측 조건분포)
규격·방수    D면적_s = Σ_h  H_h · M면적_(h,s) ,   D방수_r = Σ_h  H_h · M방수_(h,r)
점유         D점유_k = Σ_s  D면적_s · T_(s,k)                   (T = 고덕 실거래, 회전율 stock 보정)
1인 비율     = H_1 / Σ_h H_h
```
여기서 `ρ_a`·`P(h|a)`·`T_(s,k)`는 실측이고, 규격매핑 `M`만 문헌·상식 가정이며 민감도로 검증한다.

---

## IV. 분석 결과

### 1. 고덕신도시로의 성장 집중

평택 인구 순증 중 고덕이 약 38%(2013→2025)를 차지하며, **2022년 이후 순증은 사실상 전부 고덕**이다(고덕 +34,878 / 평택 나머지 −3,005). 고덕 인구는 13,651→77,337명(×5.7), 비중 3.1→12.7%로 늘었다. 신규 아파트 개발 점유율도 1→73%로 급등했고, 외곽 대비 가격배율은 0.96→2.49배(연식통제 시 1.22→1.67)로 벌어졌다. 인구·개발·가격이 모두 고덕 한 곳으로 수렴한다.

**그림 1. 고덕 집중 — 고덕 vs 평택(고덕 제외)** / **Figure 1. Concentration in Godeok vs. rest of Pyeongtaek**
![그림1](../analysis/20_godeok_concentration.png)
<sub>Source: KOSIS DT_1B04005N 기반 저자 작성.</sub>

**그림 2. 개발의 공간 집중(고덕 점유 1→73%)** / **Figure 2. Spatial concentration of development**
![그림2](../analysis/13_development_concentration.png)
<sub>Source: 단지 메타(NAVER 부동산) 기반 저자 작성.</sub>

**그림 3. 국지 가격 거리감쇠(고덕 인접 vs 외곽)** / **Figure 3. Local price gradient by distance**
![그림3](../analysis/12_local_premium_gradient.png)
<sub>Source: 국토교통부 실거래 기반 저자 작성.</sub>

### 2. 유입 인구의 연령 구조

유입(2018→2025)의 무게중심은 25–39세 근로연령(+24,986명)으로, 청소년 5–19세(+10,451명)의 2.4배, 영유아 0–4세(+5,255명)의 4.8배이다. 다만 영유아·청소년·40대도 대거 증가하여, "젊은 근로연령 + 어린 자녀"의 젊은 소가구·가족 혼합 양상을 보인다(순수 1인 근로자 도시도, 전형적 가족 도시도 아님).

**그림 4. 고덕 연령 구성 — 근로연령(25–39) + 어린 자녀** / **Figure 4. Age structure of Godeok inflow**
![그림4](../analysis/22_godeok_age.png)
<sub>Source: KOSIS DT_1B04005N(고덕면·고덕동) 기반 저자 작성.</sub>

### 3. 신축 주거 규격의 공급 구조

고덕신도시 신축 아파트의 규격 구성을 단지 메타(NAVER 부동산) 기준으로 집계했다. 대상은 고덕 소재 **29개 단지·총 22,368세대**이며, 각 세대를 방(침실) 수와 전용면적으로 분류했다(표 2, 그림 5).

**방(침실) 수** 기준으로는 **3방이 17,527세대(78.4%)로 압도적**이고, 4방+ 3,266세대(14.6%), 1–2방은 1,575세대(**7.0%**)에 불과하다. 즉 3방 이상이 전체의 **93.0%**를 차지해, 소형 방수(1–2방)는 사실상 배제되어 있다. **전용면적** 기준으로도 국민평형(60–85㎡)이 13,188세대(**59.0%**)로 절반을 넘고, 소형(<60㎡)은 6,725세대(30.1%), 대형(≥85㎡)은 2,455세대(11.0%)이다.

요컨대 고덕 신축 공급은 **국민평형·3방이라는 전국 표준 템플릿에 강하게 수렴**한다. 이 공급 구조가 유입 인구의 가구 구조(§IV.2, IV.4)와 정합하는지가 이후 분석의 핵심이다.

<br>**표 2. 고덕 신축 아파트 공급 규격 구성 (29단지·22,368세대)**
**Table 2. Composition of new-apartment unit types in Godeok (29 complexes, 22,368 units)**

| 구분 | 범주 | 세대수 | 비중 |
|---|---|---|---|
| 방수 | 1–2방 | 1,575 | 7.0% |
| 방수 | **3방** | **17,527** | **78.4%** |
| 방수 | 4방+ | 3,266 | 14.6% |
| 면적 | 소형 <60㎡ | 6,725 | 30.1% |
| 면적 | **국민평형 60–85㎡** | **13,188** | **59.0%** |
| 면적 | 대형 ≥85㎡ | 2,455 | 11.0% |

<sub>Source: master sqlite(complexes+pyeong_types) 기반 저자 집계(`analysis/28_supply_structure.py`).</sub>

**그림 5. 고덕 신축 공급 구조 — 방수·면적 분포** / **Figure 5. Unit-type composition of new supply in Godeok**
![그림5](../analysis/28_supply_structure.png)
<sub>Source: 단지 메타(NAVER 부동산) 기반 저자 작성.</sub>

### 4. 수요–공급 규격 gap 지수

평택 2024년 실측 가구원수(1인 37.5%·2인 27.5%·3인 18.6%·4인 13.4%·5인+ 3.0%, KOSIS DT_1JC1516)에 규격수요 매핑을 적용해 산출한 수요를 공급과 대조한 결과는 표 3과 같다. 선행 근사 분포로 계산한 값과 사실상 동일하여, 실측이 프로토타입 추정을 확증한다.

<br>**표 3. 규격 수요–공급 gap (Gap = 공급 − 수요; 음수 = 부족)**
**Table 3. Unit-size demand–supply gap (supply − demand; negative = shortage)**

| 규격 | 수요(%) | 공급(%) | Gap(%p) |
|---|---|---|---|
| 소형 <60㎡ | 47.9 | 30.1 | **−17.8 (부족)** |
| 국민평형 60–85㎡ | 41.6 | 59.0 | +17.4 (과잉) |
| 대형 ≥85㎡ | 10.5 | 11.0 | +0.5 (균형) |

<sub>Source: 저자 계산(`analysis/21_gap_index_prototype.py`).</sub>

규격수요 매핑·가구배분 가정을 '가족편중(보수)'~'고덕형 소가구' 세 시나리오로 변주해도 **소형 gap = −5.8 ~ −33.2%p로 전부 음수(부족)**, 국민평형 gap은 전부 양수(과잉)로 부호가 뒤집히지 않았다(그림 7). 고덕은 젊은 근로가 다수여서 소가구 비중이 평택 평균보다 높을 개연성이 커, 실측 기준(−17.8%p)은 보수적(더 큰 부족 가능)일 수 있다.

**그림 6. 규격 수요–공급 gap 지수** / **Figure 6. Unit-size demand–supply gap index**
![그림5](../analysis/21_gap_index_prototype.png)
<sub>Source: 저자 계산.</sub>

**그림 7. gap 민감도 — 가정 변주에도 소형 부족 강건** / **Figure 7. Sensitivity of the gap to mapping assumptions**
![그림6](../analysis/21b_gap_sensitivity.png)
<sub>Source: 저자 계산.</sub>

### 5. 시장 분화 — 소형 수요의 전월세 실현

고덕에서 매매의 소형 비중(44%)보다 전월세의 소형 비중(56%)이 높고, 전월세 중 월세 비중이 76%에 달한다. 즉 젊은 근로·소가구의 소형 수요는 신축 자가가 아니라 전월세(특히 월세)로 우회 실현된다. 이는 수요 자체가 부재했다는 대안 설명을 배제하는 근거가 된다.

**그림 8. 전월세 — 소형 실재처·월세화** / **Figure 8. Lease market: where small-unit demand is realized**
![그림7](../analysis/10_rent_analysis.png)
<sub>Source: 국토교통부 실거래 기반 저자 작성.</sub>

### 6. 규격 변화의 전국적 성격(배경)

국민평형화·소형 감소는 안성·광주(반도체 前)에서도 동일하거나 더 강하게 나타나며, 거시(팬데믹·금리) 사이클을 보정하면 평택 고유 추세가 사라진다. 따라서 규격 '추세'는 전국 구조이며, 본 연구의 초점은 "반도체가 규격을 바꿨나"가 아니라 "고덕의 특수 인구에 규격 공급이 정합하나"이다. 이는 본 연구가 모든 공급 미스매치를 반도체 효과로 귀속시키지 않음을 뒷받침한다.

**그림 9. 규격의 전국성 — 거시 사이클 보정** / **Figure 9. Nationwide nature of the unit-size trend**
![그림8](../analysis/08_macro_adjusted.png)
<sub>Source: 저자 계산.</sub>

### 7. 공간 근접의 독립 효과 — 캠퍼스 거리 hedonic

고덕 집중이 '캠퍼스 근접' 때문인지 '신도시 라벨' 때문인지 부분 분리하기 위해, 평택 실거래(단지 좌표 매칭 41,196건, 매칭률 58%)에 hedonic 회귀를 적용했다(표 4).

<br>**표 4. 캠퍼스 거리 hedonic 회귀 결과**
**Table 4. Hedonic regression on distance to campus**

| 변수 | 계수(효과) | 유의성 |
|---|---|---|
| 캠퍼스 거리(km) | **−3.7%/km** | p<0.0001 |
| 신도시 더미(고덕, 순프리미엄) | +3.2% | p<0.0001 |
| 고덕 제외 서브샘플(n=37,281) | −3.7%/km | p<0.0001 |

<sub>Source: 저자 계산(`analysis/23_distance_hedonic.py`). 통제변수: ln면적·연식·연도 고정효과, HC0 robust.</sub>

가격 프리미엄의 대부분은 이산적 신도시 라벨(+3.2%)이 아니라 캠퍼스로의 연속 거리(−3.7%/km)에서 온다. 신도시가 하나도 없는 서브샘플에서도 −3.7%/km가 유지되어, 근접 효과는 신도시의 산물이 아닌 독립 효과이다. 캠퍼스 기준점을 정문·P2·중앙으로 바꿔도 −2.5 ~ −3.7%/km로 강건하다. 이는 공급 계획의 단위가 행정적 신도시 경계가 아니라 고용 앵커로부터의 통근 접근성이어야 함을 시사한다.

**그림 10. 캠퍼스 연속거리 hedonic — 근접 vs 신도시 분리** / **Figure 10. Continuous distance-to-campus hedonic**
![그림9](../analysis/23_distance_hedonic.png)
<sub>Source: 저자 계산.</sub>

**그림 11. hedonic — 연식 통제 프리미엄(배경)** / **Figure 11. Hedonic premium controlling for building age**
![그림10](../analysis/16_hedonic.png)
<sub>Source: 저자 계산.</sub>

### 8. 연령유입 기반 주거설계 예측모델

gap 진단을 "연령유입 → 가구형성 → 규격·방수·점유 설계"의 예측 사슬로 일반화한다(모델식은 III.3-3) 참조). 가구주 25–39세는 1인가구 51.4%·1–2인 72.9%(전연령 1인 37.1%)로, 젊은 가구주일수록 소가구가 압도적이다(DT_1JC1511). 이 실측 조건분포와 헤드십(20–24세 0.17 → 40대+ 0.57)을 사슬에 대입해 고덕 유입(2018→2025)에 적용한 결과는 표 5와 같다.

<br>**표 5. 설계모델 적용 결과(고덕) — Gap = 공급 − 수요(음수 = 부족)**
**Table 5. Design-model results for Godeok**

| 지표 | 값 |
|---|---|
| 신규 유입 1인가구 비율 | 39.3% |
| 면적 소형 gap | −17.4%p |
| **방수 1–2방 gap** | **−44.8%p** (부족이 면적보다 큼) |
| 점유(flow→stock 보정) | 매매 10→31 / 전세 26→19 / 월세 64→50% |

<sub>Source: 저자 계산(`analysis/24_design_model.py`, `26_tenure_stock_adjust.py`).</sub>

미스매치(부족)는 면적(−17%p)보다 방수(1–2방, −45%p)에서 훨씬 크다. 규격매핑을 변주해도 소형 gap −7~−24%p, 1–2방 gap −33~−53%p로 전부 음수(부족)이며(그림 13), 특히 방수 부족은 공급의 3방 극단편중(78%) 때문에 어떤 가정에서도 강건하다.

**검증(이식 가능성).** 평택에서 캘리브레이션한 파라미터로 타 도시 가구원수를 예측한 결과(표 6), 평택 자기일관성 MAPE 0.8%, 안성 6.0%, 화성 11.0%였다. 사슬은 광역 구조를 포착하되 도시별 국지차가 존재한다.

<br>**표 6. 모델 검증 — 타 도시 가구원수 예측 오차(MAPE)**
**Table 6. Model validation — cross-city prediction error (MAPE)**

| 도시 | MAPE(%) | 해석 |
|---|---|---|
| 평택(자기일관성) | 0.8 | 사슬 기계 정확 |
| 안성(유사 대조) | 6.0 | 양호한 이식 |
| 화성(가족 多 신도시) | 11.0 | 소가구 과대예측(국지차) |

<sub>Source: 저자 계산(`analysis/25_model_validation.py`).</sub>

**계획기간 안정성.** 유입지속(A) vs 코호트 성숙(B, 자녀성장·고령화) 시나리오에서 2035년에도 1인율 39→34%, 1–2방 수요 52→48%, 월세 ~49%로 소폭만 이동하여, 규격 다양화 결론은 계획기간(2030/2035) 내 유지된다(그림 16).

**그림 12. 연령유입 기반 설계 예측모델** / **Figure 12. Age-inflow-based housing design model**
![그림11](../analysis/24_design_model.png)
<sub>Source: 저자 계산.</sub>

**그림 13. 모델 민감도 — 매핑 변주에도 소형·1–2방 부족 강건** / **Figure 13. Model sensitivity**
![그림12](../analysis/24b_model_sensitivity.png)
<sub>Source: 저자 계산.</sub>

**그림 14. 모델 검증(transferability)** / **Figure 14. Model validation across cities**
![그림13](../analysis/25_model_validation.png)
<sub>Source: 저자 계산.</sub>

**그림 15. 점유 회전율 보정 — flow vs stock** / **Figure 15. Tenure turnover adjustment**
![그림14](../analysis/26_tenure_stock_adjust.png)
<sub>Source: 저자 계산.</sub>

**그림 16. 설계 target 궤적(2025→2035)** / **Figure 16. Design-target trajectory**
![그림15](../analysis/27_forecast_design.png)
<sub>Source: 저자 계산.</sub>

---

## V. 결론

### 1. 종합 논의

본 연구는 삼성 반도체 평택캠퍼스가 주변 주거시장에 미친 영향을 고덕신도시 사례를 통해 분석하고, 공급된 주택 규격이 실제 유입 인구의 가구형성 구조와 정합적인지를 검증했다.

분석 결과, 반도체 투자로 촉발된 성장은 평택 내 단일 지점(고덕)에 극도로 집중되었으며(개발 점유율 1→73%, 가격배율 0.96→2.49, IV.1), 이 지점으로 유입된 인구는 25–39세 근로연령층과 그 어린 자녀를 중심으로 뚜렷한 인구학적 프로파일을 형성했다(IV.2). 그러나 신축 공급은 국민평형·3방 위주의 표준 템플릿을 따랐고(IV.3), 그 결과 실제 가구원수 기반 수요와의 괴리(gap)가 발생했다(IV.4). 이 괴리는 면적 기준(−17.8%p)보다 방수 기준(−44.8%p)에서 현저히 컸으며, 다수의 민감도 분석에도 부호가 강건하게 유지되었다. 억눌린 소형·소방 수요는 매매 대신 전월세(특히 월세, 76%)를 통해 우회적으로 실현되고 있었는데(IV.5), 이는 수요 자체가 부재했다는 대안 설명을 배제하는 근거가 된다.

가격 프리미엄의 원천을 분해한 결과, 이는 "신도시"라는 지위 자체보다 반도체 캠퍼스와의 물리적 거리(−3.7%/km)에서 발생하는 것으로 나타났다(신도시 더미 효과는 +3.2%에 불과, IV.7). 이는 신도시 개발 담론에서 통용되어온 "신도시 라벨 프리미엄" 가설과 배치되는 결과이며, 공급 계획의 단위가 행정적 신도시 경계가 아니라 고용 앵커로부터의 통근 접근성이어야 함을 시사한다.

이상을 종합하면, 반도체 캠퍼스와 같은 고용 앵커형 개발은 표준화된 신도시 공급 템플릿으로는 포착되지 않는 고유한 수요 구조─젊고 소형가구 중심적인─를 만들어내며, 주택 공급 계획은 이 구조를 사전에 진단하여 역산되어야 한다. 본 연구는 연령유입→가구형성→규격수요로 이어지는 예측 사슬을 정식화하고(IV.8), 이를 평택 외 타 도시(안성·화성)에 이식하여 검증함으로써(MAPE 0.8–11.0%) 이러한 진단이 고덕 사례에 국한되지 않는 일반화 가능한 도구임을 확인했다.

### 2. 비판적 검토

성급한 결론을 방지하기 위해 6단계 논증을 거쳤다. ① **주장**: 고덕 신축 규격은 젊은 근로·소가구 수요를 충분히 반영하지 못한다. ② **삼각검증**: 인구(25–39 압도·월세 76%) + 공급(3방 79%) + gap(소형 −18%p 부족)의 독립 3소스가 동일 방향을 가리킨다. ③ **가정 의심**: "국민평형 3방=젊은 가족 적합"이라는 통념을 명시적으로 의심한다(젊은 근로 상당수는 자녀 前 1–2인). ④ **반론(steelman)**: 어린 자녀 가족엔 3방이 적합할 수 있고, 소형 수요가 전월세로 충족된다면 '부족'이 아니라 자가 진입장벽일 수 있다. ⑤ **관측 vs 추론**: 가구원수는 평택 실측이나 규격수요 매핑은 가정이며, gap의 크기는 매핑에 민감하나 방향성(소형 부족)은 감도분석에서 강건하다. ⑥ **잠정 결론**: 공급은 전국 표준 국민평형에 수렴하고 고덕의 젊은 근로 특수성은 전월세로 우회 실현되는 정합성 결손의 정황이다(인과·최적량 단정은 유보).

### 3. 정책·설계 제언

- **방수(최우선)**: 미스매치(부족)는 면적(−17%p)보다 방수(1–2방, −45%p)에서 훨씬 크다. 1–2방 소형방 규격의 대폭 확대가 필요하다(현 고덕 공급 3방 78% 편중).
- **면적·점유**: 젊은 근로·1–2인·유동(월세 76%, stock 보정 후에도 ~50%) 대응 소형(<60㎡)·임대형(특히 월세, 장기임대·오피스텔형 포함) 확대.
- **적용 범위**: 반도체 전용이 아니라 "젊은 근로·소가구 집중 신도시" 일반(혁신도시 등)에 준용 가능하며, 설계모델은 타 도시 연령유입에 이식 가능하다(MAPE 6–11%). 향후 용인 등 예정된 후속 반도체 클러스터의 공급 계획 단계에서 사전 진단 도구로 활용될 수 있다.

### 4. 연구의 의의 및 한계점

본 연구는 인구·공급·거래를 결합해 규격 정합성을 진단하고, 연령유입에서 규격·방수·점유를 산출하는 예측모델을 제시했다는 데 의의가 있다. 한계는 다음과 같다. (1) 처치 입지 내생성 — 고덕=계획 신도시라 '공장 근접'과 '신도시 패키지'의 완전 분리는 어려우나, 거리 hedonic으로 부분 분리하였다(잔여 교란: 캠퍼스 거리와 도심 접근성 중첩). (2) 규격/방수 매핑 M은 가정이며 민감도로 방향의 강건성만 확인하였다. (3) 점유는 거래건수의 회전율 stock 보정 가정(매매 보유기간 6–10년)을 사용하였다. (4) 단일 사례(고덕)로, 다도시 일반화는 이식 검증으로 일부 보강하였으나 도시별 국지차가 남는다. (5) 규격 '추세'는 전국 현상이므로 본 연구는 정합성 진단이지 반도체 인과 주장이 아니다. 향후 매핑 계수의 실증화, 2중심 모델(캠퍼스 vs 도심), 다중 반도체·혁신도시로의 이식 확대, 점유 stock의 직접 관측이 필요하다.

---

## 인용문헌 (References)

1. 대한국토·도시계획학회, 2024. "1인가구 증가와 소형주택 수요에 관한 논의", 「국토계획」, 59(6). *[서지 확인·보완 필요]*
   Korea Planning Association, 2024. "Discussions on the Rise of Single-person Households and Small-housing Demand", *Journal of Korea Planning Association*, 59(6). *[to be verified]*
2. 국토교통부, 2015–2025. 「아파트 실거래가 공개시스템」, 세종.
   Ministry of Land, Infrastructure and Transport, 2015–2025. *Real Transaction Price Disclosure System for Apartments*, Sejong.
3. 통계청, 2011–2025. 「KOSIS 국가통계포털」(DT_1B04005N·DT_1JC1516·DT_1JC1511), 대전.
   Statistics Korea, 2011–2025. *KOSIS* (DT_1B04005N, DT_1JC1516, DT_1JC1511), Daejeon.
4. Dallas Fed, 2023. "Semiconductor Boomtowns and Regional Housing Effects." *[서지 확인 필요]*
5. Greenstone, M., Hornbeck, R., and Moretti, E., 2010. "Identifying Agglomeration Spillovers: Evidence from Winners and Losers of Large Plant Openings", *Journal of Political Economy*, 118(3): 536–598.
6. *Journal of Housing and the Built Environment*, 2025. "Data-driven Assessment of Housing Demand–Supply Gaps." *[서지 확인 필요]*
7. Mankiw, N.G., and Weil, D.N., 1989. "The Baby Boom, the Baby Bust, and the Housing Market", *Regional Science and Urban Economics*, 19(2): 235–258.
8. Muggeo, V.M.R., 2003. "Estimating Regression Models with Unknown Break-points", *Statistics in Medicine*, 22(19): 3055–3071.
9. Zeng, Y., Land, K.C., Gu, D., and Wang, Z., 2014. *Household and Living Arrangement Projections: The Extended Cohort-Component Method*, Springer.

<sub>⚠️ 본 인용문헌은 초안이며, 게재/제출 전 각 서지사항(권·호·페이지·DOI)의 원문 대조 확인이 필요하다. *[확인 필요]* 표시 항목은 특히 원 출처 확정을 요한다.</sub>

---

<div align="right"><sub>접수일 [ ] · 심사일 [ ] · 수정일 [ ] · 게재확정일 [ ] &nbsp;—&nbsp; <b>미투고 학생 원고(초안)</b></sub></div>
