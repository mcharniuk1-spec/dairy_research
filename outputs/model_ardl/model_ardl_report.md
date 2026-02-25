# RW3 Module Report - model_ardl

## Interpretation Guide
- ADF p>0.05 and KPSS p<0.05 -> likely I(1)-like; prefer differences/cointegration models.
- ADF p<0.05 and KPSS p>0.05 -> stationary; level models are more admissible.
- Ljung-Box p<0.05 -> autocorrelation; add lag structure.
- BP/White p<0.05 -> heteroskedasticity; use robust or HAC standard errors.
- JB p<0.05 -> non-normality; use robust inference and avoid strict normality assumptions.
- Stability flag=1 -> potential breaks/drift; use rolling or split-sample robustness.
- For retail transmission, compare no-promo vs promo-controlled estimates.

## Notes
- module=model_ardl
- xlsx_files=1
- png_files=1
- Interpretation: read test diagnostics first, then coefficients/effects with robustness context.

## Tables

### model_ardl_output_ARDL_Summary

| standardized_type | y_series_source | x_series_sources | frequency | sample_period | lags_selected | short_run_coef | long_run_coef | coint_or_bounds_p | diagnostics_flags | eligible_for_ecm_form | interpretation_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| butter | ProducerUA | EU | weekly | 2021-12-28..2025-12-23 | p=2, q=2 | 0.638088813491537 | 0.8477031455859193 | 0.7705229151133584 | LB=8.79e-15; BP=0.462; White=0.515 | no | ARDL captures short- and long-run transmission under I(0)/I(1)-mix assumptions. |
| butter | ProZorro | EU | weekly | 2025-04-08..2026-01-06 | p=1, q=0 | -0.1126541894710495 | -0.3318711999239127 | 0.1636038972284045 | LB=0.633; BP=0.0462; White=0.255 | no | ARDL captures short- and long-run transmission under I(0)/I(1)-mix assumptions. |
| cream | ProducerUA | EU | weekly | 2021-12-28..2025-12-23 | p=2, q=2 | 0.04922198585267523 | 0.1895293235950405 | 0.5456672984077288 | LB=1.37e-21; BP=0.59; White=0.0654 | no | ARDL captures short- and long-run transmission under I(0)/I(1)-mix assumptions. |
| cream | ProZorro | EU | weekly | 2025-04-15..2026-01-06 | p=2, q=0 | 0.2894838020743842 | 0.2798247240248903 | 7.914017296706472e-06 | LB=0.978; BP=0.322; White=0.753 | yes | ARDL captures short- and long-run transmission under I(0)/I(1)-mix assumptions. |
| hard_cheese | ProducerUA | EU | weekly | 2021-12-28..2025-12-23 | p=2, q=2 | 0.3551626072614864 | 0.6208905309984175 | 0.3497660842704009 | LB=2.94e-23; BP=0.0859; White=0.119 | no | ARDL captures short- and long-run transmission under I(0)/I(1)-mix assumptions. |
| hard_cheese | ConsumerUA | EU | weekly | 2021-12-28..2026-01-13 | p=2, q=2 | 0.452794007447562 | 0.8390572807646949 | 0.5031244319467403 | LB=5.79e-21; BP=0.157; White=0.0643 | no | ARDL captures short- and long-run transmission under I(0)/I(1)-mix assumptions. |
| hard_cheese | ProZorro | EU | weekly | 2025-04-08..2026-01-06 | p=1, q=0 | -0.2865029854639456 | -0.4489016720895597 | 0.001297823529196093 | LB=0.705; BP=0.318; White=0.49 | yes | ARDL captures short- and long-run transmission under I(0)/I(1)-mix assumptions. |
| milk | ProducerUA | EU | weekly | 2021-12-28..2025-12-23 | p=3, q=2 | 0.4145372929609987 | 0.7957185748702496 | 0.8924029758886471 | LB=4.73e-08; BP=0.0925; White=0.164 | no | ARDL captures short- and long-run transmission under I(0)/I(1)-mix assumptions. |
| milk | ConsumerUA | EU | weekly | 2021-12-28..2026-01-13 | p=3, q=2 | 0.3710293334168067 | 0.7473279445716343 | 0.9515547171935748 | LB=8.41e-08; BP=0.149; White=0.261 | no | ARDL captures short- and long-run transmission under I(0)/I(1)-mix assumptions. |
| milk | ProZorro | EU | weekly | 2025-04-08..2026-01-06 | p=2, q=0 | 0.7545075848393812 | 0.8868136250061809 | 4.278777154383951e-05 | LB=0.92; BP=0.381; White=0.577 | yes | ARDL captures short- and long-run transmission under I(0)/I(1)-mix assumptions. |
| other | ProZorro | EU | weekly | 2025-04-08..2026-01-06 | p=1, q=0 | -0.09704672500046962 | 10.87221183583123 | 0.4120659935594279 | LB=0.12; BP=0.572; White=0.292 | no | ARDL captures short- and long-run transmission under I(0)/I(1)-mix assumptions. |

### model_ardl_output_Model_Series

| standardized_type | source | week | price |
| --- | --- | --- | --- |
| butter | EU | 2021-12-28 00:00:00 | 181.9599584085987 |
| butter | EU | 2022-01-04 00:00:00 | 181.9599584085987 |
| butter | EU | 2022-01-11 00:00:00 | 182.3093215348751 |
| butter | EU | 2022-01-18 00:00:00 | 182.8200885225466 |
| butter | EU | 2022-01-25 00:00:00 | 184.2776415657501 |
| butter | EU | 2022-02-01 00:00:00 | 188.7173822459525 |
| butter | EU | 2022-02-08 00:00:00 | 188.8619315870532 |
| butter | EU | 2022-02-15 00:00:00 | 189.1146080195921 |
| butter | EU | 2022-02-22 00:00:00 | 196.7903444397339 |
| butter | EU | 2022-03-01 00:00:00 | 194.7985027873246 |
| butter | EU | 2022-03-08 00:00:00 | 196.6613221508721 |
| butter | EU | 2022-03-15 00:00:00 | 201.8132039162534 |
| butter | EU | 2022-03-22 00:00:00 | 206.171337558882 |
| butter | EU | 2022-03-29 00:00:00 | 212.9652461581115 |
| butter | EU | 2022-04-05 00:00:00 | 213.8829244376504 |
| butter | EU | 2022-04-12 00:00:00 | 216.3955538461629 |
| butter | EU | 2022-04-19 00:00:00 | 219.2128198306872 |
| butter | EU | 2022-04-26 00:00:00 | 212.710837448498 |
| butter | EU | 2022-05-03 00:00:00 | 213.3685718125327 |
| butter | EU | 2022-05-10 00:00:00 | 209.380191467247 |
| butter | EU | 2022-05-17 00:00:00 | 215.0727594097097 |
| butter | EU | 2022-05-24 00:00:00 | 220.2465593354796 |
| butter | EU | 2022-05-31 00:00:00 | 222.6935416882488 |
| butter | EU | 2022-06-07 00:00:00 | 222.4323242924934 |
| butter | EU | 2022-06-14 00:00:00 | 218.5355516966459 |

## Graphs

- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/model_ardl/ardl_short_run.png
