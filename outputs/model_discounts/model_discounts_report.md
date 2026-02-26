# Silpo Discount Models

## Interpretation Guide
- ADF p>0.05 and KPSS p<0.05 -> likely I(1)-like; prefer differences/cointegration models.
- ADF p<0.05 and KPSS p>0.05 -> stationary; level models are more admissible.
- Ljung-Box p<0.05 -> autocorrelation; add lag structure.
- BP/White p<0.05 -> heteroskedasticity; use robust or HAC standard errors.
- JB p<0.05 -> non-normality; use robust inference and avoid strict normality assumptions.
- Stability flag=1 -> potential breaks/drift; use rolling or split-sample robustness.
- For retail transmission, compare no-promo vs promo-controlled estimates.

## Notes
- occ_rows=12
- depth_rows=12
- trans_rows=12
- Interpretation option: module compares observed vs promo-controlled primary-chain transmission (Silpo only).

## Tables

### Silpo_Transmission_PromoCtrl

| standardized_type | model_family | link | coef_observed | coef_promo_controlled | delta_promo_control | note |
| --- | --- | --- | --- | --- | --- | --- |
| butter | ARDL | prozorro_to_retail | 0.2001943602714764 | 0.2001943602714764 | 0.0 | positive delta means stronger transmission after promo control |
| butter | NARDL | prozorro_to_retail | 0.04860976737983126 | 0.04860976737983126 | 0.0 | positive delta means stronger transmission after promo control |
| cream | ARDL | prozorro_to_retail | -0.02719087049912439 | -0.02719087049912439 | 0.0 | positive delta means stronger transmission after promo control |
| cream | NARDL | prozorro_to_retail | -0.070469572016711 | -0.070469572016711 | 0.0 | positive delta means stronger transmission after promo control |
| hard_cheese | ARDL | prozorro_to_retail | 1.045350879786881 | 1.045350879786881 | 0.0 | positive delta means stronger transmission after promo control |
| hard_cheese | NARDL | prozorro_to_retail | 0.03093538709143862 | 0.03093538709143862 | 0.0 | positive delta means stronger transmission after promo control |
| milk | ECM | prozorro_to_retail | 0.03780420860354025 | 0.03780420860354025 | 0.0 | positive delta means stronger transmission after promo control |
| milk | NARDL | prozorro_to_retail | 0.1309588230301683 | 0.1309588230301683 | 0.0 | positive delta means stronger transmission after promo control |
| other | ARDL | prozorro_to_retail | 5.213950941002082 | 5.213950941002082 | 0.0 | positive delta means stronger transmission after promo control |
| other | NARDL | prozorro_to_retail | 0.9816109260310832 | 0.9816109260310832 | 0.0 | positive delta means stronger transmission after promo control |
| sour_cream | ARDL | prozorro_to_retail | -0.09602698663315934 | -0.09602698663315934 | 0.0 | positive delta means stronger transmission after promo control |
| sour_cream | NARDL | prozorro_to_retail | -0.02591699786459659 | -0.02591699786459659 | 0.0 | positive delta means stronger transmission after promo control |

### Silpo_Discounts_Occurrence

| standardized_type | promo_signal | definition |
| --- | --- | --- |
| butter | 0 | 1 if /promo-controlled - observed/ > 0.02 |
| butter | 0 | 1 if /promo-controlled - observed/ > 0.02 |
| cream | 0 | 1 if /promo-controlled - observed/ > 0.02 |
| cream | 0 | 1 if /promo-controlled - observed/ > 0.02 |
| hard_cheese | 0 | 1 if /promo-controlled - observed/ > 0.02 |
| hard_cheese | 0 | 1 if /promo-controlled - observed/ > 0.02 |
| milk | 0 | 1 if /promo-controlled - observed/ > 0.02 |
| milk | 0 | 1 if /promo-controlled - observed/ > 0.02 |
| other | 0 | 1 if /promo-controlled - observed/ > 0.02 |
| other | 0 | 1 if /promo-controlled - observed/ > 0.02 |
| sour_cream | 0 | 1 if /promo-controlled - observed/ > 0.02 |
| sour_cream | 0 | 1 if /promo-controlled - observed/ > 0.02 |

### Silpo_Discounts_Depth

| standardized_type | promo_depth_proxy | definition |
| --- | --- | --- |
| butter | 0.0 | absolute difference between promo-controlled and observed SR coefficients |
| butter | 0.0 | absolute difference between promo-controlled and observed SR coefficients |
| cream | 0.0 | absolute difference between promo-controlled and observed SR coefficients |
| cream | 0.0 | absolute difference between promo-controlled and observed SR coefficients |
| hard_cheese | 0.0 | absolute difference between promo-controlled and observed SR coefficients |
| hard_cheese | 0.0 | absolute difference between promo-controlled and observed SR coefficients |
| milk | 0.0 | absolute difference between promo-controlled and observed SR coefficients |
| milk | 0.0 | absolute difference between promo-controlled and observed SR coefficients |
| other | 0.0 | absolute difference between promo-controlled and observed SR coefficients |
| other | 0.0 | absolute difference between promo-controlled and observed SR coefficients |
| sour_cream | 0.0 | absolute difference between promo-controlled and observed SR coefficients |
| sour_cream | 0.0 | absolute difference between promo-controlled and observed SR coefficients |

## Graphs

- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/model_discounts/discount_delta_producer.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/model_discounts/discount_delta_eu.png
