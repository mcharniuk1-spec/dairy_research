# RW3 Module Report - model_discounts

## Interpretation Guide
- ADF p>0.05 and KPSS p<0.05 -> likely I(1)-like; prefer differences/cointegration models.
- ADF p<0.05 and KPSS p>0.05 -> stationary; level models are more admissible.
- Ljung-Box p<0.05 -> autocorrelation; add lag structure.
- BP/White p<0.05 -> heteroskedasticity; use robust or HAC standard errors.
- JB p<0.05 -> non-normality; use robust inference and avoid strict normality assumptions.
- Stability flag=1 -> potential breaks/drift; use rolling or split-sample robustness.
- For retail transmission, compare no-promo vs promo-controlled estimates.

## Notes
- module=model_discounts
- xlsx_files=1
- png_files=2
- Interpretation: read test diagnostics first, then coefficients/effects with robustness context.

## Tables

### model_discounts_output_Silpo_Di

| standardized_type | n_obs | model | interpretation_note |
| --- | --- | --- | --- |
| nan | 0 | ols_hc1 | Insufficient discounted observations for depth model. |

### model_discounts_output_Silpo_Tr

| standardized_type | n_obs | coef_EU_no_promo | coef_EU_with_promo | coef_Producer_no_promo | coef_Producer_with_promo | delta_EU | delta_Producer | promo_coef_present | promo_coef_depth | interpretation_note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| butter | 33 | 1.535644521267677 | -1.660182202847171 | -3.999278302034052 | 1.766933115146946 | -3.195826724114848 | 5.766211417180998 | -0.8947798337292888 | 0 | Difference between no-promo and promo-controlled pass-through. |
| cream | 33 | 1.543144113274722 | 1.41819009958284 | -2.828347575510229 | -2.764913204007323 | -0.1249540136918827 | 0.06343437150290576 | -0.1271753750785895 | 0 | Difference between no-promo and promo-controlled pass-through. |
| hard_cheese | 33 | -1.566095507221104 | 0.1552460384676559 | 0.6140932156535026 | -0.8329859269793987 | 1.72134154568876 | -1.447079142632901 | -0.3639259312553088 | 0 | Difference between no-promo and promo-controlled pass-through. |
| milk | 33 | 1.357731332296655 | 4.27157712515603 | -1.247354240050975 | -2.005255656927778 | 2.913845792859375 | -0.7579014168768037 | -0.6067609497040047 | 0 | Difference between no-promo and promo-controlled pass-through. |

## Graphs

- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/model_discounts/discount_delta_eu.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/separately RW3/outputs/model_discounts/discount_delta_producer.png
