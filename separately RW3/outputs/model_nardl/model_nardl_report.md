# RW3 Module Report - model_nardl

## Interpretation Guide
- ADF p>0.05 and KPSS p<0.05 -> likely I(1)-like; prefer differences/cointegration models.
- ADF p<0.05 and KPSS p>0.05 -> stationary; level models are more admissible.
- Ljung-Box p<0.05 -> autocorrelation; add lag structure.
- BP/White p<0.05 -> heteroskedasticity; use robust or HAC standard errors.
- JB p<0.05 -> non-normality; use robust inference and avoid strict normality assumptions.
- Stability flag=1 -> potential breaks/drift; use rolling or split-sample robustness.
- For retail transmission, compare no-promo vs promo-controlled estimates.

## Notes
- module=model_nardl
- xlsx_files=1
- png_files=2
- Interpretation: read test diagnostics first, then coefficients/effects with robustness context.

## Tables

### model_nardl_output_NARDL_Summar

| standardized_type | y_series_source | x_series_sources | frequency | sample_period | lags_selected | short_run_coef | long_run_coef | asymmetry_short_p | asymmetry_long_p | diagnostics_flags | interpretation_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| butter | ProducerUA | EU | weekly | 2021-12-28..2025-12-23 | dy(1), x_pos, x_neg | -0.00257929957347239 | 0.431674313712216 | 0.7032988697348881 | 3.62400323940141e-35 | HAC SE applied | Low p-values indicate asymmetric transmission to positive vs negative shocks. |
| butter | ProZorro | EU | weekly | 2025-04-08..2026-01-06 | dy(1), x_pos, x_neg | 0.2980520944183506 | 0.324865661584349 | 0.4610198263573729 | 0.5053658392991783 | HAC SE applied | Low p-values indicate asymmetric transmission to positive vs negative shocks. |
| cream | ProducerUA | EU | weekly | 2021-12-28..2025-12-23 | dy(1), x_pos, x_neg | -0.003304786284085873 | -0.0004551774905197647 | 0.6688359246375976 | 0.9806218562475245 | HAC SE applied | Low p-values indicate asymmetric transmission to positive vs negative shocks. |
| cream | ProZorro | EU | weekly | 2025-04-15..2026-01-06 | dy(1), x_pos, x_neg | -0.947164083818236 | 0.1786141240120238 | 0.1472898220935979 | 0.7515583051997151 | HAC SE applied | Low p-values indicate asymmetric transmission to positive vs negative shocks. |
| hard_cheese | ProducerUA | EU | weekly | 2021-12-28..2025-12-23 | dy(1), x_pos, x_neg | -0.03242904522300962 | 0.339326206737692 | 0.7969953657108445 | 4.335992962700479e-12 | HAC SE applied | Low p-values indicate asymmetric transmission to positive vs negative shocks. |
| hard_cheese | ConsumerUA | EU | weekly | 2021-12-28..2026-01-13 | dy(1), x_pos, x_neg | -0.04203621536336792 | 0.4733525368886606 | 0.5978648634303664 | 1.739171585276989e-20 | HAC SE applied | Low p-values indicate asymmetric transmission to positive vs negative shocks. |
| hard_cheese | ProZorro | EU | weekly | 2025-04-08..2026-01-06 | dy(1), x_pos, x_neg | 0.7230817021185868 | 0.3612117582178556 | 0.3447177432281329 | 0.1494152419119614 | HAC SE applied | Low p-values indicate asymmetric transmission to positive vs negative shocks. |
| milk | ProducerUA | EU | weekly | 2021-12-28..2025-12-23 | dy(1), x_pos, x_neg | -0.02357513460484666 | 0.4248204235844112 | 0.8261199738418743 | 3.651106085098579e-33 | HAC SE applied | Low p-values indicate asymmetric transmission to positive vs negative shocks. |
| milk | ConsumerUA | EU | weekly | 2021-12-28..2026-01-13 | dy(1), x_pos, x_neg | -0.04993934884027437 | 0.4355387708736216 | 0.8169994381630011 | 1.833419471578697e-37 | HAC SE applied | Low p-values indicate asymmetric transmission to positive vs negative shocks. |
| milk | ProZorro | EU | weekly | 2025-04-08..2026-01-06 | dy(1), x_pos, x_neg | -0.5494196632537425 | -0.8902831834836844 | 0.285030587647836 | 0.1175527869214251 | HAC SE applied | Low p-values indicate asymmetric transmission to positive vs negative shocks. |
| other | ProZorro | EU | weekly | 2025-04-08..2026-01-06 | dy(1), x_pos, x_neg | -0.4328150807688999 | 1.516592402846752 | 0.0008442188009509941 | 0.001194185354368458 | HAC SE applied | Low p-values indicate asymmetric transmission to positive vs negative shocks. |

## Graphs

- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/model_nardl/nardl_long_run.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/model_nardl/nardl_short_run.png
