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
- standardized_type=cream
- retailer=silpo_novus
- promo_variant=promo_controlled
- frequency=daily
- Primary chain is strictly ProducerUA -> ProZorro -> Retail. Retail is estimated separately for silpo, novus, and silpo_novus. Combined rule: daily median of available silpo and novus standardized_type prices.

## Tables

### PreTests

| series | adf_level_p | kpss_level_p | adf_diff1_p | kpss_diff1_p | adf_diff2_p | kpss_diff2_p | integration_class | stability_flag | standardized_type | retailer | promo_variant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| producer | 3.1663521310609106e-05 | 0.01 | 1.807358615624225e-13 | 0.1 | 2.250471045105603e-20 | 0.1 | I(1) | 1.0 | cream | silpo_novus | promo_controlled |
| prozorro | 5.15934840442518e-22 | 0.1 | 3.6046356335359884e-13 | 0.1 | 1.1693001750830719e-11 | 0.09309066682789993 | I(0) | 0.0 | cream | silpo_novus | promo_controlled |
| retail | 0.9973149052836614 | 0.02241119506040381 | 0.062198401623127224 | 0.1 | 9.358690774180871e-07 | 0.1 | I(2) | 0.0 | cream | silpo_novus | promo_controlled |
| producer_to_prozorro | nan | nan | nan | nan | nan | nan | pair | nan | cream | silpo_novus | promo_controlled |
| prozorro_to_retail | nan | nan | nan | nan | nan | nan | pair | nan | cream | silpo_novus | promo_controlled |
| producer_to_retail | nan | nan | nan | nan | nan | nan | pair | nan | cream | silpo_novus | promo_controlled |

### ModelCoefficients

| standardized_type | retailer | promo_variant | frequency | link | model_family | y_series | x_series | n_obs | sr_coef | lr_coef | ect_coef |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cream | silpo_novus | promo_controlled | daily | none | none | n/a | n/a | 1803 | nan | nan | nan |

### ResidualDiagnostics

| model_family | link | y_series | x_series | ljungbox_p | arch_p | jb_p | unreliable_flag |
| --- | --- | --- | --- | --- | --- | --- | --- |
| none | none | n/a | n/a | nan | nan | nan | 1 |

### SeriesUsed

| date | producer | prozorro | retail | standardized_type | retailer | promo_variant | combined_rule |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021-02-01 00:00:00 | 16.55928516245106 | nan | nan | cream | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-02 00:00:00 | 16.56413671316524 | nan | nan | cream | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-03 00:00:00 | 16.56910996285577 | nan | nan | cream | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-04 00:00:00 | 16.57420126019822 | nan | nan | cream | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-05 00:00:00 | 16.57940695386814 | nan | nan | cream | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-06 00:00:00 | 16.58472339254112 | nan | nan | cream | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-07 00:00:00 | 16.5901469248927 | nan | nan | cream | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-08 00:00:00 | 16.59567389959844 | nan | nan | cream | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-09 00:00:00 | 16.60133523107501 | nan | nan | cream | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-10 00:00:00 | 16.60715014958769 | nan | nan | cream | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-11 00:00:00 | 16.61309747758499 | nan | nan | cream | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-12 00:00:00 | 16.61915603751542 | nan | nan | cream | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-13 00:00:00 | 16.62530465182749 | nan | nan | cream | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-14 00:00:00 | 16.63152214296973 | nan | nan | cream | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-15 00:00:00 | 16.63778733339064 | nan | nan | cream | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-16 00:00:00 | 16.64495111861826 | nan | nan | cream | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-17 00:00:00 | 16.65331829474998 | nan | nan | cream | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-18 00:00:00 | 16.66204853508837 | nan | nan | cream | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-19 00:00:00 | 16.67030151293599 | nan | nan | cream | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-20 00:00:00 | 16.6772369015954 | nan | nan | cream | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-21 00:00:00 | 16.68201437436917 | nan | nan | cream | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-22 00:00:00 | 16.68379360455986 | nan | nan | cream | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-23 00:00:00 | 16.50269387396052 | nan | nan | cream | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-24 00:00:00 | 16.03564720030959 | nan | nan | cream | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-25 00:00:00 | 15.39703236082771 | nan | nan | cream | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |

### LagProfile

| pair | lag | corr |
| --- | --- | --- |
| producer_to_prozorro | 1 | 0.06146229004493464 |
| producer_to_prozorro | 2 | 0.06187172383641456 |
| producer_to_prozorro | 3 | 0.06314532535711788 |
| producer_to_prozorro | 4 | 0.06320312979983103 |
| producer_to_prozorro | 5 | 0.06245313280573821 |
| producer_to_prozorro | 6 | 0.06282849386241454 |
| producer_to_prozorro | 7 | 0.06579244345091867 |
| producer_to_prozorro | 8 | 0.07036064213557568 |
| producer_to_prozorro | 9 | 0.0740021648388298 |
| producer_to_prozorro | 10 | 0.07999426010710693 |
| producer_to_prozorro | 11 | 0.08672309347422189 |
| producer_to_prozorro | 12 | 0.0955548834637671 |
| producer_to_prozorro | 13 | 0.10393825381312094 |
| producer_to_prozorro | 14 | 0.10980154996288898 |
| producer_to_prozorro | 15 | 0.11026586073085809 |
| producer_to_prozorro | 16 | 0.1040630388642432 |
| producer_to_prozorro | 17 | 0.09141072312581083 |
| producer_to_prozorro | 18 | 0.07741161321894428 |
| producer_to_prozorro | 19 | 0.06731513319302308 |
| producer_to_prozorro | 20 | 0.061079129894117214 |
| producer_to_prozorro | 21 | 0.05953068607471382 |
| producer_to_prozorro | 22 | 0.06072146887343792 |
| producer_to_prozorro | 23 | 0.05896910731704648 |
| producer_to_prozorro | 24 | 0.05122603053484502 |
| producer_to_prozorro | 25 | 0.040063549807138873 |

### ModelEligibility

| standardized_type | retailer | promo_variant | frequency | integration_producer | integration_prozorro | integration_retail | n_obs_producer | n_obs_prozorro | n_obs_retail | n_obs_pair_prod_prozorro | n_obs_pair_prozorro_retail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cream | silpo_novus | promo_controlled | daily | I(1) | I(0) | I(2) | 1793 | 209 | 55 | 199 | 48 |

### NARDL_Multipliers

_No rows_

### VECM_IRF

_No rows_

## Graphs

- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/cream/silpo_novus/time_series_promo_controlled.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/cream/silpo_novus/lag_profile_promo_controlled.png
