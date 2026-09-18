<!-- v11 EN (2026-08-08): English edition of MANUSCRIPT_v11.md. Public rental total confirmed (7,720 units, 25.7%); supplier reclassification; data provenance stated; conclusion prose revised. -->
<!-- ⚠️ No real journal ISSN/DOI/banner is printed (so that an unpublished student manuscript is never mistaken for a published article). -->

*Journal-style manuscript draft (formatted after *Journal of Korea Planning Association*) — unpublished student research. 📎 Appendix (symbols, validation, sensitivity) → [`APPENDIX_v12_EN.md`](APPENDIX_v12_EN.md) · 📑 Evidence map → [`PAPER_GUIDE.md`](PAPER_GUIDE.md) · Companion tool [`design_simulator.html`](design_simulator.html) · Revision history [`_CHANGELOG.md`](_CHANGELOG.md)*

<br>

# Does the Housing Unit Composition of a New Town near a Semiconductor Cluster Reflect Its Population Structure?
### : Who Gets Left Out of the New Town? The Godeok Case and a Demand–Supply Gap and Housing-Access Based Proposal for Unit Diversification<sup>*</sup>

<br>

**SEOYEON JEON**<sup>1</sup>

<sup>1</sup> Valor International Scholars, Republic of Korea. E-mail: seoyeon.jeon@valorschool.org, alisnaea43@gmail.com

---

> **Abstract**
>
> Advanced AI semiconductors are mass-produced in only a few countries, so the clusters that make them — and the new towns built to house their workforce — will keep recurring. A cluster's site, land and power are allocated at the planning stage; the housing demand it generates is not. Taking Godeok International New Town beside Samsung's Pyeongtaek Campus as a case, this study asks whether the unit composition supplied there reflects the household structure of the people who actually moved in, who is left out when it does not, and **whether public housing support reaches those who are**. Combining population, supply and transaction data, we compute a demand–supply unit-composition gap, re-estimate demand locally under the observed mean household size, and add transaction-based housing-access measures. Godeok absorbed essentially all of Pyeongtaek's net growth and proved to be a young-family town rather than a town of single workers, so the city-wide single-person share overstates small-unit demand. Re-estimation makes the mismatch axis-specific: the room-count axis is a barbell, with three-bedroom units oversupplied by 24pp while both extremes fall short, whereas on the floor-area axis only large units are short; 55.3% of all units sit in a single 84–85m² band. Access measures show the monthly-rent concentration to be marginalization rather than preference. A standard-size unit costs 16.1 times entry-level annual income and 65% of monthly income to service, and once public rental is separated out, private small units rent at 18–30% of income against 5–8% for public ones. Affordable housing is thus supplied almost exclusively through public rental, while the private stock offers no enterable price point and public eligibility, set against the urban-worker average, excludes the very inflow the cluster creates — a single earner on 50 million KRW is over the ceiling for permanent rental, national rental and youth Happy Housing alike. The answer to the policy question is that a blind spot does open. The problem is not missing instruments but that public volume and eligibility are built around household formation and the urban-worker average, so the population a cluster attracts falls between them — too well paid for public programmes, not well paid enough for the market — while no access condition attaches to private supply. Where the public sector prepares the land and private developers build most of the housing, the effective lever is the conditions of land supply.

**Keywords**: semiconductor-adjacent new town, AI semiconductor cluster, housing-vulnerable households, housing unit-size fit, demand–supply gap, housing affordability and access, tenure insecurity, real transaction data

<sub>* This study was conducted as a student research project, drawing on open data from the Ministry of Land, Infrastructure and Transport (real transaction prices), Statistics Korea (KOSIS), NAVER Real Estate, and LH/GH tenant recruitment announcements.</sub>

---

## 1. Introduction

### 1.1 Background

**As a housing problem of the AI era.** The advanced semiconductors behind AI computation — leading-edge logic and high-bandwidth memory — can be mass-produced at commercial scale in only **three countries: the United States, South Korea, and Taiwan**.<sup>1)</sup> That concentration in a handful of countries means **semiconductor clusters will necessarily be built repeatedly in those same countries.** Because a cluster is an object of national industrial policy, its site, land, power, and water are allocated precisely at the planning stage — yet **the housing demand the cluster generates is not planned to the same standard.** The housing problem observed in Godeok is therefore not a one-off event but a structural problem reproduced repeatedly by any country holding an AI semiconductor supply chain.

Large industrial siting decisions produce planned new towns nearby and concentrate young working-age populations (Greenstone et al., 2010). Samsung Electronics' Pyeongtaek Campus (P1 2017, P2 2020, P3 2022) was accompanied by the development of Godeok International New Town, and population, development, and housing prices were rapidly reorganized around it. The conventional expectation is "family inflow → demand for the standard three-bedroom unit," but if the center of gravity of the inflow differs from that expectation, supply built to the convention may diverge from demand. Whether the housing **unit composition** (floor area, room count, tenure form) supplied in such a new town is consistent with the age and household structure of the actual inflow has not been verified.

**This study's focus is on who bears that divergence.** A unit-composition mismatch is not merely market inefficiency. **When a supply plan presumes one household form as the standard, households outside that standard become invisible from the planning stage onward.** A standard unit type also presumes the income class able to afford it, so standardizing the unit type amounts to standardizing which households can enter. Those who bear the consequence are **housing-vulnerable households** — young single-person households, newlyweds and prospective newlyweds, low-income working households, and households that fall down the priority order in public-rental eligibility. They are recorded statistically as "no demand," or are pushed into the most insecure layer of the market (short-term monthly rent) and disappear from the planner's field of view. A consistency diagnosis therefore cannot stop at "what diverged and by how much"; it must also ask **"who is marginalized as a result of that divergence."** This study quantifies that question with transaction-based housing-affordability indicators (§4.8), and in that respect it is not a report on unit composition but **a report on the marginalization of housing-vulnerable households**.

<sub>1) This statement is based on countries holding mass-production capability in leading-edge foundry (Taiwan, South Korea, United States) and HBM (South Korea, United States). Widening the frame to the whole supply chain including design, equipment, and materials admits more participants, but it is concentration at the **finished-product mass-production stage** that bears on this study's argument (the recurrence of cluster development). ⚠️ Requires verification against primary industry sources (SEMI, U.S. Department of Commerce CHIPS reports, etc.) before submission or publication.</sub>

### 1.2 Objectives

The research questions are: **(1) Does Godeok's housing supply composition reflect the local population? (2) If it does not, which unit types should be diversified? (3) Who is marginalized in housing as a consequence of that mismatch, and through what pathway does that marginalization operate? (4) And does public housing support reach them?**

The contributions are (i) a consistency diagnosis using multi-layer data on population, supply, and transactions (sales and leases); (ii) a household-form-based demand–supply gap framework; (iii) a formalized predictive chain from age inflow to unit size, room count, and tenure, validated in both directions—cross-city transfer and time-axis backcast; (iv) an annual design roadmap and a companion calculation tool that provide a route to practical application; (v) a formalization of the marginalization mechanism as a three-stage chain of **design → price → path divergence** using access indicators (PIR, mortgage burden ratio, rental share); and (vi) a critical review that makes assumptions and limitations explicit and corrects the conclusions of earlier drafts.

---

## 2. Literature Review

### 2.1 Regional effects of large industrial siting

Large industrial siting produces broad regional effects on employment, population, and housing markets (Greenstone et al., 2010; Dallas Fed, 2023). Advanced-industry clusters such as semiconductors concentrate young working-age populations in particular over a short period, making the demand structure for housing in adjacent areas different from that of ordinary cities.

### 2.2 Population structure and housing demand

Population age structure governs both the quantity and the composition of housing demand (Mankiw and Weil, 1989). Households form out of population (headship), and the distribution of household sizes determines the unit types required. The cohort-component method is the standard approach for projecting households from age-specific population (Zeng et al., 2014). The design model in this study extends that approach to the design of unit size, room count, and tenure.

### 2.3 Diagnosing demand–supply consistency (gaps)

Approaches that diagnose how well housing supply matches demand in terms of a gap have been proposed (*Journal of Housing and the Built Environment*, 2025). Discussion of the rise of single-person households and small-housing demand in Korea has also accumulated (Korea Planning Association, 2024). This study applies such gap diagnosis to the design of unit composition in a semiconductor-adjacent new town.

### 2.4 Distinctiveness

Whereas earlier work has treated unit-size *trends* (such as convergence on the standard size) as a nationwide phenomenon, this study (i) diagnoses the consistency between local population structure and supply composition in one specific new town (Godeok); (ii) uses **measured** household-size and household-head-age × household-size distributions; (iii) presents a predictive model deriving unit size, room count, and tenure from age inflow and validates its transfer to other cities; and (iv) extends the unit-composition diagnosis into a **housing-access diagnosis**.

---

## 3. Methods

### 3.1 Scope

