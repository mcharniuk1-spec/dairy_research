# ECM Summary from RW4 Primary Chain

## Interpretation Guide
- ADF p>0.05 and KPSS p<0.05 -> likely I(1)-like; prefer differences/cointegration models.
- ADF p<0.05 and KPSS p>0.05 -> stationary; level models are more admissible.
- Ljung-Box p<0.05 -> autocorrelation; add lag structure.
- BP/White p<0.05 -> heteroskedasticity; use robust or HAC standard errors.
- JB p<0.05 -> non-normality; use robust inference and avoid strict normality assumptions.
- Stability flag=1 -> potential breaks/drift; use rolling or split-sample robustness.
- For retail transmission, compare no-promo vs promo-controlled estimates.

## Notes
- RW4 domestic vertical chain is FarmGateUA -> ProducerUA -> ProZorro -> Retail, estimated with both forward and reverse-flow pairs. Farm-gate enters from two alternative reconstruction workbooks and both linear/pchip interpolation variants are carried end-to-end. Retail_combined is the anchored downstream index built from Silpo effective prices, Novus observed prices, and a level-aligned ConsumerUA anchor, while Retail_combined_core keeps the strict retailer-only overlap for robustness.
- family=ECM
- rows=286
- source=/Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/primary_chain_summary/primary_chain_consolidated.xlsx

## Tables

### ECM_Summary

| panel_level | panel_name | segment_name | product | standardized_type | retailer_panel | brand | price_variant | reconstruction_variant | farm_gate_source | frequency | intersection_rule |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| pairwise_product | pairwise::farm_gate_producer::Вершки::initial::linear | Вершки | Вершки | cream | nan | nan | nan | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_producer::Вершки::initial::linear | Вершки | Вершки | cream | nan | nan | nan | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_producer::Кефір::initial::linear | Кефір | Кефір | milk | nan | nan | nan | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_producer::Кефір::initial::linear | Кефір | Кефір | milk | nan | nan | nan | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_producer::Молоко питне::initial::linear | Молоко питне | Молоко питне | milk | nan | nan | nan | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_producer::Сир твердий::initial::linear | Сир твердий | Сир твердий | hard_cheese | nan | nan | nan | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_producer::Сир твердий::initial::linear | Сир твердий | Сир твердий | hard_cheese | nan | nan | nan | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_producer::Сметана::initial::linear | Сметана | Сметана | sour_cream | nan | nan | nan | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_producer::Сметана::initial::linear | Сметана | Сметана | sour_cream | nan | nan | nan | linear | initial | daily | pairwise_overlap |
| product | product::Сир твердий::Silpo::observed::initial::linear | Сир твердий | Сир твердий | hard_cheese | Silpo | nan | observed | linear | initial | daily | chain_common_support |
| pairwise_product | pairwise::farm_gate_retail::Сир кисломолочний::Silpo::observed::initial::linear | Сир кисломолочний | Сир кисломолочний | cottage_cheese | Silpo | nan | observed | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_retail::Сир кисломолочний::Silpo::observed::initial::linear | Сир кисломолочний | Сир кисломолочний | cottage_cheese | Silpo | nan | observed | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::prozorro_retail::Сир твердий::Silpo::observed::initial::linear | Сир твердий | Сир твердий | hard_cheese | Silpo | nan | observed | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_retail::Інше/невідомо::Silpo::baseline::initial::linear | Інше/невідомо | Інше/невідомо | other | Silpo | nan | baseline | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_retail::Йогурт::Silpo::baseline::initial::linear | Йогурт | Йогурт | yogurt_dessert | Silpo | nan | baseline | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_retail::Молоко питне::Silpo::baseline::initial::linear | Молоко питне | Молоко питне | milk | Silpo | nan | baseline | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_retail::Молоко питне::Silpo::baseline::initial::linear | Молоко питне | Молоко питне | milk | Silpo | nan | baseline | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::producer_retail::Молоко питне::Silpo::baseline::initial::linear | Молоко питне | Молоко питне | milk | Silpo | nan | baseline | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::producer_retail::Молоко питне::Silpo::baseline::initial::linear | Молоко питне | Молоко питне | milk | Silpo | nan | baseline | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_retail::Молоко питне::Retail_combined::observed::initial::linear | Молоко питне | Молоко питне | milk | Retail_combined | nan | observed | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_retail::Молоко питне::Retail_combined::observed::initial::linear | Молоко питне | Молоко питне | milk | Retail_combined | nan | observed | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_retail::Сир твердий::Retail_combined::observed::initial::linear | Сир твердий | Сир твердий | hard_cheese | Retail_combined | nan | observed | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_retail::Сир твердий::Retail_combined::observed::initial::linear | Сир твердий | Сир твердий | hard_cheese | Retail_combined | nan | observed | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_retail::Сметана::Retail_combined::observed::initial::linear | Сметана | Сметана | sour_cream | Retail_combined | nan | observed | linear | initial | daily | pairwise_overlap |
| pairwise_product | pairwise::farm_gate_retail::Сметана::Retail_combined::observed::initial::linear | Сметана | Сметана | sour_cream | Retail_combined | nan | observed | linear | initial | daily | pairwise_overlap |
