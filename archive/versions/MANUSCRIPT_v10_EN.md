<!-- v10_EN (2026-08-08): English counterpart of MANUSCRIPT_v10.md. Synchronized content and numbering
     (Figures 1-9, Tables 1-11). Revision history is kept in _CHANGELOG.md, not in the manuscript. -->
<!-- ⚠️ No real journal ISSN/DOI/banner is printed (so that an unpublished student manuscript is never mistaken for a published article). -->

*Journal-style manuscript draft (formatted after *Journal of Korea Planning Association*) — unpublished student research. 📎 Appendix (symbols, validation, sensitivity) → [`APPENDIX_v10_EN.md`](APPENDIX_v10_EN.md) · 📑 Evidence map → [`PAPER_GUIDE.md`](PAPER_GUIDE.md) · Companion tool [`design_simulator.html`](design_simulator.html) · Revision history [`_CHANGELOG.md`](_CHANGELOG.md)*

<br>

# Does the Housing Unit Composition of a New Town near a Semiconductor Cluster Reflect Its Population Structure?
### : Who Gets Left Out of the New Town? The Godeok Case and a Demand–Supply Gap and Housing-Access Based Proposal for Unit Diversification<sup>*</sup>

<br>

**SEOYEON JEON**<sup>**</sup>

---

> **Abstract**
>
> **Background.** Advanced AI semiconductors can be mass-produced in only three countries — the United States, South Korea, and Taiwan — so the clusters concentrating their research and production, and the new towns housing that workforce, will keep being built there. Yet a cluster's site, land, and power are allocated precisely at the planning stage while **the housing demand it generates is not.**
>
> **Purpose.** This study analyzes **Pyeongtaek, Korea (Godeok International New Town) as a representative semiconductor-cluster city, to establish the housing marginalization of the young working class the cluster drew in.** It asks whether the unit composition supplied there reflects the household structure of the actual inflow, which unit types to diversify if not, and who is marginalized as a consequence and by what pathway.
>
> **Methods.** Combining population, supply (unit-type and room-count metadata), and transaction data, we compute a **demand–supply unit-composition gap**, re-estimate it locally via a **maximum-entropy exponential tilt** constrained by the observed mean household size, adjudicate marginalization with **access indicators** (PIR, mortgage burden, and sector-separated rent burden), and validate the predictive chain by rolling-origin backcast (linear MAPE 5.6%).
>
> **Results.** Godeok, which absorbed essentially all of Pyeongtaek's net growth (×5.7), proved to be a **young-family town** rather than a town of single workers (ages 0–14 at **19.4%** against a national 10.3%; mean household size **3.0–3.5** versus 2.18 city-wide), so the city-wide single-person share (37.5%) overstates small-unit demand. Re-estimation makes the mismatch axis-specific: the **room-count axis is a barbell** (three-bedroom units oversupplied by 24pp, 1–2-room units short by 20pp, robust to all variation) while only large units are short on the **floor-area axis**, and supply places **55.3% of all units in a single 84–85㎡ band**. The monthly-rent concentration (73.4% versus 53.5% in the control city) is then confirmed as marginalization rather than preference: a median standard-size price of 580 million KRW gives a **PIR of 16.1** (against 5.1 as the international "severely unaffordable" threshold) and a mortgage burden of **65% of income**. Since **81% of small-unit rent transactions are public rental**, separating sectors gives an effective rent of **0.24M KRW (5–8% of income) for public units versus 0.89M (18–30%) for private ones**.
>
> **Conclusions and implications.** Affordable housing is supplied almost exclusively through public rental; the private stock (84%) offers no enterable price point, and public eligibility leaves out much of the very inflow the cluster creates (one 1,600-unit complex gives priority to SME workers). Young single-earner, newlywed, and low-income households are therefore left in short-term private rent, the most insecure tenure. The problem is not missing policy instruments but that **(i) public volume and eligibility are not designed around the cluster's inflow, and (ii) no access condition attaches to private supply**. Where the public sector prepares the land and private developers build most of the housing, the effective lever is **the conditions of land supply**: later clusters should allocate volumes, unit types, and rent ceilings for young and newly married households in advance at the planning stage. This is a consistency and access diagnosis, not a causal or optimal-allocation claim.
>
> **Keywords**: semiconductor-adjacent new town, AI semiconductor cluster, housing-vulnerable households, housing unit-size fit, demand–supply gap, housing affordability and access, tenure insecurity, real transaction data

<sub>* This study was conducted as a student research project, drawing on open data from the Ministry of Land, Infrastructure and Transport (real transaction prices), Statistics Korea (KOSIS), NAVER Real Estate, and LH/GH tenant recruitment announcements.</sub>
<sub>** Valor International Scholars (first and corresponding author). E-mail: seoyeon.jeon@valorschool.org, alisnaea43@gmail.com</sub>

---

## I. Introduction

### 1. Background

**As a housing problem of the AI era.** The advanced semiconductors behind AI computation — leading-edge logic and high-bandwidth memory — can be mass-produced at commercial scale in only **three countries: the United States, South Korea, and Taiwan**.<sup>1)</sup> That concentration in a handful of countries means **semiconductor clusters will necessarily be built repeatedly in those same countries.** Because a cluster is an object of national industrial policy, its site, land, power, and water are allocated precisely at the planning stage — yet **the housing demand the cluster generates is not planned to the same standard.** The housing problem observed in Godeok is therefore not a one-off event but a structural problem reproduced repeatedly by any country holding an AI semiconductor supply chain.

Large industrial siting decisions produce planned new towns nearby and concentrate young working-age populations (Greenstone et al., 2010). Samsung Electronics' Pyeongtaek Campus (P1 2017, P2 2020, P3 2022) was accompanied by the development of Godeok International New Town, and population, development, and housing prices were rapidly reorganized around it. The conventional expectation is "family inflow → demand for the standard three-bedroom unit," but if the center of gravity of the inflow differs from that expectation, supply built to the convention may diverge from demand. Whether the housing **unit composition** (floor area, room count, tenure form) supplied in such a new town is consistent with the age and household structure of the actual inflow has not been verified.

**This study's focus is on who bears that divergence.** A unit-composition mismatch is not merely market inefficiency. **When a supply plan presumes one household form as the standard, households outside that standard become invisible from the planning stage onward.** A standard unit type also presumes the income class able to afford it, so standardizing the unit type amounts to standardizing which households can enter. Those who bear the consequence are **housing-vulnerable households** — young single-person households, newlyweds and prospective newlyweds, low-income working households, and households that fall down the priority order in public-rental eligibility. They are recorded statistically as "no demand," or are pushed into the most insecure layer of the market (short-term monthly rent) and disappear from the planner's field of view. A consistency diagnosis therefore cannot stop at "what diverged and by how much"; it must also ask **"who is marginalized as a result of that divergence."** This study quantifies that question with transaction-based housing-affordability indicators (§IV.8), and in that respect it is not a report on unit composition but **a report on the marginalization of housing-vulnerable households**.

<sub>1) This statement is based on countries holding mass-production capability in leading-edge foundry (Taiwan, South Korea, United States) and HBM (South Korea, United States). Widening the frame to the whole supply chain including design, equipment, and materials admits more participants, but it is concentration at the **finished-product mass-production stage** that bears on this study's argument (the recurrence of cluster development). ⚠️ Requires verification against primary industry sources (SEMI, U.S. Department of Commerce CHIPS reports, etc.) before submission or publication.</sub>

### 2. Objectives

