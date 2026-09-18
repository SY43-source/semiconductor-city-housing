<!-- v9 EN (2026-07-31): English edition of MANUSCRIPT_v9.md. Adds the housing-access (affordability) axis: new §IV.10, reframed conclusion and recommendations. Identical figures, tables and numbers otherwise. -->
<!-- Journal-style formatting after Journal of Korea Planning Association. Journal ISSN/DOI/branding intentionally omitted (unpublished student manuscript). -->

> **v8 → v9 revision note (2026-07-31)**
> §IV.10 of v8 took only the 29 complexes listed in the NAVER Real Estate metadata as its population and stated that **"direct LH public-rental supply in Godeok is zero."** That mistook a gap in the data source for a fact. MOLIT lease transactions plainly contain **Godeok Gyeonggi Happy Housing, LH Complexes 2, 12, 15, 17 and 35**, totalling **4,640 units** in confirmed notices alone. v9 therefore (i) **merges the sources** (complex metadata plus public-rental notices) and re-estimates the stock (28,597+ units; **public rental 16.2%+, rental total 24.1%+**); (ii) **splits Table 12 by sector**, correcting v8's claim that a small unit rents affordably at 0.29M KRW — that figure was a **blend in which public rental accounts for 81%**, while private small units cost **0.89M (30/21/18% of income)**; and (iii) recasts the argument from "exclusion through absence of alternatives" to **"no affordable small units in the private market, with affordable housing concentrated in public rental."** **The ownership barrier (Table 11; PIR 16.1) and the gap index (§IV.4) rest on sale and supply data and are unchanged.** v8 is preserved as a rollback point with a citation warning ([`MANUSCRIPT_v8_EN.md`](MANUSCRIPT_v8_EN.md)).

*Journal-style manuscript (formatting after *Journal of Korea Planning Association*) — unpublished student research. Korean edition: [`MANUSCRIPT_v9.md`](MANUSCRIPT_v9.md) · Evidence map: [`PAPER_GUIDE.md`](PAPER_GUIDE.md) · Interactive tool: [`design_simulator.html`](design_simulator.html) · Revision history: [`_CHANGELOG.md`](_CHANGELOG.md)*

<br>

# Does the Housing Unit Composition of a New Town near a Semiconductor Cluster Reflect Its Population Structure?
### : Who Gets Left Out of the New Town? The Godeok Case and a Demand–Supply Gap and Housing-Access Based Proposal for Unit Diversification<sup>*</sup>

<br>

**SEOYEON JEON**<sup>**</sup>

---

> **Abstract**
>
> Semiconductor clusters give rise to planned new towns nearby that concentrate specific age cohorts. Using Godeok New Town, adjacent to Samsung's Pyeongtaek Campus, as a case, this study diagnoses whether the supply of housing unit types reflects the area's demographic structure and proposes unit diversification grounded in a demand–supply gap framework. Most of Pyeongtaek's net population growth concentrated in Godeok alone (population ×5.7; city share 3.1%→12.7%; virtually all net growth since 2022). The inflow centers on working-age adults 25–39 (2.4× the teenage inflow) **together with young children**: Godeok's share of ages 0–14 is **19.4%** (Pyeongtaek 12.6%, nation 10.3%) while ages 65+ are only **6.7%** (Pyeongtaek 14.6%), and its average household size is **3.0–3.5 persons** versus 2.18 for the city. Godeok is therefore a **young-family town**, not a town of single workers—so applying the city-wide single-person share (37.5%), which largely originates from elderly one-person households in the old urban core, overstates small-unit demand. Re-estimating demand for Godeok via a maximum-entropy exponential tilt under the observed household-size constraint reverses the sign of the small-unit gap: small units (<60㎡) move from a 17.8pp shortage to a **+0.6 to +9.5pp surplus**, **large units (≥85㎡) turn out to be short by 9.5–15.5pp**, and the **1–2-room shortage persists in direction but shrinks** (−45.5 → −15.7 to −25.4pp). The mismatch takes a different form on each axis: on the **room-count axis it is a barbell**—the three-bedroom template is oversupplied by 24.3pp while both extremes are short (1–2 rooms −20.3pp, 4+ rooms −4.0pp)—whereas on the **floor-area axis it is one-directional**, with only large units short. On the continuous area axis, supply concentrates 55.3% of all units in a single 84–85㎡ band. Monthly-rent concentration is confirmed as genuinely local (Godeok 73.4% vs. control city Anseong 53.5%). Adding a **housing-access (affordability)** axis shows this concentration to be exclusion rather than preference: the median sale price of a standard-size unit is 580 million KRW, a **price-to-income ratio of 16.1** for an entry-level worker (against 5.1 as the international "severely unaffordable" threshold), and mortgage servicing would take **65% of monthly income**, whereas the effective cost of renting a small unit is **10%**; that rental figure must be split by sector: LH and GH public rental amounts to **at least 4,640 units (16.2%+ of stock)**, and **81% of small-unit rent transactions are public**. Separated, effective rent is **0.24M KRW (5–9% of income) for public units versus 0.89M (18–30%) for private ones** — affordable housing is supplied almost exclusively through public rental, while the private stock (84%) offers no enterable price point. This raises the need for **ex-ante allocation of cluster-specific housing instruments** comparable to the U.S. Housing Choice Voucher, Public Housing and LIHTC. We formalize an **age-inflow-to-design chain** (inflow → household formation → unit size, room count, tenure) with an explicit symbol system, validate the population forecast by rolling-origin backcast (linear model MAPE 5.6%, versus 33.8% for a logistic specification), and derive an **annual design roadmap** through 2035. This is a data-grounded consistency diagnosis and reference guidance, not a causal or optimal-allocation claim.
>
> **Keywords**: semiconductor-adjacent new town, housing unit-size fit, demand–supply gap, unit diversification, housing affordability and access, tenure insecurity, single-person and working households, real transaction data

<sub>* Conducted as a student summer research project, drawing on open data from the Ministry of Land, Infrastructure and Transport (MOLIT), Statistics Korea (KOSIS), and NAVER Real Estate.</sub>
<sub>** Valor International Scholars (first and corresponding author).</sub>

---

## I. Introduction

### 1. Background

The semiconductor industry builds planned new towns in its vicinity and concentrates young working populations there (Greenstone et al., 2010). With the operation of Samsung Electronics' Pyeongtaek Campus (P1 2017, P2 2020, P3 2022), Godeok International New Town was developed, and population, development, and housing prices were rapidly reorganized. Conventional wisdom holds that "family in-migration implies demand for standard three-bedroom units," but if the center of gravity of in-migration is young workers in small households, supply built to that convention may diverge from demand. Whether the **unit composition** (floor area, room count, tenure form) supplied in such new towns is consistent with the age and household structure of the actual in-migrating population has not been verified.

What this study emphasizes is that a mismatch in unit composition is not merely market inefficiency. **When a supply plan presupposes one household form as the standard, households outside that standard become invisible at the planning stage.** A standard unit type also presupposes the income level able to afford it, so uniformity of unit types translates into uniformity of the households that can enter. Households that do not fit the standard are recorded as "no demand," or are pushed into the most precarious layer of the market (short-term monthly rent) and disappear from the planner's field of view. A diagnosis of unit-composition consistency therefore cannot stop at "what is mismatched and by how much"; it must also ask **who is excluded as a result**. This study quantifies that question with transaction-based housing-access (affordability) measures (§IV.10).

### 2. Objectives

This study asks: **(1) Does the housing unit composition supplied in Godeok New Town reflect the area's population? (2) If not, which unit types should be diversified? (3) Who is excluded from housing as a result of that mismatch, and through what mechanism does the exclusion operate?** Its contributions are: (i) diagnosing unit-composition consistency using multi-layered data on population, supply, and transactions (sales and leases); (ii) presenting a household-composition-based demand–supply gap framework as decision support; (iii) presenting an **age-inflow-based housing design prediction model formalized through an entity–symbol system**, with measured household formation, region-specific recalibration, and validation both across cities and along the time axis; (iv) providing an **annual design roadmap and an accompanying calculation tool** as a route to practical application; (v) **formalizing the exclusion mechanism (design → price → tenure diversion) with housing-access measures** (price-to-income ratio, mortgage burden rate, rental share), thereby extending a unit-composition diagnosis into a housing-access diagnosis; and (vi) making assumptions and limitations transparent through critical review, including a self-correction of the conclusions of an earlier draft.

---

## II. Literature Review

### 1. Regional effects of large industrial establishments

Large industrial establishments generate broad regional effects on employment, population, and housing markets (Greenstone et al., 2010; Dallas Fed, 2023). Advanced-industry clusters such as semiconductors concentrate young working populations especially rapidly, making the demand structure of nearby housing different from that of ordinary cities.

