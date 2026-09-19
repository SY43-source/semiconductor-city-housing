# Evidence Map — where every number comes from

> **Purpose**: trace every statistic, table, and figure in the manuscript back to the script that computed it and the dataset it came from. Korean terms are kept below because they match the column names in the data; the structure is `number → figure/table → script → dataset`.
>
> **Current manuscript**: [`paper/Semiconductor-City-Housing-KO.pdf`](paper/Semiconductor-City-Housing-KO.pdf) · [English](paper/Semiconductor-City-Housing-EN.pdf) · [Appendix](paper/Appendix-KO.pdf)
> **Reading order**: this map → manuscript → appendix (validation and sensitivity) → [`data/DATA_SOURCES.md`](data/DATA_SOURCES.md) → [`analysis/*.py`](analysis/) → [`archive/versions/_CHANGELOG.md`](archive/versions/_CHANGELOG.md)
>
> **Numbering**: figures 1–7 and tables 1–11 in the manuscript; figures A1–A5 and tables A1–A5 in the appendix. Earlier drafts used a different numbering scheme — see the changelog before citing an archived version.
> **Maintenance rule**: when the manuscript changes, update this file in the same commit. It fell three versions out of date once before.

---

## 🎯 In one line

**Godeok New Town was built to a single template — three bedrooms at 84–85㎡, one size band holding 55.3% of all units — for a population the template does not fit. The households squeezed out are not poor by policy's definition: they earn around or above the urban-worker average, and that is precisely why public rental eligibility excludes them. Affordable housing exists there almost only in the public stock (5–8% of income); the private 76% has no enterable price point.**

**AI 반도체 양산국이 미·한·대만 3개국뿐이어서 클러스터 신도시는 반복 조성되는데, 고덕은 3방·국민평형 단일 템플릿에 편중돼(84~85㎡ 한 규격군 55.3%) 그 결과 주거 취약계층이 소외된다 — 감당 가능한 주거는 공공임대(소득의 5–8%)에만 있고 민간 재고 84%에는 진입 가격대가 없다.**

**본 연구의 성격**: 규격 진단 보고서가 아니라 **주거 취약계층 소외에 관한 분석 보고서**(§I.1). 초록은 **연구 배경 → 연구 목적 → 연구 방법 → 주요 결과 → 결론 및 시사점** 5부 구조. 소외 대상 = 청년 단독가구 · 신혼/예비 신혼부부 · 저소득 근로가구 · 공공임대 입주자격 우선순위에서 밀리는 가구.

5대 핵심 결론:
1. **집중**: 평택 성장이 고덕 한 곳으로 수렴(인구 ×5.7·개발 1→73%·가격배율 0.96→2.49) — §IV.1
2. **인구**: 유입 무게중심 = 25–39세 젊은 근로 **+ 어린 자녀** → '젊은 1인 근로자 도시'가 아닌 **젊은 가족 도시**(0–14세 19.4%·평균 가구원수 3.0–3.5명) — §IV.2
3. **미스매치**: 축마다 형태가 다름 — **방수축=양극(barbell)**(3방 +24%p 과잉, 1–2방 −20%p·4방+ −4%p 부족, **모수·매핑 변주에 강건**), **면적축=대형 부족 단방향**(−9.5~−15.5%p, **m̄ 가정에 조건부**). 소형(면적)은 1차 산정의 부족(−17.8)에서 **과잉(+0.6~+9.5)으로 부호 반전** — §IV.4
4. **소외**: 월세 편중 73.4%는 선호가 아니라 가격 장벽 결과. PIR 16.1배·자가 부담률 65%. **공공 24만원(5–8%) vs 민간 89만원(18–30%)** → 감당 가능 주거는 공공임대 단일 경로 — §IV.8
5. **로드맵**: 2026–31 연 3,392세대(소형 845·국평 1,749·대형 799), 2032 포화. 10년 누적 20,692세대 = 계획잔여의 58% → 총량 과잉 위험. **보정 후 궤적에서도 부호 유지** — §IV.7

---

## 📊 Key figures and where they come from

