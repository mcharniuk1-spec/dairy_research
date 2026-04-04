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
- retailer=silpo
- promo_variant=promo_controlled
- frequency=daily
- Primary chain is strictly ProducerUA -> ProZorro -> Retail. Retail is estimated separately for silpo, novus, and silpo_novus. Combined rule: daily median of available silpo and novus standardized_type prices.

## Tables

### PreTests

| series | adf_level_p | kpss_level_p | adf_diff1_p | kpss_diff1_p | adf_diff2_p | kpss_diff2_p | integration_class | stability_flag | standardized_type | retailer | promo_variant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| producer | 0.01408153516990551 | 0.01 | 4.706435460152205e-13 | 0.1 | 3.085032729165153e-21 | 0.1 | I(1) | 1.0 | sour_cream | silpo | promo_controlled |
| prozorro | 0.21880956753864866 | 0.04947047925942609 | 2.411890357322739e-12 | 0.1 | 3.969186107841103e-13 | 0.1 | I(1) | 0.0 | sour_cream | silpo | promo_controlled |
| retail | 0.0001866404404338293 | 0.1 | 1.2992938855568006e-06 | 0.1 | 1.670971302457964e-10 | 0.1 | I(0) | 0.0 | sour_cream | silpo | promo_controlled |
| producer_to_prozorro | nan | nan | nan | nan | nan | nan | pair | nan | sour_cream | silpo | promo_controlled |
| prozorro_to_retail | nan | nan | nan | nan | nan | nan | pair | nan | sour_cream | silpo | promo_controlled |
| producer_to_retail | nan | nan | nan | nan | nan | nan | pair | nan | sour_cream | silpo | promo_controlled |

### ModelCoefficients

| standardized_type | retailer | promo_variant | frequency | link | model_family | y_series | x_series | n_obs | sr_coef | lr_coef | ect_coef |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sour_cream | silpo | promo_controlled | daily | producer_to_prozorro | ARDL | prozorro | producer | 178 | 0.15033213274852208 | 0.532018058976545 | nan |
| sour_cream | silpo | promo_controlled | daily | producer_to_prozorro | NARDL | prozorro | producer | 176 | 0.8049124174362638 | 0.31818036940691613 | -0.9103202976511392 |
| sour_cream | silpo | promo_controlled | daily | prozorro_to_retail | ARDL | retail | prozorro | 38 | -0.09602698663316289 | -0.07808211302448108 | nan |
| sour_cream | silpo | promo_controlled | daily | prozorro_to_retail | NARDL | retail | prozorro | 36 | -0.025916997864596635 | -0.022225374920711808 | -0.8330689213690317 |

### ResidualDiagnostics

| model_family | link | y_series | x_series | ljungbox_p | arch_p | jb_p | unreliable_flag |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ARDL | producer_to_prozorro | prozorro | producer | 0.9991919902903723 | 0.4332665662563698 | 0.028152037118156784 | 0 |
| NARDL | producer_to_prozorro | prozorro | producer | 0.07252573667137008 | 0.012783066753899843 | 0.032619696848474544 | 1 |
| ARDL | prozorro_to_retail | retail | prozorro | 0.9055231898701895 | 1.0 | 3.661771980151874e-23 | 0 |
| NARDL | prozorro_to_retail | retail | prozorro | 0.7865388890305405 | 0.33444920538763856 | 0.29874884459634815 | 0 |

### SeriesUsed