The research questions are: **(1) Does Godeok's housing supply composition reflect the local population? (2) If it does not, which unit types should be diversified? (3) Who is marginalized in housing as a consequence of that mismatch, and through what pathway does that marginalization operate?**

The contributions are (i) a consistency diagnosis using multi-layer data on population, supply, and transactions (sales and leases); (ii) a household-form-based demand–supply gap framework; (iii) a formalized predictive chain from age inflow to unit size, room count, and tenure, validated in both directions—cross-city transfer and time-axis backcast; (iv) an annual design roadmap and a companion calculation tool that provide a route to practical application; (v) a formalization of the marginalization mechanism as a three-stage chain of **design → price → path divergence** using access indicators (PIR, mortgage burden ratio, rental share); and (vi) a critical review that makes assumptions and limitations explicit and corrects the conclusions of earlier drafts.

---

## II. Literature Review

### 1. Regional effects of large industrial siting

Large industrial siting produces broad regional effects on employment, population, and housing markets (Greenstone et al., 2010; Dallas Fed, 2023). Advanced-industry clusters such as semiconductors concentrate young working-age populations in particular over a short period, making the demand structure for housing in adjacent areas different from that of ordinary cities.

### 2. Population structure and housing demand

Population age structure governs both the quantity and the composition of housing demand (Mankiw and Weil, 1989). Households form out of population (headship), and the distribution of household sizes determines the unit types required. The cohort-component method is the standard approach for projecting households from age-specific population (Zeng et al., 2014). The design model in this study extends that approach to the design of unit size, room count, and tenure.

### 3. Diagnosing demand–supply consistency (gaps)

Approaches that diagnose how well housing supply matches demand in terms of a gap have been proposed (*Journal of Housing and the Built Environment*, 2025). Discussion of the rise of single-person households and small-housing demand in Korea has also accumulated (Korea Planning Association, 2024). This study applies such gap diagnosis to the design of unit composition in a semiconductor-adjacent new town.

### 4. Distinctiveness

Whereas earlier work has treated unit-size *trends* (such as convergence on the standard size) as a nationwide phenomenon, this study (i) diagnoses the consistency between local population structure and supply composition in one specific new town (Godeok); (ii) uses **measured** household-size and household-head-age × household-size distributions; (iii) presents a predictive model deriving unit size, room count, and tenure from age inflow and validates its transfer to other cities; and (iv) extends the unit-composition diagnosis into a **housing-access diagnosis**.

---

## III. Methods

### 1. Scope

The spatial scope is Godeok New Town near Samsung's Pyeongtaek Campus (Godeok-myeon and Godeok-dong, Pyeongtaek), with the whole of Pyeongtaek as the comparison baseline and Anseong, Hwaseong, and Gwangju as control cities. The temporal scope is 2015–2025 for transactions and 2011–2025 for population (data listed in Table 1). **Godeok is identified by legal administrative district** (Godeok-dong and Godeok-myeon), not by complex-name matching (§V.2).

### 2. Data

<br>**Table 1. Overview of analysis data**

| ID | Data | Source / code | Period | Files |
|---|---|---|---|---|
| D1 | Apartment sale and lease transactions | MOLIT real transaction prices | 2015–2025 | `realprice/` |
| D2 | Population by five-year age band | KOSIS DT_1B04005N | 2011–2025 | `population/` |
| D3b | Households by household size (measured) | KOSIS DT_1JC1516 | 2015–2024 | `employment/` |
| D3c | Household-head age × household size (measured) | KOSIS DT_1JC1511 | 2024 | `employment/` |
| D7 | Complex, unit-type, room-count, coordinate metadata | NAVER Real Estate | ~2026 | master sqlite |
| D8 | Public-rental tenant recruitment and completion notices | LH Cheongyak Plus, MyHome portal | ~2026 | confirmed subset |

<sub>Source: open data from MOLIT, Statistics Korea, NAVER Real Estate, and LH. Details in `DATA_SOURCES.md`.</sub>

### 3. Analytical approach

**1) Demand–supply gap framework.** Demand shares by unit type are computed as the (measured) household-form distribution × a (assumed) household-size-to-unit-type mapping, and compared against supply shares. **Gap = supply − demand** (`G_s = S_s − D^A_s`), so a **negative value indicates a shortage** (calling for more supply) and a positive value a surplus. The mapping assumption is tested by sensitivity analysis (Appendix A-2).

**2) Distance-to-campus hedonic.** Transactions are matched to complex coordinates, and log unit price is regressed on continuous distance from the campus (km), a new-town dummy, floor area, building age, and year fixed effects (HC0 robust). This partially separates "proximity to the plant" from "the new-town package."

**3) Age-inflow-based housing design model.** From net inflow `n_a` by age band `a`, the following chain yields unit size, room count, tenure, and the single-person share. Full symbol definitions are in Appendix A-1 (Table A1).
```
Household formation  H_h    = Σ_a  n_a · ρ_a · P(h | head age a)   (ρ = headship, P = measured conditional distribution, DT_1JC1511)
Size and rooms       D^A_s  = Σ_h  H_h · M^A_(h,s) ,   D^R_r = Σ_h  H_h · M^R_(h,r)
Tenure               D^K_k  = Σ_s  D^A_s · T_(s,k)                 (T = Godeok transactions, turnover-adjusted to stock)
Single-person share  = H_1 / Σ_h H_h
```
Headship `ρ_a`, the conditional distribution `P(h|a)`, and tenure propensity `T_(s,k)` are **measured**; only the unit-type mapping `M` is an **assumption**, and it is tested by sensitivity analysis.

**4) Godeok-specific recalibration.** Because `ρ` and `P(h|a)` are city-wide parameters, applying them directly to Godeok introduces bias (§IV.2, §IV.4). To correct this we impose the observed Godeok mean household size `m̄` as a constraint and apply an **exponential tilt (maximum entropy)** that minimizes KL divergence from the prior `q_h`.
```
p_h ∝ q_h · exp(λh) ,   subject to  Σ_h p_h·h = m̄        (λ solved by one-dimensional root finding)
```
`m̄` is treated as an observed band (conservative 2.99 / baseline 3.23 / upper 3.46 persons) so that results are reported as bands.

---

## IV. Results

### 1. Concentration of growth in Godeok

Godeok accounts for roughly 38% of Pyeongtaek's net population increase (2013→2025), and **essentially all net growth since 2022** (Godeok +34,878; rest of Pyeongtaek −3,005). Godeok's population rose from 13,651 to 77,337 (×5.7) and its city share from 3.1% to 12.7%. Its share of new apartment development jumped from 1% to 73%, and the price ratio against the periphery widened from 0.96 to 2.49 (1.22 to 1.67 controlling for building age). **Population, development, and prices all converge on this single location** (Figure 1).

**The unit-size *trend* itself, however, is a nationwide structure, and we note this at the outset.** Convergence on the standard size and the decline of small units appear equally or more strongly in Anseong and Gwangju (before any semiconductor investment), and adjusting for macro cycles (pandemic, interest rates) removes any Pyeongtaek-specific trend (Figure A2). The focus of this study is therefore not "did semiconductors change unit composition" but **"is the supplied composition consistent with Godeok's particular population"** — which is also why this study does not attribute every supply mismatch to a semiconductor effect.

**Figure 1. Concentration in Godeok vs. rest of Pyeongtaek**
![Figure1](../analysis/20_godeok_concentration.png)
<sub>Source: author's analysis based on KOSIS DT_1B04005N.</sub>

### 2. Age structure of the inflow