The spatial scope is Godeok New Town near Samsung's Pyeongtaek Campus (Godeok-myeon and Godeok-dong, Pyeongtaek), with the whole of Pyeongtaek as the comparison baseline and Anseong, Hwaseong, and Gwangju as control cities. The temporal scope is 2015–2025 for transactions and 2011–2025 for population (data listed in Table 1). **Godeok is identified by legal administrative district** (Godeok-dong and Godeok-myeon), not by complex-name matching (§5.2).

### 3.2 Data

<br>**Table 1. Overview of analysis data**

| ID | Data | Source / code | Period | Files |
|---|---|---|---|---|
| D1 | Apartment sale and lease transactions | MOLIT real transaction prices | 2015–2025 | `realprice/` |
| D2 | Population by five-year age band | KOSIS DT_1B04005N | 2011–2025 | `population/` |
| D3b | Households by household size (measured) | KOSIS DT_1JC1516 | 2015–2024 | `employment/` |
| D3c | Household-head age × household size (measured) | KOSIS DT_1JC1511 | 2024 | `employment/` |
| D7 | Complex, unit-type, room-count, unit-count, coordinate metadata | Naver Real Estate (JSON) | ~2026 | master sqlite |
| D8 | Public-rental tenant recruitment and completion notices | LH Cheongyak Plus, MyHome portal | ~2026 | confirmed subset |

<sub>Source: open data from MOLIT, Statistics Korea, NAVER Real Estate, and LH/GH. Details in `DATA_SOURCES.md`.</sub>

All of the material analysed here is primary. From MOLIT real transaction prices we downloaded 253,255 sale records and 156,330 lease records covering 2015–2025, of which 26,710 fall in Godeok. Population and household figures are quoted directly from Statistics Korea's KOSIS tables, and public rental volumes and rent terms were confirmed from LH Cheongyak Plus, MyHome and GH tenant-recruitment notices.

One further source was necessary. National statistics do not record how many rooms a dwelling has or its exclusive floor area, and a study of unit-composition fit cannot proceed without that. We therefore turned to the real-estate service operated by Naver, the most widely used internet portal in Korea, which publishes complex-level detail in JSON form. Collecting and normalising it produced 6,244 complexes and 29,014 unit-type records nationwide (319 in Pyeongtaek, 29 in Godeok), supplying room counts, floor areas, unit counts, rental-unit counts and coordinates. Only with this can demand inferred from population structure be compared with the housing actually built on the same axis. The source is oriented to the sale market, however, and does not list public rental complexes; that gap is filled with recruitment-notice data in §4.8.

**Auditing the metadata with a local language model.** Two problems arise once a study leans on 29,014 machine-collected records. Nobody can read them all, and — as §5.2 records — this study three times mistook a name field for a measured one. Both were addressed by auditing the records with an open-source language model (Gemma) run locally through Ollama, on the authors' own machine, so that no data left it.

The model was given two tasks. First, every unit-type record in Pyeongtaek carrying both an area and a bedroom count (1,432 records) was passed in batches and asked to flag combinations that cannot coexist in Korean practice. Two records were flagged, both an 84m² four-bedroom layout that is in fact common here, so on review neither was a genuine error: the internal consistency of the metadata is high, and the model over-flags rather than under-flags.

Second, and more usefully, the model was given complex names alone and asked to say whether each was publicly or privately supplied — the very judgment that had gone wrong earlier. Against thirteen complexes whose supplier is confirmed by LH and GH notices, it answered correctly for nine, an accuracy of **69.2%**. All four errors were the same kind: Le Florent, Hestible, Yangwoo Naeanae and Shindonga Pamilie NHF 7 were called private because private contractors built them, when they are in fact LH projects mixing Newlywed Hope Town units with Happy Housing, or public rental REITs. That is the identical mistake this study made, now measured: roughly three in ten complexes cannot be classified from their name, and the failures cluster exactly on mixed-supply projects. It is the empirical reason every classification in this paper rests on a measured field rather than a label.

### 3.3 Analytical approach

**1) Demand–supply gap framework.** Demand shares by unit type are computed as the (measured) household-form distribution × a (assumed) household-size-to-unit-type mapping, and compared against supply shares. the gap is defined as <i>G<sub>s</sub></i> = <i>S<sub>s</sub></i> − <i>D</i><sup>A</sup><sub><i>s</i></sub>, i.e. **supply minus demand**, so a **negative value indicates a shortage** (calling for more supply) and a positive value a surplus. The mapping assumption is tested by sensitivity analysis (Appendix A-2).

**2) Distance-to-campus hedonic.** Transactions are matched to complex coordinates, and log unit price is regressed on continuous distance from the campus (km), a new-town dummy, floor area, building age, and year fixed effects (HC0 robust). This partially separates "proximity to the plant" from "the new-town package."

**3) Age-inflow-based housing design model.** From net inflow <i>n<sub>a</sub></i> by age band <i>a</i>, the following chain yields unit size, room count, tenure, and the single-person share. Full symbol definitions are in Appendix A-1 (Table A1).
<div class="eq"><span class="eqb"><i>H<sub>h</sub></i> = Σ<sub><i>a</i></sub> <i>n<sub>a</sub></i> · <i>ρ<sub>a</sub></i> · <i>P</i>(<i>h</i> | <i>a</i>)</span><span class="eqn">(1)</span></div>

<div class="eq"><span class="eqb"><i>D</i><sup>A</sup><sub><i>s</i></sub> = Σ<sub><i>h</i></sub> <i>H<sub>h</sub></i> · <i>M</i><sup>A</sup><sub><i>h,s</i></sub> ,&nbsp;&nbsp; <i>D</i><sup>R</sup><sub><i>r</i></sub> = Σ<sub><i>h</i></sub> <i>H<sub>h</sub></i> · <i>M</i><sup>R</sup><sub><i>h,r</i></sub></span><span class="eqn">(2)</span></div>

<div class="eq"><span class="eqb"><i>D</i><sup>K</sup><sub><i>k</i></sub> = Σ<sub><i>s</i></sub> <i>D</i><sup>A</sup><sub><i>s</i></sub> · <i>T<sub>s,k</sub></i> ,&nbsp;&nbsp; <i>σ</i><sub>1</sub> = <i>H</i><sub>1</sub> ⁄ Σ<sub><i>h</i></sub> <i>H<sub>h</sub></i></span><span class="eqn">(3)</span></div>

<div class="whr">where,<br>
<i>n<sub>a</sub></i> : net in-migration of age band <i>a</i><br>
<i>ρ<sub>a</sub></i> : headship rate of age band <i>a</i> (measured)<br>
<i>P</i>(<i>h</i>|<i>a</i>) : share of <i>h</i>-person households among heads of age <i>a</i> (measured, DT_1JC1511)<br>
<i>H<sub>h</sub></i> : number of <i>h</i>-person households formed<br>
<i>M</i><sup>A</sup>, <i>M</i><sup>R</sup> : mapping from household size to floor-area class <i>s</i> and room count <i>r</i> (assumed)<br>
<i>T<sub>s,k</sub></i> : tenure propensity of area class <i>s</i> toward tenure <i>k</i> (measured, turnover-adjusted to stock)<br>
<i>σ</i><sub>1</sub> : single-person share</div>

Of these, headship, the conditional distribution and tenure propensity are measured quantities; the mapping <i>M</i> is the only assumption, and its influence is examined by sensitivity analysis.

**4) Godeok-specific recalibration.** Because <i>ρ</i> and <i>P</i>(<i>h</i>|<i>a</i>) are city-wide parameters, applying them directly to Godeok introduces bias (§4.2, §4.4). To correct this we impose the observed Godeok mean household size <i>m̄</i> as a constraint and apply an **exponential tilt (maximum entropy)** that minimizes KL divergence from the prior <i>q<sub>h</sub></i>.
<div class="eq"><span class="eqb"><i>p<sub>h</sub></i> ∝ <i>q<sub>h</sub></i> · exp(<i>λh</i>) ,&nbsp;&nbsp; subject to&nbsp; Σ<sub><i>h</i></sub> <i>p<sub>h</sub></i> · <i>h</i> = <i>m̄</i></span><span class="eqn">(4)</span></div>

<div class="whr">where,<br>
<i>q<sub>h</sub></i> : prior distribution of household size<br>
<i>p<sub>h</sub></i> : corrected distribution<br>
<i>λ</i> : tilt parameter, obtained by one-dimensional root finding<br>
<i>m̄</i> : observed mean household size in Godeok</div>

Because <i>m̄</i> is itself observed with uncertainty, it is carried as a band — 2.99 (conservative), 3.23 (baseline) and 3.46 (upper) persons — and every result derived from it is reported as a band rather than a point.

---

## 4. Results

### 4.1 Concentration of growth in Godeok

Godeok accounts for roughly 38% of Pyeongtaek's net population increase (2013→2025), and **essentially all net growth since 2022** (Godeok +34,878; rest of Pyeongtaek −3,005). Godeok's population rose from 13,651 to 77,337 (×5.7) and its city share from 3.1% to 12.7%. Its share of new apartment development jumped from 1% to 73%, and the price ratio against the periphery widened from 0.96 to 2.49 (1.22 to 1.67 controlling for building age). **Population, development, and prices all converge on this single location** (Figure 1).