> **Sign convention** 부호 규약: gap = **supply − demand** (공급 − 수요). **Negative = shortage** 음수=부족 (more supply needed) · **Positive = surplus** 양수=과잉.
>
> **Robustness** 강건성: ✅ = direction holds across every household-size anchor and mapping variation tested. ⚠️ = sign is conditional on the mean-household-size band → [`LIMITATIONS.md`](LIMITATIONS.md) §2.

### A. Concentration — 집중 (§IV.1)
| Quantity 수치 | Value 값 | Exhibit 그림/표 | Script | Data |
|---|---|---|---|---|
| Godeok population multiple — 인구 배수 | 13,651→77,337 (**×5.7**) | Fig. 1 | `20_godeok_concentration.py` | KOSIS DT_1B04005N |
| Godeok share of city population — 인구 비중 | 3.1→12.7% | Fig. 1 | `20_..` | DT_1B04005N |
| Net increase since 2022 — 순증 | 고덕 +34,878 / 평택나머지 −3,005 | Fig. 1 | `20_..` | DT_1B04005N |
| Share of new development — 개발 점유 | 1→**73%** | (in text) | `13_development_concentration.py` | 단지 sqlite |
| Price ratio vs outskirts — 가격배율 | 0.96→**2.49** (연식통제 1.22→1.67) | (in text) | `12_local_premium_gradient.py`·`16_hedonic.py` | 실거래 매매 |
| Unit-size trend is nationwide — 추세의 전국성 | 거시 보정 시 평택 고유 추세 소멸 | Fig. A2 | `08_macro_adjusted.py` | 실거래 다도시 |

### B. Population composition — 인구 구성 (§IV.2)
| Quantity 수치 | Value 값 | Exhibit 그림/표 | Script | Data |
|---|---|---|---|---|
| Inflow aged 25–39 — 유입 | **+24,986** (청소년의 2.4배·영유아의 4.8배) | Fig. 2 | `22_godeok_age.py` | DT_1B04005N |
| Inflow aged 5–19 / 0–4 — 유입 | +10,451 / +5,255 | Fig. 2 | `22_..` | DT_1B04005N |
| Share aged 0–14 / 65+ — 비중 | **19.4%**(전국 10.3%) / **6.7%**(평택 14.6%) | inline table | `22_..` | DT_1B04005N |
| **Mean household size, Godeok** — 평균 가구원수 | **2.99~3.46명**(평택 2.18) — 상한=77,337÷22,368, 하한=2018 기저 제외 | inline table | `32_godeok_recalibration.py` | 인구÷아파트세대 실측 |

### C. Supply — 공급 (§IV.3)
| Quantity 수치 | Value 값 | Exhibit 그림/표 | Script | Data |
|---|---|---|---|---|
| Total supply — 공급 총량 | 29단지·**22,368세대** (민간 분양 재고 기준) | Table 2 | `28_supply_structure.py` | sqlite complexes+pyeong_types |
| Room-count composition — 방수 구성 | 3방 **78.4%** · 4방+ 14.6% · 1–2방 **7.0%** | Table 2 | `28_..` | sqlite `room_count` |
| Floor-area composition — 면적 구성 | 국평 **59.0%** · 소형 30.1% · 대형 11.0% | Table 2 | `28_..` | sqlite `exclusive_area_m2` |

