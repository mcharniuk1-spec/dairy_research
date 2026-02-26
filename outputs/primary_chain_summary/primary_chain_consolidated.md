# Primary Chain Consolidated Summary

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
- model_rows=102
- pretest_rows=144
- diagnostic_rows=102
- eligibility_rows=48

## Tables

### Consolidated_ModelCoefficients

| standardized_type | retailer | promo_variant | frequency | link | model_family | y_series | x_series | n_obs | sr_coef | lr_coef | ect_coef |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| butter | silpo | observed | daily | producer_to_prozorro | NARDL | prozorro | producer | 218 | -0.21277642294253607 | 0.27405320585301884 | -0.8083252331134957 |
| butter | silpo | observed | daily | prozorro_to_retail | ARDL | retail | prozorro | 41 | 0.2001943602714764 | -0.4257756633486405 | nan |
| butter | silpo | observed | daily | prozorro_to_retail | NARDL | retail | prozorro | 39 | 0.04860976737983126 | -0.12648415712694783 | -0.8756967529857956 |
| butter | silpo | promo_controlled | daily | producer_to_prozorro | NARDL | prozorro | producer | 218 | -0.21277642294253607 | 0.27405320585301884 | -0.8083252331134957 |
| butter | silpo | promo_controlled | daily | prozorro_to_retail | ARDL | retail | prozorro | 41 | 0.2001943602714764 | -0.4257756633486405 | nan |
| butter | silpo | promo_controlled | daily | prozorro_to_retail | NARDL | retail | prozorro | 39 | 0.04860976737983126 | -0.12648415712694783 | -0.8756967529857956 |
| butter | novus | observed | daily | producer_to_prozorro | NARDL | prozorro | producer | 218 | -0.21277642294253607 | 0.27405320585301884 | -0.8083252331134957 |
| butter | novus | promo_controlled | daily | producer_to_prozorro | NARDL | prozorro | producer | 218 | -0.21277642294253607 | 0.27405320585301884 | -0.8083252331134957 |
| butter | silpo_novus | observed | daily | producer_to_prozorro | NARDL | prozorro | producer | 218 | -0.21277642294253607 | 0.27405320585301884 | -0.8083252331134957 |
| butter | silpo_novus | observed | daily | prozorro_to_retail | ARDL | retail | prozorro | 51 | 0.3808399108271916 | 5.038120798935976 | nan |
| butter | silpo_novus | observed | daily | prozorro_to_retail | ECM | retail | prozorro | 49 | -0.019317533092633468 | -0.11304424771502886 | -0.5842642909954745 |
| butter | silpo_novus | observed | daily | prozorro_to_retail | NARDL | retail | prozorro | 49 | 0.03764617386887498 | -0.8051638051994185 | -0.934681111534598 |
| butter | silpo_novus | promo_controlled | daily | producer_to_prozorro | NARDL | prozorro | producer | 218 | -0.21277642294253607 | 0.27405320585301884 | -0.8083252331134957 |
| butter | silpo_novus | promo_controlled | daily | prozorro_to_retail | ARDL | retail | prozorro | 51 | 0.3808399108271916 | 5.038120798935976 | nan |
| butter | silpo_novus | promo_controlled | daily | prozorro_to_retail | ECM | retail | prozorro | 49 | -0.019317533092633468 | -0.11304424771502886 | -0.5842642909954745 |
| butter | silpo_novus | promo_controlled | daily | prozorro_to_retail | NARDL | retail | prozorro | 49 | 0.03764617386887498 | -0.8051638051994185 | -0.934681111534598 |
| cottage_cheese | silpo | observed | daily | none | none | n/a | n/a | 203 | nan | nan | nan |
| cottage_cheese | silpo | promo_controlled | daily | none | none | n/a | n/a | 203 | nan | nan | nan |
| cottage_cheese | novus | observed | daily | none | none | n/a | n/a | 203 | nan | nan | nan |
| cottage_cheese | novus | promo_controlled | daily | none | none | n/a | n/a | 203 | nan | nan | nan |
| cottage_cheese | silpo_novus | observed | daily | prozorro_to_retail | ARDL | retail | prozorro | 42 | -0.4066263125016476 | -1.685428485355531 | nan |
| cottage_cheese | silpo_novus | observed | daily | prozorro_to_retail | NARDL | retail | prozorro | 40 | -0.04779905990700553 | -0.5494671968185126 | -0.9346201147084174 |
| cottage_cheese | silpo_novus | promo_controlled | daily | prozorro_to_retail | ARDL | retail | prozorro | 42 | -0.4066263125016476 | -1.685428485355531 | nan |
| cottage_cheese | silpo_novus | promo_controlled | daily | prozorro_to_retail | NARDL | retail | prozorro | 40 | -0.04779905990700553 | -0.5494671968185126 | -0.9346201147084174 |
| cream | silpo | observed | daily | producer_to_prozorro | NARDL | prozorro | producer | 197 | 3.7936802523963236 | 0.33453408711897387 | -1.002572700947699 |