**The unit-size *trend* itself, however, is a nationwide structure, and we note this at the outset.** Convergence on the standard size and the decline of small units appear equally or more strongly in Anseong and Gwangju (before any semiconductor investment), and adjusting for macro cycles (pandemic, interest rates) removes any Pyeongtaek-specific trend (Figure A2). The focus of this study is therefore not "did semiconductors change unit composition" but **"is the supplied composition consistent with Godeok's particular population"** — which is also why this study does not attribute every supply mismatch to a semiconductor effect.

**Fig.1. Concentration in Godeok vs. rest of Pyeongtaek**
![Figure1](../analysis/20_godeok_concentration.png)
<sub>Source: author's analysis based on KOSIS DT_1B04005N.</sub>

### 4.2 Age structure of the inflow

The center of gravity of the inflow (2018→2025) is working-age adults 25–39 (+24,986), which is 2.4 times the inflow of teenagers aged 5–19 (+10,451) and 4.8 times that of infants aged 0–4 (+5,255). Infants, teenagers, and people in their forties also increased substantially, giving a pattern of **"young working age plus young children"** (Figure 2).

**Godeok is a 'young-family town', not a 'town of young single workers'.** Because this distinction governs the demand estimation that follows, it was cross-checked against the age composition of the resident stock.

| Indicator (2025) | **Godeok** | Pyeongtaek | Nation |
|---|---|---|---|
| Share aged 0–14 | **19.4%** | 12.6% | 10.3% |
| Share aged 25–44 | 45.6% | 31.9% | 26.6% |
| Share aged 65+ | **6.7%** | 14.6% | 21.2% |
| Child/parent ratio (0–14 ÷ 25–44) | **0.43** | 0.40 | 0.39 |
| Mean household size | **3.0–3.5** | 2.18 | — |

Godeok's child share is 1.9 times the national figure and its elderly share less than half Pyeongtaek's. The upper bound on mean household size is 3.46, obtained by dividing Godeok's population (77,337) by its apartment units (22,368); excluding the pre-development base population (10,382 in 2018, non-apartment housing in the former Godeok-myeon) gives 2.99 as a conservative lower bound. Both exceed the city average (2.18) by a wide margin. Consequently, **the city-wide single-person household share (37.5%) arises largely from elderly one-person households in the old urban core, and substituting it for Godeok demand systematically overstates small-unit demand** (corrected in §4.4).

**Fig.2. Age structure of the Godeok inflow — working age (25–39) plus young children**
![Figure2](../analysis/22_godeok_age.png)
<sub>Source: author's analysis based on KOSIS DT_1B04005N (Godeok-myeon, Godeok-dong).</sub>

### 4.3 Composition of new housing supply

The unit composition of new apartments in Godeok was tabulated from complex metadata (NAVER Real Estate). The population covers **29 complexes and 22,368 units** in Godeok, each classified by bedroom count and exclusive floor area (Table 2).

By **bedroom count**, **three-bedroom units dominate at 17,527 (78.4%)**, followed by 4+ bedrooms at 3,266 (14.6%), with only 1,575 units (**7.0%**) at 1–2 bedrooms. Three or more bedrooms thus make up **93.0%** of the total, so small room counts are effectively absent from supply. By **exclusive floor area**, the standard size (60–85m²) also exceeds half at 13,188 units (**59.0%**), with small units (<60m²) at 6,725 (30.1%) and large units (≥85m²) at 2,455 (11.0%).

In short, new supply in Godeok **converges strongly on the nationwide standard template of a three-bedroom, standard-size unit**. Whether this supply structure is consistent with the household structure of the inflow (§4.2, §4.4) is the core of the analysis that follows.

<br>**Table 2. Composition of new-apartment unit types in Godeok (29 complexes, 22,368 units)**

| Dimension | Category | Units | Share |
|---|---|---|---|
| Rooms | 1–2 bedrooms | 1,575 | 7.0% |
| Rooms | **3 bedrooms** | **17,527** | **78.4%** |
| Rooms | 4+ bedrooms | 3,266 | 14.6% |
| Area | Small <60m² | 6,725 | 30.1% |
| Area | **Standard 60–85m²** | **13,188** | **59.0%** |
| Area | Large ≥85m² | 2,455 | 11.0% |

<sub>Source: author's tabulation from master sqlite (complexes + pyeong_types), `analysis/28_supply_structure.py`. ⚠️ This tabulation covers the **private for-sale stock only** and does not reflect public-rental unit types (§5.4-(6)).</sub>

### 4.4 The demand–supply gap index

**(1) Why the first-pass estimate does not hold.** Substituting Pyeongtaek's measured 2024 household-size distribution (1 person 37.5%, 2 persons 27.5%, 3 persons 18.6%, 4 persons 13.4%, 5+ 3.0%; KOSIS DT_1JC1516) directly yields a shortage of 17.8pp in small units, a surplus of 17.4pp in standard units, and +0.5pp for large units (first column of Table 3). But the mean household size implied by that distribution is **2.18**, and the distribution produced by the age-inflow chain (§4.7) averages **2.22**, whereas Godeok's observed mean is **2.99–3.46** (§4.2) — a divergence of about 1.2 persons. The household composition of the first-pass estimate simply cannot accommodate Godeok's actual population, so small-unit demand is structurally overstated. First-pass values are therefore reported **only as a reference against which the re-estimate is compared.**

**(2) Godeok-specific re-estimation.** Imposing the observed mean household size <i>m̄</i> as a constraint, demand was recalibrated with the maximum-entropy exponential tilt of §3.3-4) (<i>p<sub>h</sub></i> ∝ <i>q<sub>h</sub></i>·exp(<i>λh</i>)), with <i>m̄</i> taken as a band of 2.99 (conservative) / 3.23 (baseline) / 3.46 (upper). The change in the household-size distribution and the gap correction on both axes appear in Figure 3-①–③; the computed results are in Table 3.

<br>**Table 3. Recalibrated gap band for Godeok (Gap = supply − demand; negative = shortage)**

| Unit type | First pass (m̄=2.18) | **Conservative (2.99)** | **Baseline (3.23)** | **Upper (3.46)** | Verdict |
|---|---|---|---|---|---|
| Single-person household share | 37.5% | 20.4% | 16.1% | 12.4% | — |
| Small <60m² | −17.8 | **+0.6** | **+5.2** | **+9.5** | **surplus** (sign reversal) |
| Standard 60–85m² | +17.4 | +9.1 | +7.4 | +6.2 | surplus |
| Large ≥85m² | +0.5 | **−9.5** | **−12.5** | **−15.5** | **shortage** (new) |
| 1–2 bedrooms | −45.5 | **−25.4** | **−20.4** | **−15.7** | **shortage** (direction held, magnitude reduced) |
| 3 bedrooms | +38.0 | +26.6 | +24.3 | +22.6 | surplus |
| 4+ bedrooms | — | −6.9 | −4.1 | −1.2 | shortage (slight) |

<sub>Source: author's calculation (`analysis/21_gap_index_prototype.py`, `32_godeok_recalibration.py`). The mapping M is held identical to the first pass so that only the net effect of the distributional correction is isolated. Sensitivity to mapping variation: Figures A1 and A3.</sub>

**(3) Public rental changes the picture — and the difference is itself the finding.** Table 3 is computed on the stock recorded in the complex metadata, which is private for-sale supply. Public rental is absent from that source (§4.8), so it is absent from the gap as well. Adding the 6,121 units that the metadata does not carry — their unit types taken from LH and GH recruitment notices, with unit types confirmed by notice for all 6,121, of which 5,738 are under 60m² — raises total stock to 28,489 and moves the gap substantially (Table 4).

<br>**Table 4. Gap by population of stock (baseline anchor, m̄=3.23)**

| Unit type | Private for-sale stock (22,368) | Total stock incl. public rental (28,489) | Difference |
|---|---:|---:|---:|
| Small <60m² | 30.1% → **+5.2** | 44.4% → **+19.5** | +14.3 |
| Standard 60–85m² | 59.0% → **+7.3** | 47.0% → **−4.7** | −12.0 |
| Large ≥85m² | 11.0% → −12.4 | 8.6% → −14.8 | −2.4 |
| 1–2 bedrooms | 7.0% → **−20.4** | 25.7% → **−1.7** | +18.7 |
| 3 bedrooms | 78.4% → **+24.3** | 62.9% → **+8.8** | −15.5 |
| 4+ bedrooms | 14.6% → −4.0 | 11.5% → −7.1 | −3.1 |