### D. Demand–supply gap — gap 지수 (§IV.4) · Gap = supply − demand
| Unit class 규격 | Demand 수요 | Supply 공급 | Gap (band 밴드) | Exhibit | Script |
|---|---|---|---|---|---|
| Small <60㎡ 소형 | 16.8~21.5% | 30.1% | **+0.6 ~ +9.5%p (surplus 과잉)** ⚠️ conditional 조건부 | Table 3·Fig. 3 | `32_godeok_recalibration.py` |
| Standard 60–85㎡ 국평 | 49.9~52.8% | 59.0% | +6.2 ~ +9.1%p (surplus 과잉) | Table 3·Fig. 3 | `32_..` |
| **Large ≥85㎡ 대형** | 20.5~26.5% | 11.0% | **−9.5 ~ −15.5%p (shortage 부족)** ⚠️ conditional 조건부 | Table 3·Fig. 3 | `32_..` |
| **1–2 rooms 1–2방** | 22.7~32.4% | 7.0% | **−15.7 ~ −25.4%p (shortage 부족)** ✅ robust 강건 | Table 3·Fig. 3 | `32_..` |
| 3 rooms 3방 | 51.8~55.8% | 78.4% | +22.6 ~ +26.6%p (surplus 과잉) ✅ robust 강건 | Table 3·Fig. 3 | `32_..` |
| 4+ rooms 4방+ | — | 14.6% | −1.2 ~ −6.9%p (slight shortage 경미 부족) | Table 3 | `32_..` |
| Single-person share — 1인가구 비율 | — | — | 37.5%(1차) → **12.4~20.4%**(보정) | Table 3 | `32_..` |
| **Concentration in one size band** — 단일규격 집중 | — | — | **84~85㎡ 12,366세대 = 55.3%** (상위 3규격군 84.8%, 총 14규격군) | Fig. 3-④ | `34_barbell_distribution.py` |
| *(참고) 1차 산정 소형* | *47.9%* | *30.1%* | *−17.8%p* — **기각**(m̄=2.18, 관측과 1.2명 괴리) | Table 3 첫 열 | `21_gap_index_prototype.py` |
| *(참고) 매핑 민감도* | | | *1차 산정 기준 −5.8 ~ −33.2%p* | Fig. A1 | `21b_gap_sensitivity.py` |
| Observed household sizes, Pyeongtaek — 실측 가구원수 | 1인37.5·2인27.5·3인18.6·4인13.4·5인+3.0% | | | (in text) | `kosis_hhsize_pyeongtaek.py` (DT_1JC1516) |

### E. Market split — 시장 분화 (§IV.5)
| Quantity 수치 | Value 값 | Exhibit 그림/표 | Script |
|---|---|---|---|
| Small units: sales vs leases — 매매 vs 전월세 | 35~44% < **56~59%** ⚠️거래건수 기준(면적축 미보정) | Fig. 4 | `10_rent_analysis.py` |
| Monthly-rent share of leases — 월세 비중 | **73.4%** (안성 53.5% · 평택 52.4% 대조검증 → 약 20%p 상회) | inline table·Fig. 4 | `10_..` |

### F. Distance hedonic — 거리 hedonic (§IV.6)
| Quantity 수치 | Value 값 | Exhibit 그림/표 | Script |
|---|---|---|---|
| Distance coefficient — 거리 계수 | **−3.7%/km** (p<0.0001) | Table 4·Fig. 5 | `23_distance_hedonic.py` |
| New-town dummy (net premium) — 신도시 더미 | +3.2% | Table 4·Fig. 5 | `23_..` |
| Sample excluding Godeok — 고덕 제외 | −3.7%/km (n=37,281) → 근접효과는 신도시의 산물 아님 | Table 4 | `23_..` |
| Matched sample — 매칭 표본 | 41,196건 (매칭률 58%) | (in text) | `23_..` |
| Sensitivity to campus reference point — 지점 민감도 | −2.5 ~ −3.7%/km (정문·P2·중앙) | (in text) | `23_..` |