### Consolidated_PreTests

| series | adf_level_p | kpss_level_p | adf_diff1_p | kpss_diff1_p | adf_diff2_p | kpss_diff2_p | integration_class | stability_flag | standardized_type | retailer | promo_variant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| producer | 0.08225840900715364 | 0.01 | 2.681802621264837e-12 | 0.1 | 1.3006957963952123e-20 | 0.1 | I(1) | 1 | butter | silpo | observed |
| prozorro | 0.056404226942647726 | 0.01 | 3.518946761497874e-22 | 0.1 | 1.9269184182026386e-13 | 0.1 | I(1) | 1 | butter | silpo | observed |
| retail | 2.2989340931225115e-06 | 0.1 | 2.5595238291844733e-09 | 0.1 | 8.70860721185971e-05 | 0.04166666666666662 | I(0) | 0 | butter | silpo | observed |
| producer | 0.08225840900715364 | 0.01 | 2.681802621264837e-12 | 0.1 | 1.3006957963952123e-20 | 0.1 | I(1) | 1 | butter | silpo | promo_controlled |
| prozorro | 0.056404226942647726 | 0.01 | 3.518946761497874e-22 | 0.1 | 1.9269184182026386e-13 | 0.1 | I(1) | 1 | butter | silpo | promo_controlled |
| retail | 2.2989340931225115e-06 | 0.1 | 2.5595238291844733e-09 | 0.1 | 8.70860721185971e-05 | 0.04166666666666662 | I(0) | 0 | butter | silpo | promo_controlled |
| producer | 0.08225840900715364 | 0.01 | 2.681802621264837e-12 | 0.1 | 1.3006957963952123e-20 | 0.1 | I(1) | 1 | butter | novus | observed |
| prozorro | 0.056404226942647726 | 0.01 | 3.518946761497874e-22 | 0.1 | 1.9269184182026386e-13 | 0.1 | I(1) | 1 | butter | novus | observed |
| retail | nan | nan | nan | nan | nan | nan | ambiguous | 0 | butter | novus | observed |
| producer | 0.08225840900715364 | 0.01 | 2.681802621264837e-12 | 0.1 | 1.3006957963952123e-20 | 0.1 | I(1) | 1 | butter | novus | promo_controlled |
| prozorro | 0.056404226942647726 | 0.01 | 3.518946761497874e-22 | 0.1 | 1.9269184182026386e-13 | 0.1 | I(1) | 1 | butter | novus | promo_controlled |
| retail | nan | nan | nan | nan | nan | nan | ambiguous | 0 | butter | novus | promo_controlled |
| producer | 0.08225840900715364 | 0.01 | 2.681802621264837e-12 | 0.1 | 1.3006957963952123e-20 | 0.1 | I(1) | 1 | butter | silpo_novus | observed |
| prozorro | 0.056404226942647726 | 0.01 | 3.518946761497874e-22 | 0.1 | 1.9269184182026386e-13 | 0.1 | I(1) | 1 | butter | silpo_novus | observed |
| retail | 0.009658462541496323 | 0.015275724253247233 | 0.0004241747553426809 | 0.1 | 0.0016100992365552236 | 0.1 | I(1) | 0 | butter | silpo_novus | observed |
| producer | 0.08225840900715364 | 0.01 | 2.681802621264837e-12 | 0.1 | 1.3006957963952123e-20 | 0.1 | I(1) | 1 | butter | silpo_novus | promo_controlled |
| prozorro | 0.056404226942647726 | 0.01 | 3.518946761497874e-22 | 0.1 | 1.9269184182026386e-13 | 0.1 | I(1) | 1 | butter | silpo_novus | promo_controlled |
| retail | 0.009658462541496323 | 0.015275724253247233 | 0.0004241747553426809 | 0.1 | 0.0016100992365552236 | 0.1 | I(1) | 0 | butter | silpo_novus | promo_controlled |
| producer | nan | nan | nan | nan | nan | nan | ambiguous | 0 | cottage_cheese | silpo | observed |
| prozorro | 1.1483227108295172e-10 | 0.01 | 4.589982408975803e-17 | 0.1 | 4.813752592554151e-10 | 0.1 | I(1) | 0 | cottage_cheese | silpo | observed |
| retail | 5.9157706543378735e-08 | 0.1 | 7.517018918246667e-13 | 0.0865089553841217 | 0.001856917684812617 | 0.041666666666666796 | I(0) | 0 | cottage_cheese | silpo | observed |
| producer | nan | nan | nan | nan | nan | nan | ambiguous | 0 | cottage_cheese | silpo | promo_controlled |
| prozorro | 1.1483227108295172e-10 | 0.01 | 4.589982408975803e-17 | 0.1 | 4.813752592554151e-10 | 0.1 | I(1) | 0 | cottage_cheese | silpo | promo_controlled |
| retail | 5.9157706543378735e-08 | 0.1 | 7.517018918246667e-13 | 0.0865089553841217 | 0.001856917684812617 | 0.041666666666666796 | I(0) | 0 | cottage_cheese | silpo | promo_controlled |
| producer | nan | nan | nan | nan | nan | nan | ambiguous | 0 | cottage_cheese | novus | observed |