### 2. Population structure and housing demand

Age structure governs both the quantity and the composition of housing demand (Mankiw and Weil, 1989). Households form out of population (headship), and the distribution of household size determines the required unit composition. The cohort-component method is the standard approach for projecting households from age-specific population (Zeng et al., 2014). The design prediction model in this study extends that approach to unit size, room count, and tenure.

### 3. Diagnosing demand–supply consistency (gaps)

Approaches that diagnose how well housing supply matches demand as a gap have been proposed (*Journal of Housing and the Built Environment*, 2025). Discussions of the rise of single-person households and small-housing demand in Korea have also accumulated (Korea Planning Association, 2024). This study applies such gap diagnosis to unit-composition design in a new town near a semiconductor cluster.

### 4. Distinctiveness of this study

Whereas prior work treats unit-composition *trends* (such as convergence on the standard 60–85㎡ unit) as a nationwide phenomenon, this study (i) diagnoses the consistency between the local population structure of one specific new town (Godeok) and its supplied unit composition, (ii) uses **measured** household size and household size by householder age, and (iii) presents a prediction model that derives unit size, room count, and tenure from age-specific in-migration and validates it by transfer to other cities.

---

## III. Methodology

### 1. Scope

The spatial scope is Godeok New Town near Samsung's Pyeongtaek Campus (Godeok-myeon and Godeok-dong, Pyeongtaek), with the city of Pyeongtaek as the comparison baseline and Anseong, Hwaseong, and Gwangju as control cities. The temporal scope is 2015–2025 for transactions and 2011–2025 for population.

### 2. Data

<br>**Table 1. Overview of analysis data**

| ID | Data | Source · code | Period | Files |
|---|---|---|---|---|
| D1 | Apartment sales and lease transactions | MOLIT actual transaction prices | 2015–2025 | `realprice/` |
| D2 | Population by 5-year age band | KOSIS DT_1B04005N | 2011–2025 | `population/` |
| D3b | Households by household size (measured) | KOSIS DT_1JC1516 | 2015–2024 | `employment/` |
| D3c | Household size by householder age (measured) | KOSIS DT_1JC1511 | 2024 | `employment/` |
| D7 | Complex, unit-type, room-count, coordinate metadata | NAVER Real Estate | ~2026 | master sqlite |

<sub>Source: Open data from MOLIT, Statistics Korea, and NAVER Real Estate. Details in `DATA_SOURCES.md`.</sub>

### 3. Methods

**1) Demand–supply gap framework.** Demand shares by unit type are computed as the household-composition distribution (measured) multiplied by a unit-size demand mapping (assumed), and contrasted with supply shares. We define **Gap = supply − demand**, so that **a negative value denotes a shortage** (supply expansion required) and a positive value a surplus. The mapping assumption is tested for robustness by sensitivity analysis.

**2) Distance-to-campus hedonic regression.** Transactions are matched to complex coordinates, and log unit price is regressed on continuous distance from the campus (km), a new-town dummy, floor area, building age, and year fixed effects (HC0 robust). This partially separates "proximity to the plant" from "the new-town package."

**3) Age-inflow-based housing design prediction model.** From net inflow `n_a` by age band `a`, the following chain yields unit size, room count, tenure, and the single-person share (subscripts are written with `_`; `H_h` denotes households of size h, and `Σ_a` a sum over ages a).
```
Household formation   H_h   = Σ_a  n_a · ρ_a · P(h | householder age a)     (ρ = headship, P = measured conditional distribution, DT_1JC1511)
Size · rooms          D^A_s = Σ_h  H_h · M^A_(h,s) ,   D^R_r = Σ_h  H_h · M^R_(h,r)
Tenure                D^K_k = Σ_s  D^A_s · T_(s,k)                          (T = Godeok transactions, turnover-adjusted to stock)
Single-person share   = H_1 / Σ_h H_h
```
Here `ρ_a`, `P(h|a)`, and `T_(s,k)` are measured; only the unit-size mapping `M` is assumed from the literature and general practice, and it is tested by sensitivity analysis.

**4) Region-specific recalibration for Godeok (new in v7).** Because `ρ` and `P(h|a)` above are city-wide parameters, applying them directly to Godeok introduces bias (§IV.2, §IV.4). To correct this, we take the observed average household size `m̄` for Godeok as a constraint and apply an **exponential (maximum-entropy) tilt** that minimizes the Kullback–Leibler divergence from the prior distribution `q_h`:
```
p_h ∝ q_h · exp(λh) ,   subject to  Σ_h p_h·h = m̄        (λ found by one-dimensional root finding)
```
`m̄` is treated as an observed band (conservative 2.99 / baseline 3.23 / upper 3.46 persons), so results are reported as a band.

### 4. Entity and symbol system

All entities and symbols used in this study are defined once in Table 2 and shared by every equation, table, and accompanying tool thereafter.

<br>**Table 2. Definition of entities and symbols**

| Symbol | Entity | Definition · unit | Nature |
|---|---|---|---|
| `a` | Age band | 5-year bands (20–24 … 85+) or age group `g` | index |
| `h` | Household size | 1, 2, 3, 4, 5+ persons | index |
| `s` | Floor-area band | small <60㎡ / standard 60–85㎡ / large ≥85㎡ | index |
| `r` | Room-count band | 1–2 rooms / 3 rooms / 4+ rooms | index |
| `k` | Tenure | purchase / *jeonse* (deposit lease) / monthly rent | index |
| `t` | Year | 2013 … 2035 | index |
| `P_(a,t)` | Population stock | Godeok population by age (persons) | **measured** (DT_1B04005N) |
| `n_(a,t)` | Net inflow | annual net increase by age (persons) | measured · forecast |
| `ρ_a` | Headship | householder rate by age (dimensionless) | **measured** (DT_1JC1511 ÷ population) |
| `P(h│a)` | Conditional household-size distribution | distribution of household size for householder age `a` | **measured** (DT_1JC1511) |
| `m̄` | Average household size | observed anchor for Godeok (persons/household) | **measured band** 2.99–3.46 |
| `q_h`, `p_h` | Household-size distribution | before / after tilt | derived |
| `H_t` | New households | `Σ_a n_(a,t) / m̄` (units) | derived |
| `M^A_(h,s)`, `M^R_(h,r)` | Size and room mapping | household size → area · room preference | **assumed** (sensitivity-tested) |
| `T_(s,k)` | Tenure propensity | purchase/jeonse/monthly-rent shares by area | **measured** (turnover-adjusted) |
| `D^A_(s,t)`, `D^R_(r,t)`, `D^K_(k,t)` | Demand | annual demand by size, rooms, tenure (units) | derived |
| `S_s` | Supply stock | existing supply composition (units, %) | **measured** (complex metadata) |
| `G_(s,t)` | Gap | `S_s − D^A_(s,t)` (negative = shortage) | derived |
| `x*_(s,t)` | **Design prescription** | `max(0, D^A_(s,t) − S_s)`, required new units | derived |
| `K_pop`, `K_hh` | Planned capacity | 144,173 persons / 58,300 units | **published** (development plan) |

<sub>Source: KOSIS, MOLIT transaction data, NAVER complex metadata, and the Godeok International New Town development plan.</sub>

---

## IV. Results

### 1. Concentration of growth in Godeok New Town

Godeok accounts for roughly 38% of Pyeongtaek's net population increase (2013→2025), and **essentially all net growth since 2022 occurred in Godeok** (Godeok +34,878 versus −3,005 for the rest of the city). Godeok's population rose from 13,651 to 77,337 (×5.7) and its share of the city from 3.1% to 12.7%. Its share of new apartment development jumped from 1% to 73%, and the price ratio relative to the periphery widened from 0.96 to 2.49 (1.22 → 1.67 when building age is controlled). Population, development, and prices all converge on this single location.

**Figure 1. Concentration in Godeok vs. the rest of Pyeongtaek**
![Fig1](../analysis/20_godeok_concentration.png)
<sub>Source: Authors' calculation based on KOSIS DT_1B04005N.</sub>

**Figure 2. Spatial concentration of development (Godeok share 1→73%)**
![Fig2](../analysis/13_development_concentration.png)
<sub>Source: Authors' calculation based on complex metadata (NAVER Real Estate).</sub>

**Figure 3. Local price gradient by distance**
![Fig3](../analysis/12_local_premium_gradient.png)
<sub>Source: Authors' calculation based on MOLIT transaction data.</sub>

### 2. Age structure of the in-migrating population

The center of gravity of in-migration (2018→2025) is working-age adults 25–39 (+24,986), 2.4 times the inflow of teenagers aged 5–19 (+10,451) and 4.8 times that of infants aged 0–4 (+5,255). Infants, teenagers, and adults in their forties also increased substantially, producing a pattern of "young working age plus young children."

