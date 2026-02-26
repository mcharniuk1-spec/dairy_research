# ARDL Summary from Primary Chain

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
- family=ARDL
- rows=30
- source=/Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/primary_chain_summary/primary_chain_consolidated.xlsx

## Tables

### ARDL_Summary

| standardized_type | retailer | promo_variant | frequency | link | model_family | y_series | x_series | n_obs | sr_coef | lr_coef | ect_coef |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| butter | silpo | observed | daily | prozorro_to_retail | ARDL | retail | prozorro | 41 | 0.2001943602714764 | -0.4257756633486405 | nan |
| butter | silpo | promo_controlled | daily | prozorro_to_retail | ARDL | retail | prozorro | 41 | 0.2001943602714764 | -0.4257756633486405 | nan |
| butter | silpo_novus | observed | daily | prozorro_to_retail | ARDL | retail | prozorro | 51 | 0.3808399108271916 | 5.038120798935976 | nan |
| butter | silpo_novus | promo_controlled | daily | prozorro_to_retail | ARDL | retail | prozorro | 51 | 0.3808399108271916 | 5.038120798935976 | nan |
| cottage_cheese | silpo_novus | observed | daily | prozorro_to_retail | ARDL | retail | prozorro | 42 | -0.4066263125016476 | -1.685428485355531 | nan |
| cottage_cheese | silpo_novus | promo_controlled | daily | prozorro_to_retail | ARDL | retail | prozorro | 42 | -0.4066263125016476 | -1.685428485355531 | nan |
| cream | silpo | observed | daily | prozorro_to_retail | ARDL | retail | prozorro | 42 | -0.02719087049912439 | -0.2713968465337292 | nan |
| cream | silpo | promo_controlled | daily | prozorro_to_retail | ARDL | retail | prozorro | 42 | -0.02719087049912439 | -0.2713968465337292 | nan |
| hard_cheese | silpo | observed | daily | prozorro_to_retail | ARDL | retail | prozorro | 38 | 1.045350879786881 | 16.32664882022445 | nan |
| hard_cheese | silpo | promo_controlled | daily | prozorro_to_retail | ARDL | retail | prozorro | 38 | 1.045350879786881 | 16.32664882022445 | nan |
| hard_cheese | silpo_novus | observed | daily | prozorro_to_retail | ARDL | retail | prozorro | 49 | -1.331473746880862 | -3.323240219425974 | nan |
| hard_cheese | silpo_novus | promo_controlled | daily | prozorro_to_retail | ARDL | retail | prozorro | 49 | -1.331473746880862 | -3.323240219425974 | nan |
| milk | silpo | observed | daily | producer_to_prozorro | ARDL | prozorro | producer | 201 | 0.6442401315402562 | -0.2843166259159834 | nan |
| milk | silpo | promo_controlled | daily | producer_to_prozorro | ARDL | prozorro | producer | 201 | 0.6442401315402562 | -0.2843166259159834 | nan |
| milk | novus | observed | daily | producer_to_prozorro | ARDL | prozorro | producer | 201 | 0.6442401315402562 | -0.2843166259159834 | nan |
| milk | novus | promo_controlled | daily | producer_to_prozorro | ARDL | prozorro | producer | 201 | 0.6442401315402562 | -0.2843166259159834 | nan |
| other | silpo | observed | daily | prozorro_to_retail | ARDL | retail | prozorro | 50 | 5.213950941002082 | 3.457668287525454 | nan |
| other | silpo | promo_controlled | daily | prozorro_to_retail | ARDL | retail | prozorro | 50 | 5.213950941002082 | 3.457668287525454 | nan |
| other | silpo_novus | observed | daily | prozorro_to_retail | ARDL | retail | prozorro | 52 | 3.191807377212619 | -12.70081452552591 | nan |
| other | silpo_novus | promo_controlled | daily | prozorro_to_retail | ARDL | retail | prozorro | 52 | 3.191807377212619 | -12.70081452552591 | nan |
| sour_cream | silpo | observed | daily | producer_to_prozorro | ARDL | prozorro | producer | 178 | 0.1503321327484457 | 0.53201805897649 | nan |
| sour_cream | silpo | observed | daily | prozorro_to_retail | ARDL | retail | prozorro | 38 | -0.09602698663315934 | -0.0780821130244814 | nan |
| sour_cream | silpo | promo_controlled | daily | producer_to_prozorro | ARDL | prozorro | producer | 178 | 0.1503321327484457 | 0.53201805897649 | nan |
| sour_cream | silpo | promo_controlled | daily | prozorro_to_retail | ARDL | retail | prozorro | 38 | -0.09602698663315934 | -0.0780821130244814 | nan |
| sour_cream | novus | observed | daily | producer_to_prozorro | ARDL | prozorro | producer | 178 | 0.1503321327484457 | 0.53201805897649 | nan |