### Consolidated_ResidualDiagnostics

| model_family | link | y_series | x_series | ljungbox_p | arch_p | jb_p | unreliable_flag | standardized_type | retailer | promo_variant |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| NARDL | producer_to_prozorro | prozorro | producer | 0.3043740439991276 | 0.5287391650637272 | 4.2203813853019655e-84 | 0 | butter | silpo | observed |
| ARDL | prozorro_to_retail | retail | prozorro | 0.01144894530681835 | 0.09344174279103216 | 0.6443904339549587 | 1 | butter | silpo | observed |
| NARDL | prozorro_to_retail | retail | prozorro | 0.5591712653384464 | 0.046665474894684277 | 0.8050949849331446 | 1 | butter | silpo | observed |
| NARDL | producer_to_prozorro | prozorro | producer | 0.3043740439991276 | 0.5287391650637272 | 4.2203813853019655e-84 | 0 | butter | silpo | promo_controlled |
| ARDL | prozorro_to_retail | retail | prozorro | 0.01144894530681835 | 0.09344174279103216 | 0.6443904339549587 | 1 | butter | silpo | promo_controlled |
| NARDL | prozorro_to_retail | retail | prozorro | 0.5591712653384464 | 0.046665474894684277 | 0.8050949849331446 | 1 | butter | silpo | promo_controlled |
| NARDL | producer_to_prozorro | prozorro | producer | 0.3043740439991276 | 0.5287391650637272 | 4.2203813853019655e-84 | 0 | butter | novus | observed |
| NARDL | producer_to_prozorro | prozorro | producer | 0.3043740439991276 | 0.5287391650637272 | 4.2203813853019655e-84 | 0 | butter | novus | promo_controlled |
| NARDL | producer_to_prozorro | prozorro | producer | 0.3043740439991276 | 0.5287391650637272 | 4.2203813853019655e-84 | 0 | butter | silpo_novus | observed |
| ARDL | prozorro_to_retail | retail | prozorro | 0.1517137359967815 | 0.9428759814198608 | 0.12163941337757182 | 0 | butter | silpo_novus | observed |
| ECM | prozorro_to_retail | retail | prozorro | 0.7561861082620147 | 0.1308148001577336 | 1.4411688625167337e-05 | 0 | butter | silpo_novus | observed |
| NARDL | prozorro_to_retail | retail | prozorro | 0.4526018945159763 | 0.17734130295808273 | 0.0008392768825094401 | 0 | butter | silpo_novus | observed |
| NARDL | producer_to_prozorro | prozorro | producer | 0.3043740439991276 | 0.5287391650637272 | 4.2203813853019655e-84 | 0 | butter | silpo_novus | promo_controlled |
| ARDL | prozorro_to_retail | retail | prozorro | 0.1517137359967815 | 0.9428759814198608 | 0.12163941337757182 | 0 | butter | silpo_novus | promo_controlled |
| ECM | prozorro_to_retail | retail | prozorro | 0.7561861082620147 | 0.1308148001577336 | 1.4411688625167337e-05 | 0 | butter | silpo_novus | promo_controlled |
| NARDL | prozorro_to_retail | retail | prozorro | 0.4526018945159763 | 0.17734130295808273 | 0.0008392768825094401 | 0 | butter | silpo_novus | promo_controlled |
| none | none | n/a | n/a | nan | nan | nan | 1 | cottage_cheese | silpo | observed |
| none | none | n/a | n/a | nan | nan | nan | 1 | cottage_cheese | silpo | promo_controlled |
| none | none | n/a | n/a | nan | nan | nan | 1 | cottage_cheese | novus | observed |
| none | none | n/a | n/a | nan | nan | nan | 1 | cottage_cheese | novus | promo_controlled |
| ARDL | prozorro_to_retail | retail | prozorro | 0.1007447696043067 | 0.45591024880877795 | 0.7986167356499732 | 0 | cottage_cheese | silpo_novus | observed |
| NARDL | prozorro_to_retail | retail | prozorro | 0.13802457343734706 | 0.7478438770300309 | 2.6950380978724114e-06 | 0 | cottage_cheese | silpo_novus | observed |
| ARDL | prozorro_to_retail | retail | prozorro | 0.1007447696043067 | 0.45591024880877795 | 0.7986167356499732 | 0 | cottage_cheese | silpo_novus | promo_controlled |
| NARDL | prozorro_to_retail | retail | prozorro | 0.13802457343734706 | 0.7478438770300309 | 2.6950380978724114e-06 | 0 | cottage_cheese | silpo_novus | promo_controlled |
| NARDL | producer_to_prozorro | prozorro | producer | 0.889712370853929 | 0.2018078467373643 | 1.393192716168525e-262 | 0 | cream | silpo | observed |