**Godeok is not a town of young single workers but a young-family town (newly established in v7).** Because this distinction governs the demand estimation that follows, we cross-checked it against the age composition of the resident stock.

| Indicator (2025) | **Godeok** | Pyeongtaek | Nation |
|---|---|---|---|
| Share aged 0–14 | **19.4%** | 12.6% | 10.3% |
| Share aged 25–44 | 45.6% | 31.9% | 26.6% |
| Share aged 65+ | **6.7%** | 14.6% | 21.2% |
| Child-to-parent ratio (0–14 ÷ 25–44) | **0.43** | 0.40 | 0.39 |
| Average household size | **3.0–3.5 persons** | 2.18 | — |

Godeok's share of children is 1.9 times the national figure, and its elderly share is less than half that of the city. Dividing Godeok's population (77,337) by its apartment units (22,368) gives 3.46 persons as an upper bound; excluding the pre-development baseline population (10,382 in 2018, largely non-apartment housing in the former Godeok-myeon) gives 2.99 as a conservative lower bound. Both exceed the city average (2.18) substantially. Consequently, **the city-wide single-person household share (37.5%) largely arises from elderly one-person households in the old urban core, and substituting it as Godeok demand systematically overstates small-unit demand** (corrected in §IV.4).

**Figure 4. Age structure of the Godeok inflow — working age (25–39) plus young children**
![Fig4](../analysis/22_godeok_age.png)
<sub>Source: Authors' calculation based on KOSIS DT_1B04005N (Godeok-myeon and Godeok-dong).</sub>

### 3. Composition of new housing supply

New apartment supply in Godeok was aggregated from complex metadata (NAVER Real Estate). The sample covers **29 complexes and 22,368 units** in Godeok, each classified by room count and exclusive floor area (Table 3, Figure 5).

By **room count**, **three-bedroom units dominate at 17,527 units (78.4%)**, followed by 4+ rooms at 3,266 (14.6%) and only 1,575 units (**7.0%**) with 1–2 rooms. Units with three or more rooms thus account for **93.0%** of the total, effectively excluding small room counts. By **exclusive floor area**, the standard 60–85㎡ band accounts for 13,188 units (**59.0%**), small units (<60㎡) for 6,725 (30.1%), and large units (≥85㎡) for 2,455 (11.0%).

In short, new supply in Godeok **converges strongly on the nationwide standard template of three-bedroom, standard-size units.** Whether this supply structure is consistent with the household structure of the in-migrating population (§IV.2, §IV.4) is the core of the analysis that follows.

<br>**Table 3. Composition of new-apartment unit types in Godeok (29 complexes, 22,368 units)**

| Dimension | Category | Units | Share |
|---|---|---|---|
| Rooms | 1–2 rooms | 1,575 | 7.0% |
| Rooms | **3 rooms** | **17,527** | **78.4%** |
| Rooms | 4+ rooms | 3,266 | 14.6% |
| Area | Small <60㎡ | 6,725 | 30.1% |
| Area | **Standard 60–85㎡** | **13,188** | **59.0%** |
| Area | Large ≥85㎡ | 2,455 | 11.0% |

<sub>Source: Authors' aggregation from master sqlite (complexes + pyeong_types); `analysis/28_supply_structure.py`.</sub>

**Figure 5. Unit-type composition of new supply in Godeok**
![Fig5](../analysis/28_supply_structure.png)
<sub>Source: Authors' calculation based on complex metadata (NAVER Real Estate).</sub>

### 4. Demand–supply gap index for unit types

**(1) First-pass estimate using city-wide parameters (reference only).** Substituting Pyeongtaek's measured 2024 household-size distribution (1-person 37.5%, 2-person 27.5%, 3-person 18.6%, 4-person 13.4%, 5+ 3.0%; KOSIS DT_1JC1516) yields Table 4. Varying the unit-size mapping across three scenarios left the small-unit gap negative (a shortage) throughout, at −5.8 to −33.2pp (Figure 7).

<br>**Table 4. Unit-size gap using city-wide parameters (reference only; Gap = supply − demand, negative = shortage)**

| Unit type | Demand (%) | Supply (%) | Gap (pp) |
|---|---|---|---|
| Small <60㎡ | 47.9 | 30.1 | −17.8 (shortage) |
| Standard 60–85㎡ | 41.6 | 59.0 | +17.4 (surplus) |
| Large ≥85㎡ | 10.5 | 11.0 | +0.5 (balanced) |

<sub>Source: Authors' calculation (`analysis/21_gap_index_prototype.py`). ⚠️ For the reasons given in §IV.2 this table cannot be applied to Godeok directly; it serves as a reference against which the re-estimate in (3) is compared.</sub>

**(2) Internal consistency check — the first-pass estimate does not hold.** The household-size distribution underlying Table 4 has a mean of **2.18 persons**, and the distribution produced by the age-inflow chain (§IV.8) has a mean of **2.22**. Godeok's observed average household size, however, is **2.99–3.46** (§IV.2), a discrepancy of about 1.2 persons. The household composition implied by the first-pass estimate therefore cannot accommodate Godeok's actual population, and small-unit demand is structurally overstated.

**(3) Region-specific re-estimation.** Taking the observed average household size `m̄` as a constraint, demand was recalibrated using the maximum-entropy exponential tilt of §III.3-4) (`p_h ∝ q_h·exp(λh)`), with `m̄` treated as a band (conservative 2.99, baseline 3.23, upper 3.46). Results appear in Table 5.

<br>**Table 5. Recalibrated gap band for Godeok (Gap = supply − demand, negative = shortage)**

| Unit type | First pass (m̄=2.18) | **Conservative (2.99)** | **Baseline (3.23)** | **Upper (3.46)** | Verdict |
|---|---|---|---|---|---|
| Single-person share | 37.5% | 20.4% | 16.1% | 12.4% | — |
| Small <60㎡ | −17.8 | **+0.6** | **+5.2** | **+9.5** | **surplus** (sign reversal) |
| Standard 60–85㎡ | +17.4 | +9.1 | +7.4 | +6.2 | surplus |
| Large ≥85㎡ | +0.5 | **−9.5** | **−12.5** | **−15.5** | **shortage** (new finding) |
| 1–2 rooms | −45.5 | **−25.4** | **−20.4** | **−15.7** | **shortage** (direction retained, magnitude reduced) |
| 3 rooms | +38.0 | +26.6 | +24.3 | +22.6 | surplus |
| 4+ rooms | — | −6.9 | −4.1 | −1.2 | slight shortage |

<sub>Source: Authors' calculation (`analysis/32_godeok_recalibration.py`). The mapping `M` is held identical to Table 4 so that only the net effect of correcting the distribution is isolated.</sub>

**(4) Interpretation — the mismatch takes a different form on each axis.** Examining the re-estimated results in distributional form (Figure 9), the two axes differ in structure.

- **Room-count axis: a barbell.** Demand is 27.3% for 1–2 rooms, 54.1% for 3 rooms, and 18.6% for 4+ rooms, against supply of 7.0%, 78.4%, and 14.6%. The **middle (3 rooms) is oversupplied by 24.3pp while both extremes are short** (1–2 rooms −20.3pp; 4+ rooms −4.0pp). Two distinct segments—young one- and two-person households before children, and families with children—are each underserved, and a single three-bedroom template matches neither precisely.
- **Floor-area axis: a one-directional shortage of large units.** By contrast, the demand distribution on the area axis is not bimodal but a **single peak shifted toward families** (mode near 80㎡), and the shortage appears only for large units (≥85㎡), at −9.5 to −15.5pp. Small units are in surplus. The term **"barbell" should therefore be reserved for the room-count axis.**
- **The extremity of supply (measured).** Aggregating Godeok supply into floor-area groups yields **14 groups in total**, of which the **84–85㎡ group alone accounts for 12,366 units (55.3%)**, and the **top three groups account for 84.8%** of all units (Figure 9-①). The deficit in unit-type diversity is far more evident in this concentration than in band shares (59.0% for the standard band).

This corrects the single-track prescription of the earlier draft ("expand small units") into **"relax the single three-bedroom, standard-size template and complement each axis differently."**

**Figure 6. Unit-size demand–supply gap index**
![Fig6](../analysis/21_gap_index_prototype.png)
<sub>Source: Authors' calculation.</sub>

**Figure 7. Sensitivity of the gap to mapping assumptions**
![Fig7](../analysis/21b_gap_sensitivity.png)
<sub>Source: Authors' calculation.</sub>

**Figure 8. Recalibration of demand for Godeok — household-size distribution and corrected gaps**
![Fig8](../analysis/32_godeok_recalibration.png)
<sub>Source: Authors' calculation.</sub>