The center of gravity of the inflow (2018→2025) is working-age adults 25–39 (+24,986), which is 2.4 times the inflow of teenagers aged 5–19 (+10,451) and 4.8 times that of infants aged 0–4 (+5,255). Infants, teenagers, and people in their forties also increased substantially, giving a pattern of **"young working age plus young children"** (Figure 2).

**Godeok is a 'young-family town', not a 'town of young single workers'.** Because this distinction governs the demand estimation that follows, it was cross-checked against the age composition of the resident stock.

| Indicator (2025) | **Godeok** | Pyeongtaek | Nation |
|---|---|---|---|
| Share aged 0–14 | **19.4%** | 12.6% | 10.3% |
| Share aged 25–44 | 45.6% | 31.9% | 26.6% |
| Share aged 65+ | **6.7%** | 14.6% | 21.2% |
| Child/parent ratio (0–14 ÷ 25–44) | **0.43** | 0.40 | 0.39 |
| Mean household size | **3.0–3.5** | 2.18 | — |

Godeok's child share is 1.9 times the national figure and its elderly share less than half Pyeongtaek's. The upper bound on mean household size is 3.46, obtained by dividing Godeok's population (77,337) by its apartment units (22,368); excluding the pre-development base population (10,382 in 2018, non-apartment housing in the former Godeok-myeon) gives 2.99 as a conservative lower bound. Both exceed the city average (2.18) by a wide margin. Consequently, **the city-wide single-person household share (37.5%) arises largely from elderly one-person households in the old urban core, and substituting it for Godeok demand systematically overstates small-unit demand** (corrected in §IV.4).

**Figure 2. Age structure of the Godeok inflow — working age (25–39) plus young children**
![Figure2](../analysis/22_godeok_age.png)
<sub>Source: author's analysis based on KOSIS DT_1B04005N (Godeok-myeon, Godeok-dong).</sub>

### 3. Composition of new housing supply

The unit composition of new apartments in Godeok was tabulated from complex metadata (NAVER Real Estate). The population covers **29 complexes and 22,368 units** in Godeok, each classified by bedroom count and exclusive floor area (Table 2).

By **bedroom count**, **three-bedroom units dominate at 17,527 (78.4%)**, followed by 4+ bedrooms at 3,266 (14.6%), with only 1,575 units (**7.0%**) at 1–2 bedrooms. Three or more bedrooms thus make up **93.0%** of the total, so small room counts are effectively absent from supply. By **exclusive floor area**, the standard size (60–85㎡) also exceeds half at 13,188 units (**59.0%**), with small units (<60㎡) at 6,725 (30.1%) and large units (≥85㎡) at 2,455 (11.0%).

In short, new supply in Godeok **converges strongly on the nationwide standard template of a three-bedroom, standard-size unit**. Whether this supply structure is consistent with the household structure of the inflow (§IV.2, §IV.4) is the core of the analysis that follows.

<br>**Table 2. Composition of new-apartment unit types in Godeok (29 complexes, 22,368 units)**

| Dimension | Category | Units | Share |
|---|---|---|---|
| Rooms | 1–2 bedrooms | 1,575 | 7.0% |
| Rooms | **3 bedrooms** | **17,527** | **78.4%** |
| Rooms | 4+ bedrooms | 3,266 | 14.6% |
| Area | Small <60㎡ | 6,725 | 30.1% |
| Area | **Standard 60–85㎡** | **13,188** | **59.0%** |
| Area | Large ≥85㎡ | 2,455 | 11.0% |

<sub>Source: author's tabulation from master sqlite (complexes + pyeong_types), `analysis/28_supply_structure.py`. ⚠️ This tabulation covers the **private for-sale stock only** and does not reflect public-rental unit types (§V.4-(6)).</sub>

### 4. The demand–supply gap index

**(1) Why the first-pass estimate does not hold.** Substituting Pyeongtaek's measured 2024 household-size distribution (1 person 37.5%, 2 persons 27.5%, 3 persons 18.6%, 4 persons 13.4%, 5+ 3.0%; KOSIS DT_1JC1516) directly yields a shortage of 17.8pp in small units, a surplus of 17.4pp in standard units, and +0.5pp for large units (first column of Table 3). But the mean household size implied by that distribution is **2.18**, and the distribution produced by the age-inflow chain (§IV.7) averages **2.22**, whereas Godeok's observed mean is **2.99–3.46** (§IV.2) — a divergence of about 1.2 persons. The household composition of the first-pass estimate simply cannot accommodate Godeok's actual population, so small-unit demand is structurally overstated. First-pass values are therefore reported **only as a reference against which the re-estimate is compared.**

**(2) Godeok-specific re-estimation.** Imposing the observed mean household size `m̄` as a constraint, demand was recalibrated with the maximum-entropy exponential tilt of §III.3-4) (`p_h ∝ q_h·exp(λh)`), with `m̄` taken as a band of 2.99 (conservative) / 3.23 (baseline) / 3.46 (upper). The change in the household-size distribution and the gap correction on both axes appear in Figure 3-①–③; the computed results are in Table 3.

<br>**Table 3. Recalibrated gap band for Godeok (Gap = supply − demand; negative = shortage)**

| Unit type | First pass (m̄=2.18) | **Conservative (2.99)** | **Baseline (3.23)** | **Upper (3.46)** | Verdict |
|---|---|---|---|---|---|
| Single-person household share | 37.5% | 20.4% | 16.1% | 12.4% | — |
| Small <60㎡ | −17.8 | **+0.6** | **+5.2** | **+9.5** | **surplus** (sign reversal) |
| Standard 60–85㎡ | +17.4 | +9.1 | +7.4 | +6.2 | surplus |
| Large ≥85㎡ | +0.5 | **−9.5** | **−12.5** | **−15.5** | **shortage** (new) |
| 1–2 bedrooms | −45.5 | **−25.4** | **−20.4** | **−15.7** | **shortage** (direction held, magnitude reduced) |
| 3 bedrooms | +38.0 | +26.6 | +24.3 | +22.6 | surplus |
| 4+ bedrooms | — | −6.9 | −4.1 | −1.2 | shortage (slight) |

<sub>Source: author's calculation (`analysis/21_gap_index_prototype.py`, `32_godeok_recalibration.py`). The mapping M is held identical to the first pass so that only the net effect of the distributional correction is isolated. Sensitivity to mapping variation: Figures A1 and A3.</sub>

**(3) Interpretation — the mismatch takes a different form on each axis.** Viewing the re-estimated results in distributional form (Figure 3) shows two structurally different mismatches.

- **Room-count axis = a barbell.** Demand is 27.3% for 1–2 bedrooms, 54.1% for three, and 18.6% for 4+, whereas supply is 7.0%, 78.4%, and 14.6%. The **middle (three bedrooms) is oversupplied by 24.3pp while both ends are short** (1–2 bedrooms −20.3pp, 4+ bedrooms −4.0pp). Two distinct segments — young one- and two-person households before children, and households with children — are each unmet, and the single three-bedroom template corresponds precisely to neither. **This sign holds across the entire `m̄` band and all mapping variations.**
- **Floor-area axis = one-directional "large units short."** The demand distribution on the area axis is not bimodal but a **single peak shifted toward families** (mode near 80㎡), and the shortage appears in one direction only, large units (≥85㎡) at −9.5 to −15.5pp. Small units are in surplus. **The term "barbell" must therefore be confined to the room-count axis.** The sign on the area axis is conditional on the `m̄` assumption (§V.4-(2)).
- **Extremity on the supply side (measured).** Aggregating Godeok supply into exclusive-area unit groups gives **14 groups**, of which the single **84–85㎡ group holds 12,366 units (55.3%)**, and the **top three groups hold 84.8%** of the total (Figure 3-④). The deficit in unit-type diversity is far sharper in this concentration by unit group than in the band share (standard size 59.0%).

