<!-- APPENDIX_v12_EN (2026-09-18): English counterpart of APPENDIX_v12.md, supplementary to MANUSCRIPT_v12_EN.md.
     Figures removed from the manuscript remain as PNGs and scripts under analysis/ (see A-7). -->

*This appendix is supplementary to [`MANUSCRIPT_v12_EN.md`](MANUSCRIPT_v12_EN.md). Its contents are not used directly in the main argument but are provided separately so that the symbol definitions, model validation, and sensitivity to assumptions can be reproduced and checked. To be attached as supplementary material at submission.*

<br>

# Appendix — Symbol System, Model Validation, and Sensitivity to Assumptions

**SEOYEON JEON**

---

## A-1. Entity and symbol system

All entities and symbols used in this study are defined uniformly in Table A1. Every equation and table in the manuscript, and the companion tool [`design_simulator.html`](design_simulator.html), share these definitions.

<br>**Table A1. Definition of entities and symbols**

| Symbol | Entity | Definition / unit | Character |
|---|---|---|---|
| `a` | age band | five-year bands (20–24 … 85+) or age group `g` | index |
| `h` | household size | 1, 2, 3, 4, 5+ persons | index |
| `s` | area band | small <60m² / standard 60–85m² / large ≥85m² | index |
| `r` | room band | 1–2 rooms / 3 rooms / 4+ rooms | index |
| `k` | tenure form | sale / jeonse / monthly rent | index |
| `t` | year | 2013 … 2035 | index |
| `n_a` | net inflow | net increase for age band `a` (persons) | **measured** (DT_1B04005N differences) |
| `ρ_a` | headship | household-head rate by age (dimensionless) | **measured** (DT_1JC1511 ÷ population) |
| `P(h|a)` | conditional household-size distribution | household-size distribution for head age `a` | **measured** (DT_1JC1511) |
| `m̄` | mean household size | observed Godeok anchor (persons per household) | **measured band** 2.99–3.46 |
| `q_h`, `p_h` | household-size distribution | before / after correction | derived |
| `M^A_(h,s)`, `M^R_(h,r)` | size and room mapping | household size → area and room propensity | **assumed** (sensitivity-tested) |
| `T_(s,k)` | tenure propensity | sale / jeonse / rent shares by area | **measured** (turnover-adjusted to stock) |
| `D^A_s`, `D^R_r`, `D^K_k` | demand | demand share (%) and units by area, rooms, tenure | derived |
| `S_s` | supply stock | composition of existing supply (units, %) | **measured** (complex metadata) |
| `G_s` | gap | `S_s − D^A_s` (negative = shortage, positive = surplus) | derived |
| `K_pop` | planned carrying population | 144,173 persons (ceiling clip in the forecast) | **published** (development plan) |

<sub>Source: KOSIS, MOLIT real transactions, NAVER complex metadata, Godeok International New Town development plan.</sub>

---

## A-2. Sensitivity to the unit-type mapping assumption

As stated in §III.3-1) of the manuscript, among the inputs to the chain, headship `ρ_a`, the conditional distribution `P(h|a)`, and tenure propensity `T_(s,k)` are measured, and **only the unit-type mapping `M` is assumed**. Whether varying `M` flips the sign of the gap therefore governs the robustness of the conclusions.

Varying `M` across three scenarios (strong small-unit preference, baseline, strong large-unit preference), **the 1–2-room shortage on the room axis retains its sign in every scenario** (−15.7 to −25.4pp). The **floor-area axis, by contrast, is sensitive to the mean-household-size assumption `m̄`**: under the first pass (m̄=2.18) small units are short by 5.8 to 33.2pp, whereas under the Godeok-specific re-estimate (m̄=2.99–3.46) they are in surplus by 0.6 to 9.5pp — a sign reversal. This is the basis for the statement in §V.2 that the room-axis conclusion is robust to parameter choice while the area-axis conclusion is conditional.

