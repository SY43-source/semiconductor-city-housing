# Limitations

These are stated in §5.4 of the manuscript. They are repeated here because a reader should be able to find what the study does *not* establish without reading twenty-five pages first.

**This is a consistency and access diagnosis. It is not a causal estimate and not an optimal-allocation result.** Nothing below is a caveat added after the fact; each limitation is attached to a specific result and, where it matters, to the sensitivity analysis that tests it.

---

## What is robust, and what is conditional

The clearest thing to know before citing any number:

| Result | Status |
|---|---|
| **Room-count gap** — three-bedroom oversupply, one- and two-room shortage | **Robust.** The direction holds across the full household-size band and every mapping variation tested (Fig. A1, A3) |
| **Floor-area gap** — small-unit surplus, large-unit shortage | **Conditional.** The sign depends on the mean household size assumption (see 2 below) |
| **Affordability gaps** — PIR 16.1, public vs private rent | **Directional.** Read as the size and direction of a gap, not as exact burden estimates (see 3) |

---

## 1. Endogeneity of the treatment location

The distance hedonic separates proximity from other effects only partially, because distance to the campus overlaps with accessibility to the urban core. The size and room mappings *M* are assumptions; sensitivity analysis confirms the robustness of direction only, not of magnitude (Figures A1, A3).

## 2. Mean household size is an approximation

Mean household size *m̄* is population divided by apartment units. Residents of non-apartment housing and unoccupied or vacant units are not directly observed, so it is carried as a band of 2.99–3.46 rather than a point value.

**The floor-area conclusion is conditional on that band. The room-count conclusion is not.** The turnover adjustment was applied to the tenure axis only, not to the area distribution.

## 3. Incomes are scenarios, not measurements

The access analysis (§4.8) uses three income scenarios. The actual income distribution, asset holdings, and prior-residence transitions of Godeok households were not observed.

Ownership burden assumes LTV 70%, 4% interest, 30 years. Effective rent assumes a 5.5% jeonse-to-monthly conversion rate. Standard-size and large-unit rents could not be separated into public and private because of sample size.

## 4. Public rental totals are established; one internal split is not

The 7,720 units in Table 10 were verified against LH and GH tenant-recruitment notices and the building register, and the supplier of all 8,380 rental units is identified — private rental consists solely of Eulim Square's 660 units.

What remains open is the internal split of LH Complexes 15 and 35 across national rental, permanent rental, and senior welfare housing. Identifying public complexes from transaction-record names also rests on nominal classification, the same category of method that produced three earlier errors in this study; the complex metadata omits public rental, so no alternative source was available.

## 5. The planning-horizon trajectory

The trajectory was recomputed after correction and is consistent with §4.4. But the cohort-maturation scenario shifts the age profile by one five-year band and does not model mortality, out-migration, or re-entry separately. The correction coefficient is held fixed across the horizon; if Godeok's household structure converges toward the city average, the 2035 single-person share would be higher than the 12.9% estimated here.

Annual projections depend on a three-year slope, so a change to the campus expansion schedule requires re-estimation. Post-saturation values are lower bounds.

## 6. Three populations coexist — check which one a ratio refers to

| Population | Count | Used for |
|---|---:|---|
| Units by unit type (complex metadata) | 22,368 | Unit-composition analysis, §4.3–4.4 |
| Total units | 23,957 | Private tenure analysis |
| Stock merged with public-rental notices | 30,088 | Stock recomputation, Table 11 |

**The gaps in §4.3 and §4.4 are on a private for-sale basis** and do not include public-rental unit types. Since public rental is concentrated in small units (16–44㎡), small-unit supply is larger than tabulated, and the small-unit surplus may widen. Recomputing the gap with public-rental unit types included is the highest-priority next step.

## 7. A single case

Transfer validation to other cities reinforces the method partially, but local differences remain. What the study would need next: a survey of resident households including income and transition paths, empirical estimation of the mapping coefficients, a two-center model, and wider multi-city transfer.

---

## Conclusions that were withdrawn

Four earlier conclusions were wrong and were replaced. They are documented in [`archive/versions/_CHANGELOG.md`](archive/versions/_CHANGELOG.md), with the drafts that carried them left in place rather than deleted.

The one worth knowing about: the first gap estimate substituted the city-wide single-person rate into a district where mean household size is a full person larger. It produced a small-unit *shortage* of 17.8 percentage points. Recalculated against the observed household size, the sign reversed. The error is the reason §4.4 carries a household-size band at all.
