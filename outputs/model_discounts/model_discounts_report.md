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
- occ_rows=1
- depth_rows=1
- trans_rows=1
- Interpretation option: module compares observed vs promo-controlled primary-chain transmission (Silpo only).

## Tables

### Silpo_Transmission_PromoCtrl

| note |
| --- |
| No primary-chain silpo rows available to build discount comparison. |

### Silpo_Discounts_Occurrence

| note |
| --- |
| No rows |

### Silpo_Discounts_Depth

| note |
| --- |
| No rows |

## Graphs

- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/model_discounts/discount_delta_producer.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/model_discounts/discount_delta_eu.png
