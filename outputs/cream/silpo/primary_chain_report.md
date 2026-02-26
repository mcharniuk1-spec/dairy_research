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
- retailer=silpo
- promo_variant=promo_controlled
- frequency=daily
- Primary chain is strictly ProducerUA -> ProZorro -> Retail. Retail is estimated separately for silpo, novus, and silpo_novus. Combined rule: daily median of available silpo and novus standardized_type prices.

## Tables

### PreTests

| series | adf_level_p | kpss_level_p | adf_diff1_p | kpss_diff1_p | adf_diff2_p | kpss_diff2_p | integration_class | stability_flag | standardized_type | retailer | promo_variant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| producer | 3.1663521310609106e-05 | 0.01 | 1.807358615624225e-13 | 0.1 | 2.250471045105603e-20 | 0.1 | I(1) | 1.0 | cream | silpo | promo_controlled |
| prozorro | 5.15934840442518e-22 | 0.1 | 3.6046356335359884e-13 | 0.1 | 1.1693001750830719e-11 | 0.09309066682789993 | I(0) | 0.0 | cream | silpo | promo_controlled |
| retail | 0.0801729662500495 | 0.1 | 0.0004821332512077595 | 0.1 | 4.135571752859827e-05 | 0.1 | I(1) | 0.0 | cream | silpo | promo_controlled |
| producer_to_prozorro | nan | nan | nan | nan | nan | nan | pair | nan | cream | silpo | promo_controlled |
| prozorro_to_retail | nan | nan | nan | nan | nan | nan | pair | nan | cream | silpo | promo_controlled |
| producer_to_retail | nan | nan | nan | nan | nan | nan | pair | nan | cream | silpo | promo_controlled |

### ModelCoefficients

| standardized_type | retailer | promo_variant | frequency | link | model_family | y_series | x_series | n_obs | sr_coef | lr_coef | ect_coef |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| cream | silpo | promo_controlled | daily | producer_to_prozorro | NARDL | prozorro | producer | 197 | 3.7936802523963236 | 0.33453408711897387 | -1.002572700947699 |
| cream | silpo | promo_controlled | daily | prozorro_to_retail | ARDL | retail | prozorro | 42 | -0.027190870499124387 | -0.2713968465337292 | nan |
| cream | silpo | promo_controlled | daily | prozorro_to_retail | NARDL | retail | prozorro | 40 | -0.070469572016711 | -0.23542918833682522 | -0.539409399232454 |

### ResidualDiagnostics

| model_family | link | y_series | x_series | ljungbox_p | arch_p | jb_p | unreliable_flag |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NARDL | producer_to_prozorro | prozorro | producer | 0.889712370853929 | 0.2018078467373643 | 1.393192716168525e-262 | 0 |
| ARDL | prozorro_to_retail | retail | prozorro | 0.004919229359110526 | 0.5840482434798735 | 0.8870969508504547 | 1 |
| NARDL | prozorro_to_retail | retail | prozorro | 0.5530832153948084 | 0.6339111636110053 | 0.7966413904775785 | 0 |

### SeriesUsed

