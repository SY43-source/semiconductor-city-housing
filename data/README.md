# Data

Raw datasets are **not redistributed in this repository**. They are public but large, and several are subject to the terms of the issuing agency. This directory documents what each dataset is, where it came from, and how to obtain it again.

See [DATA_SOURCES.md](DATA_SOURCES.md) for the full provenance table (Korean; column names match the source files).

## What the study used

| Dataset | Records | Source |
|---|---|---|
| Apartment sale transactions, 2015–2025 | 253,255 | Ministry of Land, Infrastructure and Transport — Real Transaction Price Disclosure System |
| Apartment lease/rent transactions, 2015–2025 | 156,330 | same |
| Population by five-year age band, 2011–2025 | — | Statistics Korea (KOSIS), table DT_1B04005N |
| Households by size / by head's age | — | Statistics Korea (KOSIS), tables DT_1JC1516, DT_1JC1511 |
| Complex and unit-type metadata | 29,014 records over 6,244 complexes | Normalized from a public real-estate listing service. Room count and exclusive floor area are not published in national statistics, which is why this source was necessary |
| Public rental unit composition and rents | 8,380 units | LH and GH tenant recruitment announcements |

## Running the scripts against your own copy

Analysis scripts resolve repository paths automatically, but read their input from a local data root. Set it before running:

```bash
export DATA_ROOT=/path/to/your/data
export INVENTORY_DB=/path/to/complex_metadata.sqlite
```

Every script reads these two variables, falling back to the author's local paths when they are unset. Repository paths (where figures are written) resolve automatically from the script's own location, so no configuration is needed for those.

Expected layout under `DATA_ROOT`:

```
realprice/     apartment sale and lease transactions, by region
population/    KOSIS population and household tables
employment/    manufacturing employment and household-size series
housing_supply/  permits by unit size
```