The prescription is therefore not the single-track "expand small units" but **"relax the single three-bedroom / standard-size template, with different remedies on each axis."**

**Figure 3. Demand recalibration and the resulting unit-composition mismatch**
![Figure3](../analysis/37_gap_consolidated.png)
<sub>Source: author's calculation (`analysis/37_gap_consolidated.py`). ① household-size distribution under the rejected city-wide parameters and the Godeok-specific corrected band; ② floor-area demand after correction (error bars = band across the three anchors) against supply; ③ the same contrast on the room-count axis; ④ Pareto chart of supply unit groups (bars = share, line = cumulative). Boxed values in ② and ③ are the gap (supply − demand). Unit groups in ④ aggregate measured units into 1㎡ buckets and then merge contiguous runs into practical unit groups.</sub>

### 5. Market segmentation — small-unit demand realized through leases

In Godeok the small-unit share of lease transactions (56–59%) exceeds that of sales (35–44%), and monthly rent accounts for **73.4%** of leases. Demand for small and mobile occupancy is thus realized not through owner-occupied new construction but through leases, and particularly monthly rent (Figure 4).

**Control-city check.** To determine whether this rent concentration is specific to Godeok or reflects a nationwide shift toward monthly rent, it was compared against control cities.

| Area | Jeonse | Monthly rent | Monthly-rent share |
|---|---|---|---|
| **Godeok** | 6,758 | 18,643 | **73.4%** |
| Pyeongtaek (all) | 74,363 | 81,967 | 52.4% |
| Anseong (control, no semiconductor) | 23,092 | 26,575 | 53.5% |

Godeok's monthly-rent share exceeds both the control city (Anseong, 53.5%) and Pyeongtaek as a whole (52.4%) by roughly 20pp. The concentration is therefore **local to Godeok rather than a nationwide trend**, and it is the empirical result that survives the re-estimation of §IV.4 **most robustly**. Whether its cause is preference or marginalization is adjudicated in §IV.8.

⚠️ Note that the area shares (small units 56–59%) are **transaction counts**, so fast-turnover small and monthly-rent units are over-sampled. The tenure axis was turnover-adjusted to stock (§IV.7), but the corresponding correction on the area axis remains future work.

**Figure 4. Lease market: where small-unit demand is realized**
![Figure4](../analysis/10_rent_analysis.png)
<sub>Source: author's analysis based on MOLIT real transaction data.</sub>

### 6. The independent effect of spatial proximity — distance-to-campus hedonic

To partially separate whether Godeok's concentration stems from campus proximity or from the "new town" label, a hedonic regression was applied to Pyeongtaek transactions matched to complex coordinates (41,196 records, 58% match rate; Table 4).

<br>**Table 4. Hedonic regression on distance to campus**

| Variable | Coefficient (effect) | Significance |
|---|---|---|
| Distance to campus (km) | **−3.7%/km** | p<0.0001 |
| New-town dummy (Godeok, net premium) | +3.2% | p<0.0001 |
| Subsample excluding Godeok (n=37,281) | −3.7%/km | p<0.0001 |

<sub>Source: author's calculation (`analysis/23_distance_hedonic.py`). Controls: ln(area), building age, year fixed effects; HC0 robust.</sub>

Most of the price premium comes from continuous distance to the campus (−3.7%/km) rather than from the discrete new-town label (+3.2%) (Figure 5). The −3.7%/km gradient persists even in a subsample containing no new town at all, so the proximity effect is independent rather than a product of the new town. It is robust to relocating the campus reference point to the main gate, P2, or the centroid (−2.5 to −3.7%/km). This suggests that the unit of supply planning should be **commuting accessibility from the employment anchor**, not the administrative boundary of a new town.

**Figure 5. Continuous distance-to-campus hedonic — separating proximity from the new town**
![Figure5](../analysis/23_distance_hedonic.png)
<sub>Source: author's calculation.</sub>

### 7. The age-inflow design model and the annual roadmap

**(1) Applying the chain.** The gap diagnosis is generalized into a predictive chain of "age inflow → household formation → design of unit size, room count, and tenure" (model equations in §III.3-3). Household heads aged 25–39 are 51.4% one-person and 72.9% one- or two-person households (against 37.1% one-person across all ages; DT_1JC1511), so the younger the head, the more overwhelmingly small the household. Substituting this measured conditional distribution and headship (0.17 at ages 20–24 rising to 0.57 at 40+) into the chain and applying it to the Godeok inflow (2018→2025), the uncorrected chain uses city-wide parameters (`ρ_a`, `P(h|a)`) and overstates single-person households at 39.3%, with a distributional mean of only 2.22 persons. After Godeok-specific correction (baseline `m̄`=3.23) the single-person share is **16.1%** and the distributional mean is 3.23, consistent with observation; the gaps are those in the baseline column of Table 3. Tenure shifts under turnover adjustment to stock, from sale 10→31, jeonse 26→19, and monthly rent 64→50% (Figure A4); adding the Godeok-specific correction on top, the reduction in small households moves this further to **sale 35, jeonse 22, and monthly rent 43%**. The before/after comparison is given in Table A4.

