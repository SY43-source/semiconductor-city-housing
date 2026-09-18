# Housing in a Semiconductor Cluster City

**Does the housing built beside a semiconductor cluster fit the people who actually moved in — and who is left out when it does not?**

A study of Godeok New Town, built next to Samsung's Pyeongtaek Campus, using 409,585 official real-estate transactions (2015–2025), Statistics Korea population data, and 29,014 unit-type records normalized from listing data.

**Author**: Seoyeon Jeon · Single-authored student research manuscript, not submitted for publication.

---

## Read the paper

| | Korean | English |
|---|---|---|
| **Manuscript** | [Semiconductor-City-Housing-KO.pdf](paper/Semiconductor-City-Housing-KO.pdf) (25 pp) | [Semiconductor-City-Housing-EN.pdf](paper/Semiconductor-City-Housing-EN.pdf) (20 pp) |
| **Appendix** | [Appendix-KO.pdf](paper/Appendix-KO.pdf) (7 pp) | [Appendix-EN.pdf](paper/Appendix-EN.pdf) (6 pp) |

Markdown sources are in [`paper/source/`](paper/source/). The English edition is set in a two-column journal layout; the Korean edition in single column.

---

## What the study finds

1. **Growth collapsed onto one point.** Effectively all of Pyeongtaek's net population growth went to Godeok (×5.7). New development there rose from 1% to 73% of the city's total, and the price ratio against the outskirts from 0.96 to 2.49.

2. **The arrivals were young families, not single workers.** Children aged 0–14 are 19.4% of Godeok (10.3% nationally); mean household size is 3.0–3.5 against 2.18 city-wide. Substituting the city-wide single-person share (37.5%) therefore overstates small-unit demand — an error this study made and corrected.

3. **The mismatch differs by axis.** On room count it is a **barbell**: the three-bedroom template is oversupplied by 22.6–26.6pp while both ends are short (1–2 rooms by 15.7–25.4pp). On floor area only large units are short. A single 84–85㎡ size band holds 55.3% of all units (12,366 of 22,368).

4. **The cost falls on households that cannot buy.** The price-to-income ratio is 16.1 for an entry-level worker (5.1 is the international "severely unaffordable" threshold) and mortgage servicing takes 65% of income. Rent splits sharply by sector: 0.24M KRW/month for public units (5–8% of income) against 0.89M for private ones (18–30%).

5. **Vulnerability here is a function of eligibility, not income.** Public rental supplies 7,720 units (25.7% of stock) at an affordable price, but its income ceilings fall below a single-earner household making 50M KRW a year. That household is too well paid for public programs and too poorly paid for the market — a combination with no name in the existing classification.

---

## Where the numbers come from

**[EVIDENCE_MAP.md](EVIDENCE_MAP.md) — start here.** Every statistic, table, and figure in the paper is traced to the script that computed it and the dataset it came from. If you want to check a number, this is the one-page index.

```
claim in the paper  →  EVIDENCE_MAP.md  →  analysis/NN_*.py  →  data/DATA_SOURCES.md
```

---

## Repository layout

| Path | Contents |
|---|---|
| [`paper/`](paper/) | Current manuscript and appendix, Korean and English, plus Markdown sources |
| [`EVIDENCE_MAP.md`](EVIDENCE_MAP.md) | Number → figure/table → script → dataset index |
| [`analysis/`](analysis/) | 40 numbered analysis scripts and the figures they produce |
| [`src/`](src/) | Data collectors (Statistics Korea OpenAPI) and the PDF builder |
| [`data/`](data/) | [DATA_SOURCES.md](data/DATA_SOURCES.md) — provenance and how to re-obtain each dataset |
| [`archive/versions/`](archive/versions/) | Every earlier draft (v1–v11) and the revision log |
| [`archive/notes/`](archive/notes/) | Planning and methodology notes written during the study |
| [`docs/`](docs/) | Interactive housing-design simulator (single HTML file) |

Figures are numbered 1–7 in the manuscript and A1–A5 in the appendix; tables 1–11 and A1–A5.

---

## The record of being wrong

Earlier drafts are kept, not discarded, and [`archive/versions/_CHANGELOG.md`](archive/versions/_CHANGELOG.md) records four occasions on which a conclusion was withdrawn and replaced:

| Version | What was wrong |
|---|---|
| v6 → v7 | The gap estimate used the city-wide single-person share; the floor-area conclusion reversed sign once recalculated against observed household size |
| v8 → v9 | Public rental was missing entirely — absence from the data source had been read as absence in reality |
| v9 → v10 | The conclusion still quoted figures that the analysis section had already rejected |
| v10 → v12 | 1,200 units classified as private rental turned out to be LH public supply |

Drafts affected by a withdrawn claim carry an explicit warning at the top of the changelog entry.

---

## Running the analysis

Requires Python 3.11 with `pandas`, `numpy`, `scipy`, `matplotlib`. Scripts resolve paths relative to the repository, so they run from a clone:

```bash
python3.11 analysis/37_gap_consolidated.py   # Figure 3 — consolidated mismatch
python3.11 analysis/32_godeok_recalibration.py   # Table 3 — recalibrated gap band
```

Scripts that read the transaction and population datasets expect them under a local data root; see [`data/DATA_SOURCES.md`](data/DATA_SOURCES.md) for what each file is and where to obtain it. Raw datasets are not redistributed here.

---

## Scope and limits

This is a consistency and access diagnosis, not a causal claim and not an optimal-allocation result. Section V.4 of the manuscript states seven limitations in full, including the household-size band that the floor-area conclusion is conditional on, and the fact that the income figures are scenarios rather than observed household incomes.
