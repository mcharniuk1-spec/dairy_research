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
- standardized_type=hard_cheese
- retailer=silpo_novus
- promo_variant=promo_controlled
- frequency=daily
- Primary chain is strictly ProducerUA -> ProZorro -> Retail. Retail is estimated separately for silpo, novus, and silpo_novus. Combined rule: daily median of available silpo and novus standardized_type prices.

## Tables

### PreTests

| series | adf_level_p | kpss_level_p | adf_diff1_p | kpss_diff1_p | adf_diff2_p | kpss_diff2_p | integration_class | stability_flag | standardized_type | retailer | promo_variant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| producer | 0.0016491839417993707 | 0.01 | 1.6681343764911542e-12 | 0.1 | 4.160589056408666e-21 | 0.1 | I(1) | 1.0 | hard_cheese | silpo_novus | promo_controlled |
| prozorro | 2.633366148124232e-10 | 0.08893253878307611 | 1.532473806066898e-08 | 0.1 | 1.196556730322677e-10 | 0.04166666666668085 | I(0) | 0.0 | hard_cheese | silpo_novus | promo_controlled |
| retail | 0.009639020091333756 | 0.1 | 1.9158401072775886e-24 | 0.1 | 0.0012553169947406174 | 0.1 | I(0) | 0.0 | hard_cheese | silpo_novus | promo_controlled |
| producer_to_prozorro | nan | nan | nan | nan | nan | nan | pair | nan | hard_cheese | silpo_novus | promo_controlled |
| prozorro_to_retail | nan | nan | nan | nan | nan | nan | pair | nan | hard_cheese | silpo_novus | promo_controlled |
| producer_to_retail | nan | nan | nan | nan | nan | nan | pair | nan | hard_cheese | silpo_novus | promo_controlled |

### ModelCoefficients

| standardized_type | retailer | promo_variant | frequency | link | model_family | y_series | x_series | n_obs | sr_coef | lr_coef | ect_coef |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| hard_cheese | silpo_novus | promo_controlled | daily | producer_to_prozorro | NARDL | prozorro | producer | 187 | -1.9016842806737577 | 0.31953965595429923 | -0.7038872412653931 |
| hard_cheese | silpo_novus | promo_controlled | daily | prozorro_to_retail | ARDL | retail | prozorro | 49 | -1.3314737468808606 | -3.323240219425985 | nan |
| hard_cheese | silpo_novus | promo_controlled | daily | prozorro_to_retail | NARDL | retail | prozorro | 47 | -0.28691764994779967 | -7.004767874733442 | -0.585728639694365 |

### ResidualDiagnostics

| model_family | link | y_series | x_series | ljungbox_p | arch_p | jb_p | unreliable_flag |
| --- | --- | --- | --- | --- | --- | --- | --- |
| NARDL | producer_to_prozorro | prozorro | producer | 0.30453926702142525 | 0.2688968463348201 | 0.05424410826903467 | 0 |
| ARDL | prozorro_to_retail | retail | prozorro | 0.8676166313512658 | 0.4620989193667864 | 0.25082409572050557 | 0 |
| NARDL | prozorro_to_retail | retail | prozorro | 0.9705702295552534 | 0.49641237836935637 | 0.15198175860588 | 0 |

### SeriesUsed

| date | producer | prozorro | retail | standardized_type | retailer | promo_variant | combined_rule |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2021-02-01 00:00:00 | 32.03526456031363 | nan | nan | hard_cheese | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-02 00:00:00 | 32.04618683176164 | nan | nan | hard_cheese | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-03 00:00:00 | 32.05676642836296 | nan | nan | hard_cheese | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-04 00:00:00 | 32.06697823935806 | nan | nan | hard_cheese | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-05 00:00:00 | 32.07679715398746 | nan | nan | hard_cheese | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-06 00:00:00 | 32.08619806149162 | nan | nan | hard_cheese | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-07 00:00:00 | 32.09515585111103 | nan | nan | hard_cheese | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-08 00:00:00 | 32.10364541208618 | nan | nan | hard_cheese | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-09 00:00:00 | 32.11123400633844 | nan | nan | hard_cheese | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-10 00:00:00 | 32.1178387696982 | nan | nan | hard_cheese | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-11 00:00:00 | 32.12395940226944 | nan | nan | hard_cheese | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-12 00:00:00 | 32.13009560415616 | nan | nan | hard_cheese | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-13 00:00:00 | 32.13674707546236 | nan | nan | hard_cheese | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-14 00:00:00 | 32.14441351629204 | nan | nan | hard_cheese | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-15 00:00:00 | 32.15359462674919 | nan | nan | hard_cheese | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-16 00:00:00 | 32.16772969300264 | nan | nan | hard_cheese | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-17 00:00:00 | 32.18792409272353 | nan | nan | hard_cheese | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-18 00:00:00 | 32.21117666326934 | nan | nan | hard_cheese | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-19 00:00:00 | 32.23448624199752 | nan | nan | hard_cheese | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-20 00:00:00 | 32.25485166626554 | nan | nan | hard_cheese | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-21 00:00:00 | 32.26927177343089 | nan | nan | hard_cheese | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-22 00:00:00 | 32.274745400851 | nan | nan | hard_cheese | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-23 00:00:00 | 31.92798797934096 | nan | nan | hard_cheese | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-24 00:00:00 | 31.03371883965718 | nan | nan | hard_cheese | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |
| 2021-02-25 00:00:00 | 29.81094266906914 | nan | nan | hard_cheese | silpo_novus | promo_controlled | daily_median_of_available_silpo_novus |