### G. Design model and annual roadmap — 설계 예측모델 (§IV.7)
| Quantity 수치 | Value 값 | Exhibit 그림/표 | Script | Data |
|---|---|---|---|---|
| 가구주 25–39세 1인율 | **51.4%** (1–2인 72.9% / 전연령 1인 37.1%) | (in text) | `kosis_headship_pyeongtaek.py` | KOSIS **DT_1JC1511** |
| 헤드십 ρ | 20–24세 0.17 → 40대+ 0.57 | (in text) | `kosis_headship_pyeongtaek.py` | DT_1JC1511 ÷ DT_1B04005N |
| 신규 유입 1인율 | 39.3% → **보정 16.1%** | Table A4 | `24_design_model.py`·`32_..` | 사슬 |
| 분포 평균 가구원수 | 2.22명(관측과 1.2명 괴리) → **보정 3.23명** | Table A4 | `32_..` | 사슬 |
| 점유(flow→stock) | 매매 10→31 / 전세 26→19 / 월세 64→**50%** | Fig. A4 | `26_tenure_stock_adjust.py` | `godeok_tenure_by_size.csv` |
| **점유(+고덕 보정)** | 매매 **35** / 전세 **22** / 월세 **43%** | Table A4 | `36_forecast_design_recalibrated.py` | 사슬 |
| 검증 MAPE(이식) | 평택 0.8 / 안성 6.0 / 화성 11.0% | Table A2 | `25_model_validation.py` | DT_1JC1516·DT_1B04005N |
| 모델 민감도 | 매핑 변주에도 1–2방 부족 부호 유지 | Fig. A3 | `24b_model_sensitivity.py` | 사슬 |
| 예측모형 선택 | 로지스틱 MAPE 33.8% **기각**(전 origin 과대예측) → **선형 5.6% 채택** (감쇠선형 13.3%) | Table A3·Fig. A5 | `31_backcast_validation.py` | DT_1B04005N |
| 개발 진척률 | 2025년 계획인구의 53.6% (별도 출처 사업 진척률 약 52%와 일치) | (in text) | `31_..` | 개발계획 공시 |
| 연간 유입(2026–31) | 10,958명/년 → **신규 3,392세대/년** | Table 5·Fig. 6 | `33_annual_design_roadmap.py` | 사슬 |
| 연간 평형 배분 | 소형 845 · 국평 1,749 · 대형 799세대 (1–2방 927·3방 1,832·4방+ 633·월세 1,446) | Table 5·Fig. 6 | `33_..` | 사슬 |
| 포화 시점 | **2032년** (계획 인구 144,173명 도달) ⚠️이후 값은 하한 | Table 5 | `33_..` | 선형모형 |
| 10년 누적 | **20,692세대** (밴드 19,317~22,353) = 계획잔여 35,932의 **58%** → 총량 과잉 위험 | Table 5 | `33_..` | 사슬 |
| **계획기간 궤적(보정 후)** | 1인율 **16.0→12.9%** · 1–2방 27.2→24.2% · 월세 42.9→42.0% · 평균 가구원수 3.23→3.36명 | **표 6** | `36_forecast_design_recalibrated.py` | 사슬 |
| **2035 부호 강건성** | 3방 +21.3~+24.6 / 1–2방 −22.0~−13.0 / 대형 −17.0~−11.1 / 소형 +3.7~+12.0 %p (3앵커 전체) | Table 6 | `36_..` | 사슬 |
| *(참고) 보정 전 궤적* | *1인율 39→34% · 1–2방 52→48% · 월세 50→49%* — 수준이 §IV.4와 불정합 | Table 6 참고열 | `27_forecast_design.py` | 사슬 |
| 계획 규모(공시) | K_pop 144,173명 / K_hh 58,300세대 (기공급 22,368) | (in text) | — | 개발계획 공시 |
| 시뮬레이터 프로파일 민감도 | 실측형 3.23(1인율 16.2%) / 젊은근로형 3.01(21.2%) / 가족형 3.57(10.7%) | Table A5 | `design_simulator.html` | 사슬 |