**Figure A1. Sensitivity of the gap to mapping assumptions**
![FigureA1](../analysis/21b_gap_sensitivity.png)
<sub>Source: author's calculation (`analysis/21b_gap_sensitivity.py`). ⚠️ This figure is on a first-pass basis (m̄=2.18), so its indication of a small-unit shortage pertains to the parameter set rejected in §IV.4-(1). It should be read only for **the relative magnitude of sensitivity** to mapping variation.</sub>

**Figure A3. Model sensitivity of the design chain**
![FigureA3](../analysis/24b_model_sensitivity.png)
<sub>Source: author's calculation (`analysis/24b_model_sensitivity.py`).</sub>

---

## A-3. The nationwide character of the unit-size trend — background check

This is the evidence behind the background check summarized in §IV.1 of the manuscript. Convergence on the standard size and the decline of small units appear equally or more strongly in Anseong and Gwangju (before any semiconductor investment), and adjusting for macro cycles (pandemic, interest rates) removes any Pyeongtaek-specific trend. This study therefore does not attribute the unit-size *trend* itself to a semiconductor effect; its focus is the **consistency between Godeok's local population structure and its supply composition**.

**Figure A2. Nationwide nature of the unit-size trend — macro-cycle adjusted**
![FigureA2](../analysis/08_macro_adjusted.png)
<sub>Source: author's calculation (`analysis/08_macro_adjusted.py`).</sub>

---

## A-4. Design model — before/after correction and the tenure turnover adjustment

<br>**Table A4. Design-model results for Godeok, before and after recalibration (Gap = supply − demand; negative = shortage)**

| Indicator | Before (city-wide parameters) | **After (Godeok-specific, baseline m̄=3.23)** |
|---|---|---|
| Single-person share of new inflow | 39.3% | **16.1%** |
| Mean household size of the distribution | 2.22 (1.2 persons from observation) | **3.23** (consistent with observation) |
| Small-unit area gap | −17.4pp shortage | **+5.2pp surplus** |
| Large-unit area gap | +0.2pp | **−12.5pp shortage** |
| **1–2-room gap** | −44.8pp | **−20.4pp shortage** (direction held) |
| Tenure (flow→stock adjusted) | sale 31 / jeonse 19 / rent **50%** | sale 35 / jeonse 22 / rent **43%** |

<sub>Source: author's calculation (`analysis/24_design_model.py`, `26_tenure_stock_adjust.py`, `32_godeok_recalibration.py`, `36_forecast_design_recalibrated.py`). The "before" column pertains to the **rejected parameter set** and is presented only for contrast with the re-estimate.</sub>

Two adjustments compound on the tenure axis. **First, the flow→stock adjustment** is required because transactions are **counts**, so fast-turnover monthly rentals are over-sampled (raw 64% → 50% stock-adjusted). **Second, the Godeok-specific correction** reduces the share of small households, shrinking small-unit demand and with it the rent propensity concentrated in small units, bringing monthly-rent demand down once more from 50% to **43%**. Even with both adjustments, monthly-rent demand remains in the low 40s — locally high relative to control cities, and not enough to overturn the unit-diversification or access conclusions.

**Figure A4. Tenure turnover adjustment — flow vs. stock**
![FigureA4](../analysis/26_tenure_stock_adjust.png)
<sub>Source: author's calculation (`analysis/26_tenure_stock_adjust.py`).</sub>

---

## A-5. Model validation — cross-city transfer and time-axis backcast

<br>**Table A2. Cross-city prediction error for household size (MAPE)**

| City | MAPE (%) | Interpretation |
|---|---|---|
| Pyeongtaek (self-consistency) | 0.8 | chain mechanically accurate |
| Anseong (similar control) | 6.0 | good transfer |
| Hwaseong (family-heavy new town) | 11.0 | small households over-predicted (local difference) |

<sub>Source: author's calculation (`analysis/25_model_validation.py`).</sub>

<br>**Table A3. Rolling-origin backcast comparison of population forecast models**

