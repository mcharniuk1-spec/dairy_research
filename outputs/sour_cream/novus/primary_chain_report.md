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
- standardized_type=sour_cream
- retailer=novus
- promo_variant=promo_controlled
- frequency=daily
- Primary chain is strictly ProducerUA -> ProZorro -> Retail. Retail is estimated separately for silpo, novus, and silpo_novus. Combined rule: daily median of available silpo and novus standardized_type prices.

## Tables

### PreTests

| series | adf_level_p | kpss_level_p | adf_diff1_p | kpss_diff1_p | adf_diff2_p | kpss_diff2_p | integration_class | stability_flag | standardized_type | retailer | promo_variant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| producer | 0.014081535169907735 | 0.01 | 4.706435460154828e-13 | 0.1 | 3.085032729165042e-21 | 0.1 | I(1) | 1.0 | sour_cream | novus | promo_controlled |
| prozorro | 0.21880956753864628 | 0.04947047925942609 | 2.411890357322739e-12 | 0.1 | 3.969186107838014e-13 | 0.1 | I(1) | 0.0 | sour_cream | novus | promo_controlled |
| retail | nan | nan | nan | nan | nan | nan | ambiguous | 0.0 | sour_cream | novus | promo_controlled |
| producer_to_prozorro | nan | nan | nan | nan | nan | nan | pair | nan | sour_cream | novus | promo_controlled |
| prozorro_to_retail | nan | nan | nan | nan | nan | nan | pair | nan | sour_cream | novus | promo_controlled |
| producer_to_retail | nan | nan | nan | nan | nan | nan | pair | nan | sour_cream | novus | promo_controlled |

### ModelCoefficients

| standardized_type | retailer | promo_variant | frequency | link | model_family | y_series | x_series | n_obs | sr_coef | lr_coef | ect_coef |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sour_cream | novus | promo_controlled | daily | producer_to_prozorro | ARDL | prozorro | producer | 178 | 0.1503321327484457 | 0.53201805897649 | nan |
| sour_cream | novus | promo_controlled | daily | producer_to_prozorro | NARDL | prozorro | producer | 176 | 0.8049124174362647 | 0.3181803694069162 | -0.9103202976511395 |

### ResidualDiagnostics

| model_family | link | y_series | x_series | ljungbox_p | arch_p | jb_p | unreliable_flag |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ARDL | producer_to_prozorro | prozorro | producer | 0.9991919902903724 | 0.4332665662567991 | 0.028152037118155036 | 0 |
| NARDL | producer_to_prozorro | prozorro | producer | 0.0725257366713705 | 0.012783066753899433 | 0.03261969684847455 | 1 |

### SeriesUsed

| date | producer | prozorro | retail | standardized_type | retailer | promo_variant | combined_rule |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021-02-01 00:00:00 | 12.7168318078645 | nan | nan | sour_cream | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-02 00:00:00 | 12.72632554286918 | nan | nan | sour_cream | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-03 00:00:00 | 12.73569490777093 | nan | nan | sour_cream | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-04 00:00:00 | 12.74493705667296 | nan | nan | sour_cream | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-05 00:00:00 | 12.75404914367847 | nan | nan | sour_cream | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-06 00:00:00 | 12.76302832289066 | nan | nan | sour_cream | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-07 00:00:00 | 12.77187174841275 | nan | nan | sour_cream | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-08 00:00:00 | 12.78057657434793 | nan | nan | sour_cream | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-09 00:00:00 | 12.78861583935331 | nan | nan | sour_cream | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-10 00:00:00 | 12.79582084628455 | nan | nan | sour_cream | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-11 00:00:00 | 12.80272614554264 | nan | nan | sour_cream | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-12 00:00:00 | 12.80986628752861 | nan | nan | sour_cream | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-13 00:00:00 | 12.81777582264346 | nan | nan | sour_cream | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-14 00:00:00 | 12.8269893012882 | nan | nan | sour_cream | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-15 00:00:00 | 12.83804127386385 | nan | nan | sour_cream | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-16 00:00:00 | 12.85602638141248 | nan | nan | sour_cream | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-17 00:00:00 | 12.88286036370906 | nan | nan | sour_cream | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-18 00:00:00 | 12.91430941925396 | nan | nan | sour_cream | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-19 00:00:00 | 12.94613974654752 | nan | nan | sour_cream | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-20 00:00:00 | 12.97411754409009 | nan | nan | sour_cream | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-21 00:00:00 | 12.99400901038205 | nan | nan | sour_cream | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-22 00:00:00 | 13.00158034392373 | nan | nan | sour_cream | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-23 00:00:00 | 12.85209968138777 | nan | nan | sour_cream | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-24 00:00:00 | 12.46659692011084 | nan | nan | sour_cream | novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-25 00:00:00 | 11.93948089958932 | nan | nan | sour_cream | novus | promo_controlled | daily_median_of_available_silpo_novus |