| date | producer | prozorro | retail | standardized_type | retailer | promo_variant | combined_rule |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021-02-01 00:00:00 | 16.55928516245106 | nan | nan | cream | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-02 00:00:00 | 16.56413671316524 | nan | nan | cream | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-03 00:00:00 | 16.56910996285577 | nan | nan | cream | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-04 00:00:00 | 16.57420126019822 | nan | nan | cream | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-05 00:00:00 | 16.57940695386814 | nan | nan | cream | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-06 00:00:00 | 16.58472339254112 | nan | nan | cream | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-07 00:00:00 | 16.5901469248927 | nan | nan | cream | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-08 00:00:00 | 16.59567389959844 | nan | nan | cream | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-09 00:00:00 | 16.60133523107501 | nan | nan | cream | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-10 00:00:00 | 16.60715014958769 | nan | nan | cream | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-11 00:00:00 | 16.61309747758499 | nan | nan | cream | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-12 00:00:00 | 16.61915603751542 | nan | nan | cream | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-13 00:00:00 | 16.62530465182749 | nan | nan | cream | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-14 00:00:00 | 16.63152214296973 | nan | nan | cream | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-15 00:00:00 | 16.63778733339064 | nan | nan | cream | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-16 00:00:00 | 16.64495111861826 | nan | nan | cream | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-17 00:00:00 | 16.65331829474998 | nan | nan | cream | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-18 00:00:00 | 16.66204853508837 | nan | nan | cream | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-19 00:00:00 | 16.67030151293599 | nan | nan | cream | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-20 00:00:00 | 16.6772369015954 | nan | nan | cream | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-21 00:00:00 | 16.68201437436917 | nan | nan | cream | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-22 00:00:00 | 16.68379360455986 | nan | nan | cream | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-23 00:00:00 | 16.50269387396052 | nan | nan | cream | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-24 00:00:00 | 16.03564720030959 | nan | nan | cream | silpo | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-25 00:00:00 | 15.39703236082771 | nan | nan | cream | silpo | promo_controlled | daily_median_of_available_silpo_novus |

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
| cream | silpo | promo_controlled | daily | I(1) | I(0) | I(1) | 1793 | 209 | 48 | 199 | 42 |

### NARDL_Multipliers

| horizon | mult_pos | mult_neg | link |
| --- | --- | --- | --- |
| 0 | 2.9056194294341315 | -0.8880608229621922 | producer_to_prozorro |
| 1 | 3.166679443444792 | -0.9678500646420563 | producer_to_prozorro |
| 2 | 3.1901347969659235 | -0.9750188563770777 | producer_to_prozorro |
| 3 | 3.192242180629738 | -0.9756629479094464 | producer_to_prozorro |
| 4 | 3.1924315218776758 | -0.9757208173409214 | producer_to_prozorro |
| 5 | 3.1924485335442205 | -0.9757260167123321 | producer_to_prozorro |
| 6 | 3.192450061984546 | -0.975726483858153 | producer_to_prozorro |
| 7 | 3.192450199309706 | -0.9757265258296146 | producer_to_prozorro |
| 8 | 3.192450211647904 | -0.9757265296006076 | producer_to_prozorro |
| 9 | 3.1924502127564494 | -0.9757265299394184 | producer_to_prozorro |
| 10 | 3.1924502128560484 | -0.9757265299698594 | producer_to_prozorro |
| 11 | 3.1924502128649968 | -0.9757265299725945 | producer_to_prozorro |
| 12 | 3.192450212865801 | -0.9757265299728402 | producer_to_prozorro |
| 13 | 3.192450212865873 | -0.9757265299728622 | producer_to_prozorro |
| 14 | 3.1924502128658796 | -0.9757265299728642 | producer_to_prozorro |
| 15 | 3.19245021286588 | -0.9757265299728644 | producer_to_prozorro |
| 16 | 3.19245021286588 | -0.9757265299728645 | producer_to_prozorro |
| 17 | 3.19245021286588 | -0.9757265299728645 | producer_to_prozorro |
| 18 | 3.19245021286588 | -0.9757265299728645 | producer_to_prozorro |
| 19 | 3.19245021286588 | -0.9757265299728645 | producer_to_prozorro |
| 20 | 3.19245021286588 | -0.9757265299728645 | producer_to_prozorro |
| 0 | 0.0464158882449621 | 0.1168854602616731 | prozorro_to_retail |
| 1 | 0.03956155280035692 | 0.09962472943169626 | prozorro_to_retail |
| 2 | 0.040573747463943266 | 0.1021736591969376 | prozorro_to_retail |
| 3 | 0.04042427447049661 | 0.10179725317959507 | prozorro_to_retail |

### VECM_IRF

_No rows_

## Graphs

- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/cream/silpo/time_series_promo_controlled.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/cream/silpo/lag_profile_promo_controlled.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/cream/silpo/nardl_multipliers_promo_controlled.png