**Figure 9. Mismatch in distributional form — single-specification concentration in supply, large-unit shortage on the area axis, barbell shortage on the room axis**
![Fig9](../analysis/34_barbell_distribution.png)
<sub>Source: Authors' calculation (`analysis/34_barbell_distribution.py`). Panel ① is a Pareto chart of measured units aggregated into floor-area groups (bars = share, line = cumulative). In panel ②, the demand curve is a mixture of normal distributions of preferred floor area by household size; each μ and σ was calibrated to reproduce the band probabilities of the mapping `M^A` (error ≤0.02). It is an interpretive device for continuous display, not a new observation.</sub>

### 5. Market segmentation — small-unit demand realized through leases

In Godeok the small-unit share is higher among lease transactions (56–59%) than among sales (35–44%), and monthly rent accounts for 73–76% of leases. Demand for small units and for mobile residence is therefore realized not through new-build ownership but through leases, and especially monthly rent.

**Control-city validation (new in v7).** To determine whether this monthly-rent concentration is specific to Godeok or reflects a nationwide shift toward monthly rent, we compared control cities.

| Area | Jeonse | Monthly rent | Monthly-rent share |
|---|---|---|---|
| **Godeok** | 6,758 | 18,643 | **73.4%** |
| Pyeongtaek (whole city) | 74,363 | 81,967 | 52.4% |
| Anseong (control, no semiconductor cluster) | 23,092 | 26,575 | 53.5% |

Godeok's monthly-rent share exceeds both the control city (Anseong 53.5%) and the city as a whole (52.4%) by roughly **20 percentage points**. The concentration is thus **a local characteristic of Godeok** rather than a nationwide trend, reflecting the mobile residential behavior of a young working population. It is the empirical result that survives most robustly after the re-estimation of §IV.4.

⚠️ One caveat: area shares (56–59% small among leases) are measured on transaction counts, so fast-turnover small and monthly-rent units are oversampled. The tenure axis was turnover-adjusted to stock (§IV.8), but adjustment of the area axis is left to future work.

**Figure 10. Lease market: where small-unit demand is realized**
![Fig10](../analysis/10_rent_analysis.png)
<sub>Source: Authors' calculation based on MOLIT transaction data.</sub>

### 6. The nationwide character of changes in unit composition (background)

Convergence on standard-size units and the decline of small units appear equally or more strongly in Anseong and in Gwangju (before its semiconductor development), and adjusting for macro cycles (pandemic liquidity, interest rates) removes any trend specific to Pyeongtaek. The unit-composition *trend* is therefore a nationwide structural phenomenon, and the focus of this study is not "did semiconductors change unit composition" but "is unit supply consistent with Godeok's distinctive population." This also supports the position that the study does not attribute all supply mismatch to semiconductor development.

**Figure 11. Nationwide nature of the unit-size trend — macro-cycle adjustment**
![Fig11](../analysis/08_macro_adjusted.png)
<sub>Source: Authors' calculation.</sub>

### 7. The independent effect of spatial proximity — distance-to-campus hedonic

To partially separate whether concentration in Godeok stems from **proximity to the campus** or merely from the **new-town label**, a hedonic regression was applied to Pyeongtaek transactions matched to complex coordinates (41,196 records; match rate 58%) (Table 6).

<br>**Table 6. Hedonic regression on distance to campus**

| Variable | Coefficient (effect) | Significance |
|---|---|---|
| Distance to campus (km) | **−3.7%/km** | p<0.0001 |
| New-town dummy (Godeok, net premium) | +3.2% | p<0.0001 |
| Subsample excluding Godeok (n=37,281) | −3.7%/km | p<0.0001 |

<sub>Source: Authors' calculation (`analysis/23_distance_hedonic.py`). Controls: ln(area), building age, year fixed effects; HC0 robust.</sub>

Most of the price premium comes from continuous distance to the campus (−3.7%/km) rather than from the discrete new-town label (+3.2%). The same −3.7%/km persists in a subsample containing no new town at all, so proximity is an independent effect rather than a product of new-town development. Shifting the campus reference point among the main gate, the P2 block, and the centroid leaves the estimate at −2.5 to −3.7%/km. This suggests that the unit of supply planning should be commuting accessibility from the employment anchor rather than administrative new-town boundaries.

**Figure 12. Continuous distance-to-campus hedonic**
![Fig12](../analysis/23_distance_hedonic.png)
<sub>Source: Authors' calculation.</sub>

**Figure 13. Hedonic premium controlling for building age (background)**
![Fig13](../analysis/16_hedonic.png)
<sub>Source: Authors' calculation.</sub>

### 8. Age-inflow-based housing design prediction model

The gap diagnosis is generalized into a prediction chain running from age-specific in-migration through household formation to unit size, room count, and tenure (for the model equations see §III.3-3)). Householders aged 25–39 comprise 51.4% one-person and 72.9% one- or two-person households (against 37.1% one-person across all ages), so the younger the householder, the more overwhelmingly small the household (DT_1JC1511). Substituting this measured conditional distribution and headship rates (0.17 at ages 20–24 rising to 0.57 from the forties onward) into the chain and applying it to Godeok in-migration (2018→2025) yields Table 7.

<br>**Table 7. Design-model results for Godeok (Gap = supply − demand, negative = shortage)**

| Indicator | Before correction (city-wide parameters) | **After correction (Godeok-specific, baseline m̄=3.23)** |
|---|---|---|
| Single-person share among new households | 39.3% | **16.1%** |
| Mean household size implied by the distribution | 2.22 (1.2 persons from observation) | **3.23** (consistent with observation) |
| Small-unit area gap | −17.4pp shortage | **+5.2pp surplus** |
| Large-unit area gap | +0.2pp | **−12.5pp shortage** |
| **1–2-room gap** | −44.8pp | **−20.4pp shortage** (direction retained) |
| Tenure (flow → stock adjusted) | purchase 10→31 / jeonse 26→19 / monthly rent 64→50% | (unchanged) |

<sub>Source: Authors' calculation (`analysis/24_design_model.py`, `26_tenure_stock_adjust.py`, `32_godeok_recalibration.py`).</sub>

Before correction, the chain used city-wide parameters (`ρ_a`, `P(h|a)`) and therefore overstated small households (§IV.4-(2)). After Godeok-specific correction, the **1–2-room shortage retains its direction**, remaining negative at −15.7 to −25.4pp across mapping variations. The area axis, by contrast, reverses sign, showing a small-unit surplus and a large-unit shortage. Among the conclusions produced by the chain, the room-count axis is thus robust to parameter choice while the area axis is sensitive to it.

**Validation (transferability).** Predicting household size in other cities with parameters calibrated on Pyeongtaek (Table 8) gives a self-consistency MAPE of 0.8% for Pyeongtaek, 6.0% for Anseong, and 11.0% for Hwaseong. The chain captures broad regional structure while local differences between cities remain.

<br>**Table 8. Model validation — cross-city prediction error (MAPE)**

| City | MAPE (%) | Interpretation |
|---|---|---|
| Pyeongtaek (self-consistency) | 0.8 | chain mechanics accurate |
| Anseong (similar control) | 6.0 | good transfer |
| Hwaseong (family-heavy new town) | 11.0 | small households overpredicted (local difference) |

<sub>Source: Authors' calculation (`analysis/25_model_validation.py`).</sub>

**Stability over the planning horizon.** Under scenarios of continued inflow (A) versus cohort maturation (B: children growing up, ageing), by 2035 the single-person share moves only from 39% to 34%, 1–2-room demand from 52% to 48%, and monthly rent to about 49%, so the unit-diversification conclusion holds over the planning horizon (2030/2035) (Figure 18).

**Figure 14. Age-inflow-based housing design model**
![Fig14](../analysis/24_design_model.png)
<sub>Source: Authors' calculation.</sub>

**Figure 15. Model sensitivity**
![Fig15](../analysis/24b_model_sensitivity.png)
<sub>Source: Authors' calculation.</sub>

**Figure 16. Model validation across cities**
![Fig16](../analysis/25_model_validation.png)
<sub>Source: Authors' calculation.</sub>

**Figure 17. Tenure turnover adjustment (flow vs. stock)**
![Fig17](../analysis/26_tenure_stock_adjust.png)
<sub>Source: Authors' calculation.</sub>

**Figure 18. Design-target trajectory (2025→2035)**
![Fig18](../analysis/27_forecast_design.png)
<sub>Source: Authors' calculation.</sub>

### 9. Annual design roadmap (new in v7)

The preceding sections treat static compositions (%). What a developer actually needs is **how many units, of which type, in which year**, so the age-inflow forecast is connected to the chain and converted into annual unit counts.

