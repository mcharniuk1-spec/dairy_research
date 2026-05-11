# New Model Dataset Audit

## Mandatory Audit Finding

The new modelling workflow must rebuild clean data from the raw files before any econometric model is estimated.

Known risks explicitly handled:

- `Processor_price` is reported in hryvnia per tonne and is converted to hryvnia per kilogram (UAH/kg) by dividing by `1000`.
- `Farm_price` / `Farm_milk_2015.xlsx` carries the short unit label `Гривня`, but the magnitude is economically a tonne price. It is converted to UAH/kg by dividing by `1000`.
- `ProzorroM(full)` stores numeric fields with non-breaking spaces and text formatting. Numeric columns are parsed before aggregation.
- Silpo and Novus have visible retail classification errors. Product labels are rebuilt from `product_title` and `product_name`.
- Every cleaned table contains a controlled `product` column.

## Cleaned Dataset Coverage

| dataset | rows | date_min | date_max | products | quality_ok_share |
| --- | --- | --- | --- | --- | --- |
| clean_farmgate_monthly | 3645 | 2015-01-01 | 2026-03-01 | raw_milk | 0.832 |
| clean_processor_monthly | 954 | 2013-01-01 | 2026-03-01 | butter, drinking_milk, hard_cheese, kefir, skim_milk_powder, sour_cream | 1 |
| clean_consumer_monthly | 8658 | 2017-01-01 | 2026-03-01 | drinking_milk, soft_cheese, sour_cream | 0.964 |
| clean_prozorro_lot_level | 16573 | 2023-01-02 | 2026-04-29 | butter, condensed_milk, cottage_cheese, cream, drinking_milk, hard_cheese, kefir, other_dairy, skim_milk_powder, soft_cheese | 1 |
| clean_retail_sku_day | 88295 | 2025-10-21 | 2026-01-08 | butter, condensed_milk, cottage_cheese, cream, drinking_milk, exclude_non_dairy, hard_cheese, kefir, other_dairy, skim_milk_powder, sour_cream, yogurt | 0.914 |
| clean_farm_volumes | 19110 | 2025-01-01 | 2026-03-01 | butter, condensed_milk, cream, drinking_milk, kefir, other_dairy, raw_milk, skim_milk_powder | 1 |
| clean_cost_index | 171 | 2015-01-01 | 2025-10-01 | livestock_products | 1 |

## Integrated Consumer Sheet Corruption Check

| check | affected_rows | affected_ukraine_rows | decision |
| --- | --- | --- | --- |
| Integrated Consumer_price implausible values above 1000 UAH/kg | 340 | 12 | Use raw Consumer_2017_2026.xlsx, not the combined sheet, for official consumer models. |

## Old-Model vs New Observed Validation

| comparison | n | correlation | MAE | RMSE | MAPE_pct | sign_agreement | decision |
| --- | --- | --- | --- | --- | --- | --- | --- |
| FarmGate(oldmodel) vs observed Farm_milk_2015 | 46 | 0.9631 | 1.397 | 1.665 | 9.498 | 0.7333 | Old reconstruction validates well; usable as robustness. |
| Producer(oldmodel) vs Processor_price: butter | 50 | 0.8863 | 23.82 | 38.27 | 10.11 | 0.6531 | Old reconstruction validates well; usable as robustness. |
| Producer(oldmodel) vs Processor_price: drinking_milk | 50 | 0.8392 | 2.184 | 3.863 | 7.402 | 0.6531 | Partial validation; appendix/support only. |
| Producer(oldmodel) vs Processor_price: hard_cheese | 50 | 0.7827 | 15.73 | 23.52 | 7.933 | 0.6735 | Partial validation; appendix/support only. |
| Producer(oldmodel) vs Processor_price: kefir | 50 | 0.9122 | 1.878 | 3.007 | 5.599 | 0.6939 | Old reconstruction validates well; usable as robustness. |
| Producer(oldmodel) vs Processor_price: skim_milk_powder | 50 | 0.5123 | 7.699 | 11.31 | 7.917 | 0.7551 | Weak validation; do not use for main inference. |
| Producer(oldmodel) vs Processor_price: sour_cream | 50 | 0.8978 | 5.655 | 9.446 | 6.832 | 0.6122 | Old reconstruction validates well; usable as robustness. |
| Consumer(oldmodel) vs Consumer_2017_2026: drinking_milk | 50 | 0.8816 | 3.103 | 4.975 | 7.685 | 0.6531 | Old reconstruction validates well; usable as robustness. |
| Consumer(oldmodel) vs Consumer_2017_2026: soft_cheese | 50 | 0.9015 | 13.79 | 22.04 | 7.356 | 0.5306 | Old reconstruction validates well; usable as robustness. |
| Consumer(oldmodel) vs Consumer_2017_2026: sour_cream | 50 | 0.8784 | 9.711 | 14.79 | 8.71 | 0.6327 | Old reconstruction validates well; usable as robustness. |

## Product Dictionary

| product | label | role | main_use |
| --- | --- | --- | --- |
| raw_milk | Raw milk | Farm-gate raw material | H1 upstream |
| drinking_milk | Drinking milk | Comparable dairy product group | H1/H2 where matching is available |
| sour_cream | Sour cream | Comparable dairy product group | H1/H2 where matching is available |
| kefir | Kefir | Comparable dairy product group | H1/H2 where matching is available |
| butter | Butter | Comparable dairy product group | H1/H2 where matching is available |
| hard_cheese | Hard cheese | Comparable dairy product group | H1/H2 where matching is available |
| soft_cheese | Soft cheese | Comparable dairy product group | Audit or exclusion |
| cottage_cheese | Cottage cheese | Comparable dairy product group | H2 / retail-ProZorro mechanism if support is sufficient |
| skim_milk_powder | Skim milk powder | Comparable dairy product group | H1/H2 where matching is available |
| cream | Cream | Comparable dairy product group | H2 / retail-ProZorro mechanism if support is sufficient |
| condensed_milk | Condensed milk | Comparable dairy product group | H2 / retail-ProZorro mechanism if support is sufficient |
| yogurt | Yogurt | Comparable dairy product group | H2 / retail-ProZorro mechanism if support is sufficient |
| other_dairy | Other dairy | Dairy but weakly comparable | Audit or exclusion |
| exclude_non_dairy | Excluded non-dairy | Excluded | Audit or exclusion |

## Decision

Observed State Statistics Service of Ukraine (SSSU) monthly data are the main empirical base. Old reconstructed sheets are retained only as robustness or appendix evidence unless their validation is strong. ProZorro and retail data are useful for institutional and promotional mechanisms, but their shorter overlap makes them weaker than the official monthly core.
