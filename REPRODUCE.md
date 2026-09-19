# Reproducing the results

Every figure and table in the paper comes from a script in [`analysis/`](analysis/). This page says exactly which command produces which exhibit, and — just as important — what you can and cannot reproduce from a clone of this repository.

## What you can reproduce from this repository alone

**The code, in full.** Every script is here, with the transformations, model specifications, and thresholds visible.

**The figures, if you supply the data.** The raw datasets are public but are not redistributed here: the transaction files are large and are published under the issuing agency's terms. [`data/DATA_SOURCES.md`](data/DATA_SOURCES.md) identifies each one and where to obtain it.

So a reader who wants to check a number has two routes: read the script (immediate), or obtain the data and re-run it (a few hours of downloading). Both are supported. Neither is hidden behind anything.

---

## Setup

```bash
python3.11 -m pip install pandas numpy scipy matplotlib
```

Point the scripts at your data:

```bash
export DATA_ROOT=/path/to/data              # transaction, population, employment files
export INVENTORY_DB=/path/to/complexes.sqlite   # complex and unit-type metadata
```

Repository paths resolve automatically — figures are written next to the script that made them, whatever directory you cloned into.

---

## Manuscript figures

| Fig. | Command | Produces |
|---|---|---|
| **1** | `python3.11 analysis/20_godeok_concentration.py` | Growth concentration in Godeok |
| **2** | `python3.11 analysis/22_godeok_age.py` | Age structure of the inflow |
| **3** | `python3.11 analysis/37_gap_consolidated.py` | Recalibration and the resulting mismatch |
| **4** | `python3.11 analysis/10_rent_analysis.py` | Market split — where small-unit demand goes |
| **5** | `python3.11 analysis/23_distance_hedonic.py` | Distance-to-campus hedonic |
| **6** | `python3.11 analysis/33_annual_design_roadmap.py` | Annual design roadmap to 2035 |
| **7** | `python3.11 analysis/35_affordability.py` | Affordability and access |

## Appendix figures

| Fig. | Command |
|---|---|
| **A1** | `python3.11 analysis/21b_gap_sensitivity.py` |
| **A2** | `python3.11 analysis/08_macro_adjusted.py` |
| **A3** | `python3.11 analysis/24b_model_sensitivity.py` |
| **A4** | `python3.11 analysis/26_tenure_stock_adjust.py` |
| **A5** | `python3.11 analysis/31_backcast_validation.py` |

## Key tables

| Table | Command | Produces |
|---|---|---|
| **2** | `python3.11 analysis/28_supply_structure.py` | Supply structure — room count and floor area |
| **3** | `python3.11 analysis/32_godeok_recalibration.py` | Recalibrated gap band |
| **10–11** | `python3.11 analysis/35_affordability.py` | Public rental totals, affordability by sector |

Scripts print their headline values on completion, so you can check a number without opening the figure. For instance, `32_godeok_recalibration.py` prints the gap band that appears in Table 3.

---

## Rebuilding the PDFs

```bash
python3.11 src/build_pdf.py all
```

Reads [`paper/source/*.md`](paper/source/) and writes the four PDFs in [`paper/`](paper/). Requires `markdown` and `weasyprint`. To rebuild a superseded draft instead: `python3.11 src/build_pdf.py v10`.

---

## Checking that the documents still agree with the paper

The manuscript is the source; `README.md`, `EVIDENCE_MAP.md`, `LIMITATIONS.md`, `REPRODUCE.md`, and `figures/README.md` are derived from it. When the manuscript is revised, a derived document can silently fall behind — that has happened here, which is why there is a check for it:

```bash
python3.11 src/consistency_check.py
```

It anchors ten key quantities in the manuscript, then verifies that the Korean and English editions agree on them, that no withdrawn figure survives in a current document, that no link points at a superseded draft, that every figure the manuscript references exists, and that every relative link resolves.

| Exit | Meaning |
|---|---|
| 0 | Pass |
| 1 | A mismatch was found — fix it |
| **2** | **Could not check** — e.g. an anchor quantity was not found in the manuscript, which usually means the manuscript changed and the anchor list needs updating. **This is not a pass.** |

The separation of 2 from 0 is deliberate: a checker that finds nothing because it looked at nothing should not report success. To confirm the checker actually catches faults, it can inject them into a copy of the repository and assert the exit code:

```bash
python3.11 src/consistency_check.py --self-test
```

---

## Verifying a single claim without running anything

The fastest path for a specific number is [`EVIDENCE_MAP.md`](EVIDENCE_MAP.md), which maps each statistic to its figure or table, the script that computed it, and the dataset underneath. [`figures/README.md`](figures/README.md) does the same starting from a figure number.

---

## The data audit

One analysis is worth noting because it audits the data rather than the housing. `38_llm_crosscheck.py` runs a local language model over the unit-type records to look for internal contradictions, and separately measures how accurately supply type can be judged from a complex's name — the answer is 69.2%, which is why the study stopped relying on name-based classification after it produced three errors. It needs a local Ollama installation:

```bash
export GEMMA_CLIENT_DIR=/path/to/queue/client
export OLLAMA_MODEL=gemma3:latest
python3.11 analysis/38_llm_crosscheck.py
```

Its output is committed at `analysis/38_llm_crosscheck.json`, so the result can be read without re-running it.