### LagProfile

| pair | lag | corr |
| --- | --- | --- |
| producer_to_prozorro | 1 | 0.05463411003148463 |
| producer_to_prozorro | 2 | 0.06465611259680928 |
| producer_to_prozorro | 3 | 0.0701974599652885 |
| producer_to_prozorro | 4 | 0.07719408938724882 |
| producer_to_prozorro | 5 | 0.07629421025159185 |
| producer_to_prozorro | 6 | 0.07219617159882989 |
| producer_to_prozorro | 7 | 0.07415560821992007 |
| producer_to_prozorro | 8 | 0.06531679646419819 |
| producer_to_prozorro | 9 | 0.061899198654111504 |
| producer_to_prozorro | 10 | 0.060185993622165784 |
| producer_to_prozorro | 11 | 0.06148166507681315 |
| producer_to_prozorro | 12 | 0.06268836727775298 |
| producer_to_prozorro | 13 | 0.06350343977923857 |
| producer_to_prozorro | 14 | 0.062210901509847344 |
| producer_to_prozorro | 15 | 0.05877108946366168 |
| producer_to_prozorro | 16 | 0.055021016375123494 |
| producer_to_prozorro | 17 | 0.05223217889559242 |
| producer_to_prozorro | 18 | 0.05074559649625219 |
| producer_to_prozorro | 19 | 0.0498392096731601 |
| producer_to_prozorro | 20 | 0.04919496620365539 |
| producer_to_prozorro | 21 | 0.04983540657339228 |
| producer_to_prozorro | 22 | 0.051914573072286835 |
| producer_to_prozorro | 23 | 0.057863513984741634 |
| producer_to_prozorro | 24 | 0.06963651857061677 |
| producer_to_prozorro | 25 | 0.08477701379613752 |

### ModelEligibility

| standardized_type | retailer | promo_variant | frequency | integration_producer | integration_prozorro | integration_retail | n_obs_producer | n_obs_prozorro | n_obs_retail | n_obs_pair_prod_prozorro | n_obs_pair_prozorro_retail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| hard_cheese | silpo_novus | promo_controlled | daily | I(1) | I(0) | I(0) | 1793 | 199 | 60 | 189 | 49 |

### NARDL_Multipliers

| horizon | mult_pos | mult_neg | link |
| --- | --- | --- | --- |
| 0 | -1.8528869181133245 | 0.04879736256043321 | producer_to_prozorro |
| 1 | -1.5201163099464257 | 0.04003356383238646 | producer_to_prozorro |
| 2 | -1.5798804955409376 | 0.041607504802056605 | producer_to_prozorro |
| 3 | -1.5691471020496954 | 0.041324831699572157 | producer_to_prozorro |
| 4 | -1.5710747738600248 | 0.04137559858626482 | producer_to_prozorro |
| 5 | -1.5707285722033568 | 0.041366481069381136 | producer_to_prozorro |
| 6 | -1.5707907485481254 | 0.041368118536626815 | producer_to_prozorro |
| 7 | -1.570779581941108 | 0.041367824454475406 | producer_to_prozorro |
| 8 | -1.5707815874162248 | 0.04136787727037875 | producer_to_prozorro |
| 9 | -1.5707812272414252 | 0.04136786778486719 | producer_to_prozorro |
| 10 | -1.570781291927287 | 0.04136786948842472 | producer_to_prozorro |
| 11 | -1.5707812803099812 | 0.04136786918247303 | producer_to_prozorro |
| 12 | -1.5707812823964 | 0.041367869237420654 | producer_to_prozorro |
| 13 | -1.570781282021688 | 0.04136786922755229 | producer_to_prozorro |
| 14 | -1.5707812820889848 | 0.04136786922932461 | producer_to_prozorro |
| 15 | -1.5707812820768985 | 0.04136786922900631 | producer_to_prozorro |
| 16 | -1.5707812820790692 | 0.04136786922906347 | producer_to_prozorro |
| 17 | -1.5707812820786793 | 0.04136786922905321 | producer_to_prozorro |
| 18 | -1.5707812820787495 | 0.04136786922905505 | producer_to_prozorro |
| 19 | -1.5707812820787368 | 0.04136786922905472 | producer_to_prozorro |
| 20 | -1.570781282078739 | 0.04136786922905478 | producer_to_prozorro |
| 0 | 1.56495154212292 | 1.8518691920707198 | prozorro_to_retail |
| 1 | 1.02554079653284 | 1.213563075400108 | prozorro_to_retail |
| 2 | 1.2114660118678413 | 1.4335757524961248 | prozorro_to_retail |
| 3 | 1.1473809227590746 | 1.3577413263191702 | prozorro_to_retail |

### VECM_IRF

_No rows_

## Graphs

- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/hard_cheese/silpo_novus/time_series_promo_controlled.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/hard_cheese/silpo_novus/lag_profile_promo_controlled.png
- /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/hard_cheese/silpo_novus/nardl_multipliers_promo_controlled.png