### LagProfile

| pair | lag | corr |
| --- | --- | --- |
| producer_to_prozorro | 1 | 0.07433869937437788 |
| producer_to_prozorro | 2 | 0.06992193974139833 |
| producer_to_prozorro | 3 | 0.05247780353970976 |
| producer_to_prozorro | 4 | 0.03707093523380621 |
| producer_to_prozorro | 5 | 0.04488476174629457 |
| producer_to_prozorro | 6 | 0.03942159255359992 |
| producer_to_prozorro | 7 | 0.04774350069192749 |
| producer_to_prozorro | 8 | 0.055533922878419725 |
| producer_to_prozorro | 9 | 0.05815494362517447 |
| producer_to_prozorro | 10 | 0.05835686030753 |
| producer_to_prozorro | 11 | 0.05572808262664563 |
| producer_to_prozorro | 12 | 0.05132684090763728 |
| producer_to_prozorro | 13 | 0.0478799443885565 |
| producer_to_prozorro | 14 | 0.0459078796867533 |
| producer_to_prozorro | 15 | 0.04627227965570159 |
| producer_to_prozorro | 16 | 0.04980743752852967 |
| producer_to_prozorro | 17 | 0.05457381656925348 |
| producer_to_prozorro | 18 | 0.05403494026121064 |
| producer_to_prozorro | 19 | 0.045342075346488105 |
| producer_to_prozorro | 20 | 0.030030963601459588 |
| producer_to_prozorro | 21 | 0.011140301716297355 |
| producer_to_prozorro | 22 | -0.006115614807159968 |
| producer_to_prozorro | 23 | -0.017626157690186797 |
| producer_to_prozorro | 24 | -0.022831222527256615 |
| producer_to_prozorro | 25 | -0.024681880076761423 |

### ModelEligibility

| standardized_type | retailer | promo_variant | frequency | integration_producer | integration_prozorro | integration_retail | n_obs_producer | n_obs_prozorro | n_obs_retail | n_obs_pair_prod_prozorro | n_obs_pair_prozorro_retail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sour_cream | novus | promo_controlled | daily | I(1) | I(1) | ambiguous | 1793 | 188 | 13 | 178 | 12 |

### NARDL_Multipliers

| horizon | mult_pos | mult_neg | link |
| --- | --- | --- | --- |
| 0 | 0.5272629908128263 | -0.27764942662343833 | producer_to_prozorro |
| 1 | 0.5660151486488385 | -0.29805577903403124 | producer_to_prozorro |
| 2 | 0.5688633093639157 | -0.2995555812262039 | producer_to_prozorro |
| 3 | 0.5690726401447521 | -0.2996658119313484 | producer_to_prozorro |
| 4 | 0.5690880252933407 | -0.29967391353862705 | producer_to_prozorro |
| 5 | 0.5690891560529745 | -0.29967450898107123 | producer_to_prozorro |
| 6 | 0.5690892391602219 | -0.2996745527442027 | producer_to_prozorro |
| 7 | 0.569089245268341 | -0.29967455596065407 | producer_to_prozorro |
| 8 | 0.5690892457172685 | -0.2996745561970531 | producer_to_prozorro |
| 9 | 0.5690892457502632 | -0.2996745562144276 | producer_to_prozorro |
| 10 | 0.5690892457526882 | -0.2996745562157046 | producer_to_prozorro |
| 11 | 0.5690892457528665 | -0.29967455621579847 | producer_to_prozorro |
| 12 | 0.5690892457528796 | -0.29967455621580535 | producer_to_prozorro |
| 13 | 0.5690892457528804 | -0.29967455621580585 | producer_to_prozorro |
| 14 | 0.5690892457528806 | -0.2996745562158059 | producer_to_prozorro |
| 15 | 0.5690892457528806 | -0.2996745562158059 | producer_to_prozorro |
| 16 | 0.5690892457528806 | -0.2996745562158059 | producer_to_prozorro |
| 17 | 0.5690892457528806 | -0.2996745562158059 | producer_to_prozorro |
| 18 | 0.5690892457528806 | -0.2996745562158059 | producer_to_prozorro |
| 19 | 0.5690892457528806 | -0.2996745562158059 | producer_to_prozorro |
| 20 | 0.5690892457528806 | -0.2996745562158059 | producer_to_prozorro |

### VECM_IRF

_No rows_

## Graphs

- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/sour_cream/novus/time_series_promo_controlled.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/sour_cream/novus/lag_profile_promo_controlled.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/sour_cream/novus/nardl_multipliers_promo_controlled.png