<sub>Source: author's calculation. Public-rental unit types are taken from LH and GH recruitment notices — LH Complex 2: 16.33/21.2/26.23/36.26m²; LH Complex 15: 383 national rental units at 29–46m², 798 permanent rental units at 26.25m², including 114 senior welfare units; LH Complex 12: 26/36/44m²; Gyeonggi Happy Housing: 18.57–44.81m²; LH Complex 17: types 16A–36A; LH Complex 35: 29.43–46.49m². **All 6,121 units are confirmed by notice.** Centreville NHF 3 (383 units) spans 51–84m²: the notice lists 248 units by construction count (51.27m² 30; 59.80m² 15; 74.79m² 45; 84.25m² 20; 84.73m² 80; 84.75m² 58), and the 135-unit remainder against the complex total of 383 is the 59.93m² type omitted from that notice — a reading corroborated by lease transactions, where the same type accounts for 35.1% of records against a 35.2% share of units. The resulting split is 180 small units (47.0%) and 203 standard-size (53.0%). The 1,200 rental units inside mixed complexes are already contained in the 22,368 and are not added again.</sub>

The two columns say different things, and both are true. Small and one- to two-bedroom units are not missing from Godeok: **they exist, and once public rental is counted the 1–2 bedroom shortage all but disappears (−20.4 → −1.7pp)**. But they exist only inside stock that is allocated by eligibility screening rather than bought on the market. For a household that does not qualify — a worker at a large establishment, a single earner outside the priority categories — the relevant column is the first one, where 1–2 bedroom units are 7.0% of what can be purchased. The 18.7pp difference between the two columns is the size of the small-unit stock that exists but is rationed, and that is precisely the mechanism §4.8 goes on to examine. Because of this, the gaps in Table 3 should be read as **the composition of what the market supplies**, not of what physically stands in Godeok.

**(3) Interpretation — the mismatch takes a different form on each axis.** Viewing the re-estimated results in distributional form (Figure 3) shows two structurally different mismatches.

- **Room-count axis = a barbell.** Demand is 27.3% for 1–2 bedrooms, 54.1% for three, and 18.6% for 4+, whereas supply is 7.0%, 78.4%, and 14.6%. The **middle (three bedrooms) is oversupplied by 24.3pp while both ends are short** (1–2 bedrooms −20.3pp, 4+ bedrooms −4.0pp). Two distinct segments — young one- and two-person households before children, and households with children — are each unmet, and the single three-bedroom template corresponds precisely to neither. **This sign holds across the entire <i>m̄</i> band and all mapping variations.**
- **Floor-area axis = one-directional "large units short."** The demand distribution on the area axis is not bimodal but a **single peak shifted toward families** (mode near 80m²), and the shortage appears in one direction only, large units (≥85m²) at −9.5 to −15.5pp. Small units are in surplus. **The term "barbell" must therefore be confined to the room-count axis.** The sign on the area axis is conditional on the <i>m̄</i> assumption (§5.4-(2)).
- **Extremity on the supply side (measured).** Aggregating Godeok supply into exclusive-area unit groups gives **14 groups**, of which the single **84–85m² group holds 12,366 units (55.3%)**, and the **top three groups hold 84.8%** of the total (Figure 3-④). The deficit in unit-type diversity is far sharper in this concentration by unit group than in the band share (standard size 59.0%).

The prescription is therefore not the single-track "expand small units" but **"relax the single three-bedroom / standard-size template, with different remedies on each axis."**

**Fig.3. Demand recalibration and the resulting unit-composition mismatch**
![Figure3](../analysis/37_gap_consolidated.png)
<sub>Source: author's calculation (`analysis/37_gap_consolidated.py`). ① household-size distribution under the rejected city-wide parameters and the Godeok-specific corrected band; ② floor-area demand after correction (error bars = band across the three anchors) against supply; ③ the same contrast on the room-count axis; ④ Pareto chart of supply unit groups (bars = share, line = cumulative). Boxed values in ② and ③ are the gap (supply − demand). Unit groups in ④ aggregate measured units into 1m² buckets and then merge contiguous runs into practical unit groups.</sub>

### 4.5 Market segmentation — small-unit demand realized through leases

In Godeok the small-unit share of lease transactions (56–59%) exceeds that of sales (35–44%), and monthly rent accounts for **73.4%** of leases. Demand for small and mobile occupancy is thus realized not through owner-occupied new construction but through leases, and particularly monthly rent (Figure 4).

**Control-city check.** To determine whether this rent concentration is specific to Godeok or reflects a nationwide shift toward monthly rent, it was compared against control cities.

| Area | Jeonse | Monthly rent | Monthly-rent share |
|---|---|---|---|
| **Godeok** | 6,758 | 18,643 | **73.4%** |
| Pyeongtaek (all) | 74,363 | 81,967 | 52.4% |
| Anseong (control, no semiconductor) | 23,092 | 26,575 | 53.5% |

Godeok's monthly-rent share exceeds both the control city (Anseong, 53.5%) and Pyeongtaek as a whole (52.4%) by roughly 20pp. The concentration is therefore **local to Godeok rather than a nationwide trend**, and it is the empirical result that survives the re-estimation of §4.4 **most robustly**. Whether its cause is preference or marginalization is adjudicated in §4.8.

⚠️ Note that the area shares (small units 56–59%) are **transaction counts**, so fast-turnover small and monthly-rent units are over-sampled. The tenure axis was turnover-adjusted to stock (§4.7), but the corresponding correction on the area axis remains future work.

**Fig.4. Lease market: where small-unit demand is realized**
![Figure4](../analysis/10_rent_analysis.png)
<sub>Source: author's analysis based on MOLIT real transaction data.</sub>

### 4.6 The independent effect of spatial proximity — distance-to-campus hedonic

To partially separate whether Godeok's concentration stems from campus proximity or from the "new town" label, a hedonic regression was applied to Pyeongtaek transactions matched to complex coordinates (41,196 records, 58% match rate; Table 5).

<br>**Table 5. Hedonic regression on distance to campus**

| Variable | Coefficient (effect) | Significance |
|---|---|---|
| Distance to campus (km) | **−3.7%/km** | p<0.0001 |
| New-town dummy (Godeok, net premium) | +3.2% | p<0.0001 |
| Subsample excluding Godeok (n=37,281) | −3.7%/km | p<0.0001 |

<sub>Source: author's calculation (`analysis/23_distance_hedonic.py`). Controls: ln(area), building age, year fixed effects; HC0 robust.</sub>

Most of the price premium comes from continuous distance to the campus (−3.7%/km) rather than from the discrete new-town label (+3.2%) (Figure 5). The −3.7%/km gradient persists even in a subsample containing no new town at all, so the proximity effect is independent rather than a product of the new town. It is robust to relocating the campus reference point to the main gate, P2, or the centroid (−2.5 to −3.7%/km). This suggests that the unit of supply planning should be **commuting accessibility from the employment anchor**, not the administrative boundary of a new town.

**Fig.5. Continuous distance-to-campus hedonic — separating proximity from the new town**
![Figure5](../analysis/23_distance_hedonic.png)
<sub>Source: author's calculation.</sub>

### 4.7 The age-inflow design model and the annual roadmap

**(1) Applying the chain.** The gap diagnosis is generalized into a predictive chain of "age inflow → household formation → design of unit size, room count, and tenure" (model equations in §3.3-3). Household heads aged 25–39 are 51.4% one-person and 72.9% one- or two-person households (against 37.1% one-person across all ages; DT_1JC1511), so the younger the head, the more overwhelmingly small the household. Substituting this measured conditional distribution and headship (0.17 at ages 20–24 rising to 0.57 at 40+) into the chain and applying it to the Godeok inflow (2018→2025), the uncorrected chain uses city-wide parameters (<i>ρ<sub>a</sub></i>, <i>P</i>(<i>h</i>|<i>a</i>)) and overstates single-person households at 39.3%, with a distributional mean of only 2.22 persons. After Godeok-specific correction (baseline <i>m̄</i>=3.23) the single-person share is **16.1%** and the distributional mean is 3.23, consistent with observation; the gaps are those in the baseline column of Table 3. Tenure shifts under turnover adjustment to stock, from sale 10→31, jeonse 26→19, and monthly rent 64→50% (Figure A4); adding the Godeok-specific correction on top, the reduction in small households moves this further to **sale 35, jeonse 22, and monthly rent 43%**. The before/after comparison is given in Table A4.