**(2) Validation — transferability and the time axis.** Predicting household sizes in other cities with parameters calibrated on Pyeongtaek yields **MAPE of 0.8% for Pyeongtaek itself, 6.0% for Anseong, and 11.0% for Hwaseong**, so the chain captures the regional structure while local differences between cities remain (Table A2). On the time axis, a logistic specification pinned to the planned carrying population (`K_pop`=144,173) **over-predicted consistently at every origin** in a rolling-origin backcast and was rejected at a mean MAPE of 33.8%, while a **linear model based on the most recent three-year slope was adopted at MAPE 5.6%** (Table A3, Figure A5). The cause is extrapolation of the slope of the early rapid-growth phase as a saturation rate. (Godeok's development has run past its original 2008–2022 planning horizon; the 2025 figure of 53.6% of planned population agrees with an independently reported project progress rate of about 52%.)

**(3) Annual prescription.** Using the adopted model (linear, clipped at the `K_pop` ceiling) to derive annual net inflow, and applying the measured inflow age profile and Godeok-specific household formation (baseline `m̄`=3.23), gives Table 5 and Figure 6. Scenario bands are shown in Figure 6.

<br>**Table 5. Annual new-household requirements by unit type (baseline scenario, m̄=3.23)**

| Year | Net inflow | New households | Small (≈60㎡) | Standard (≈83㎡) | Large (≈103㎡+) | 1–2 rooms | 3 rooms | 4+ rooms | Monthly-rent volume |
|---|---|---|---|---|---|---|---|---|---|
| 2026 | 10,958 | 3,392 | 845 | 1,749 | 799 | 927 | 1,832 | 633 | 1,446 |
| 2027–2031 | 10,958 each | 3,392 each | 845 each | 1,749 each | 799 each | 927 each | 1,832 each | 633 each | 1,446 each |
| 2032 | 1,091 | 338 | 84 | 174 | 80 | 92 | 182 | 63 | 144 |
| 2033–2035 | 0 (saturated) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **10-year cumulative** | **66,836** | **20,692** | **5,151** | **10,666** | **4,875** | — | — | — | — |

<sub>Source: author's calculation (`analysis/33_annual_design_roadmap.py`). Scenario band for cumulative new households: 22,353 conservative / 20,692 baseline / 19,317 upper.</sub>

**(4) Comparison with planned volume.** Against the roughly **35,932 units remaining** after subtracting the 22,368 already supplied from Godeok's planned total of 58,300, population-based cumulative demand over ten years is **20,692 units (58% of the remainder)**. Population trends alone therefore cannot absorb the planned volume, and **the planned remainder exceeds population-based demand** — a risk of **aggregate oversupply** distinct from the question of unit mix. (⚠️ Planned units cover all housing types while measured supply covers apartment complexes, so the populations differ and the figure should be read as an upper approximation.)

**(5) Stability over the planning horizon — the corrected trajectory.** A continued-inflow scenario (A) was compared against a cohort-maturation scenario (B: children growing up and ageing, shifting the age profile by one five-year band) with the Godeok-specific correction applied. The correction parameter `λ` was **determined once by anchoring the observation year (A) to the `m̄` band and then applied unchanged to B** — the bias that `ρ` and `P(h|a)` are city-wide parameters is a **structural** bias that persists when the age profile shifts, so holding the correction parameter fixed is correct and B's mean household size must be allowed to move as a result (re-imposing `m̄` on B would by definition erase the effect of cohort maturation). The results are in Table 6.

<br>**Table 6. Planning-horizon trajectory (2025 → 2035) after Godeok-specific recalibration, baseline anchor m̄=3.23**

| Indicator | 2025 (A, inflow continues) | 2035 (B, cohort maturation) | Reference: uncorrected |
|---|---|---|---|
| Mean household size | 3.23 | 3.36 | 2.22 → 2.35 |
| Single-person share | 16.0% | 12.9% | 39.3 → 34.2% |
| 1–2-room demand | 27.2% | 24.2% | 52 → 48% |
| Monthly-rent demand (stock-adjusted) | 42.9% | 42.0% | 50 → 49% |
| **1–2-room gap** | **−20.2pp** | **−17.2pp** | −44.8pp |
| **3-room gap** | **+24.3pp** | **+22.6pp** | +38.0pp |
| Large-unit gap | −12.5pp | −14.1pp | +0.2pp |

<sub>Source: author's calculation (`analysis/36_forecast_design_recalibrated.py`). The corrected 2025 (A) values reproduce the baseline column of Table 3 in §IV.4 (single-person share 16.1%, small +5.2, 1–2 rooms −20.4, 3 rooms +24.3), cross-confirming the consistency of the chain and the re-estimate.</sub>

As the cohort matures, the single-person share (16.0→12.9%), 1–2-room demand (27.2→24.2%), and monthly-rent demand (42.9→42.0%) decline slightly while demand for family-sized units rises. **The signs nonetheless hold throughout the planning horizon**: across all three anchors, 2035 still shows a three-room surplus of +21.3 to +24.6pp, a 1–2-room shortage of −22.0 to −13.0pp, a large-unit shortage of −17.0 to −11.1pp, and a small-unit surplus of +3.7 to +12.0pp. The **unit-diversification conclusion therefore holds within the planning horizon (2030/2035), with the weight of the room-axis prescription shifting somewhat from 1–2 rooms toward large and 4+-room units as the cohort matures.** This recomputes a trajectory that through earlier drafts had been presented only with uncorrected parameters, leaving its level inconsistent with §IV.4.

**(6) Practical use.** The chain is implemented in the companion tool [`design_simulator.html`](design_simulator.html), which recomputes the area-demand distribution curve, household-size composition, annual unit requirements, and design recommendations as inflow by age band, inflow scale, decay rate, and mean household size are adjusted. How results move as the inflow profile changes is summarized in Table A5. Lowering mean household size to 2.18 (Pyeongtaek as a whole) in the direct-entry mode reproduces the first pass's "small units short" conclusion, so a developer can see directly **how parameter choice changes the conclusion**.

**Figure 6. Annual design roadmap — required units by size and scenario band**
![Figure6](../analysis/33_annual_design_roadmap.png)
<sub>Source: author's calculation (`analysis/33_annual_design_roadmap.py`, `27_forecast_design.py`).</sub>

⚠️ **Limitation**: the linear model reaches the planned population in 2032, after which net inflow and therefore new demand are computed as zero. In reality demand continues after saturation through household fission (children leaving home, divorce), so values after 2032 should be read as a **lower bound on inflow-based demand**. Annual inflow is also fixed at the recent three-year slope, so any change to campus expansion schedules (P4, P5) requires re-estimation.

---

### 8. Who gets left out — price barriers and path divergence

§IV.4 showed that supply composition diverges from household structure, and §IV.5 that suppressed demand for small units and low room counts is realized through leases rather than sales (73.4% monthly rent). Why the detour occurs remains open. Two explanations compete. **(a) Preference** — young workers are highly mobile and choose monthly rent voluntarily. **(b) Exclusion** — the entry price of ownership is unaffordable relative to income, so they are pushed out. Since the two carry opposite policy implications (no intervention needed under the first, intervention required under the second), they must be adjudicated. This section does so with transaction-based access indicators.

**(1) The barrier to ownership.** In Godeok apartment sales for 2024–25, the median price of a standard-size unit (60–85㎡) is **580 million KRW** (n=905). For three entry-level annual income scenarios (conservative 36M, middle 50M, high 60M KRW), the price-to-income ratio (PIR) and monthly payment (assuming LTV 70%, 4% interest, 30-year level payments) are given in Table 7.

<br>**Table 7. Entry barriers to ownership by unit type (Godeok, 2024–25 transactions)**

| Unit type | Median price | Equity (30%) | Monthly payment | PIR at 36M | PIR at 50M | PIR at 60M | n |
|---|---:|---:|---:|---:|---:|---:|---:|
| Small <60㎡ | 340M KRW | 102M | 1.14M | 9.4 | 6.8 | 5.7 | 557 |
| **Standard 60–85㎡** | **580M KRW** | **174M** | **1.94M** | **16.1** | **11.6** | **9.7** | 905 |
| Large ≥85㎡ | 710M KRW | 213M | 2.37M | 19.7 | 14.2 | 11.8 | 95 |

<sub>Source: MOLIT real transaction prices (2024–2025), author's calculation. Prices are medians; PIR and monthly payments are computed under the stated assumptions.</sub>

Under the internationally used affordability standard (Demographia), a PIR at or above 5.1 is classified as "severely unaffordable." Godeok's standard-size unit is **16.1 under the conservative scenario, 3.2 times that threshold**, and **9.7 even under the high-income scenario (60M KRW), about twice the threshold**. Even on optimistic income assumptions, entry-level ownership of a standard-size unit does not hold.

**(2) Monthly housing cost — ownership impossible, affordable renting only in the public sector.** Comparing the monthly mortgage payment against the effective cost of renting (rent plus the jeonse-conversion equivalent of the deposit, at a 5.5% conversion rate) as a share of monthly income gives Table 8. **Rent must be read with public and private separated**: **81% of small-unit rent transactions (4,570 of 5,617) are public rental**, so the undivided median of 0.29M KRW is not a private market price.

<br>**Table 8. Monthly housing-cost burden — ownership vs. rent, public and private separated (% of monthly income)**

| Unit type | Monthly payment | Ownership burden<br>(36M/50M/60M) | Rent — **public** | Public burden | Rent — **private** | Private burden | Rent n |
|---|---:|---:|---:|---:|---:|---:|---:|
| Small <60㎡ | 1.14M | 38 / 27 / 23% | **0.24M** | **8 / 6 / 5%** | **0.89M** | **30 / 21 / 18%** | 5,617<br>(public 4,570, private 1,047) |
| **Standard 60–85㎡** | **1.94M** | **65 / 47 / 39%** | (not separated) | — | **1.25M** | **42 / 30 / 25%** | 1,779 |
| Large ≥85㎡ | 2.37M | 79 / 57 / 47% | (not separated) | — | 1.26M<sup>†</sup> | 42 / 30 / 25% | 313 |

<sub>Source: MOLIT real transaction prices (2024–2025), deposits converted at 5.5%, author's calculation. The conventional affordability line is 30% of monthly income. Internal decomposition of the 0.24M public figure: 0.27M for named complexes (n=3,460) and an estimated 0.21M for numbered complexes (n=1,110). <sup>†</sup>Standard and large units were not separated by sector because of small samples, so these are **mixed values**; given that public volume is concentrated in small units (16–44㎡), the true private figures may be higher.</sub>

Applying the conventional threshold that classifies housing costs above 30% of income as "cost-burdened," **standard-size ownership exceeds the line under all three income scenarios** (39–65%). Moving to renting, **private small units sit right at the line at 30/21/18%**, and private standard-size units exceed it at 42/30/25%. The only option clearly inside the line is **public small-unit rental (5–8%)**. The gaps between ownership and renting, and between private and public, are too large to be explained by preference, and they support explanation **(b), marginalization**.

**(3) The tenure structure of supply — public rental exists, and effectively monopolizes affordable housing.** Exclusion becomes a policy problem only under the condition that "those pushed out have an alternative in which to settle stably." Answering this requires **merging data sources**. The complex metadata used for the unit-composition analysis (NAVER Real Estate) is centered on the sale market and **does not list public-rental complexes** (a nationwide search returns zero hits for "Pyeongtaek Godeok Gyeonggi Happy House"), so metadata alone yields 2,249 rental units, 9.4%, and zero LH supply. Yet MOLIT lease transactions show public-rental transactions at **49.3%** (of 10,190 in Godeok) — unambiguously present. This section therefore merges public-rental announcement and completion data into the complex metadata to recompute the stock (Tables 9 and 9).

<br>**Table 9. Public rental complexes in Godeok (confirmed by announcement or completion)**

| Complex | Units | Type | Eligibility |
|---|---:|---|---|
| Pyeongtaek Godeok LH Complex 2 (Block A-6) | 1,600 | Happy House | students, newlyweds, housing-vulnerable, low income / **job-linked, priority for SME workers** |
| Pyeongtaek Godeok LH Complex 15 | 1,295 | LH public rental | (type unconfirmed) |
| Pyeongtaek Godeok LH Complex 12 (Block A57-1) | 900 | Happy House (26, 36, 44㎡) | youth, newlyweds, etc. |
| Pyeongtaek Godeok LH Complex 35 | 549 | LH public rental | (type unconfirmed) |
| Pyeongtaek Godeok LH Complex 17 | 296 | LH public rental | (type unconfirmed) |
| Pyeongtaek Godeok Gyeonggi Happy House (GH) | **unconfirmed** | Happy House | **youth** |
| Pyeongtaek Godeok Social Rental Housing, Phase 1 | **unconfirmed** | social rental housing | (type unconfirmed) |
| **Confirmed total** | **4,640** |  | ⚠️ **lower bound** — two unconfirmed complexes omitted |

<sub>Source: LH Cheongyak Plus and MyHome portal tenant recruitment announcements; completion press releases. The two complexes with unconfirmed unit counts are omitted from the total, so the true figure is larger.</sub>

<br>**Table 10. Recomputed tenure composition of Godeok's apartment stock (merged sources)**

| Category | Units | Share | Source |
|---|---:|---:|---|
| Private for sale | 21,708 | 75.9% | complex metadata |
| Private rental | 2,249 | 7.9% | complex metadata `lease_households` |
| **Public rental** | **4,640** | **16.2%** | announcements and completions (**lower bound**) |
| **Rental total** | **6,889** | **24.1%** |  |
| Total | 28,597 | 100.0% | ⚠️ lower bound |

<sub>Source: author's tabulation. Complex metadata alone yields "rental 9.4%, LH zero," which mistakes a gap in the source for a fact about the world (§V.2).</sub>

The announced rental terms are consistent with the transaction data: LH Complex 2's 16-type carries a deposit of 22.8M KRW and monthly rent of 0.10M, and the youth type at Gyeonggi Happy House a deposit of 19.05M and rent of 0.09M — in line with the effective burdens of 0.21–0.27M in Table 8. The result is clear. In Godeok, the housing an entry-level worker can afford is **effectively concentrated in the single channel of public rental**, and the private market offers no enterable option either in ownership (PIR 16.1) or in renting (0.89M for small, 1.25M for standard units).

**(4) Why rent concentration is nonetheless observed.** Even with more than 4,640 public-rental units, realized tenure is 73.4% monthly rent (§IV.5). The two facts are not contradictory because public rental is limited **both in volume and in eligibility**. The confirmed 16.2% is small relative to the scale of inflow, and eligibility is restricted — LH Complex 2 (1,600 units), for instance, is **job-linked with priority for SME workers**, so workers at large-enterprise sites and other young households fall down the priority order. The problem is therefore not "an absence of policy instruments" but that **the scale and target of those instruments are not designed around the inflow structure the cluster generates**.

**(5) Where the problem lies — not missing instruments but their scale, target, and attached conditions.** Korea has housing-access instruments in law — Happy House, national rental housing, publicly supported private rental — and they **are in fact operating** in Godeok (Table 9). The problem is therefore not their absence but two things: **(i) public volume is small relative to the inflow and its eligibility does not match the cluster's employment structure, and (ii) no access condition attaches to private supply (84% of stock)**. The second is the crux. Where private developers supply most of the stock and none of that volume has an affordable price point, expanding public rental improves access only **in proportion to its own share**. Because Godeok is a structure in which the public sector prepared the land and private developers supplied 84% of the stock, the public sector effectively loses any lever over unit type, tenure, or price point beyond its own supply once the land is transferred. That is why the point of intervention must be **the conditions of land supply** (§V.3).

**(6) Formalizing the marginalization mechanism.** Taken together, marginalization operates in three stages.

> **① Design stage** — private supply is standardized into a single three-bedroom, standard-size template (three bedrooms 78.4%; 55.3% in one 84–85㎡ group; §IV.3).
> **② Price stage** — the price of that standard type (580M KRW; PIR 16.1; mortgage burden 65%) exceeds the ownership entry line for entry-level incomes, and private renting likewise sits at or above the affordability line (0.89M for small, 1.25M for standard units).
> **③ Path-divergence stage** — the only affordable path is public rental (5–8%). Households that enter it settle stably, but because of limited volume (16.2%) and restricted eligibility (SME-worker priority and the like), **those who do not enter remain in short-term private monthly rent**. The 73.4% monthly-rent share in realized tenure is the outcome of this divergence.

Figure 7 brings the chain together in three panels: PIR, burden ratios, and the inversion of tenure. Its implication is that unit diversification is not a matter of aesthetics or market efficiency but **a question of who can settle in this city**. Alternatives do exist — but **only in the public sector, while the private sector supplies no accessible price point at all**. If the gap of §IV.4 is the language of planning, the access indicators of this section are **what that gap becomes when it reaches people**.

<br>**Figure 7. Housing access — why young workers are pushed into monthly rent**
![Figure7](../analysis/35_affordability.png)
<sub>Source: MOLIT real transaction prices (2024–2025), NAVER Real Estate complex metadata, LH announcements; author's calculation. ① PIR against the international affordability threshold; ② mortgage payments vs. rent against the 30%-of-income line; ③ the inversion between planned tenure (97.0% for sale) and realized tenure (73.4% monthly rent).</sub>

⚠️ **Assumptions and limitations**: incomes are scenarios rather than measured values (no income data exist for Godeok's resident households); ownership burden assumes LTV 70%, 4% interest, and 30-year level payments; effective rent assumes a 5.5% jeonse conversion rate. Public-rental complexes are identified from transaction complex names and therefore carry the limitation of nominal classification, and the programme type and eligibility of the 2,249 private rental units are unconfirmed. The figures in Tables 7 and 7 should accordingly be read as indicating **the size of the gaps** between ownership and renting, and between public and private, rather than exact burden amounts. Those gaps are nonetheless too large to be reversed by varying the assumptions (the standard-size ownership burden exceeds the 30% line even under a relaxed 3% interest, 80% LTV assumption).

---

## V. Conclusion

### 1. Discussion

This study analyzed the effect of Samsung's Pyeongtaek semiconductor campus on the surrounding housing market through the case of Godeok New Town, and examined whether the housing unit composition supplied there is consistent with the household-formation structure of the actual inflow — and who is marginalized as a result.

Growth concentrated extremely on a single location within Pyeongtaek (development share 1→73%, price ratio 0.96→2.49; §IV.1), and the population that moved there formed a distinct demographic profile centered on working-age adults 25–39 and their young children (§IV.2). New supply nonetheless followed the standard template of three-bedroom, standard-size units (§IV.3), producing a divergence from demand based on actual household sizes (§IV.4).

**The character of that divergence, and its robustness, differ by axis.** On the room-count axis, three-bedroom units are oversupplied by 22.6–26.6pp while 1–2-room units are short by 15.7–25.4pp and 4+-room units by 1.2–6.9pp — a **barbell structure** whose sign holds across the whole mean-household-size band and all mapping variations. On the floor-area axis, large units (≥85㎡) are short by 9.5–15.5pp while small units are in surplus by 0.6–9.5pp, but that sign is conditional on the assumed mean household size. Suppressed demand for small units and low room counts was realized through leases rather than sales (73.4% monthly rent; §IV.5), which rules out the alternative explanation that the demand simply did not exist.

Decomposing the source of the price premium shows that it arises from physical distance to the semiconductor campus (−3.7%/km) rather than from new-town status as such (the new-town dummy contributes only +3.2%; §IV.6). This runs against the "new-town label premium" hypothesis common in development discourse and suggests that the unit of supply planning should be **commuting accessibility from the employment anchor** rather than an administrative new-town boundary.

The consequences of the mismatch did not stop at market statistics (§IV.8). Standard-size ownership is closed off at PIR 16.1 and a 65% mortgage burden, and private renting also sits at or above the affordability line (0.89M for small units at 30/21/18%; 1.25M for standard units at 42/30/25%). The only option inside the line is **public rental (5–8%)**, which does exist at more than 4,640 units but amounts to only 16.2% of stock with restricted eligibility (LH Complex 2's 1,600 units give priority to SME workers). The 73.4% monthly-rent share observed here is therefore not natural market segmentation but the outcome of a marginalization chain running **design (a single unit type) → price (an entry barrier) → path divergence (whether one enters public rental)**. Households that enter public rental settle; those that do not remain in private short-term rent. What this study diagnoses is thus not inefficiency in the unit mix but **the housing-access question of who can settle in this city**.

In sum, employment-anchor development generates a demand structure that standardized new-town supply templates do not capture. That structure, however, was not the anticipated "young small households" but a form in which **young families predominate while young one- and two-person households also exist**. This study formalized the chain, validated it in both directions — cross-city transfer (MAPE 0.8–11.0%) and time-axis backcast (MAPE 5.6%) — and then provided a route to practical application through an annual design roadmap (§IV.7) and a companion calculation tool.

### 2. Critical review — self-correction within this study

To guard against premature conclusions, the argument passed through six stages: claim, triangulation, interrogation of assumptions, adoption of the steelmanned counter-argument, separation of observation from inference, and provisional conclusion. In triangulation, three independent sources — population (a preponderance of ages 25–39), supply (78.4% three-bedroom), and tenure (73.4% monthly rent, about 20pp above the control city) — pointed jointly to a consistency deficit. In the course of this, the conclusions of earlier drafts were **corrected three times**. (i) The city-wide single-person share (37.5%) had been substituted for Godeok demand to conclude that small units were short; but because Godeok is a family town with a child share 1.9 times the national figure that parameter is inappropriate, and the internal contradiction that the distributional mean diverged from observation by 1.2 persons emerged, **reversing the sign on the floor-area axis** (§IV.4). (ii) Rental volume had been classified by complex **name** and reported at 3.0%, whereas the true figure was 9.4%; the same pattern was found in area identification, and complex-name matching was **replaced by legal-district identification** (26 false positives, 126 false negatives; small-unit median price 354M→340M KRW). (iii) A single source (complex metadata) had been used to conclude "zero LH public rental," but that source is centered on the sale market and does not list public rental at all; transactions showed public rental at 49.3% and confirmed announcements alone at 4,640 units. The derived error was larger still — the 0.29M small-unit rent offered as evidence of affordability was a **mixed value in which public rental made up 81%**, effectively reading public rents as private market prices.

Three methodological lessons follow. **① Do not substitute wide-area average parameters for a locally specific case** — the same bias appeared in the population forecast, where the logistic model over-extrapolated early rapid growth (§IV.7-(2)), and in both cases it surfaced only through ex post validation (internal consistency checks and backcasting). **② Do not use nominal classification (names, labels) as a proxy for a measured field.** **③ Do not read the absence of something in a single source as its absence in the world** — "not in the data" and "does not exist" are different, and market-oriented sources omit the public sector systematically.

### 3. Policy and design recommendations

- **First priority — relax the three-bedroom / standard-size monoculture**: the re-estimate puts the three-bedroom gap at +22.6 to +26.6pp and the standard-size gap at +6.2 to +9.1pp, **a surplus under every scenario**, while on the continuous area axis **55.3% sits in a single 84–85㎡ group**. Reducing the share of that single template is the starting point, and it simultaneously **eases both the barbell shortage on the room axis and the large-unit shortage on the area axis**. Expanding large units (≥85㎡, 4+ rooms) is consistent with a 19.4% child share and a mean household size of 3.0–3.5, but it is conditional on the mean-household-size assumption and must be re-confirmed by site-level surveys of resident households.
- **Expand 1–2-room units — securing an enterable unit type**: the room-count gap of −15.7 to −25.4pp is a shortage under all parameters and mappings, yet supply for young one- and two-person households (72.9% of heads aged 25–39) is only 7.0%. This is not mere mix adjustment but **the creation of the one unit type open to income groups that cannot clear the ownership entry line**. The small-unit median of 340M KRW (PIR 9.4/6.8/5.7) is also high, but entry prospects differ materially from the standard size (16.1/11.6/9.7).
- **Redesign the scale and target of public rental — a question of allocation, not existence**: public rental exists and its rents are affordable (small units 0.24M, 5–8% of income), but the volume falls short of the inflow and eligibility is restricted (LH Complex 2's 1,600 units give priority to SME workers, pushing large-enterprise workers and other young households down the order). The plan presumes ownership at 97.0% for sale, while realized tenure is 73.4% monthly rent. **Target redesign and volume expansion** reflecting the cluster's employment structure (age, employer size) are needed, and public rental and private long-term rental volumes should be specified in the plan **as a separate total from for-sale units**.
- **Attach access conditions to private supply — the largest gap**: of 23,957 private units, essentially none are affordable (private small-unit rent 0.89M = 30/21/18% of income). Expanding public rental improves access only in proportion to its share, so **unless an access condition attaches to private supply — 84% of the stock — the structure will not change.** Because Godeok is a structure in which the public sector prepared the land and private developers supplied most of the housing, the only lever the public sector effectively retains is **the conditions of land supply**. We therefore propose a government (land, tax) – employer (employment scale and age structure information) – builder (supply execution) partnership that **specifies volumes, unit types, and rent ceilings targeted at young and newly married households as conditions of land supply** at the planning stage. Conditions attached at the planning stage are more effective than ex post regulation because neither unit type nor price point can be reversed once construction is complete.
- **A housing ladder, and pre-emptive application to later clusters**: the path from public small-unit rental (5–8%) through private small and mid-size rental (30/21/18%) to ownership (PIR 16.1) is broken, because the gaps between rungs are too large to climb. Placing rental and small for-sale units in the middle price range (near the 30% line) to design **a path along which households can move through the life cycle within one city** is a task above adjusting the volume of individual unit types, and it is the condition for converting an inflow population into a settled one. Since semiconductor clusters will continue to be built in Korea, Godeok's marginalization structure should be treated as **a pattern that reproduces itself**. Godeok, already under development, must rely mainly on ex post instruments, but later clusters such as Yongin **can allocate in advance at the planning stage**. There, **the local mean household size must be measured directly** (the central lesson of this study), and the unit-composition gap (§IV.4) and access indicators (§IV.8) should be **computed together** so that "who is marginalized" is established before the plan is finalized. Site-level monthly-rent shares and PIR are signals of **access failure** rather than market characteristics and should serve as monitoring indicators; and the **aggregate oversupply risk** implied by 20,692 units of ten-year cumulative demand against 35,932 planned remaining units (58%) should be examined alongside (§IV.7-(4)).

### 4. Contributions and limitations

This study combines population, supply, and transaction data to diagnose unit-composition consistency, presents a predictive chain and practical tool deriving unit size, room count, tenure, and annual volumes from age inflow, and extends this into a housing-access diagnosis. Its limitations are as follows.

**(1) Endogeneity of treatment location** — the distance hedonic separates this only partially, since distance to the campus overlaps with accessibility to the urban core. The size and room mappings `M` are assumptions, and sensitivity analysis confirms only the robustness of direction (Figures A1, A3).

**(2) Mean household size `m̄` is an approximation** (population ÷ apartment units), since non-apartment residents and unoccupied or vacant units are not directly observed; it is therefore handled as a band of 2.99–3.46. **The floor-area conclusion (small-unit surplus, large-unit shortage) is conditional on that band**, whereas the room-count conclusion is not. The turnover adjustment was also not applied to the area distribution (only to the tenure axis).

**(3) Incomes in the access analysis (§IV.8) are three scenarios rather than measurements**, and the income distribution, asset holdings, and prior-residence transitions of Godeok's actual resident households were not observed. Ownership burden depends on LTV 70%, 4% interest, and 30 years; effective rent on a 5.5% conversion rate. Access results should therefore be read as **the size and direction of gaps** rather than exact burden estimates. Standard-size and large-unit rents could not be separated by sector because of sample constraints.

**(4) The public-rental total is a lower bound.** The 4,640 units in Table 9 sum only the five complexes confirmed by announcement or completion, excluding Gyeonggi Happy House (GH) and Social Rental Housing Phase 1, whose unit counts are unconfirmed. Public rental at 16.2% and total rental at 24.1% are therefore **lower bounds**, to be fixed by cross-checking against Pyeongtaek housing statistics and LH supply records. Public-rental complexes are identified from transaction complex names and thus carry the limitation of nominal classification (§V.2), but no alternative source exists because complex metadata omits public rental; the programme type and eligibility of the 2,249 private rental units also remain unconfirmed. Two name-based classification routines (rental identification and area identification) were replaced with measured fields during validation, but similar patterns may persist in other scripts, so anyone reproducing this work should first check whether each classification criterion is nominal or measured.

**(5) The planning-horizon trajectory (§IV.7-(5)) was computed with uncorrected parameters**, so its level is not consistent with §IV.4 and it requires recomputation after correction. Annual projections depend on the recent three-year slope, so changes to campus expansion schedules require re-estimation, and post-saturation values are lower bounds.

**(6) Three populations coexist** — the unit-composition analysis uses the sum of units by unit type in the complex metadata (22,368), the private tenure analysis the sum of total units (23,957), and the stock recomputation (Table 10) the value merged with public-rental announcements (28,597) — so any cited ratio must be checked against its population. In particular the gaps in §IV.3 and §IV.4 are **on a private for-sale basis** and do not reflect public-rental unit types; given that public rental is concentrated in small units (16–44㎡), small-unit supply is larger than tabulated here and **the small-unit surplus may widen somewhat**. Recomputing the gap with public-rental unit types included is the highest-priority next step.

**(7) A single case**, partially reinforced by transfer validation, but local differences between cities remain. Future work requires surveys of resident households (including income and transition paths), empirical estimation of the mapping coefficients, a two-center model, and wider multi-city transfer.

---

## References

1. Korea Planning Association, 2024. "Discussions on the Rise of Single-person Households and Small-housing Demand", *Journal of Korea Planning Association*, 59(6). *[to be verified]*
2. Ministry of Land, Infrastructure and Transport, 2015–2025. *Real Transaction Price Disclosure System for Apartments*, Sejong.
3. Statistics Korea, 2011–2025. *KOSIS* (DT_1B04005N, DT_1JC1516, DT_1JC1511), Daejeon.
4. Korea Land and Housing Corporation and Gyeonggi Housing and Urban Development Corporation, 2019–2026. *Tenant Recruitment Announcements* (Pyeongtaek Godeok Blocks A-6, A57-1, etc.).
5. Dallas Fed, 2023. "Semiconductor Boomtowns and Regional Housing Effects." *[to be verified]*
6. Greenstone, M., Hornbeck, R., and Moretti, E., 2010. "Identifying Agglomeration Spillovers: Evidence from Winners and Losers of Large Plant Openings", *Journal of Political Economy*, 118(3): 536–598.
7. *Journal of Housing and the Built Environment*, 2025. "Data-driven Assessment of Housing Demand–Supply Gaps." *[to be verified]*
8. Mankiw, N.G., and Weil, D.N., 1989. "The Baby Boom, the Baby Bust, and the Housing Market", *Regional Science and Urban Economics*, 19(2): 235–258.
9. Zeng, Y., Land, K.C., Gu, D., and Wang, Z., 2014. *Household and Living Arrangement Projections: The Extended Cohort-Component Method*, Springer.

<sub>⚠️ These references are a draft; each entry (volume, issue, pages, DOI) requires verification against the original before submission or publication. Items marked *[to be verified]* particularly require confirmation of the original source.</sub>

---

<div align="right"><sub>Received [ ] · Reviewed [ ] · Revised [ ] · Accepted [ ] &nbsp;—&nbsp; <b>Unsubmitted student manuscript (draft)</b></sub></div>