**(1) Choice of population forecast model — replaced after validation.** A logistic specification with the planned carrying capacity (`K_pop`=144,173) fixed as its saturation point was applied first, but rolling-origin backcasting (fitting only to data up to an origin year, then predicting later years) **overpredicted consistently at every origin**, giving a mean MAPE of 33.8%, and was rejected. The cause is extrapolating the steep gradient of the early growth phase as the saturation rate: Godeok's development has run past its original 2008–2022 planning period, and its 2025 progress stands at 53.6% of planned population, consistent with an independently reported project progress of about 52%. Comparing alternative models the same way, a **linear model based on the most recent three-year gradient performed best, with a MAPE of 5.6%** (Table 9).

<br>**Table 9. Rolling-origin backcast comparison of population forecast models**

| Model | Mean MAPE (%) | Verdict |
|---|---|---|
| Logistic (K fixed) | 33.8 | rejected — consistent overprediction |
| **Linear (recent three-year gradient)** | **5.6** | **adopted** |
| Damped linear (φ=0.8) | 13.3 | second best |

<sub>Source: Authors' calculation (`analysis/31_backcast_validation.py`). Mean of prediction errors for years after each of the origins 2021, 2022, and 2023.</sub>

**(2) Annual prescription.** Using the adopted model (linear, clipped at `K_pop`), annual net inflow was computed and combined with the measured inflow age profile and Godeok-specific household formation (baseline `m̄`=3.23). Results appear in Table 10.

<br>**Table 10. Annual new-household requirements by unit type (baseline m̄=3.23)**

| Year | Net inflow (persons) | New households | Small (18 pyeong) | Standard (25 pyeong) | Large (31+ pyeong) | 1–2 rooms | 3 rooms | 4+ rooms | Monthly-rent volume |
|---|---|---|---|---|---|---|---|---|---|
| 2026 | 10,958 | 3,392 | 845 | 1,749 | 799 | 927 | 1,832 | 633 | 1,446 |
| 2027–2031 | 10,958 each | 3,392 each | 845 each | 1,749 each | 799 each | 927 each | 1,832 each | 633 each | 1,446 each |
| 2032 | 1,091 | 338 | 84 | 174 | 80 | 92 | 182 | 63 | 144 |
| 2033–2035 | 0 (saturated) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **10-year total** | **66,836** | **20,692** | **5,151** | **10,666** | **4,875** | — | — | — | — |

<sub>Source: Authors' calculation (`analysis/33_annual_design_roadmap.py`). Scenario band for cumulative new households: conservative 22,353 / baseline 20,692 / upper 19,317 units.</sub>

**(3) Comparison with planned volume.** Against the **remaining roughly 35,932 units** (planned total of 58,300 less 22,368 already supplied in Godeok), cumulative ten-year demand derived from population is **20,692 units, or 58% of the remainder**. Population trends alone therefore cannot absorb the planned volume: **planned remaining volume exceeds population-based demand.** Separately from the question of unit composition, this signals a **risk of aggregate oversupply**. (⚠️ Planned unit counts cover all housing types whereas measured supply covers apartment complexes, so the populations differ and the comparison should be read as an upper-bound approximation.)

**(4) Practical use.** The chain in this section is implemented in the accompanying tool [`design_simulator.html`](design_simulator.html): adjusting age-specific inflow, inflow scale, decay rate, and average household size immediately recomputes the **floor-area demand distribution curve, household-size composition, annual required unit counts, and design recommendations**. Average household size offers (i) an **automatic mode** that estimates householders from the age composition via headship and corrects for the observed Godeok bias (observed 3.23 ÷ estimated 2.48 = ×1.30) and (ii) a **manual mode** for sensitivity checks. In automatic mode, changing the inflow profile moves the results as follows.

| Inflow profile | Average household size | Single-person share | Small-unit gap | Large-unit gap | 1–2-room gap |
|---|---|---|---|---|---|
| Godeok measured | 3.23 | 16.2% | +5.2 | −12.6 | −20.3 |
| Young-worker-concentrated | 3.01 | 21.2% | +0.6 | −9.9 | **−25.3** |
| Family-centered | 3.57 | 10.7% | +11.4 | **−17.0** | −13.6 |

Developers can substitute their own demand outlook to reproduce or revise the compositions in this study. Setting average household size to 2.18 (the city-wide figure) in manual mode reproduces the "small-unit shortage" conclusion of the earlier draft, making it possible to see directly **how the choice of parameters changes the conclusion**.

**Figure 19. Backcast validation of the population forecast**
![Fig19](../analysis/31_backcast_validation.png)
<sub>Source: Authors' calculation.</sub>

**Figure 20. Annual design roadmap — required units by type and scenario band**
![Fig20](../analysis/33_annual_design_roadmap.png)
<sub>Source: Authors' calculation.</sub>

⚠️ **Limitation.** Because the linear model reaches planned population in 2032, net inflow and hence new demand are computed as zero thereafter. In practice, demand continues to arise after saturation through household fission (children forming their own households, divorce, and so on), so values from 2032 onward should be read as a **lower bound on inflow-based demand**. Annual inflow is also fixed at the recent three-year gradient, so any change in the campus expansion schedule (P4, P5) requires re-estimation.

---

### 10. Who gets left out — the price barrier and tenure diversion (new in v8)

§IV.4 showed that supplied unit types diverge from household structure, and §IV.5 showed that the suppressed demand for small units and small room counts is realized indirectly through leases (73.4% monthly rent). Why that diversion occurs, however, remained open. Two explanations compete. **(a) Preference** — young workers are highly mobile and choose monthly rent voluntarily. **(b) Exclusion** — the entry price of ownership is unaffordable at their income, so they are pushed out. Because the two carry opposite policy implications (the first requires no intervention, the second does), they must be distinguished. This section separates them using transaction-based access measures.

**(1) The barrier to ownership.** Among 2024–25 apartment sale transactions in Godeok, the median price of a standard-size unit (60–85㎡) is **580 million KRW** (n=905). For three entry-level income scenarios (conservative 36 million, middle 50 million, high 60 million KRW per year), the price-to-income ratio (PIR) and monthly mortgage payment (assuming LTV 70%, a 4% rate, and 30-year equal amortization) are given in Table 11.

<br>**Table 11. Barrier to ownership by unit type (Godeok, 2024–25 transactions)**

| Unit type | Median price | Equity required (30%) | Monthly payment | PIR at 36M | PIR at 50M | PIR at 60M | n |
|---|---:|---:|---:|---:|---:|---:|---:|
| Small <60㎡ | 340M KRW | 102M | 1.14M KRW | 9.4 | 6.8 | 5.7 | 557 |
| **Standard 60–85㎡** | **580M KRW** | **174M** | **1.94M KRW** | **16.1** | **11.6** | **9.7** | 905 |
| Large ≥85㎡ | 710M KRW | 213M | 2.37M KRW | 19.7 | 14.2 | 11.8 | 95 |

<sub>Source: MOLIT real transaction prices (2024–2025), authors' calculation. Prices are medians; PIR and monthly payments follow the stated assumptions. **Godeok is identified by legal dong** (Godeok-dong, Godeok-myeon), not by complex name — name matching falsely captures 'Godeok City' and 'Godeok Koaroo' in Icheung-dong and misses Taepyeong and Yeonghwa Blenheim, whose transactions are recorded under 'Godeok-myeon Gung-ri' (§V.4-(x)).</sub>

Under the internationally used affordability classification (Demographia), a PIR of 5.1 or above is "severely unaffordable." Godeok's standard-size unit stands at **16.1 under the conservative scenario, 3.2 times that threshold**, and **even under the high-income scenario (60 million KRW) it is 9.7, about twice the threshold**. Even on optimistic income assumptions, ownership of a standard-size unit is not attainable for an entry-level worker.

**(2) Monthly housing cost — ownership is out of reach, renting is not.** Comparing monthly mortgage payments with the effective cost of monthly rent (rent plus the imputed cost of the deposit at a 5.5% conversion rate), as a share of monthly income, gives Table 12.

<br>**Table 12. Monthly housing cost burden — mortgage versus monthly rent (% of monthly income)**

| Unit type | Monthly payment | Burden at 36M / 50M / 60M | Effective rent | Burden at 36M / 50M / 60M | Rent n |
|---|---:|---:|---:|---:|---:|
| Small <60㎡ | 1.14M KRW | 38 / 27 / 23% | private **0.89M** / public **0.24M** | private **30 / 21 / 18%** · public **8 / 6 / 5%** | 5,617 |
| Standard 60–85㎡ | 1.94M KRW | **65 / 47 / 39%** | private **1.25M KRW** | private **42 / 30 / 25%** | 1,779 |
| Large ≥85㎡ | 2.37M KRW | 79 / 57 / 47% | 1.26M KRW | 42 / 30 / 25% | 313 |

