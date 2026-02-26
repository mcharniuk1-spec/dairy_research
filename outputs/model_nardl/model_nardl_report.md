# NARDL Summary from Primary Chain

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
- family=NARDL
- rows=48
- source=/Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/primary_chain_summary/primary_chain_consolidated.xlsx

## Tables

### NARDL_Summary

| standardized_type | retailer | promo_variant | frequency | link | model_family | y_series | x_series | n_obs | sr_coef | lr_coef | ect_coef |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| butter | silpo | observed | daily | producer_to_prozorro | NARDL | prozorro | producer | 218 | -0.2127764229425361 | 0.2740532058530188 | -0.8083252331134957 |
| butter | silpo | observed | daily | prozorro_to_retail | NARDL | retail | prozorro | 39 | 0.04860976737983126 | -0.1264841571269478 | -0.8756967529857956 |
| butter | silpo | promo_controlled | daily | producer_to_prozorro | NARDL | prozorro | producer | 218 | -0.2127764229425361 | 0.2740532058530188 | -0.8083252331134957 |
| butter | silpo | promo_controlled | daily | prozorro_to_retail | NARDL | retail | prozorro | 39 | 0.04860976737983126 | -0.1264841571269478 | -0.8756967529857956 |
| butter | novus | observed | daily | producer_to_prozorro | NARDL | prozorro | producer | 218 | -0.2127764229425361 | 0.2740532058530188 | -0.8083252331134957 |
| butter | novus | promo_controlled | daily | producer_to_prozorro | NARDL | prozorro | producer | 218 | -0.2127764229425361 | 0.2740532058530188 | -0.8083252331134957 |
| butter | silpo_novus | observed | daily | producer_to_prozorro | NARDL | prozorro | producer | 218 | -0.2127764229425361 | 0.2740532058530188 | -0.8083252331134957 |
| butter | silpo_novus | observed | daily | prozorro_to_retail | NARDL | retail | prozorro | 49 | 0.03764617386887498 | -0.8051638051994185 | -0.934681111534598 |
| butter | silpo_novus | promo_controlled | daily | producer_to_prozorro | NARDL | prozorro | producer | 218 | -0.2127764229425361 | 0.2740532058530188 | -0.8083252331134957 |
| butter | silpo_novus | promo_controlled | daily | prozorro_to_retail | NARDL | retail | prozorro | 49 | 0.03764617386887498 | -0.8051638051994185 | -0.934681111534598 |
| cottage_cheese | silpo_novus | observed | daily | prozorro_to_retail | NARDL | retail | prozorro | 40 | -0.04779905990700553 | -0.5494671968185126 | -0.9346201147084174 |
| cottage_cheese | silpo_novus | promo_controlled | daily | prozorro_to_retail | NARDL | retail | prozorro | 40 | -0.04779905990700553 | -0.5494671968185126 | -0.9346201147084174 |
| cream | silpo | observed | daily | producer_to_prozorro | NARDL | prozorro | producer | 197 | 3.793680252396324 | 0.3345340871189739 | -1.002572700947699 |
| cream | silpo | observed | daily | prozorro_to_retail | NARDL | retail | prozorro | 40 | -0.070469572016711 | -0.2354291883368252 | -0.539409399232454 |
| cream | silpo | promo_controlled | daily | producer_to_prozorro | NARDL | prozorro | producer | 197 | 3.793680252396324 | 0.3345340871189739 | -1.002572700947699 |
| cream | silpo | promo_controlled | daily | prozorro_to_retail | NARDL | retail | prozorro | 40 | -0.070469572016711 | -0.2354291883368252 | -0.539409399232454 |
| cream | novus | observed | daily | producer_to_prozorro | NARDL | prozorro | producer | 197 | 3.793680252396324 | 0.3345340871189739 | -1.002572700947699 |
| cream | novus | promo_controlled | daily | producer_to_prozorro | NARDL | prozorro | producer | 197 | 3.793680252396324 | 0.3345340871189739 | -1.002572700947699 |
| hard_cheese | silpo | observed | daily | producer_to_prozorro | NARDL | prozorro | producer | 187 | -1.901684280673745 | 0.3195396559542991 | -0.703887241265392 |
| hard_cheese | silpo | observed | daily | prozorro_to_retail | NARDL | retail | prozorro | 36 | 0.03093538709143862 | 0.01877747610695744 | -1.131301223411889 |
| hard_cheese | silpo | promo_controlled | daily | producer_to_prozorro | NARDL | prozorro | producer | 187 | -1.901684280673745 | 0.3195396559542991 | -0.703887241265392 |
| hard_cheese | silpo | promo_controlled | daily | prozorro_to_retail | NARDL | retail | prozorro | 36 | 0.03093538709143862 | 0.01877747610695744 | -1.131301223411889 |
| hard_cheese | novus | observed | daily | producer_to_prozorro | NARDL | prozorro | producer | 187 | -1.901684280673745 | 0.3195396559542991 | -0.703887241265392 |
| hard_cheese | novus | promo_controlled | daily | producer_to_prozorro | NARDL | prozorro | producer | 187 | -1.901684280673745 | 0.3195396559542991 | -0.703887241265392 |
| hard_cheese | silpo_novus | observed | daily | producer_to_prozorro | NARDL | prozorro | producer | 187 | -1.901684280673745 | 0.3195396559542991 | -0.703887241265392 |