**(2) Validation — transferability and the time axis.** Predicting household sizes in other cities with parameters calibrated on Pyeongtaek yields **MAPE of 0.8% for Pyeongtaek itself, 6.0% for Anseong, and 11.0% for Hwaseong**, so the chain captures the regional structure while local differences between cities remain (Table A2). On the time axis, a logistic specification pinned to the planned carrying population (<i>K</i><sub>pop</sub>=144,173) **over-predicted consistently at every origin** in a rolling-origin backcast and was rejected at a mean MAPE of 33.8%, while a **linear model based on the most recent three-year slope was adopted at MAPE 5.6%** (Table A3, Figure A5). The cause is extrapolation of the slope of the early rapid-growth phase as a saturation rate. (Godeok's development has run past its original 2008–2022 planning horizon; the 2025 figure of 53.6% of planned population agrees with an independently reported project progress rate of about 52%.)

**(3) Annual prescription.** Using the adopted model (linear, clipped at the <i>K</i><sub>pop</sub> ceiling) to derive annual net inflow, and applying the measured inflow age profile and Godeok-specific household formation (baseline <i>m̄</i>=3.23), gives Table 6 and Figure 6. Scenario bands are shown in Figure 6.

<br>**Table 6. Annual new-household requirements by unit type (baseline scenario, m̄=3.23)**

| Year | Net inflow | New households | Small (≈60m²) | Standard (≈83m²) | Large (≈103m²+) | 1–2 rooms | 3 rooms | 4+ rooms | Monthly-rent volume |
|---|---|---|---|---|---|---|---|---|---|
| 2026 | 10,958 | 3,392 | 845 | 1,749 | 799 | 927 | 1,832 | 633 | 1,446 |
| 2027–2031 | 10,958 each | 3,392 each | 845 each | 1,749 each | 799 each | 927 each | 1,832 each | 633 each | 1,446 each |
| 2032 | 1,091 | 338 | 84 | 174 | 80 | 92 | 182 | 63 | 144 |
| 2033–2035 | 0 (saturated) | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| **10-year cumulative** | **66,836** | **20,692** | **5,151** | **10,666** | **4,875** | — | — | — | — |

<sub>Source: author's calculation (`analysis/33_annual_design_roadmap.py`). Scenario band for cumulative new households: 22,353 conservative / 20,692 baseline / 19,317 upper.</sub>

**(4) Comparison with planned volume.** Against the roughly **35,932 units remaining** after subtracting the 22,368 already supplied from Godeok's planned total of 58,300, population-based cumulative demand over ten years is **20,692 units (58% of the remainder)**. Population trends alone therefore cannot absorb the planned volume, and **the planned remainder exceeds population-based demand** — a risk of **aggregate oversupply** distinct from the question of unit mix. (⚠️ Planned units cover all housing types while measured supply covers apartment complexes, so the populations differ and the figure should be read as an upper approximation.)

**(5) Stability over the planning horizon — the corrected trajectory.** A continued-inflow scenario (A) was compared against a cohort-maturation scenario (B: children growing up and ageing, shifting the age profile by one five-year band) with the Godeok-specific correction applied. The correction parameter <i>λ</i> was **determined once by anchoring the observation year (A) to the <i>m̄</i> band and then applied unchanged to B** — the bias that <i>ρ</i> and <i>P</i>(<i>h</i>|<i>a</i>) are city-wide parameters is a **structural** bias that persists when the age profile shifts, so holding the correction parameter fixed is correct and B's mean household size must be allowed to move as a result (re-imposing <i>m̄</i> on B would by definition erase the effect of cohort maturation). The results are in Table 6.

<br>**Table 7. Planning-horizon trajectory (2025 → 2035) after Godeok-specific recalibration, baseline anchor m̄=3.23**

| Indicator | 2025 (A, inflow continues) | 2035 (B, cohort maturation) | Reference: uncorrected |
|---|---|---|---|
| Mean household size | 3.23 | 3.36 | 2.22 → 2.35 |
| Single-person share | 16.0% | 12.9% | 39.3 → 34.2% |
| 1–2-room demand | 27.2% | 24.2% | 52 → 48% |
| Monthly-rent demand (stock-adjusted) | 42.9% | 42.0% | 50 → 49% |
| **1–2-room gap** | **−20.2pp** | **−17.2pp** | −44.8pp |
| **3-room gap** | **+24.3pp** | **+22.6pp** | +38.0pp |
| Large-unit gap | −12.5pp | −14.1pp | +0.2pp |

<sub>Source: author's calculation (`analysis/36_forecast_design_recalibrated.py`). The corrected 2025 (A) values reproduce the baseline column of Table 3 in §4.4 (single-person share 16.1%, small +5.2, 1–2 rooms −20.4, 3 rooms +24.3), cross-confirming the consistency of the chain and the re-estimate.</sub>

As the cohort matures, the single-person share (16.0→12.9%), 1–2-room demand (27.2→24.2%), and monthly-rent demand (42.9→42.0%) decline slightly while demand for family-sized units rises. **The signs nonetheless hold throughout the planning horizon**: across all three anchors, 2035 still shows a three-room surplus of +21.3 to +24.6pp, a 1–2-room shortage of −22.0 to −13.0pp, a large-unit shortage of −17.0 to −11.1pp, and a small-unit surplus of +3.7 to +12.0pp. The **unit-diversification conclusion therefore holds within the planning horizon (2030/2035), with the weight of the room-axis prescription shifting somewhat from 1–2 rooms toward large and 4+-room units as the cohort matures.** This recomputes a trajectory that through earlier drafts had been presented only with uncorrected parameters, leaving its level inconsistent with §4.4.

**(6) Practical use.** The chain is implemented in the companion tool [`design_simulator.html`](design_simulator.html), which recomputes the area-demand distribution curve, household-size composition, annual unit requirements, and design recommendations as inflow by age band, inflow scale, decay rate, and mean household size are adjusted. How results move as the inflow profile changes is summarized in Table A5. Lowering mean household size to 2.18 (Pyeongtaek as a whole) in the direct-entry mode reproduces the first pass's "small units short" conclusion, so a developer can see directly **how parameter choice changes the conclusion**.

**Fig.6. Annual design roadmap — required units by size and scenario band**
![Figure6](../analysis/33_annual_design_roadmap.png)
<sub>Source: author's calculation (`analysis/33_annual_design_roadmap.py`, `27_forecast_design.py`).</sub>

⚠️ **Limitation**: the linear model reaches the planned population in 2032, after which net inflow and therefore new demand are computed as zero. In reality demand continues after saturation through household fission (children leaving home, divorce), so values after 2032 should be read as a **lower bound on inflow-based demand**. Annual inflow is also fixed at the recent three-year slope, so any change to campus expansion schedules (P4, P5) requires re-estimation.

---

### 4.8 Who gets left out — price barriers and path divergence

§4.4 showed that supply composition diverges from household structure, and §4.5 that suppressed demand for small units and low room counts is realized through leases rather than sales (73.4% monthly rent). Why the detour occurs remains open. Two explanations compete. **(a) Preference** — young workers are highly mobile and choose monthly rent voluntarily. **(b) Exclusion** — the entry price of ownership is unaffordable relative to income, so they are pushed out. Since the two carry opposite policy implications (no intervention needed under the first, intervention required under the second), they must be adjudicated. This section does so with transaction-based access indicators.

**(1) The barrier to ownership.** In Godeok apartment sales for 2024–25, the median price of a standard-size unit (60–85m²) is **580 million KRW** (n=905). For three entry-level annual income scenarios (conservative 36M, middle 50M, high 60M KRW), the price-to-income ratio (PIR) and monthly payment (assuming LTV 70%, 4% interest, 30-year level payments) are given in Table 7.

<br>**Table 8. Entry barriers to ownership by unit type (Godeok, 2024–25 transactions)**

| Unit type | Median price | Equity (30%) | Monthly payment | PIR at 36M | PIR at 50M | PIR at 60M | n |
|---|---:|---:|---:|---:|---:|---:|---:|
| Small <60m² | 340M KRW | 102M | 1.14M | 9.4 | 6.8 | 5.7 | 557 |
| **Standard 60–85m²** | **580M KRW** | **174M** | **1.94M** | **16.1** | **11.6** | **9.7** | 905 |
| Large ≥85m² | 710M KRW | 213M | 2.37M | 19.7 | 14.2 | 11.8 | 95 |

<sub>Source: MOLIT real transaction prices (2024–2025), author's calculation. Prices are medians; PIR and monthly payments are computed under the stated assumptions.</sub>

Under the internationally used affordability standard (Demographia), a PIR at or above 5.1 is classified as "severely unaffordable." Godeok's standard-size unit is **16.1 under the conservative scenario, 3.2 times that threshold**, and **9.7 even under the high-income scenario (60M KRW), about twice the threshold**. Even on optimistic income assumptions, entry-level ownership of a standard-size unit does not hold.

**(2) Monthly housing cost — ownership impossible, affordable renting only in the public sector.** Comparing the monthly mortgage payment against the effective cost of renting (rent plus the jeonse-conversion equivalent of the deposit, at a 5.5% conversion rate) as a share of monthly income gives Table 8. **Rent must be read with public and private separated**: **81% of small-unit rent transactions (4,570 of 5,617) are public rental**, so the undivided median of 0.29M KRW is not a private market price.

<br>**Table 9. Monthly housing-cost burden — ownership vs. rent, public and private separated (% of monthly income)**

| Unit type | Monthly payment | Ownership burden<br>(36M/50M/60M) | Rent — **public** | Public burden | Rent — **private** | Private burden | Rent n |
|---|---:|---:|---:|---:|---:|---:|---:|
| Small <60m² | 1.14M | 38 / 27 / 23% | **0.24M** | **8 / 6 / 5%** | **0.89M** | **30 / 21 / 18%** | 5,617<br>(public 4,570, private 1,047) |
| **Standard 60–85m²** | **1.94M** | **65 / 47 / 39%** | (not separated) | — | **1.25M** | **42 / 30 / 25%** | 1,779 |
| Large ≥85m² | 2.37M | 79 / 57 / 47% | (not separated) | — | 1.26M<sup>†</sup> | 42 / 30 / 25% | 313 |

<sub>Source: MOLIT real transaction prices (2024–2025), deposits converted at 5.5%, author's calculation. The conventional affordability line is 30% of monthly income. Internal decomposition of the 0.24M public figure: 0.27M for named complexes (n=3,460) and an estimated 0.21M for numbered complexes (n=1,110). <sup>†</sup>Standard and large units were not separated by sector because of small samples, so these are **mixed values**; given that public volume is concentrated in small units (16–44m²), the true private figures may be higher.</sub>

Applying the conventional threshold that classifies housing costs above 30% of income as "cost-burdened," **standard-size ownership exceeds the line under all three income scenarios** (39–65%). Moving to renting, **private small units sit right at the line at 30/21/18%**, and private standard-size units exceed it at 42/30/25%. The only option clearly inside the line is **public small-unit rental (5–8%)**. The gaps between ownership and renting, and between private and public, are too large to be explained by preference, and they support explanation **(b), marginalization**.

**(3) The tenure structure of supply — where affordable housing actually comes from.** For exclusion to be a policy problem, those pushed out must have somewhere to settle. Answering that requires more than one source. The complex metadata used for the unit-composition analysis (NAVER Real Estate) covers the sale and resale market and does not list public rental complexes; "Pyeongtaek Godeok Gyeonggi Happy Housing" does not appear even in a nationwide search. Read alone, that source shows 2,249 rental units (9.4%) and no LH supply at all. Yet in MOLIT lease transactions, public rental complexes account for 49.3% of Godeok's 10,190 records. The stock was there; the source was not. We therefore merged the metadata with LH and GH tenant-recruitment notices and completion records.

<br>**Table 10. Public rental complexes in Godeok**

| Complex (block) | Units | Type | Source |
|---|---:|---|---|
| Godeok LH Complex 2 (A-6) | 1,600 | Happy Housing — students, newlyweds, vulnerable and low-income households; **job-linked, priority for SME employees** | LH recruitment notice |
| Godeok LH Complex 15 (A-58) | 1,295 | National rental, permanent rental, senior welfare housing | completion records |
| Godeok LH Complex 12 (A57-1) | 900 | Happy Housing (26/36/44m²) | LH recruitment notice |
| Godeok Seojeongni Station Gyeonggi Happy Housing (A-62) | 800 | Happy Housing — students, young adults, early-career workers, newlyweds, seniors, housing-benefit recipients | **GH recruitment notice (primary)** |
| Godeok LH Complex 17 (blocks Ca1, Ca2) | 594 | Happy Housing | **LH recruitment notice (primary)** |
| Godeok LH Complex 35 (A-2) | 549 | National and permanent rental | completion records |
| Godeok Centreville NHF 3 (A-1) | 383 | 10-year public rental REIT | complex records (occupied 2021.07) |
| **Subtotal — wholly rental complexes** | **6,131** | | |
| Godeok Dahaeve (A-53) | 389 / 1,167 | Newlywed Hope Town + Happy Housing | LH notice (778 for sale + 389 Happy Housing) |
| Shindonga Pamilie NHF 7 (A-10) | 609 / 719 | 10-year public rental REIT | metadata rental units |
| Godeok Le Florent (A-7) | 295 / 891 | Newlywed Hope Town + Happy Housing | metadata rental units |
| Godeok Hestible (A-3) | 167 / 496 | Newlywed Hope Town + Happy Housing | metadata rental units |
| Godeok Yangwoo Naeanae (A57-2) | 129 / 385 | Newlywed Hope Town + Happy Housing | metadata rental units |
| **Subtotal — rental within mixed complexes** | **1,589** | | |
| Godeok Social Rental Housing, phase 1 | 5 | social rental (multi-household) | building register (completed 2021.01) |
| Godeok Social Rental Housing, phase 3 | 5 | social rental (multi-household) | building register (completed 2022.05) |
| **Public rental total** | **7,720** | | |

<sub>Source: LH Cheongyak Plus and MyHome notices, GH recruitment notices, completion records, and complex metadata `lease_households`. The last four complexes mix for-sale (Newlywed Hope Town) and rental units, so only the rental portion is counted; the rental share sitting near 33% in three of them suggests an allocation attached to land-supply conditions.</sub>

<br>**Table 11. Tenure composition of Godeok's apartment stock**

| Category | Units | Share | Source |
|---|---:|---:|---|
| Private, for sale | 21,708 | 72.1% | complex metadata |
| Private rental | 660 | 2.2% | metadata `lease_households` (Eulim Square) |
| **Public rental (LH, GH)** | **7,720** | **25.7%** | notices and completions plus metadata |
| **Rental total** | **8,380** | **27.9%** | |
| Total | 30,088 | 100.0% | |

<sub>Source: authors' aggregation. The nine public rental complexes absent from the metadata (6,131 units) were added to the denominator as well.</sub>

**(3-1) Eligibility closes the door the price opened.** Affordability and access are not the same thing. Public rental is cheap, but it is allocated against income and asset ceilings, and those ceilings are set against the urban-worker average — not against what a semiconductor cluster pays. Table 11 places this study's income scenarios against the ceilings in force.

<br>**Table 11. Income ceilings for public rental against the study's income scenarios (annual, KRW)**

| Programme | 1-person | 2-person | 3-person | Units in Godeok |
|---|---:|---:|---:|---:|
| Permanent and national rental (90 / 80 / 70% of urban-worker mean) | 41.18M | 56.32M | 68.61M | 1,730 |
| Happy Housing, youth category (100%) | 45.76M | 70.40M | 98.02M | 3,894 |
| **Study scenario — conservative 36M** | eligible | eligible | eligible | |
| **Study scenario — middle 50M** | **ineligible** | eligible | eligible | |
| **Study scenario — high 60M** | **ineligible** | **ineligible (perm./nat.)** | eligible | |

<sub>Source: LH eligibility rules, 2025 urban-worker mean monthly income by household size (1-person 3,813,363 KRW; 2-person 5,866,270; 3-person 8,168,429). Asset ceilings also apply: 251M KRW total assets for the youth category, 345M for national rental, and 45.42M for a vehicle.</sub>

The pattern is plain. A single earner on 50 million KRW — the middle of the three scenarios, and an ordinary starting salary at a large semiconductor employer — is **over the ceiling for permanent rental, national rental and the youth category of Happy Housing alike**. Only by forming a two- or three-person household does eligibility return. Programmes designed around the urban-worker average therefore exclude precisely the population a cluster brings in: young, single, and paid above that average.

Eligibility is also written around household formation, and that is the second filter. Public rental allocates its larger units to married applicants: in the Gyeonggi Happy Housing notice, of the 776 units listed by category, **366 (47.2%) are reserved for newlyweds** against 274 (35.3%) for young single applicants, and the largest unit type in the complex — 44.81m², 274 units — is entirely newlywed. Add the 980 units in Newlywed Hope Town projects (Dahaeve, Le Florent, Hestible, Yangwoo Naeanae), where marriage or imminent marriage is presupposed, and the pattern is unmistakable.

The income ceiling bends the same way. A single applicant faces 41.18M KRW for permanent and national rental against 56.32M for a two-person household, and 45.76M against 70.40M for Happy Housing — **a rise of 37% and 54% simply on marrying**. The same person, on the same salary, is ineligible alone and eligible once married.

The two filters compound. A young worker before marriage is caught by both: fewer units are open to them, and the income line they must clear is the lowest of any household size. None of this is an accident of administration — priority for newlyweds and low-income households follows from birth-rate and housing-welfare objectives, and those are legitimate aims. The point is narrower: **a design built around household formation does not fit a site type whose defining feature is an inflow of young, unmarried, above-average earners.** The instrument is sound; the match between instrument and place is not.

Two further filters narrow it again. The largest complex, LH Complex 2 with 1,600 units, gives priority to employees of small and medium enterprises, which reverses the position of workers at the anchor tenant itself. And permanent rental with its 26.25m² units (798 of them, including 114 senior welfare units) is aimed at the lowest income bracket and at older residents, a population the cluster does not generate at all.

Read together with §4.4, this closes the argument. The 18.7pp of small-unit stock that appears once public rental is counted is not stock this population can enter. **Ownership is closed by price (PIR 16.1), private tenancy sits at or beyond the affordability line (18–30% of income), and public rental — the only affordable option at 5–8% — is closed by eligibility.** All three doors are shut for the same household at the same time, and what remains is short-term private rent.

Public rental is not absent; it is substantial. At 25.7% it far exceeds the city-wide rental share, and its rents are affordable (0.24M KRW for small units, 5–8% of income). Two things nonetheless constrain it. The first is volume: 25.7% is not generous relative to the scale of in-migration, and no such price point exists anywhere in the remaining stock. The second is targeting. The largest complex, LH Complex 2 with 1,600 units, is job-linked and gives priority to SME employees, so workers at large establishments and other young households rank lower. The composition of the inflow the cluster generates and the eligibility rules of public rental are not aligned.

One further caution: judging the supplier by the builder's name misreads the situation. Le Florent, Hestible, Yangwoo Naeanae and Dahaeve were built by Hanshin, Jinheung, Yangwoo and Daeheung respectively, but they are LH projects mixing Newlywed Hope Town units with Happy Housing, and Shindonga Pamilie NHF 7 and Centreville NHF 3 are public rental REITs. Being built by a private contractor is not the same as being supplied privately.

**(4) Why rent concentration is nonetheless observed.** Even with 7,720 public-rental units, realized tenure is 73.4% monthly rent (§4.5). The two facts are not contradictory because public rental is limited **both in volume and in eligibility**. The confirmed 25.7% is small relative to the scale of inflow, and eligibility is restricted — LH Complex 2 (1,600 units), for instance, is **job-linked with priority for SME workers**, so workers at large-enterprise sites and other young households fall down the priority order. The problem is therefore not "an absence of policy instruments" but that **the scale and target of those instruments are not designed around the inflow structure the cluster generates**.

**(5) Where the problem lies — not missing instruments but their scale, target, and attached conditions.** Korea has housing-access instruments in law — Happy House, national rental housing, publicly supported private rental — and they **are in fact operating** in Godeok (Table 10). The problem is therefore not their absence but two things: **(i) public volume is small relative to the inflow and its eligibility does not match the cluster's employment structure, and (ii) no access condition attaches to private supply (76% of stock)**. The second is the crux. Where private developers supply most of the stock and none of that volume has an affordable price point, expanding public rental improves access only **in proportion to its own share**. Because Godeok is a structure in which the public sector prepared the land and private developers supplied 76% of the stock, the public sector effectively loses any lever over unit type, tenure, or price point beyond its own supply once the land is transferred. That is why the point of intervention must be **the conditions of land supply** (§5.3).

**(6) Formalizing the marginalization mechanism.** Taken together, marginalization operates in three stages.

> **① Design stage** — private supply is standardized into a single three-bedroom, standard-size template (three bedrooms 78.4%; 55.3% in one 84–85m² group; §4.3).
> **② Price stage** — the price of that standard type (580M KRW; PIR 16.1; mortgage burden 65%) exceeds the ownership entry line for entry-level incomes, and private renting likewise sits at or above the affordability line (0.89M for small, 1.25M for standard units).
> **③ Path-divergence stage** — the only affordable path is public rental (5–8%). Households that enter it settle stably, but because of limited volume (25.7%) and restricted eligibility (SME-worker priority and the like), **those who do not enter remain in short-term private monthly rent**. The 73.4% monthly-rent share in realized tenure is the outcome of this divergence.

Figure 7 brings the chain together in three panels: PIR, burden ratios, and the inversion of tenure. Its implication is that unit diversification is not a matter of aesthetics or market efficiency but **a question of who can settle in this city**. Alternatives do exist — but **only in the public sector, while the private sector supplies no accessible price point at all**. If the gap of §4.4 is the language of planning, the access indicators of this section are **what that gap becomes when it reaches people**.

<br>**Fig.7. Housing access — why young workers are pushed into monthly rent**
![Figure7](../analysis/35_affordability.png)
<sub>Source: MOLIT real transaction prices (2024–2025), NAVER Real Estate complex metadata, LH announcements; author's calculation. ① PIR against the international affordability threshold; ② mortgage payments vs. rent against the 30%-of-income line; ③ the inversion between planned tenure (97.0% for sale) and realized tenure (73.4% monthly rent).</sub>

⚠️ **Assumptions and limitations**: incomes are scenarios rather than measured values (no income data exist for Godeok's resident households); ownership burden assumes LTV 70%, 4% interest, and 30-year level payments; effective rent assumes a 5.5% jeonse conversion rate. Public-rental complexes are identified from transaction complex names and therefore carry the limitation of nominal classification, and the programme type and eligibility of the 2,249 private rental units are unconfirmed. The figures in Tables 7 and 7 should accordingly be read as indicating **the size of the gaps** between ownership and renting, and between public and private, rather than exact burden amounts. Those gaps are nonetheless too large to be reversed by varying the assumptions (the standard-size ownership burden exceeds the 30% line even under a relaxed 3% interest, 80% LTV assumption).

---

## 5. Conclusion

### 5.1 Discussion

This study read the mark left by Samsung's Pyeongtaek campus on the surrounding housing market through the case of Godeok New Town, asking whether the housing built there fits the household composition of the people who actually moved in and, where it does not, who carries the cost.

Growth concentrated on a single point within Pyeongtaek: the development share rose from 1% to 73% and the price ratio from 0.96 to 2.49 (§4.1). Those who moved in were working-age adults aged 25–39 together with their young children (§4.2). The housing built for them, however, followed the standard-size, three-bedroom template (§4.3), and it diverged from the demand implied by observed household sizes (§4.4).

The divergence takes a different shape on each axis, and we can be more confident about one than the other. On the room-count axis, three-bedroom units are in surplus by 22.6–26.6pp while one- and two-room units fall short by 15.7–25.4pp and four-plus rooms by 1.2–6.9pp — a barbell whose direction holds across the whole household-size band and every mapping variant we tried. On the floor-area axis, large units fall short by 9.5–15.5pp and small units appear in surplus by 0.6–9.5pp, but that sign flips if the assumed average household size changes. Suppressed demand for small room counts was being met not through purchase but through leases, and above all through monthly rent at 73.4% (§4.5). The explanation that the demand simply never existed does not sit with that.

Decomposing the price premium shows distance to the campus (−3.7%/km) mattering far more than new-town status itself, whose dummy effect is only 3.2% (§4.6). That runs against the familiar assumption that the new-town label creates value, and it suggests planning at the scale of commuting distance from the employment anchor rather than the administrative boundary.

The consequences of the mismatch did not stay inside the statistics (§4.8). Buying a standard-size unit takes 16.1 times annual income, with mortgage payments consuming 65% of it. Turning to tenancy does not help much: private small units cost 0.89M KRW (30/21/18% of income) and private standard-size units 1.25M (42/30/25%), at or beyond the affordability line. The only option that clearly sits inside it is small public rental units, at 5–8%. Public rental is far from negligible — 7,720 units, 25.7% of the stock — but the remaining 76% contains no such price point, and the largest complex gives priority to SME employees. The observed 73.4% monthly-rent share is therefore not the market sorting itself out but the outcome of whether a household pushed out of ownership managed to enter public rental. Those who did settle; those who did not remain in short-term private rentals. This is not a story about an inefficient unit mix but about who gets to stay in this city.

That reframes what housing vulnerability means here. In policy it is normally read off income: those on housing benefit, in *jjokbang* rooms or below the minimum housing standard. The households this study traces are not poor by that measure. They earn around the urban-worker average or above it, and that is precisely why public programmes do not reach them — the ceilings for permanent rental, national rental and Happy Housing all sit below a single earner on 50 million KRW. Nor does the market reach them, because it supplies nothing they can afford at that income. **Vulnerability here is not a function of income but of eligibility: of whether any route to affordable housing is open at all.** Measured that way, a young single worker at a semiconductor cluster is housing-vulnerable while earning above the median — a combination the existing categories do not have a name for.

That is the answer to the fourth question — whether public housing support reaches them. It does not, and the reason is structural rather than local. Public programmes are designed around household formation and the urban-worker average because they were built for a population defined by low income and family formation. A semiconductor cluster produces the opposite profile — young, unmarried, paid above average, arriving in numbers over a short period. The instruments are not defective; they were simply not written for this place. And because clusters of this kind will keep being built, so will the blind spot, unless allocation is set at the planning stage against the inflow the cluster actually generates.

Employment-anchor development produces a demand structure the standard new-town template does not capture. That structure, though, was not the "young small households" we first assumed but young families at its core with young one- and two-person households alongside them. We built the chain running from age-specific in-migration through household formation to unit size, room count and tenure, checked it in both directions — transfer to other cities (MAPE 0.8–11.0%) and backcasting over time (MAPE 5.6%) — and added an annual design roadmap (§4.7) and a calculation tool so the diagnosis can be used in practice.

A word on the evidence this rests on. Everything here comes from primary data released by public agencies and from market records. From MOLIT real transaction prices we used 253,255 sale records and 156,330 lease records covering 2015–2025, of which 26,710 are in Godeok. Population and household figures are taken directly from Statistics Korea's KOSIS tables — five-year age groups (2011–2025), households by size, and household size by head's age. Public rental volumes and rent terms come from LH and GH tenant-recruitment notices. One thing those sources cannot supply: national statistics do not record how many rooms a dwelling has or its exclusive floor area. A study about unit composition cannot start without that. We therefore used the real-estate service run by Naver — the internet portal most widely used in Korea — which publishes complex-level detail in JSON form; collecting and normalising it gave 6,244 complexes and 29,014 unit-type records nationwide (319 in Pyeongtaek, 29 in Godeok). Room counts, floor areas, unit counts, rental-unit counts and coordinates come from there. Joining the two families of data is what made it possible to place demand inferred from population structure and the housing actually built on the same axis. The weakness of that combination is equally clear: market data contain only what reaches the market. Missing public rental entirely was the proof of it (§5.2).

### 5.2 Critical review — the study's own corrections

To avoid settling too early we worked through a fixed order: state the claim, triangulate, question the assumptions, take the counterargument seriously, separate what was observed from what was inferred, and only then draw a provisional conclusion. Triangulation had three independent sources pointing the same way — population (25–39 dominant), supply (78.4% three-bedroom) and tenure (73.4% monthly rent, 20pp above the control city). Along the way we corrected our own conclusions four times.

First, we substituted Pyeongtaek's city-wide single-person share of 37.5% for Godeok demand and wrote that small units were in short supply. But Godeok is a family town whose child share is 1.9 times the national figure, and the distribution built from those parameters had a mean 1.2 persons away from the observed value — an internal contradiction. We reversed the sign on the floor-area axis (§4.4).

Second, we classified rental units by whether the word "rental" appeared in the complex name and reported 3.0%. The real figure was 9.4%: most rental units sit in mixed complexes whose names say nothing about it. The same habit had crept into how we selected the area, so we replaced name matching with a legal-dong criterion — "Godeok City" in Icheung-dong was being pulled in while Taepyeong and Yeonghwa Blenheim, recorded as "Godeok-myeon Gung-ri", were being left out (26 false positives, 126 omissions).

Third, working from the complex metadata alone we wrote that Godeok had no LH public rental, without establishing that a sale-oriented source does not carry public rental in the first place. Transactions showed public rental at 49.3%. The derived error was worse: the 0.29M KRW small-unit rent we offered as evidence of affordability was a blend in which public rental made up 81%, so we had effectively read a public rent as a private-market one.

Fourth, even the public-rental total we then found was initially put at 7,720 units; confirming Gyeonggi Happy Housing at 800 units (from the recruitment notice itself), LH Complex 17 phase 2 and Centreville NHF 3 raised it to 7,720. That also forced a correction to how supply was attributed: 1,200 units counted as private rental because a private contractor had built them were in fact LH supply — mixed Newlywed Hope Town and Happy Housing projects, and public rental REITs. The finding that 25.7% of the stock is public rental came out of that.

Three lessons follow. First, do not substitute broad regional averages into a specific local case; the same bias appeared in the population forecast, where a logistic model overextrapolated the early growth phase, and in both cases it surfaced only in ex-post checks (§4.7-(2)). Second, do not use a nominal label as a stand-in for a measured field. Third, distinguish what is missing from a source from what is missing from the world; sources built around markets omit the public sector systematically.

### 5.3 Policy and design recommendations

- **First priority — relax the three-bedroom / standard-size monoculture**: the re-estimate puts the three-bedroom gap at +22.6 to +26.6pp and the standard-size gap at +6.2 to +9.1pp, **a surplus under every scenario**, while on the continuous area axis **55.3% sits in a single 84–85m² group**. Reducing the share of that single template is the starting point, and it simultaneously **eases both the barbell shortage on the room axis and the large-unit shortage on the area axis**. Expanding large units (≥85m², 4+ rooms) is consistent with a 19.4% child share and a mean household size of 3.0–3.5, but it is conditional on the mean-household-size assumption and must be re-confirmed by site-level surveys of resident households.
- **Expand 1–2-room units — securing an enterable unit type**: the room-count gap of −15.7 to −25.4pp is a shortage under all parameters and mappings, yet supply for young one- and two-person households (72.9% of heads aged 25–39) is only 7.0%. This is not mere mix adjustment but **the creation of the one unit type open to income groups that cannot clear the ownership entry line**. The small-unit median of 340M KRW (PIR 9.4/6.8/5.7) is also high, but entry prospects differ materially from the standard size (16.1/11.6/9.7).
- **Redesign the scale and target of public rental — a question of allocation, not existence**: public rental exists and its rents are affordable (small units 0.24M, 5–8% of income), but the volume falls short of the inflow and eligibility is restricted (LH Complex 2's 1,600 units give priority to SME workers, pushing large-enterprise workers and other young households down the order). The plan presumes ownership at 97.0% for sale, while realized tenure is 73.4% monthly rent. **Target redesign and volume expansion** reflecting the cluster's employment structure (age, employer size) are needed, and public rental and private long-term rental volumes should be specified in the plan **as a separate total from for-sale units**.
- **Attach access conditions to private supply — the largest gap**: of 22,757 private units, essentially none are affordable (private small-unit rent 0.89M = 30/21/18% of income). Expanding public rental improves access only in proportion to its share, so **unless an access condition attaches to private supply — 76% of the stock — the structure will not change.** Because Godeok is a structure in which the public sector prepared the land and private developers supplied most of the housing, the only lever the public sector effectively retains is **the conditions of land supply**. We therefore propose a government (land, tax) – employer (employment scale and age structure information) – builder (supply execution) partnership that **specifies volumes, unit types, and rent ceilings targeted at young and newly married households as conditions of land supply** at the planning stage. Conditions attached at the planning stage are more effective than ex post regulation because neither unit type nor price point can be reversed once construction is complete.
- **A housing ladder, and pre-emptive application to later clusters**: the path from public small-unit rental (5–8%) through private small and mid-size rental (30/21/18%) to ownership (PIR 16.1) is broken, because the gaps between rungs are too large to climb. Placing rental and small for-sale units in the middle price range (near the 30% line) to design **a path along which households can move through the life cycle within one city** is a task above adjusting the volume of individual unit types, and it is the condition for converting an inflow population into a settled one. Since semiconductor clusters will continue to be built in Korea, Godeok's marginalization structure should be treated as **a pattern that reproduces itself**. Godeok, already under development, must rely mainly on ex post instruments, but later clusters such as Yongin **can allocate in advance at the planning stage**. There, **the local mean household size must be measured directly** (the central lesson of this study), and the unit-composition gap (§4.4) and access indicators (§4.8) should be **computed together** so that "who is marginalized" is established before the plan is finalized. Site-level monthly-rent shares and PIR are signals of **access failure** rather than market characteristics and should serve as monitoring indicators; and the **aggregate oversupply risk** implied by 20,692 units of ten-year cumulative demand against 35,932 planned remaining units (58%) should be examined alongside (§4.7-(4)).

### 5.4 Contributions and limitations

This study combines population, supply, and transaction data to diagnose unit-composition consistency, presents a predictive chain and practical tool deriving unit size, room count, tenure, and annual volumes from age inflow, and extends this into a housing-access diagnosis. Its limitations are as follows.

**(1) Endogeneity of treatment location** — the distance hedonic separates this only partially, since distance to the campus overlaps with accessibility to the urban core. The size and room mappings <i>M</i> are assumptions, and sensitivity analysis confirms only the robustness of direction (Figures A1, A3).

**(2) Mean household size <i>m̄</i> is an approximation** (population ÷ apartment units), since non-apartment residents and unoccupied or vacant units are not directly observed; it is therefore handled as a band of 2.99–3.46. **The floor-area conclusion (small-unit surplus, large-unit shortage) is conditional on that band**, whereas the room-count conclusion is not. The turnover adjustment was also not applied to the area distribution (only to the tenure axis).

**(3) Incomes in the access analysis (§4.8) are three scenarios rather than measurements**, and the income distribution, asset holdings, and prior-residence transitions of Godeok's actual resident households were not observed. Ownership burden depends on LTV 70%, 4% interest, and 30 years; effective rent on a 5.5% conversion rate. Access results should therefore be read as **the size and direction of gaps** rather than exact burden estimates. Standard-size and large-unit rents could not be separated by sector because of sample constraints.

**(4) The public-rental total and its supplier attribution are now established.** The 7,720 units in Table 10 were verified against LH and GH tenant-recruitment notices and the building register, and the supplier of every one of the 8,380 rental units is identified: private rental consists solely of Eulim Square's 660 units. What remains open is the internal split of LH Complexes 15 and 35 across national rental, permanent rental and senior welfare housing. Identifying public complexes from transaction-record names also rests on nominal classification (§5.2), but the complex metadata omits public rental so no alternative source was available.

**(5) The planning-horizon trajectory (§4.7-(5)) was computed with uncorrected parameters**, so its level is not consistent with §4.4 and it requires recomputation after correction. Annual projections depend on the recent three-year slope, so changes to campus expansion schedules require re-estimation, and post-saturation values are lower bounds.

**(6) Three populations coexist** — the unit-composition analysis uses the sum of units by unit type in the complex metadata (22,368), the private tenure analysis the sum of total units (23,957), and the stock recomputation (Table 11) the value merged with public-rental announcements (30,088) — so any cited ratio must be checked against its population. In particular the gaps in §4.3 and §4.4 are **on a private for-sale basis** and do not reflect public-rental unit types; given that public rental is concentrated in small units (16–44m²), small-unit supply is larger than tabulated here and **the small-unit surplus may widen somewhat**. Recomputing the gap with public-rental unit types included is the highest-priority next step.

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