<sub>Source: MOLIT real transaction prices (2024–2025), authors' calculation. The affordability line is conventionally 30% of monthly income. ⚠️ **Rents must be read split by sector** — 81% of small-unit rent transactions are public, so the blended median (0.29M) is not a private-market rent (§IV.10-(4), Table 15).</sub>

Applying the convention that housing costs above 30% of income constitute a cost burden, **ownership of a standard-size unit exceeds the line under all three income scenarios** (39–65%). Moving to tenancy does not resolve it: **private small units reach 30/21/18%** and private standard-size units 42/30/25%. Only **public rental small units (5–9%)** sit clearly inside the line. Gaps of this magnitude — between owning and renting, and between private and public — are not explicable by preference, and support explanation (b), **exclusion**. The observed concentration in monthly rent is not a taste for mobility but the result of seeking the one affordable tenancy route once the ownership path is closed (§IV.10-(4)).

**(3) The tenure structure of supply — public rental exists, and it effectively monopolizes affordable housing.** Exclusion becomes a policy problem when those pushed out have no stable alternative.

⚠️ **Why two sources must be merged.** The complex metadata used for the unit-composition analysis (NAVER Real Estate) is oriented to the sale and resale market and therefore **does not list public rental complexes at all** (a nationwide search returns zero for "Pyeongtaek Godeok Gyeonggi Happy Housing"). Read alone, it puts Godeok's rental stock at 2,249 units (9.4%) with zero LH supply. **MOLIT lease transactions, however, plainly contain public rental complexes**: they account for **49.3%** of Godeok's 10,190 lease records. This section therefore merges the complex metadata with **public-rental notices and completion records**.

<br>**Table 13. Public rental complexes in Godeok (confirmed by notice or completion)**

| Complex | Units | Type | Eligibility |
|---|---:|---|---|
| Godeok LH Complex 2 (Block A-6) | 1,600 | Happy Housing (*haengbok jutaek*) | Students, newlyweds, vulnerable and low-income households / **job-linked, priority for SME employees** |
| Godeok LH Complex 15 | 1,295 | LH public rental | (type unconfirmed) |
| Godeok LH Complex 12 (Block A57-1) | 900 | Happy Housing (26/36/44㎡) | Young single adults, newlyweds |
| Godeok LH Complex 35 | 549 | LH public rental | (type unconfirmed) |
| Godeok LH Complex 17 | 296 | LH public rental | (type unconfirmed) |
| Godeok Gyeonggi Happy Housing (GH) | **unconfirmed** | Happy Housing | **Young single adults** |
| Godeok Social Rental Housing, Phase 1 | **unconfirmed** | Social rental | (type unconfirmed) |
| **Confirmed total** | **4,640** |  | ⚠️ **lower bound** — two complexes excluded |

<sub>Source: LH Cheongyak Plus and MyHome tenant-recruitment notices; completion reports. Two complexes with unconfirmed unit counts are excluded, so the true total is higher.</sub>

<br>**Table 14. Godeok apartment stock by tenure, re-estimated across merged sources**

| Category | Units | Share | Source |
|---|---:|---:|---|
| Private, for sale | 21,708 | 75.9% | complex metadata |
| Private rental | 2,249 | 7.9% | metadata `lease_households` |
| **Public rental** | **4,640** | **16.2%** | notices and completions (**lower bound**) |
| **Rental total** | **6,889** | **24.1%** |  |
| Total | 28,597 | 100.0% | ⚠️ lower bound |

<sub>Source: authors' aggregation. The "9.4% rental, zero LH" reported in v8 mistook a gap in a single source for a fact; this table supersedes it.</sub>

**(4) Affordable housing is supplied only through public rental.** What matters more than the existence of stock is whether its rent is affordable. Splitting small-unit (<60㎡) monthly rents in the 2024– transaction data between public and private is decisive (Table 15).

<br>**Table 15. Effective small-unit (<60㎡) rent burden — public versus private (% of monthly income)**

| Category | Median effective rent | Burden at 36M / 50M / 60M KRW | n |
|---|---:|---:|---:|
| Public rental (named complexes) | **0.27M KRW** | **9 / 7 / 5%** | 3,460 |
| Public rental (numbered, probable) | **0.21M KRW** | **7 / 5 / 4%** | 1,110 |
| **Private** | **0.89M KRW** | **30 / 21 / 18%** | 1,047 |
| (blended median — before splitting) | 0.29M KRW | 10 / 7 / 6% | 5,617 |

<sub>Source: MOLIT lease transactions (2024–2025), deposits converted at 5.5%, authors' calculation. **81% of small-unit rent transactions are public**, so the blended median (0.29M) must not be read as a private-market rent.</sub>

Published rent terms corroborate this: the 16-pyeong type at LH Complex 2 carries a deposit of 22.8M KRW and monthly rent of 0.10M, and the youth type at Gyeonggi Happy Housing a deposit of 19.05M and monthly rent of 0.09M — consistent with the measured effective burden of 0.20–0.29M.

The result is clear. **Private small units at 0.89M KRW reach 30% of income under the conservative scenario**, and private standard-size units at 1.25M exceed it (42/30/25%). **Public rental small units, at 5–9%, sit comfortably inside the line.** Housing an entry-level worker can afford in Godeok is thus concentrated on a **single channel — public rental** — while the private market offers no enterable option either in ownership (PIR 16.1) or in tenancy (0.89–1.25M KRW).

**(5) Why monthly-rent concentration persists nonetheless.** Public rental of 4,640 units or more exists, yet realized tenure is 73.4% monthly rent (§IV.5). The two are not contradictory, because public rental is limited in **both volume and eligibility**. The confirmed 16.2% is small relative to the scale of in-migration, and eligibility is restricted: LH Complex 2 (1,600 units), for instance, is **job-linked with priority for SME employees**, so workers at large establishments and other young households rank lower. The problem is therefore not "no policy instrument" but that **the scale and targeting of the instruments were not designed around the inflow structure the cluster generates** — the actual mechanism behind what v8 misdiagnosed as an absence of public rental.

**(6) International comparison — institutionalized access instruments.** The three U.S. instruments speak to the Godeok structure in different ways.

| Instrument | Mechanism | Point of action | Implication for Godeok |
|---|---|---|---|
| **Housing Choice Voucher (Section 8)** | Demand-side subsidy — the household pays about 30% of income, the voucher covers the balance (HUD) | **Tenure stage** | Brings within the line the burden of households left in **private rent (0.89M KRW)** because they could not enter public rental; applies at once, with no new construction |
| **Public Housing** | Publicly owned and operated | **Supply stage** | **Already present** in Godeok (4,640+ units). The issue is not existence but **scale and targeting** |
| **LIHTC (income-restricted housing)** | Tax credits induce private developers to reserve units for income-restricted households for 30+ years (IRC §42) | **Incentive structure facing private suppliers** | **The largest gap** — of 23,957 privately supplied units, essentially none is affordable (private small-unit rent 0.89M). No instrument attaches access conditions to private supply |

Korea likewise has counterpart instruments on the books — *haengbok* housing, national rental, publicly supported private rental — and they **are in fact operating** in Godeok. The problem is twofold: **(i) their scale is small relative to in-migration, and (ii) no access condition attaches to privately supplied units, which are 84% of the stock.** The second is decisive. Where private supply carries no affordable price point at all, expanding public rental improves access only in proportion to its own share. That is the lesson of LIHTC: change the composition of private supply **through incentives rather than regulation**.

**(7) Formalizing the exclusion mechanism.** Taken together, exclusion operates in three stages.

> **① Design stage** — private supply is standardized into a single three-bedroom, standard-size template (78.4%; 55.3% in one 84–85㎡ group; §IV.3).
> **② Price stage** — the price of that type (580M KRW; PIR 16.1; mortgage burden 65%) exceeds the ownership-entry threshold, and private tenancy likewise reaches or exceeds the line (small 0.89M, standard 1.25M).
> **③ Branching stage** — the only affordable route is public rental (5–9%). Households that enter it settle stably; those excluded by its limited volume (16.2%) and restricted eligibility (SME priority and the like) **remain in short-term private rent**. The realized 73.4% monthly-rent share is the outcome of that branching.

The implication is that unit diversification is a question of **who can settle in this city**, not of aesthetics or market efficiency. And the real structure is more specific than the "complete absence of alternatives" that v8 assumed: alternatives exist, but **only in the public sector, while the private sector supplies no accessible price point whatsoever**. If the gap in §IV.4 is the language of planning, the access measures here are **what that gap becomes once it reaches people**.

<br>**Figure 21. Housing access — why young workers are pushed into monthly rent**
![Fig21](../analysis/35_affordability.png)
<sub>Source: MOLIT real transaction prices (2024–2025) and NAVER Real Estate complex metadata, authors' calculation. (1) PIR against the international affordability threshold; (2) mortgage versus rent against the 30%-of-income line; (3) the reversal between planned tenure (97.0% for sale) and realized tenure (73.4% monthly rent). Figure labels are in Korean in the current edition.</sub>