### H. Housing access and exclusion — 주거 접근성 (§IV.8) ⭐ where the study lands
| Quantity 수치 | Value 값 | Exhibit 그림/표 | Script | Data |
|---|---|---|---|---|
| Median sale price, standard unit — 국평 중위가 | **5.80억원** (n=905) | Table 7·Fig. 7 | `35_affordability.py` | 실거래 매매 2024–25 |
| Median sale price, small / large — 중위가 | 3.40억(n=557) / 7.10억(n=95) | Table 7 | `35_..` | 실거래 |
| **Price-to-income ratio, standard unit** — 국평 PIR | **16.1 / 11.6 / 9.7배** (연소득 3,600/5,000/6,000만) vs 국제기준 5.1배 | Table 7·Fig. 7-① | `35_..` | 실거래 + 소득 시나리오 |
| Mortgage burden as share of income — 자가 부담률 | 국평 **65 / 47 / 39%** (LTV 70%·금리 4%·30년) | Table 8·Fig. 7-② | `35_..` | 실거래 |
| **Small-unit monthly rent — public** 공공 | **24만원 = 소득의 8 / 6 / 5%** (명시단지 27만 n=3,460 · 번호단지 21만 n=1,110) | Table 8 | `35_..` | 전월세 실거래, 전환율 5.5% |
| **Small-unit monthly rent — private** 민간 | **89만원 = 소득의 30 / 21 / 18%** (n=1,047) | Table 8 | `35_..` | 전월세 실거래 |
| Public share of small-unit rent transactions — 공공 비중 | **81%** (4,570 / 5,617건) → 혼합 중위 29만원은 민간 시장가 아님 | Table 8 | `35_..` | 전월세 실거래 |
| Private monthly rent, standard / large — 민간 월세 | 125만원(42/30/25%) / 126만원<sup>†</sup>(혼합, 분리 미실시) | Table 8 | `35_..` | 전월세 실거래 |
| **Public rental stock** — 공공임대 재고 | **7,720 units = 25.7% of stock** — 공고로 전량 확정(하한 단서 해제) | Table 10 Table 10 | (공고 수집) | LH·GH 입주자모집공고 + 건축물대장 |
| **Stock recomputation** — 재고 재산정 | 민간분양 21,708 (72.1%) · 민간임대 660 (2.2%) · 공공임대 **7,720 (25.7%)** = **30,088세대**, 임대 계 **8,380 (27.9%)** | Table 11 Table 11 | 저자 집계 | 단지메타 + 공고 병합 |
| Public rental share in transaction records — 실거래상 비중 | 고덕 전월세 10,190건 중 **49.3%** (명시 5단지 34.0%) | (in text) | `35_..` | 전월세 실거래 |
| Rent terms from official notices — 공고 임대조건 | LH2 16형 보증금 2,280만·월 10만 / 경기행복주택 청년 보증금 1,905만·월 9만 | (in text) | (공고) | LH·GH 공고 |
| Planned vs realized tenure — 계획 vs 실현 | 계획 분양 **97.0%** vs 실현 월세 **73.4%** (역전) | Fig. 7-③ | `35_..` | 개발계획 + 실거래 |

---

## 🖼 Figures and tables (index → [`figures/README.md`](figures/README.md))

### Manuscript figures 1–7 — ⭐ = central. All seven are cited in the text
| 그림 | 내용 | § | 스크립트 | PNG |
|---|---|---|---|---|
| 1 | 고덕 집중 (고덕 vs 평택-고덕제외) | IV.1 | `20_godeok_concentration.py` | `analysis/20_*.png` |
| **2** | ⭐ 고덕 연령 구성 (25–39 + 어린자녀) — 논문 최대 반전의 근거 | IV.2 | `22_godeok_age.py` | `analysis/22_*.png` |
| **3** | ⭐ **통합 4패널** — ①가구원수 분포 보정 ②면적축 gap ③방수축 gap(barbell) ④공급 규격군 파레토(84~85㎡ 55.3%) | IV.4 | **`37_gap_consolidated.py`** | `analysis/37_*.png` |
| 4 | 전월세 (소형 실재처·월세화) | IV.5 | `10_rent_analysis.py` | `analysis/10_*.png` |
| 5 | ⭐ 캠퍼스 연속거리 hedonic | IV.6 | `23_distance_hedonic.py` | `analysis/23_*.png` |
| 6 | 연도별 설계 로드맵 (평형별 세대수·시나리오 밴드) | IV.7 | `33_annual_design_roadmap.py` | `analysis/33_*.png` |
| **7** | ⭐ **주거 접근성** (①PIR ②감당선 대비 ③계획/실현 점유 역전) | IV.8 | `35_affordability.py` | `analysis/35_*.png` |

> **통합 원칙(v10)**: 세부를 여러 장으로 쪼개지 않고 한 장에 함축한다. §IV.4 는 v10 초기판까지 그림 3장·8패널(28_+32_+34_)로 같은 이야기를 반복했는데, 이를 **그림 3 한 장(4패널)** 으로 합쳐 "왜 보정하나 → 두 축이 어떻게 다르나 → 공급은 왜 극단인가"의 한 줄기로 만들었다. 표와 수치가 겹치는 그림(`28_supply_structure` = 표 2)은 제거했다.

