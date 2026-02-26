# ECM Summary from Primary Chain

## Interpretation Guide
- ADF p>0.05 and KPSS p<0.05 -> likely I(1)-like; prefer differences/cointegration models.
- ADF p<0.05 and KPSS p>0.05 -> stationary; level models are more admissible.
- Ljung-Box p<0.05 -> autocorrelation; add lag structure.
- BP/White p<0.05 -> heteroskedasticity; use robust or HAC standard errors.
- JB p<0.05 -> non-normality; use robust inference and avoid strict normality assumptions.
- Stability flag=1 -> potential breaks/drift; use rolling or split-sample robustness.
- For retail transmission, compare no-promo vs promo-controlled estimates.

## Notes
- Primary chain is strictly ProducerUA -> ProZorro -> Retail. Retail is estimated separately for silpo, novus, and silpo_novus. Combined rule: daily median of available silpo and novus standardized_type prices.
- family=ECM
- rows=8
- source=/Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/primary_chain_summary/primary_chain_consolidated.xlsx

## Tables

### ECM_Summary

| standardized_type | retailer | promo_variant | frequency | link | model_family | y_series | x_series | n_obs | sr_coef | lr_coef | ect_coef |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| butter | silpo_novus | observed | daily | prozorro_to_retail | ECM | retail | prozorro | 49 | -0.01931753309263347 | -0.1130442477150289 | -0.5842642909954745 |
| butter | silpo_novus | promo_controlled | daily | prozorro_to_retail | ECM | retail | prozorro | 49 | -0.01931753309263347 | -0.1130442477150289 | -0.5842642909954745 |
| milk | silpo | observed | daily | producer_to_prozorro | ECM | prozorro | producer | 197 | -0.002155003969288638 | -0.3006834081052232 | -0.9538372381620318 |
| milk | silpo | observed | daily | prozorro_to_retail | ECM | retail | prozorro | 35 | 0.03780420860354025 | 0.07959450904544814 | -0.9002155090608189 |
| milk | silpo | promo_controlled | daily | producer_to_prozorro | ECM | prozorro | producer | 197 | -0.002155003969288638 | -0.3006834081052232 | -0.9538372381620318 |
| milk | silpo | promo_controlled | daily | prozorro_to_retail | ECM | retail | prozorro | 35 | 0.03780420860354025 | 0.07959450904544814 | -0.9002155090608189 |
| milk | novus | observed | daily | producer_to_prozorro | ECM | prozorro | producer | 197 | -0.002155003969288638 | -0.3006834081052232 | -0.9538372381620318 |
| milk | novus | promo_controlled | daily | producer_to_prozorro | ECM | prozorro | producer | 197 | -0.002155003969288638 | -0.3006834081052232 | -0.9538372381620318 |
