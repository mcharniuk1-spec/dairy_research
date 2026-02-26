# Primary VPT Chain: ProducerUA -> ProZorro -> Retail

## Interpretation Guide
- ADF p>0.05 and KPSS p<0.05 -> likely I(1)-like; prefer differences/cointegration models.
- ADF p<0.05 and KPSS p>0.05 -> stationary; level models are more admissible.
- Ljung-Box p<0.05 -> autocorrelation; add lag structure.
- BP/White p<0.05 -> heteroskedasticity; use robust or HAC standard errors.
- JB p<0.05 -> non-normality; use robust inference and avoid strict normality assumptions.
- Stability flag=1 -> potential breaks/drift; use rolling or split-sample robustness.
- For retail transmission, compare no-promo vs promo-controlled estimates.

## Notes
- standardized_type=milk
- retailer=silpo_novus
- promo_variant=promo_controlled
- frequency=daily
- Primary chain is strictly ProducerUA -> ProZorro -> Retail. Retail is estimated separately for silpo, novus, and silpo_novus. Combined rule: daily median of available silpo and novus standardized_type prices.

## Tables

### PreTests

| series | adf_level_p | kpss_level_p | adf_diff1_p | kpss_diff1_p | adf_diff2_p | kpss_diff2_p | integration_class | stability_flag | standardized_type | retailer | promo_variant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| producer | 0.012483062457831949 | 0.01 | 4.729732285866721e-13 | 0.1 | 1.068911264269411e-21 | 0.1 | I(1) | 1.0 | milk | silpo_novus | promo_controlled |
| prozorro | 0.0014111002754477221 | 0.01 | 3.8189780115701814e-13 | 0.1 | 4.4125656034645e-11 | 0.1 | I(1) | 0.0 | milk | silpo_novus | promo_controlled |
| retail | 0.9135252706786217 | 0.08526130462523543 | 0.1118185172729621 | 0.1 | 0.0034682897791077313 | 0.1 | I(2) | 0.0 | milk | silpo_novus | promo_controlled |
| producer_to_prozorro | nan | nan | nan | nan | nan | nan | pair | nan | milk | silpo_novus | promo_controlled |
| prozorro_to_retail | nan | nan | nan | nan | nan | nan | pair | nan | milk | silpo_novus | promo_controlled |
| producer_to_retail | nan | nan | nan | nan | nan | nan | pair | nan | milk | silpo_novus | promo_controlled |

### ModelCoefficients

| standardized_type | retailer | promo_variant | frequency | link | model_family | y_series | x_series | n_obs | sr_coef | lr_coef | ect_coef |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| milk | silpo_novus | promo_controlled | daily | none | none | n/a | n/a | 1803 | nan | nan | nan |

### ResidualDiagnostics

| model_family | link | y_series | x_series | ljungbox_p | arch_p | jb_p | unreliable_flag |
| --- | --- | --- | --- | --- | --- | --- | --- |
| none | none | n/a | n/a | nan | nan | nan | 1 |

### SeriesUsed

| date | producer | prozorro | retail | standardized_type | retailer | promo_variant | combined_rule |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021-02-01 00:00:00 | 4.889813923695362 | nan | nan | milk | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-02 00:00:00 | 4.880939529121857 | nan | nan | milk | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-03 00:00:00 | 4.873865236176802 | nan | nan | milk | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-04 00:00:00 | 4.868432562653949 | nan | nan | milk | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-05 00:00:00 | 4.864483026347049 | nan | nan | milk | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-06 00:00:00 | 4.861858145049856 | nan | nan | milk | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-07 00:00:00 | 4.860399436556123 | nan | nan | milk | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-08 00:00:00 | 4.8599484186596005 | nan | nan | milk | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-09 00:00:00 | 4.861523687586162 | nan | nan | milk | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-10 00:00:00 | 4.865852176359705 | nan | nan | milk | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-11 00:00:00 | 4.872337907971017 | nan | nan | milk | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-12 00:00:00 | 4.880384905410883 | nan | nan | milk | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-13 00:00:00 | 4.889397191670094 | nan | nan | milk | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-14 00:00:00 | 4.898778789739431 | nan | nan | milk | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-15 00:00:00 | 4.907933722609686 | nan | nan | milk | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-16 00:00:00 | 4.919261740789084 | nan | nan | milk | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-17 00:00:00 | 4.93424761149779 | nan | nan | milk | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-18 00:00:00 | 4.950922882794503 | nan | nan | milk | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-19 00:00:00 | 4.967319102737919 | nan | nan | milk | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-20 00:00:00 | 4.981467819386735 | nan | nan | milk | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-21 00:00:00 | 4.991400580799647 | nan | nan | milk | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-22 00:00:00 | 4.995148935035351 | nan | nan | milk | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-23 00:00:00 | 4.937254183107472 | nan | nan | milk | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-24 00:00:00 | 4.7879466649776745 | nan | nan | milk | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-25 00:00:00 | 4.583791487126728 | nan | nan | milk | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |

### LagProfile

| pair | lag | corr |
| --- | --- | --- |
| producer_to_prozorro | 1 | -0.1619954987840599 |
| producer_to_prozorro | 2 | -0.1596960610741088 |
| producer_to_prozorro | 3 | -0.1550755940895887 |
| producer_to_prozorro | 4 | -0.14782606735994822 |
| producer_to_prozorro | 5 | -0.13755773452175912 |
| producer_to_prozorro | 6 | -0.12184188698467123 |
| producer_to_prozorro | 7 | -0.1052691917763927 |
| producer_to_prozorro | 8 | -0.08910616067044506 |
| producer_to_prozorro | 9 | -0.07590716773933302 |
| producer_to_prozorro | 10 | -0.06623846374994181 |
| producer_to_prozorro | 11 | -0.0604388966635031 |
| producer_to_prozorro | 12 | -0.053445772573508486 |
| producer_to_prozorro | 13 | -0.044442939499120704 |
| producer_to_prozorro | 14 | -0.03488503971137872 |
| producer_to_prozorro | 15 | -0.027271625330034636 |
| producer_to_prozorro | 16 | -0.02250000775439031 |
| producer_to_prozorro | 17 | -0.021139446186402542 |
| producer_to_prozorro | 18 | -0.017275889530894442 |
| producer_to_prozorro | 19 | -0.0052249478693689524 |
| producer_to_prozorro | 20 | 0.012485029223047036 |
| producer_to_prozorro | 21 | 0.03347787604499084 |
| producer_to_prozorro | 22 | 0.05374998643553993 |
| producer_to_prozorro | 23 | 0.06948873713684375 |
| producer_to_prozorro | 24 | 0.07823993038535337 |
| producer_to_prozorro | 25 | 0.08172443030355239 |

### ModelEligibility

| standardized_type | retailer | promo_variant | frequency | integration_producer | integration_prozorro | integration_retail | n_obs_producer | n_obs_prozorro | n_obs_retail | n_obs_pair_prod_prozorro | n_obs_pair_prozorro_retail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| milk | silpo_novus | promo_controlled | daily | I(1) | I(1) | I(2) | 1793 | 211 | 59 | 201 | 48 |

### NARDL_Multipliers

_No rows_

### VECM_IRF

_No rows_

## Graphs

- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/milk/silpo_novus/time_series_promo_controlled.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/milk/silpo_novus/lag_profile_promo_controlled.png