### Appendix figures A1–A5 → [`paper/Appendix-KO.pdf`](paper/Appendix-KO.pdf)
| 부그림 | 내용 | 부록 § | 스크립트 |
|---|---|---|---|
| A1 | gap 민감도 (매핑 변주) ⚠️1차 산정 기준 | A-2 | `21b_gap_sensitivity.py` |
| A2 | 규격 전국성 (거시 사이클 보정) | A-3 | `08_macro_adjusted.py` |
| A3 | 설계 사슬 모델 민감도 | A-2 | `24b_model_sensitivity.py` |
| A4 | 점유 회전율 보정 (flow vs stock) | A-4 | `26_tenure_stock_adjust.py` |
| A5 | 인구예측 backcast 검증 (로지스틱 기각) | A-5 | `31_backcast_validation.py` |

### Tables — manuscript 1–11, appendix A1–A5
| 표 | 내용 | § |  | 부표 | 내용 | 부록 § |
|---|---|---|---|---|---|---|
| 1 | 분석 데이터 개요 (D1·D2·D3b·D3c·D7·D8) | III.2 |  | A1 | Entity 기호 정의 (21행) | A-1 |
| 2 | 공급 규격 구성 (29단지·22,368세대) | IV.3 |  | A2 | 타 도시 MAPE | A-5 |
| 3 | **재추정 gap 밴드** (1차 산정 열 포함) | IV.4 |  | A3 | backcast 모형 비교 | A-5 |
| 4 | 캠퍼스 거리 hedonic | IV.6 |  | A4 | 설계모델 보정 전/후 | A-4 |
| 5 | 연도별 필요 신규 세대수 | IV.7 |  | A5 | 시뮬레이터 프로파일 민감도 | A-6 |
| 6 | **계획기간 궤적(보정 후)** | IV.7 |  | | | |
| 7 | 자가 진입 장벽 (PIR) | IV.8 |  | | | |
| 8 | **월 주거비 부담률 (공공/민간 분리)** | IV.8 |  | | | |
| 9 | 공공임대 단지 Public rental complexes (7,720세대) | IV.8 |  | | | |
| 10 | 재고 점유유형 재산정 (자료원 병합) | IV.8 |  | | | |

> **인라인 대조표(번호 없음)** 2종: 고덕/평택/전국 인구지표(§IV.2) · 고덕/평택/안성 전월세(§IV.5).

### Figures produced but not included — PNGs and scripts kept in `analysis/` (appendix A-7)
`13_development_concentration`(그림1 중복) · `12_local_premium_gradient`(그림7 하위집합) · **`21_gap_index_prototype`(기각된 모수의 시각화)** · `16_hedonic`(중복) · `24_design_model`(부표 A4 중복) · `25_model_validation`(부표 A2 중복) · `27_forecast_design`(그림8 통합, 보정 전 모수)

---

## 🗄 Data sources (detail → [`data/DATA_SOURCES.md`](data/DATA_SOURCES.md))

| ID | 무엇 | 출처·코드 | 파일 |
|---|---|---|---|
| D1 | 아파트 매매 실거래 | 국토부 RTMSDataSvcAptTrade | `realprice/realprice_apt_trade.csv` (+전월세 `_rent_pt.csv`) |
| D2 | 5세별 인구 | KOSIS **DT_1B04005N** | `population/city_population_5yr_*.csv`, `population/godeok_age_year_matrix.csv` |
| D3 | Single-person share — 1인가구 비율 | KOSIS DT_1YL21161 | `population/city_1person_household_*.csv` |
| D3b | 가구원수별 가구(실측) | KOSIS **DT_1JC1516** | `employment/pyeongtaek_hhsize_2015_2024.csv` |
| D3c | 가구주연령×가구원수(실측) | KOSIS **DT_1JC1511** | `employment/pyeongtaek_head_age_hhsize_2024.csv` (+`_headship_2024.csv`) |
| D3d | 고덕 점유(매매/전세/월세) | 국토부 실거래 파생 | `employment/godeok_tenure_by_size.csv` |
| D7 | 아파트 단지/평형/방수/좌표 메타 | NAVER 부동산 | master sqlite (`complexes`+`pyeong_types`) |
| **D8** | **공공임대 입주자모집공고·준공** | **LH 청약플러스·마이홈포털** | (공고 확인분 → 표 9) |
| — | 파생 산출물 | 저자 계산 | `employment/godeok_demand_recalibrated.csv` · `godeok_design_roadmap.csv` · `godeok_affordability.csv` · **`godeok_forecast_recalibrated.csv`** |