### Consolidated_Eligibility

| standardized_type | retailer | promo_variant | frequency | integration_producer | integration_prozorro | integration_retail | n_obs_producer | n_obs_prozorro | n_obs_retail | n_obs_pair_prod_prozorro | n_obs_pair_prozorro_retail |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| butter | silpo | observed | daily | I(1) | I(1) | I(0) | 1793 | 230 | 48 | 220 | 41 |
| butter | silpo | promo_controlled | daily | I(1) | I(1) | I(0) | 1793 | 230 | 48 | 220 | 41 |
| butter | novus | observed | daily | I(1) | I(1) | ambiguous | 1793 | 230 | 19 | 220 | 17 |
| butter | novus | promo_controlled | daily | I(1) | I(1) | ambiguous | 1793 | 230 | 19 | 220 | 17 |
| butter | silpo_novus | observed | daily | I(1) | I(1) | I(1) | 1793 | 230 | 58 | 220 | 51 |
| butter | silpo_novus | promo_controlled | daily | I(1) | I(1) | I(1) | 1793 | 230 | 58 | 220 | 51 |
| cottage_cheese | silpo | observed | daily | ambiguous | I(1) | I(0) | 0 | 190 | 48 | 0 | 35 |
| cottage_cheese | silpo | promo_controlled | daily | ambiguous | I(1) | I(0) | 0 | 190 | 48 | 0 | 35 |
| cottage_cheese | novus | observed | daily | ambiguous | I(1) | ambiguous | 0 | 190 | 20 | 0 | 17 |
| cottage_cheese | novus | promo_controlled | daily | ambiguous | I(1) | ambiguous | 0 | 190 | 20 | 0 | 17 |
| cottage_cheese | silpo_novus | observed | daily | ambiguous | I(1) | I(0) | 0 | 190 | 55 | 0 | 42 |
| cottage_cheese | silpo_novus | promo_controlled | daily | ambiguous | I(1) | I(0) | 0 | 190 | 55 | 0 | 42 |
| cream | silpo | observed | daily | I(1) | I(0) | I(1) | 1793 | 209 | 48 | 199 | 42 |
| cream | silpo | promo_controlled | daily | I(1) | I(0) | I(1) | 1793 | 209 | 48 | 199 | 42 |
| cream | novus | observed | daily | I(1) | I(0) | ambiguous | 1793 | 209 | 18 | 199 | 16 |
| cream | novus | promo_controlled | daily | I(1) | I(0) | ambiguous | 1793 | 209 | 18 | 199 | 16 |
| cream | silpo_novus | observed | daily | I(1) | I(0) | I(2) | 1793 | 209 | 55 | 199 | 48 |
| cream | silpo_novus | promo_controlled | daily | I(1) | I(0) | I(2) | 1793 | 209 | 55 | 199 | 48 |
| hard_cheese | silpo | observed | daily | I(1) | I(0) | I(1) | 1793 | 199 | 48 | 189 | 38 |
| hard_cheese | silpo | promo_controlled | daily | I(1) | I(0) | I(1) | 1793 | 199 | 48 | 189 | 38 |
| hard_cheese | novus | observed | daily | I(1) | I(0) | I(0) | 1793 | 199 | 37 | 189 | 32 |
| hard_cheese | novus | promo_controlled | daily | I(1) | I(0) | I(0) | 1793 | 199 | 37 | 189 | 32 |
| hard_cheese | silpo_novus | observed | daily | I(1) | I(0) | I(0) | 1793 | 199 | 60 | 189 | 49 |
| hard_cheese | silpo_novus | promo_controlled | daily | I(1) | I(0) | I(0) | 1793 | 199 | 60 | 189 | 49 |
| milk | silpo | observed | daily | I(1) | I(1) | I(1) | 1793 | 211 | 48 | 201 | 37 |