| Model | Mean MAPE (%) | Verdict |
|---|---|---|
| Logistic (K fixed) | 33.8 | rejected — consistent over-prediction |
| **Linear (recent three-year slope)** | **5.6** | **adopted** |
| Damped linear (φ=0.8) | 13.3 | runner-up |

<sub>Source: author's calculation (`analysis/31_backcast_validation.py`). Mean of prediction errors for subsequent years from origins 2021, 2022, and 2023 respectively.</sub>

The methodological significance of rejecting the logistic model matches the first lesson in §V.2. Pinning the saturation point to the planned carrying population extrapolates the slope of the early rapid-growth phase as a saturation rate, and **that bias did not surface without ex post validation (backcasting).**

**Figure A5. Backcast validation of the population forecast**
![FigureA5](../analysis/31_backcast_validation.png)
<sub>Source: author's calculation (`analysis/31_backcast_validation.py`).</sub>

---

## A-6. Inflow-profile sensitivity in the companion tool

The companion tool [`design_simulator.html`](design_simulator.html) referenced in §IV.7-(6) offers two modes for mean household size: ① an **auto-linked mode** that estimates it from age composition via headship and corrects for the measured Godeok bias (observed 3.23 ÷ estimated 2.48 = ×1.30), and ② a **direct-entry mode** for sensitivity checks. In auto-linked mode, changing the inflow profile moves the results as in Table A5.

<br>**Table A5. Results by inflow profile (simulator, auto-linked mode)**

| Inflow profile | Mean household size | Single-person share | Small-unit gap | Large-unit gap | 1–2-room gap |
|---|---|---|---|---|---|
| Godeok as measured | 3.23 | 16.2% | +5.2 | −12.6 | −20.3 |
| Young-worker concentrated | 3.01 | 21.2% | +0.6 | −9.9 | **−25.3** |
| Family-centered | 3.57 | 10.7% | +11.4 | **−17.0** | −13.6 |

<sub>Source: companion tool output (`design_simulator.html`). Developers can substitute their own demand projections to reproduce or revise the mix presented in this study.</sub>

Across all three profiles the **1–2-room and large-unit shortages retain their sign** and small units remain in surplus. Lowering mean household size to 2.18 (Pyeongtaek as a whole) in direct-entry mode reproduces the first pass's "small units short" conclusion, making visible how parameter choice changes the conclusion.

---

## A-7. Figures excluded from the manuscript (for reproduction)

The following figures were excluded from the manuscript because they are not used directly in its argumentative chain or duplicate another exhibit, but **the PNG files and generating scripts remain under `analysis/`** and can be consulted for reproduction or extension.

| File | Content | Reason for exclusion |
|---|---|---|
| **`28_supply_structure.png`** | supply distribution by rooms and area | **Table 2 carries the same figures, so the chart adds no information** |
| **`32_godeok_recalibration.png`** | three-panel recalibration | **absorbed into consolidated Figure 3-①–③** |
| **`34_barbell_distribution.png`** | three-panel distributional mismatch | **absorbed into consolidated Figure 3-②–④** |
| `13_development_concentration.png` | spatial concentration of development (Godeok share 1→73%) | same message as Figure 1 |
| `12_local_premium_gradient.png` | local price gradient by distance | subset of Figure 5 (continuous-distance hedonic) |
| `21_gap_index_prototype.png` | first-pass gap index | visualization of the parameter set rejected in §IV.4-(1) — retaining it invites misreading |
| `16_hedonic.png` | premium controlling for building age | redundant with Figure 5 |
| `24_design_model.png` | schematic of the design chain | redundant with the equations in §III.3-3) and Table A4 |
| `25_model_validation.png` | cross-city validation | Table A2 (three rows) suffices |
| `27_forecast_design.png` | design-target trajectory | merged into Figure 6 (annual roadmap). ⚠️ based on uncorrected parameters (§V.4-(5)) |

---

<div align="right"><sub><b>Unsubmitted student manuscript (draft) — Appendix</b></sub></div>