### ⚠️ Data pitfalls — 데이터 함정
- **KOSIS 지역코드 2종**: `DT_1B04005N`(5세별 인구)는 **표준 행정코드**(평택=41220), 그러나 **`DT_1JC1516`·`DT_1JC1511`(가구)는 레거시 순번코드**(평택=**31070**, 경기=31, 서울=11). 표준코드 넣으면 err21.
- `DT_1JC1516` 세대구성 objL2 = **'00'**(계). `DT_1JC1511` 가구주연령 objL2 = **020~090**(5세 스텝, 020=15-19…090=85+). **085(80–84) 이후 값은 0** → 85+ 헤드십·조건분포는 80–84로 대체(`36_..` 참조).
- **분당 200건 제한**(2026-07-15~): 초과 시 `err=40`. 모든 호출은 `src/kosis_client.py`의 `kosis_get()` 경유(자동 스로틀+백오프). **`36_..`는 로컬 캐시만 사용해 API 미호출.**
- **⚠️ 단지 메타(NAVER)는 분양·매매 중심 → 공공임대 미수록.** 전국 검색에서도 '평택고덕경기행복주택' 0건. 임대·공공 관련 집계는 **반드시 실거래 + 공고를 병합**할 것. v8이 이 결손을 "LH 0건"이라는 사실로 오독했다.
- **⚠️ 명목 분류 금지.** 임대 판별(단지명 → `lease_households` 실측 필드)과 지역 판별(단지명 '고덕' 매칭 → **법정동 기준**)을 모두 교체했다. 후자는 오포착 26건·누락 126건이 있었고 소형 중위가가 3.54→3.40억으로 바뀌었다. 재현 시 각 분류 기준이 명목인지 실측인지 먼저 확인.
- **⚠️ Three populations coexist** 세 모집단 병존: unit composition 규격 22,368 / private tenure 민간 점유 23,957 / recomputed stock 재고 재산정 **30,088**세대. 비율 인용 시 모집단 확인 필수 → [`LIMITATIONS.md`](LIMITATIONS.md) §6.

---

## 🐍 Script index — `analysis/`, run with `python3.11`

**본문 그림 생성(7종)**:
`20_godeok_concentration`→그림 1 · `22_godeok_age`→그림 2 · **`37_gap_consolidated`→그림 3(통합)** · `10_rent_analysis`→그림 4 · `23_distance_hedonic`→그림 5 · `33_annual_design_roadmap`→그림 6 · `35_affordability`→그림 7

**부록 그림 생성(5종)**: `21b_gap_sensitivity`→A1 · `08_macro_adjusted`→A2 · `24b_model_sensitivity`→A3 · `26_tenure_stock_adjust`→A4 · `31_backcast_validation`→A5

**표 전용(그림 없음)**: `21_gap_index_prototype`(표 3 1차 산정 열) · `24_design_model`·`32_godeok_recalibration`(부표 A4·표 3) · `25_model_validation`(부표 A2) · **`36_forecast_design_recalibrated`(표 6 — 계획기간 궤적 보정 후, §IV.7-(5))**

**원고에서 제외(PNG·스크립트 보존, 부록 A-7)**: `28_supply_structure`·`34_barbell_distribution`(→그림 3 통합) · `13`·`12`·`21`·`16`·`24`·`25`·`27_forecast_design`

**수집기(`src/`)**: `kosis_hhsize_pyeongtaek`(D3b) · `kosis_headship_pyeongtaek`(D3c) · `kosis_client`(공용 API 클라이언트) · `build_pdf`(MD→PDF)

**배경·탐색용(원고 미인용)**: `01`(히트맵)·`02`(DiD)·`03`(미스매치)·`04`(장기인구)·`05·06`(광주)·`07`(회귀·분절)·`09`(공급vs수요)·`11`(가격발산)·`12`·`13`·`14·15`(용량반응)·`16`·`17`(대조도시)·`18·19`(인구예측)·`27`(보정 전 궤적)·`29`(연간 코호트)

---

## 📐 Definitions and conventions

