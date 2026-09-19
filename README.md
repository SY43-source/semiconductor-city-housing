# Housing in a Semiconductor Cluster City

**Does the housing built beside a semiconductor cluster fit the people who actually moved in — and who is left out when it does not?**

**Author**: Seoyeon Jeon, Valor International Scholars · Student research manuscript, not submitted for publication.

---

## The setting

Advanced semiconductors can be manufactured at scale in only three countries — the United States, South Korea, and Taiwan. The industrial clusters that make them, and the towns built to house the people who work there, therefore keep being created as a matter of national industrial policy. This study examines one of them, in enough detail to ask a question that applies to all of them.

**Pyeongtaek** is a city of roughly 600,000 people about 65 km south of Seoul, in South Korea. Samsung began building its **Pyeongtaek Campus** there in 2015; it is now among the largest semiconductor manufacturing sites in the world, and its production lines opened in stages — 2017, 2020, and 2022. **Godeok New Town** is the planned district built beside the campus to house the incoming workforce.

Two facts make this a useful case. First, the growth is unusually concentrated: essentially all of Pyeongtaek's net population increase went into Godeok, so the effect is not diluted across a whole city. Second, the housing there was planned and built inside a single decade, which means the mix of unit sizes that was chosen can be compared against the households that actually arrived.

**Evidence base**: 409,585 official real-estate transactions (2015–2025) published by the Ministry of Land, Infrastructure and Transport; population and household data from Statistics Korea; public rental terms from the LH and GH housing corporations; and 29,014 unit-type records covering 6,244 apartment complexes, normalized from a public listing service because room counts and floor areas are not published in national statistics.

---

## Read the paper

| | Korean | English |
|---|---|---|
| **Manuscript** | [Semiconductor-City-Housing-KO.pdf](paper/Semiconductor-City-Housing-KO.pdf) (25 pp) | [Semiconductor-City-Housing-EN.pdf](paper/Semiconductor-City-Housing-EN.pdf) (20 pp) |
| **Appendix** | [Appendix-KO.pdf](paper/Appendix-KO.pdf) (7 pp) | [Appendix-EN.pdf](paper/Appendix-EN.pdf) (6 pp) |

Markdown sources are in [`paper/source/`](paper/source/). The English edition is set in a two-column journal layout; the Korean edition in single column.

---

## What the study finds

1. **Growth collapsed onto one point.** Effectively all of Pyeongtaek's net population increase went to Godeok — its population rose 5.7-fold. New construction there went from 1% to 73% of the city's total, and its price per unit area against the city's outskirts from 0.96 to 2.49 times.

2. **The arrivals were young families, not single workers.** Children aged 0–14 make up 19.4% of Godeok's population against 10.3% nationally, and mean household size is 3.0–3.5 against 2.18 across the city. This matters because the study's first estimate assumed otherwise: substituting the city-wide single-person rate (37.5%) overstated demand for small units badly enough to reverse one of the findings. The error and its correction are both on the record.

3. **The mismatch has a different shape on each axis.** By room count it is a **barbell** — the three-bedroom template is oversupplied by 22.6–26.6 percentage points while both ends are short (one- and two-room units by 15.7–25.4pp). By floor area, only large units are short. Supply is extraordinarily concentrated: a single 84–85㎡ (about 900 sq ft) size band holds 55.3% of all units, 12,366 of 22,368. That size is the Korean market's default apartment, built for a family of four.

4. **The cost falls on households that cannot buy.** Buying the standard unit requires **16.1 times** an entry-level worker's annual income — the international threshold for "severely unaffordable" is 5.1 — and mortgage payments would take 65% of monthly income. Renting splits sharply by sector: a small unit costs about **240,000 KRW/month (≈US$180)** if it is public housing, 5–8% of income, against **890,000 KRW (≈US$670)** on the private market, 18–30%.

5. **Vulnerability here is a function of eligibility, not income.** Korea's public rental system supplies 7,720 units in Godeok — a quarter of the housing stock — at a price people can actually afford. But its income ceilings sit below what a single earner making 50M KRW a year (≈US$37,000) earns. That household is too well paid for the public programs and too poorly paid for the market. It has no name in the existing classification of housing vulnerability, and the clusters keep producing exactly that profile: young, unmarried, above-average earners arriving in large numbers over a short period.

---

## A note on terms

| Term | What it means |
|---|---|
| **Jeonse / monthly rent** | Korea has two rental forms: *jeonse*, a large refundable deposit with no monthly payment, and ordinary monthly rent. A shift from jeonse toward monthly rent generally signals tenants with less capital. |
| **Public rental** | Housing built and let by the state corporations **LH** (national) and **GH** (provincial) at below-market rents, allocated by eligibility rather than by price. |
| **The 84㎡ unit** | About 900 sq ft, three bedrooms. The default apartment in the Korean market, to the point that supply plans are often written around it. |
| **PIR** | Price-to-income ratio — the purchase price of a home divided by annual household income. |
| **KRW** | Korean won. Roughly 1,330 KRW to US$1 over the study period. |

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
| [`REPRODUCE.md`](REPRODUCE.md) | The command behind each figure and table, and what a clone can and cannot reproduce |
| [`LIMITATIONS.md`](LIMITATIONS.md) | What the study does not establish — which results are robust and which are conditional |
| [`analysis/`](analysis/) | 40 numbered analysis scripts and the figures they produce |
| [`figures/`](figures/) | Index mapping each figure number in the paper to its image and script |
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

Scripts that read the transaction and population datasets take their location from two environment variables:

```bash
export DATA_ROOT=/path/to/data
export INVENTORY_DB=/path/to/complex_metadata.sqlite
```

See [`data/README.md`](data/README.md) for the expected layout and [`data/DATA_SOURCES.md`](data/DATA_SOURCES.md) for what each dataset is and where to obtain it. Raw datasets are not redistributed here.

[`REPRODUCE.md`](REPRODUCE.md) lists the command behind every figure and table.

To rebuild the PDFs from the Markdown sources: `python3.11 src/build_pdf.py all`

---

## Scope and limits

This is a consistency and access diagnosis, not a causal claim and not an optimal-allocation result.

**[LIMITATIONS.md](LIMITATIONS.md)** states what the study does not establish, including which results are robust and which are conditional. In short: the room-count conclusion holds across every assumption tested; the floor-area conclusion depends on a household-size band; and the income figures are scenarios rather than observed household incomes.