⚠️ **Assumptions and limitations.** Income is a scenario rather than a measurement (no income data exist for Godeok's resident households); ownership burden assumes LTV 70%, a 4% rate and 30-year equal amortization, and effective rent assumes a 5.5% deposit-conversion rate. The rental share is classified by complex name, so private long-term rental may be omitted. Tables 11–12 should therefore be read not as precise cost estimates but as **the magnitude of the gap between owning and renting**. That gap is nonetheless too large to be reversed by varying the assumptions: even under a relaxed 3% rate and 80% LTV, the mortgage burden for a standard-size unit remains above the 30% line.

---

## V. Conclusion

### 1. Discussion

This study analyzed the effect of Samsung's Pyeongtaek semiconductor campus on the surrounding housing market through the case of Godeok New Town, and tested whether the unit composition supplied there is consistent with the household-formation structure of the in-migrating population.

Growth triggered by semiconductor investment concentrated extremely in a single location within Pyeongtaek (development share 1→73%, price ratio 0.96→2.49; §IV.1), and the population that moved there formed a distinct demographic profile centered on working-age adults 25–39 together with their young children (§IV.2). New supply, however, followed the standard template of three-bedroom, standard-size units (§IV.3), producing a gap against demand grounded in actual household size (§IV.4). Suppressed demand for small units and small room counts was being realized indirectly through leases—especially monthly rent, at 73–76% (§IV.5)—which rules out the alternative explanation that the demand simply did not exist. Access measures further show that this diversion is **the result of a price barrier rather than a preference** (§IV.10).

Decomposing the source of the price premium shows that it arises from physical distance to the semiconductor campus (−3.7%/km) rather than from new-town status itself (the new-town dummy effect is only +3.2%; §IV.7). This contradicts the "new-town label premium" hypothesis common in development discourse and suggests that the unit of supply planning should be commuting accessibility from the employment anchor rather than an administrative new-town boundary.

The consequence of the mismatch did not stop at market statistics. The median standard-size price of 580 million KRW implies a PIR of 16.1 against entry-level income (international burden threshold 5.1) and a mortgage burden of 65% of monthly income, whereas the effective burden of renting a small unit is 10% (§IV.10). **The ownership path is closed and only the rental path is open.** Moving to tenancy does not resolve it either: private rents are 0.89M KRW for small units (30/21/18%) and 1.25M for standard-size (42/30/25%). Only **public rental (5–9%)** falls inside the line, and although it exists at 4,640+ units it is just 16.2% of stock with restricted eligibility (LH Complex 2's 1,600 units give priority to SME employees). The observed 73.4% monthly rent is thus not natural market segmentation but the outcome of an exclusion chain running **design (a single unit type) → price (an entry barrier) → branching (whether a household enters public rental)**. Those who enter settle; those who do not remain in short-term private rent. What this study diagnoses, therefore, is not an inefficiency in unit composition but **a question of housing access: who is able to settle in this city**.

Taken together, employment-anchor development such as a semiconductor campus generates a demand structure that a standardized new-town supply template does not capture. That structure, however, was not the "young small-household" pattern initially assumed but one in which **young families predominate while young one- and two-person households also exist**. The mismatch consequently differs by axis: on the **room-count axis, a single three-bedroom standard misses both extremes (1–2 rooms and 4+ rooms), a barbell structure**, while on the **floor-area axis the shortage is one-directional, in large units**. On the supply side, the continuous area axis shows an extreme single peak, with 55.3% of units in the 84–85㎡ group. This study formalized the chain from age-specific in-migration through household formation to unit demand as an explicit symbol system (§III.4, §IV.8), validated it in both directions—transfer to other cities (MAPE 0.8–11.0%) and backcasting along the time axis (MAPE 5.6%)—and then set out a route to practical application through an annual design roadmap (§IV.9) and an accompanying calculation tool.

### 2. Critical review — the study's own self-correction

To guard against premature conclusions, the argument passed through six stages. (i) **Claim**: new unit composition in Godeok does not adequately reflect the household structure of the in-migrating population. (ii) **Triangulation**: population (25–39 dominant), supply (78.4% three-bedroom), and tenure (73.4% monthly rent, 20pp above the control city) point in the same direction from three independent sources. (iii) **Questioning assumptions**: the conventional view that "three-bedroom standard units suit in-migrating households" was made explicit and doubted. (iv) **Steelmanning, and accepting the counterargument**: the earlier draft (v6) substituted the city-wide single-person share (37.5%) as Godeok demand and concluded that small units were short; the counterargument that "Godeok is a family town whose child share is 1.9 times the national figure, so those parameters are inappropriate" was confirmed against measurement (§IV.2), an internal contradiction of 1.2 persons between distributional mean and observation was found, and **the conclusion was corrected** (§IV.4). (v) **Observation versus inference**: household size, headship, and tenure propensity are measured, whereas the unit-size mapping is assumed, and **the sign of the gap can reverse with the choice of parameters** on the area axis, while the room-count axis (1–2-room shortage) and the monthly-rent concentration proved robust to variations in both parameters and mapping. (vi) **Provisional conclusion**: the robust results are "surplus of the single three-bedroom template and shortage of small room counts and rental-type units," while the direction on the area axis is conditional on the assumed average household size.

A second self-correction of the same type occurred in the v8 access analysis. Rental volume was first classified by complex **name** and reported as 3.0%, but most rental units sit in mixed complexes whose names do not disclose them, and the true figure is **9.4%** (§IV.10-(3)). The direction of the conclusion (absence of direct public supply) held, but its magnitude changed threefold, and the draft's statement that rental was "virtually absent" had to be withdrawn. The same pattern appeared in geographic identification: logic that selected transactions by whether the complex name contained "Godeok" was **replaced with a legal-dong criterion** (26 false positives, 126 omissions; the small-unit median moved from 354M to 340M KRW).

A third and more fundamental correction followed in v9. Using the complex metadata as a single source, v8 concluded that "LH public rental in Godeok is zero" — without establishing that **the source, being oriented to the sale market, does not record public rental at all**. Transaction data showed public rental at 49.3% of lease records, and confirmed notices alone totalled 4,640 units. The derived error was larger still: the 0.29M KRW small-unit rent that v8 offered as evidence of affordability was a **blend in which public rental made up 81%**, so a public rent had effectively been read as a private-market rent. Two lessons follow. **(i) Never use a nominal label as a proxy for a measured field.** **(ii) Never read the absence of something in one source as its absence in the world** — "not in the data" and "does not exist" differ, and market-oriented sources omit the public sector systematically. The first was confirmed at three independent points in v8 verification; the second in v9.

The methodological lesson of this section is the **risk of substituting broad regional averages into a specific local case**. The same bias appeared in the population forecast, where a logistic model extrapolated early rapid growth (§IV.9-(1)); in both cases it surfaced only through ex-post verification (internal consistency checks and backcasting).

### 3. Policy and design recommendations

- **First priority — relax the dominance of the three-bedroom, standard-size template.** Current supply is 78.4% three-bedroom and 59.0% standard-size, and on the continuous area axis **55.3% falls in a single 84–85㎡ group**. Re-estimation puts the three-room gap at +22.6 to +26.6pp and the standard-size gap at +6.2 to +9.1pp, a **surplus under every scenario**. Reducing the share of the single template is the starting point, and it simultaneously eases both the barbell shortage on the room axis and the large-unit shortage on the area axis.
- **Expand small room counts (1–2 rooms) — securing an enterable unit type.** The room-count gap is −15.7 to −25.4pp, a shortage under all parameter and mapping variations. Householders aged 25–39 are 72.9% one- or two-person households, yet only 7.0% of supply serves them. This is not merely an adjustment of the mix but **the creation of the one unit type open to income groups that cannot cross the ownership-entry threshold**. At a median of 340 million KRW, small units still imply a PIR of 9.4/6.8/5.7, high in absolute terms, but their entry prospects differ substantively from standard-size units at 16.1/11.6/9.7 (§IV.10).
- **Redesign the scale and targeting of public rental — a question of allocation, not existence.** Public rental exists at **4,640+ units (16.2%+ of stock)** and is genuinely affordable (0.24M KRW for small units, 5–9% of income). The constraints are volume relative to in-migration and restricted eligibility: LH Complex 2's 1,600 units give **priority to SME employees**, so workers at large establishments and other young households rank lower. Targeting and volume should be rebuilt around the cluster's actual employment structure (§IV.10-(5)). The plan is 97.0% for sale on the presumption of ownership, while realized tenure is 73.4% monthly rent, and nothing bridges the two. So that young and entry-level households excluded from ownership can **settle for the long term rather than cycle through short-term rentals**, public rental (*haengbok* housing, national rental) and private long-term rental volumes should be specified in the plan **as a separate aggregate from units for sale**. - **Attach access conditions to private supply — the largest gap.** Of Godeok's 23,957 privately supplied units, essentially none is affordable (private small-unit rent **0.89M KRW**, 30/21/18% of income). Because expanding public rental improves access only in proportion to its own share, **the structure will not change unless access conditions attach to the private 84% of stock.** LIHTC-style design — shifting the mix by **incentive rather than regulation** — is the instrument that fits.
- **A cluster-specific housing policy — a coordinating body and incentive design.** Godeok was built with **public land servicing and private delivery of 84% of the stock** (23,957 private units against 4,640+ public rental), so outside its own supply the public sector loses any handle on unit type, tenure and price point once land has been supplied. The point of intervention must therefore be **the conditions attached to land supply**. The three U.S. instruments are instructive (§IV.10-(5)): (i) **Housing Choice Voucher (Section 8)**, an **ex-post** measure returning the burden of households already pushed into rent to within the affordability line; (ii) **Public Housing**, direct public supply, already present in Godeok but limited in scale and targeting; and (iii) **LIHTC**, which gives private developers a tax incentive in exchange for long-term income-restricted units. In a Korean new-town structure where delivery is entirely private, **(iii), incentive design, is the most consistent fit**. We propose a coordinating body linking government (land, taxation), employers (employment scale and age structure) and builders (delivery), so that **youth-oriented volumes and unit types are written into the conditions of land supply** at the cluster planning stage.
- **Ex-ante application to subsequent clusters.** Because semiconductor clusters will continue to be built in Korea as a matter of industrial structure, the exclusion structure observed in Godeok should be treated as **a reproducible pattern rather than a one-off event**. Godeok is already under construction, so ex-post instruments (vouchers, acquisition-based rental) dominate there, whereas subsequent clusters such as Yongin permit **ex-ante allocation at the planning stage**. The gap index (§IV.4) and access measures (§IV.10) of this study can serve as the computational basis for that allocation.
- **Design a housing ladder.** The stepwise path from public rental (5–9% burden) through private small and mid-size rental to ownership is broken: the jump from public rental to private small units (30/21/18%) is too large to climb, and ownership at PIR 16.1 is further still. Rental and small for-sale stock priced near the 30% line are needed to make the ladder continuous. Arranging unit types, tenure forms and price points together so that **households can move along the life course within a single city** is a task above adjusting the volume of any individual unit type. It is also the condition for converting in-migrants into settled residents.
- **Reconsider large units (≥85㎡, 4+ rooms).** Godeok-specific re-estimation shows large units short by 9.5 to 15.5pp. Given a child share of 19.4% and an average household size of 3.0–3.5 persons, expanding floor area for families with children is warranted. Because this conclusion is conditional on the assumed average household size, it should be confirmed site by site through measurement (surveys of moving-in households).
- **Treat monthly-rent concentration as a monitoring indicator.** Monthly rent accounts for 41–50% of tenure demand even after turnover adjustment to stock, and its local character was confirmed against control cities. That share is not a market characteristic but **a signal of failed access** (§IV.10), so site-level monthly-rent share and PIR are proposed as planning-stage monitoring indicators.
- **Manage aggregate volume.** Against the remaining 35,932 planned units, population-based cumulative ten-year demand is 20,692 units (58%), so a **risk of aggregate oversupply** should be examined alongside unit composition (§IV.9-(3)).
- **Scope of application.** The framework applies not only to semiconductor sites but to employment-anchor new towns generally, and can serve as an ex-ante diagnostic during the planning stage of subsequent clusters such as Yongin. In doing so, **the average household size of the area in question must be measured locally** — the central lesson of this study — and **access measures (PIR, mortgage burden rate, rental share) should be computed alongside the unit-composition gap**, so that "who gets left out" is established before a plan is finalized.

### 4. Contributions and limitations

This study contributes by diagnosing unit-composition consistency from combined population, supply, and transaction data, and by presenting a prediction chain and practical tool that derive unit size, room count, tenure, and annual volume from age-specific in-migration. Its limitations are as follows. (i) Endogeneity of treatment location: proximity was partially separated by the distance hedonic, but distance to campus overlaps with accessibility to the urban core. (ii) The size and room mappings `M` are assumed, and only the robustness of direction was confirmed by sensitivity analysis. (iii) **Average household size `m̄` is approximated as population divided by apartment units**; non-apartment residents and vacant or not-yet-occupied units were not observed directly, so it is treated as a band of 2.99–3.46, and conclusions on the area axis are conditional on that band. (iv) Turnover adjustment was not applied to the area distribution (only to the tenure axis). (v) The study rests on a single case; transfer validation provides partial support but local differences between cities remain. (vi) The annual forecast depends on the recent three-year gradient, so a change in the campus expansion schedule requires re-estimation, and post-saturation values are lower bounds. (vii) **Income in the access analysis (§IV.10) is a set of three scenarios rather than a measurement**; the income distribution, asset holdings and relocation histories of Godeok's actual resident households were not observed. Ownership burden depends on assumptions of LTV 70%, a 4% rate and 30 years, effective rent on a 5.5% deposit-conversion rate, and the rental share is classified by complex name, so private long-term rental may be omitted. Access results should therefore be read as **the magnitude and direction of the ownership–rental gap** rather than precise cost estimates. (viii) **The public-rental total is a lower bound.** The 4,640 units in Table 13 cover only five complexes with confirmed notices or completion records; Gyeonggi Happy Housing (GH) and Godeok Social Rental Housing Phase 1 are excluded for want of unit counts. Public rental at 16.2% and total rental at 24.1% are therefore both lower bounds. Confirmation requires Pyeongtaek housing statistics and LH supply records. Identification of public complexes also rests on transaction-record names, carrying the nominal-classification limitation noted in §V.2, but no alternative source exists because the complex metadata omits public rental entirely. The program type and eligibility of the 2,249 private rental units also remain unverified. (x) **Residual risk from nominal classification** — verification replaced name-based logic with measured fields at two points (rental identification and geographic identification), but similar patterns may remain in other scripts; when reproducing, check first whether a classification criterion is nominal or measured. (ix) **Three populations coexist**: the unit-composition analysis uses the metadata's sum of units by floor-plan type (22,368); the private tenure analysis uses its sum of total households (23,957); and the re-estimated stock (Table 14) merges public-rental notices into that figure (28,597). Any quoted share must be read against its population. In particular the unit gaps of §IV.3 and §IV.4 are computed on **private for-sale stock** and exclude public rental; since public rental is small-unit-dominated (16–44㎡), actual small-unit supply exceeds this study's count and **the small-unit surplus may be somewhat larger** — a task for v10. Future work should include surveys of moving-in households (covering income and relocation paths), empirical estimation of the mapping coefficients, a two-center model, and wider transfer across cities.

---

## References

1. Korea Planning Association, 2024. "Discussions on the Rise of Single-person Households and Small-housing Demand", *Journal of Korea Planning Association*, 59(6). *[bibliographic details to be verified]*
2. Ministry of Land, Infrastructure and Transport, 2015–2025. *Real Transaction Price Disclosure System for Apartments*, Sejong.
3. Statistics Korea, 2011–2025. *KOSIS* (DT_1B04005N, DT_1JC1516, DT_1JC1511), Daejeon.
4. Dallas Fed, 2023. "Semiconductor Boomtowns and Regional Housing Effects." *[to be verified]*
5. Greenstone, M., Hornbeck, R., and Moretti, E., 2010. "Identifying Agglomeration Spillovers: Evidence from Winners and Losers of Large Plant Openings", *Journal of Political Economy*, 118(3): 536–598.
6. *Journal of Housing and the Built Environment*, 2025. "Data-driven Assessment of Housing Demand–Supply Gaps." *[to be verified]*
7. Mankiw, N.G., and Weil, D.N., 1989. "The Baby Boom, the Baby Bust, and the Housing Market", *Regional Science and Urban Economics*, 19(2): 235–258.
8. Muggeo, V.M.R., 2003. "Estimating Regression Models with Unknown Break-points", *Statistics in Medicine*, 22(19): 3055–3071.
9. Zeng, Y., Land, K.C., Gu, D., and Wang, Z., 2014. *Household and Living Arrangement Projections: The Extended Cohort-Component Method*, Springer.

<sub>⚠️ These references are a draft. Each bibliographic entry (volume, issue, pages, DOI) requires verification against the original before submission; items marked *[to be verified]* particularly require confirmation of the original source.</sub>

---

<div align="right"><sub>Received [ ] · Reviewed [ ] · Revised [ ] · Accepted [ ] &nbsp;—&nbsp; <b>unsubmitted student manuscript (draft)</b></sub></div>