| date | producer | prozorro | retail | standardized_type | retailer | promo_variant | combined_rule |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021-02-01 00:00:00 | 12.7168318078645 | nan | nan | sour_cream | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-02 00:00:00 | 12.72632554286918 | nan | nan | sour_cream | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-03 00:00:00 | 12.73569490777093 | nan | nan | sour_cream | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-04 00:00:00 | 12.74493705667296 | nan | nan | sour_cream | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-05 00:00:00 | 12.75404914367847 | nan | nan | sour_cream | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-06 00:00:00 | 12.76302832289066 | nan | nan | sour_cream | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-07 00:00:00 | 12.77187174841275 | nan | nan | sour_cream | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-08 00:00:00 | 12.78057657434793 | nan | nan | sour_cream | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-09 00:00:00 | 12.78861583935331 | nan | nan | sour_cream | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-10 00:00:00 | 12.79582084628455 | nan | nan | sour_cream | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-11 00:00:00 | 12.80272614554264 | nan | nan | sour_cream | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-12 00:00:00 | 12.80986628752861 | nan | nan | sour_cream | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-13 00:00:00 | 12.81777582264346 | nan | nan | sour_cream | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-14 00:00:00 | 12.8269893012882 | nan | nan | sour_cream | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-15 00:00:00 | 12.83804127386385 | nan | nan | sour_cream | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-16 00:00:00 | 12.85602638141248 | nan | nan | sour_cream | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-17 00:00:00 | 12.88286036370906 | nan | nan | sour_cream | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-18 00:00:00 | 12.91430941925396 | nan | nan | sour_cream | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-19 00:00:00 | 12.94613974654752 | nan | nan | sour_cream | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-20 00:00:00 | 12.97411754409009 | nan | nan | sour_cream | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-21 00:00:00 | 12.99400901038205 | nan | nan | sour_cream | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-22 00:00:00 | 13.00158034392373 | nan | nan | sour_cream | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-23 00:00:00 | 12.85209968138777 | nan | nan | sour_cream | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-24 00:00:00 | 12.46659692011084 | nan | nan | sour_cream | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-25 00:00:00 | 11.93948089958932 | nan | nan | sour_cream | silpo | promo_controlled | daily_median_of_available_silpo_novus |

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
| sour_cream | silpo | promo_controlled | daily | I(1) | I(1) | I(0) | 1793 | 188 | 48 | 178 | 38 |

### NARDL_Multipliers

| horizon | mult_pos | mult_neg | link |
| --- | --- | --- | --- |
| 0 | 0.5272629908128266 | -0.2776494266234373 | producer_to_prozorro |
| 1 | 0.5660151486488386 | -0.2980557790340301 | producer_to_prozorro |
| 2 | 0.5688633093639158 | -0.29955558122620274 | producer_to_prozorro |
| 3 | 0.5690726401447522 | -0.29966581193134717 | producer_to_prozorro |
| 4 | 0.5690880252933408 | -0.2996739135386258 | producer_to_prozorro |
| 5 | 0.5690891560529747 | -0.29967450898107 | producer_to_prozorro |
| 6 | 0.569089239160222 | -0.29967455274420146 | producer_to_prozorro |
| 7 | 0.5690892452683411 | -0.29967455596065284 | producer_to_prozorro |
| 8 | 0.5690892457172686 | -0.29967455619705186 | producer_to_prozorro |
| 9 | 0.5690892457502633 | -0.2996745562144264 | producer_to_prozorro |
| 10 | 0.5690892457526884 | -0.2996745562157034 | producer_to_prozorro |
| 11 | 0.5690892457528666 | -0.29967455621579725 | producer_to_prozorro |
| 12 | 0.5690892457528797 | -0.29967455621580413 | producer_to_prozorro |
| 13 | 0.5690892457528807 | -0.29967455621580463 | producer_to_prozorro |
| 14 | 0.5690892457528807 | -0.2996745562158047 | producer_to_prozorro |
| 15 | 0.5690892457528807 | -0.2996745562158047 | producer_to_prozorro |
| 16 | 0.5690892457528807 | -0.2996745562158047 | producer_to_prozorro |
| 17 | 0.5690892457528807 | -0.2996745562158047 | producer_to_prozorro |
| 18 | 0.5690892457528807 | -0.2996745562158047 | producer_to_prozorro |
| 19 | 0.5690892457528807 | -0.2996745562158047 | producer_to_prozorro |
| 20 | 0.5690892457528807 | -0.2996745562158047 | producer_to_prozorro |
| 0 | 0.003140200025901027 | 0.02905719789049766 | prozorro_to_retail |
| 1 | 0.0030683005116296557 | 0.028391890458747533 | prozorro_to_retail |
| 2 | 0.0030699467571267004 | 0.0284071236543368 | prozorro_to_retail |
| 3 | 0.0030699090639063216 | 0.028406774867840833 | prozorro_to_retail |

### VECM_IRF

_No rows_

## Graphs

- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/sour_cream/silpo/time_series_promo_controlled.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/sour_cream/silpo/lag_profile_promo_controlled.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/sour_cream/silpo/nardl_multipliers_promo_controlled.png
