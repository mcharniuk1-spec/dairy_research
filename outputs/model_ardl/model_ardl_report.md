# ARDL Summary from RW4 Primary Chain

## Interpretation Guide
- ADF p>0.05 and KPSS p<0.05 -> likely I(1)-like; prefer differences/cointegration models.
- ADF p<0.05 and KPSS p>0.05 -> stationary; level models are more admissible.
- Ljung-Box p<0.05 -> autocorrelation; add lag structure.
- BP/White p<0.05 -> heteroskedasticity; use robust or HAC standard errors.
- JB p<0.05 -> non-normality; use robust inference and avoid strict normality assumptions.
- Stability flag=1 -> potential breaks/drift; use rolling or split-sample robustness.
- For retail transmission, compare no-promo vs promo-controlled estimates.

## Notes
- RW4 domestic vertical chain is FarmGateUA -> ProducerUA -> ProZorro -> Retail, estimated with both forward and reverse-flow pairs. Farm-gate enters from two alternative reconstruction workbooks and both linear/pchip interpolation variants are carried end-to-end.
- family=ARDL
- rows=279
- source=/Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/primary_chain_summary/primary_chain_consolidated.xlsx

## Tables

### ARDL_Summary

| panel_level | panel_name | segment_name | product | standardized_type | retailer_panel | brand | price_variant | reconstruction_variant | farm_gate_source | frequency | chain_direction |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| product | product::Вершки::Silpo::observed::initial::linear | Вершки | Вершки | cream | Silpo | nan | observed | linear | initial | daily | forward |
| product | product::Вершки::Silpo::observed::initial::linear | Вершки | Вершки | cream | Silpo | nan | observed | linear | initial | daily | forward |
| product | product::Молоко питне::Silpo::observed::initial::linear | Молоко питне | Молоко питне | milk | Silpo | nan | observed | linear | initial | daily | reverse |
| product | product::Молоко питне::Silpo::observed::initial::linear | Молоко питне | Молоко питне | milk | Silpo | nan | observed | linear | initial | daily | reverse |
| product | product::Молоко питне::Silpo::observed::initial::linear | Молоко питне | Молоко питне | milk | Silpo | nan | observed | linear | initial | daily | reverse |
| product | product::Сир твердий::Silpo::observed::initial::linear | Сир твердий | Сир твердий | hard_cheese | Silpo | nan | observed | linear | initial | daily | forward |
| product | product::Сир твердий::Silpo::observed::initial::linear | Сир твердий | Сир твердий | hard_cheese | Silpo | nan | observed | linear | initial | daily | forward |
| product | product::Сир твердий::Silpo::observed::initial::linear | Сир твердий | Сир твердий | hard_cheese | Silpo | nan | observed | linear | initial | daily | forward |
| product | product::Сир твердий::Silpo::observed::initial::linear | Сир твердий | Сир твердий | hard_cheese | Silpo | nan | observed | linear | initial | daily | reverse |
| product | product::Сир твердий::Silpo::observed::initial::linear | Сир твердий | Сир твердий | hard_cheese | Silpo | nan | observed | linear | initial | daily | reverse |
| product | product::Сметана::Silpo::observed::initial::linear | Сметана | Сметана | sour_cream | Silpo | nan | observed | linear | initial | daily | reverse |
| product | product::Сметана::Silpo::observed::initial::linear | Сметана | Сметана | sour_cream | Silpo | nan | observed | linear | initial | daily | reverse |
| product | product::Вершки::Silpo::baseline::initial::linear | Вершки | Вершки | cream | Silpo | nan | baseline | linear | initial | daily | forward |
| product | product::Вершки::Silpo::baseline::initial::linear | Вершки | Вершки | cream | Silpo | nan | baseline | linear | initial | daily | reverse |
| product | product::Молоко питне::Silpo::baseline::initial::linear | Молоко питне | Молоко питне | milk | Silpo | nan | baseline | linear | initial | daily | forward |
| product | product::Молоко питне::Silpo::baseline::initial::linear | Молоко питне | Молоко питне | milk | Silpo | nan | baseline | linear | initial | daily | reverse |
| product | product::Сир твердий::Silpo::baseline::initial::linear | Сир твердий | Сир твердий | hard_cheese | Silpo | nan | baseline | linear | initial | daily | forward |
| product | product::Сир твердий::Silpo::baseline::initial::linear | Сир твердий | Сир твердий | hard_cheese | Silpo | nan | baseline | linear | initial | daily | forward |
| product | product::Сир твердий::Silpo::baseline::initial::linear | Сир твердий | Сир твердий | hard_cheese | Silpo | nan | baseline | linear | initial | daily | forward |
| product | product::Сир твердий::Silpo::baseline::initial::linear | Сир твердий | Сир твердий | hard_cheese | Silpo | nan | baseline | linear | initial | daily | forward |
| product | product::Сир твердий::Silpo::baseline::initial::linear | Сир твердий | Сир твердий | hard_cheese | Silpo | nan | baseline | linear | initial | daily | reverse |
| product | product::Сир твердий::Silpo::baseline::initial::linear | Сир твердий | Сир твердий | hard_cheese | Silpo | nan | baseline | linear | initial | daily | reverse |
| product | product::Сир твердий::Silpo::baseline::initial::linear | Сир твердий | Сир твердий | hard_cheese | Silpo | nan | baseline | linear | initial | daily | reverse |
| product | product::Сметана::Silpo::baseline::initial::linear | Сметана | Сметана | sour_cream | Silpo | nan | baseline | linear | initial | daily | reverse |
| average | average::Silpo::observed::initial::linear | all_products_average | all_products_average | all_products_average | Silpo | nan | observed | linear | initial | daily | forward |