- **Gap = 공급 − 수요** → **음수 = 부족**(공급확대 필요) / **양수 = 과잉**
- **면적 밴드**: 소형 <60㎡ / 국민평형(국평) 60–85㎡ / 대형 ≥85㎡ · **방수 밴드**: 1–2방 / 3방 / 4방+
- **점유**: 매매 / 전세 / 월세. flow(거래건수) → **stock**(보유기간 보정: 매매 8년·전세 2·월세 2)
- **설계모델 사슬**: `H_h = Σ_a n_a·ρ_a·P(h|가구주연령 a)` → 규격/방수/점유. **ρ·P(h|a)·T=실측, 매핑 M=가정**(민감도 검증)
- **고덕 특화 보정**: `p_h ∝ q_h·exp(λh)`, `Σ p_h·h = m̄` (최소 KL 발산 = 최대엔트로피 해). `m̄` 밴드 = 보수 2.99 / 기준 3.23 / 상한 3.46명
- **계획기간 궤적의 λ 처리**: λ는 **관측 시점(A)에서 1회 결정 → B에 그대로 적용**. ρ·P(h|a)의 편의는 연령 프로파일이 이동해도 남는 **구조적** 편의이므로 보정계수를 고정하고 B의 m̄는 움직이게 둔다(B에 m̄ 재강제 = 코호트 성숙 효과 소거)
- **PIR** = 중위 매매가 ÷ 연소득. 국제 부담기준(Demographia) 5.1배 이상 = "심각하게 감당 불가"
- **월세 실질부담** = 월세 + 보증금 × 전월세전환율(5.5%) ÷ 12. **감당선 = 월소득의 30%**(cost-burdened 기준)
- **MAPE**: 예측-실측 평균절대오차율(작을수록 정확)
- **강건성 표기 규약**: ✅ robust 강건 = 모수(m̄ 밴드)·매핑 변주 전체에서 부호 유지(방수 축) / ⚠️ conditional 조건부 = m̄ 가정에 따라 부호 변동 가능(면적 축)

---

## ▶️ Reproducing the results

```bash
export KOSIS_API_KEY=...                                    # .secrets.env 참조 (하드코딩 금지)
python3.11 analysis/32_godeok_recalibration.py               # gap 재추정 → 그림 4 재생성
python3.11 analysis/36_forecast_design_recalibrated.py       # 계획기간 궤적(표 6) — API 미호출, 로컬 캐시만
python3.11 src/build_pdf.py                                  # 정본 PDF 4종(v10 한/영 + 부록 한/영) 재생성
python3.11 src/build_pdf.py v10                               # 한글 본문만
```
- **반드시 `python3.11`** (기본 `python3`는 matplotlib/numpy/markdown 없음).
- KOSIS 호출은 `kosis_get()` 경유(분당 200건 자동 준수). PNG는 `analysis/*.png`에 저장.
- 데이터 원본은 Studio 로컬(`/Users/Shared/seoyeon_research/` + master sqlite) — GitHub 미포함.
- PDF 빌드는 `weasyprint` CLI 필요. 한글판 폰트 = AppleMyungjo + Apple SD Gothic Neo.

---

## 🔗 Related documents
- **Manuscript**: [`paper/Semiconductor-City-Housing-KO.pdf`](paper/Semiconductor-City-Housing-KO.pdf) / [EN](paper/Semiconductor-City-Housing-EN.pdf) · **Appendix**: [KO](paper/Appendix-KO.pdf) / [EN](paper/Appendix-EN.pdf) / [`APPENDIX_v10_EN.md`](paper/Appendix-EN.pdf)
- [`archive/versions/_CHANGELOG.md`](archive/versions/_CHANGELOG.md) — revision history (v1–v12) and do-not-cite warnings on withdrawn claims · [`data/DATA_SOURCES.md`](data/DATA_SOURCES.md) — dataset detail
- [`design_simulator.html`](docs/index.html) 부속 계산 도구 · [`PAPER_WRITING_GUIDE.md`](archive/notes/PAPER_WRITING_GUIDE.md) 작성기법 · [`DATA_READINESS_AND_LITERATURE.md`](archive/notes/DATA_READINESS_AND_LITERATURE.md) 선행문헌
