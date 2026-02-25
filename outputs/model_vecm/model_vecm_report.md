# RW3 Module Report - model_vecm

## Interpretation Guide
- ADF p>0.05 and KPSS p<0.05 -> likely I(1)-like; prefer differences/cointegration models.
- ADF p<0.05 and KPSS p>0.05 -> stationary; level models are more admissible.
- Ljung-Box p<0.05 -> autocorrelation; add lag structure.
- BP/White p<0.05 -> heteroskedasticity; use robust or HAC standard errors.
- JB p<0.05 -> non-normality; use robust inference and avoid strict normality assumptions.
- Stability flag=1 -> potential breaks/drift; use rolling or split-sample robustness.
- For retail transmission, compare no-promo vs promo-controlled estimates.

## Notes
- module=model_vecm
- xlsx_files=1
- png_files=1
- Interpretation: read test diagnostics first, then coefficients/effects with robustness context.

## Tables

### model_vecm_output_VECM_Summary

| standardized_type | system | y_series_source | x_series_sources | frequency | sample_period | lags_selected | cointegration_rank | cointegration_vectors | adjustment_alpha_abs_mean | diagnostics_flags | interpretation_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| hard_cheese | System A | ProducerUA | ConsumerUA, EU | weekly | 2021-12-28..2025-12-23 | k_ar_diff=3 | 1 | 1.000; -0.643; -0.104 | 0.6905463602735168 | VECM estimated | Rank>0 supports long-run co-movement in the system. |
| milk | System A | ProducerUA | ConsumerUA, EU | weekly | 2021-12-28..2025-12-23 | k_ar_diff=3 | 3 | 1.000; 0.000; 0.000 | 0.07202042647366828 | VECM estimated | Rank>0 supports long-run co-movement in the system. |
| milk | System D | ProducerUA | EU, CME | weekly | 2021-12-28..2025-12-23 | k_ar_diff=3 | 3 | 1.000; -0.000; 0.000 | 0.06026866786576559 | VECM estimated | Rank>0 supports long-run co-movement in the system. |

## Graphs

- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/model_vecm/vecm_alpha.png
