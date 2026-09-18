# Figure index

Figures live where the scripts write them, in [`../analysis/`](../analysis/). This page maps the numbers used in the manuscript to the file and the script that produced it, so that "figure 3" resolves in one click.

To regenerate any figure, run its script — they resolve paths relative to the repository and take no arguments.

## Manuscript

| Fig. | Section | Shows | Image | Script |
|---|---|---|---|---|
| **1** | IV.1 | Growth concentration — Godeok against the rest of Pyeongtaek | [png](../analysis/20_godeok_concentration.png) | [`20_godeok_concentration.py`](../analysis/20_godeok_concentration.py) |
| **2** | IV.2 | Age structure of the inflow — working age plus young children | [png](../analysis/22_godeok_age.png) | [`22_godeok_age.py`](../analysis/22_godeok_age.py) |
| **3** | IV.4 | Demand recalibration and the resulting mismatch (4 panels) | [png](../analysis/37_gap_consolidated.png) | [`37_gap_consolidated.py`](../analysis/37_gap_consolidated.py) |
| **4** | IV.5 | Market split — where small-unit demand is actually realized | [png](../analysis/10_rent_analysis.png) | [`10_rent_analysis.py`](../analysis/10_rent_analysis.py) |
| **5** | IV.6 | Distance-to-campus hedonic, separated from the new-town label | [png](../analysis/23_distance_hedonic.png) | [`23_distance_hedonic.py`](../analysis/23_distance_hedonic.py) |
| **6** | IV.7 | Annual housing-design roadmap to 2035 | [png](../analysis/33_annual_design_roadmap.png) | [`33_annual_design_roadmap.py`](../analysis/33_annual_design_roadmap.py) |
| **7** | IV.8 | Affordability — who can and cannot enter | [png](../analysis/35_affordability.png) | [`35_affordability.py`](../analysis/35_affordability.py) |

## Appendix

| Fig. | Shows | Image | Script |
|---|---|---|---|
| **A1** | Gap sensitivity to household and unit-size mapping assumptions | [png](../analysis/21b_gap_sensitivity.png) | [`21b_gap_sensitivity.py`](../analysis/21b_gap_sensitivity.py) |
| **A2** | Macro cycle adjustment — the nationwide component of the trend | [png](../analysis/08_macro_adjusted.png) | [`08_macro_adjusted.py`](../analysis/08_macro_adjusted.py) |
| **A3** | Model sensitivity to the unit-size mapping | [png](../analysis/24b_model_sensitivity.png) | [`24b_model_sensitivity.py`](../analysis/24b_model_sensitivity.py) |
| **A4** | Tenure turnover adjustment, transaction flow to stock | [png](../analysis/26_tenure_stock_adjust.png) | [`26_tenure_stock_adjust.py`](../analysis/26_tenure_stock_adjust.py) |
| **A5** | Rolling-origin backcast validation | [png](../analysis/31_backcast_validation.png) | [`31_backcast_validation.py`](../analysis/31_backcast_validation.py) |

## Figures not in the manuscript

`analysis/` holds roughly thirty more figures from analyses that were run but not included — control-region robustness, dose-response on employment, transfer forecasts to another city, and earlier versions of the gap estimate. They are kept because the manuscript refers to some of them in passing and because they show what was tried. Their scripts carry the same numbering.
