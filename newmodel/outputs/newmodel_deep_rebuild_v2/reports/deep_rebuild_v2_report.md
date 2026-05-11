# Deep Market-Power Rebuild V2 Report

## Executive Correction

FACT - The previous DOCX was too short and structurally partial. This v2 package separates data audit, model evidence, reliability screening, figure selection, and a new full-volume DOCX draft.
FACT - The newmodel data are not model-ready until processor/farm tonne units, ProZorro text numbers, retail classification, and consumer-sheet corruption are repaired.
INTERPRETATION - The main thesis evidence should be observed Ukrainian monthly data first, old weekly/daily models second, and EU reconstruction only as appendix robustness.
HYPOTHESIS - Market power is inferred from incomplete, delayed, selective, or asymmetric adjustment, not from coefficient significance alone.
GAP - The grading images mentioned by the user are not available as identifiable local files; the report uses Commented_draft2 and the transcript as observed feedback anchors.

## Newmodel Workbook Audit

| sheet | sample_rows | columns | has_product_column | has_date_column | risk_note |
| --- | --- | --- | --- | --- | --- |
| CME III | 250 | Date; CME III UAH | False | True | No special risk beyond standard unit/date/product audit. |
| FarmGate(oldmodel) | 250 | date; sheet; ua_indicator; region; ua_product; farm_type; unit; eu_class; eu_price_unit; method; weight_signature; fit_alpha; fit_beta; fit_overlap_n; price_linear; price_pchip; product; indicator_en; region_en; unit_en; farm_type_en | True | True | Farm_price magnitudes are tonne-level despite short unit label; main model converts to UAH/kg. |
| Producer(oldmodel) | 250 | date; sheet; ua_indicator; region; ua_product; unit; eu_class; eu_price_unit; method; weight_signature; fit_alpha; fit_beta; fit_overlap_n; price_linear; price_pchip; product; indicator_en; region_en; unit_en | True | True | No special risk beyond standard unit/date/product audit. |
| Consumer(oldmodel) | 250 | date; sheet; ua_indicator; region; ua_product; unit; eu_class; eu_price_unit; method; weight_signature; fit_alpha; fit_beta; fit_overlap_n; price_linear; price_pchip; product; indicator_en; region_en; unit_en | True | True | Integrated consumer sheet has 250 sample implausible values above 1000; raw component workbook is preferred. |
| Prozorro(oldmodel) | 250 | date; product_ua; title_ua; quantity; unit_ua; unit_price; organizer; winner; organizer_region_ua; expected_value; contract_value_initial; contract_value_current; product; organizer_region_en; unit_en | True | True | ProZorroM(full) contains text numbers/non-breaking spaces; parser strips spaces and normalizes decimal signs. |
| ProzorroM(full) | 250 | Ідентифікатор процедури; ...; Профіль; Товар; Кількість; Одиниця виміру; Ціна за одиницю; Організатор; Переможець; CPV категорії; Категорія; Регіон організатора; Очікувана вартість; Сума договорів початкова; Сума договорів поточна; Дата публікації процедури | False | False | ProZorroM(full) contains text numbers/non-breaking spaces; parser strips spaces and normalizes decimal signs. |
| Europe | 250 | date; Country; Product; Price (€/100kg); EUR_UAH_rate; Price (UAH/kg) | True | True | No special risk beyond standard unit/date/product audit. |
| Silpo | 250 | timestamp; date; product_title; product_name; brand; entity; broader_category; product_ua; fat_pct; pack_qty_final; pack_unit_final; qty_std; unit_std; price_current; unit_price; discount_value; discount_%; discount_dummy_bulk; discount_dummy_discount; discount_dummy_regular; product; unit_en | True | True | Retail product labels are repaired from product_title/product_name; old labels are not trusted. |
| Farm_price | 27 | Показник; Територіальний розріз; Вид сільськогосподарської продукції; Періодичність; Одиниця виміру; 2015-M01; 2015-M02; 2015-M03; 2015-M04; 2015-M05; 2015-M06; 2015-M07; 2015-M08; 2015-M09; 2015-M10; 2015-M11; 2015-M12; 2016-M01; 2016-M02; 2016-M03; 2016-M04; 2016-M05; 2016-M06; 2016-M07; 2016-M08 | False | True | Farm_price magnitudes are tonne-level despite short unit label; main model converts to UAH/kg. |
| Consumer_price | 78 | Показник; Територіальний розріз; Тип товарів і послуг; Періодичність; Одиниця виміру; 2017-M01; 2017-M02; 2017-M03; 2017-M04; 2017-M05; 2017-M06; 2017-M07; 2017-M08; 2017-M09; 2017-M10; 2017-M11; 2017-M12; 2018-M01; 2018-M02; 2018-M03; 2018-M04; 2018-M05; 2018-M06; 2018-M07; 2018-M08 | False | True | Integrated consumer sheet has 340 sample implausible values above 1000; raw component workbook is preferred. |
| Processor_price | 6 | Показник; Територіальний розріз; Категорія розрізу; Розріз; Періодичність; Одиниця виміру; 2013-M01; 2013-M02; 2013-M03; 2013-M04; 2013-M05; 2013-M06; 2013-M07; 2013-M08; 2013-M09; 2013-M10; 2013-M11; 2013-M12; 2014-M01; 2014-M02; 2014-M03; 2014-M04; 2014-M05; 2014-M06; 2014-M07 | False | True | Processor_price is UAH per tonne in raw file; main model converts to UAH/kg. |
| Novus | 250 | timestamp; date; product_title; product_name; brand; entity; broader_category; product_ua; fat_pct; pack_qty_final; pack_unit_final; qty_std; unit_std; price_current; unit_price; discount_value; discount_dummy_bulk; discount_dummy_discount; discount_dummy_regular; product_ua_legacy_1; unit_en; product | True | True | Retail product labels are repaired from product_title/product_name; old labels are not trusted. |

## Retail Repair Audit

| check | value | product_old | product | unit_quality_flag_v2 | rows |
| --- | --- | --- | --- | --- | --- |
| retail_rows | 8.83e+04 |  |  |  |  |
| product_reclassified_rows | 2.531e+04 |  |  |  |  |
| uah_kg_rows_v1 | 1271 |  |  |  |  |
| uah_kg_rows_v2 | 1170 |  |  |  |  |
| excluded_non_dairy_rows | 1.493e+04 |  |  |  |  |
|  |  | yogurt | yogurt | package_price_only | 2.394e+04 |
|  |  | drinking_milk | drinking_milk | package_price_only | 9337 |
|  |  | butter | butter | package_price_only | 5448 |
|  |  | sour_cream | sour_cream | package_price_only | 5177 |
|  |  | hard_cheese | soft_cheese | package_price_only | 4884 |
|  |  | kefir | kefir | package_price_only | 4330 |
|  |  | exclude_non_dairy | other_dairy | package_price_only | 4042 |
|  |  | exclude_non_dairy | exclude_non_dairy | exclude_non_dairy | 3505 |
|  |  | cottage_cheese | cottage_cheese | package_price_only | 3379 |
|  |  | hard_cheese | exclude_non_dairy | exclude_non_dairy | 3285 |
|  |  | cream | cream | package_price_only | 3247 |
|  |  | other_dairy | other_dairy | package_price_only | 2451 |
|  |  | drinking_milk | exclude_non_dairy | exclude_non_dairy | 2125 |
|  |  | yogurt | exclude_non_dairy | exclude_non_dairy | 1895 |
|  |  | condensed_milk | condensed_milk | package_price_only | 1480 |
|  |  | cottage_cheese | exclude_non_dairy | exclude_non_dairy | 997 |
|  |  | cottage_cheese | other_dairy | package_price_only | 923 |
|  |  | butter | exclude_non_dairy | exclude_non_dairy | 915 |
|  |  | kefir | other_dairy | package_price_only | 879 |
|  |  | condensed_milk | exclude_non_dairy | exclude_non_dairy | 874 |
|  |  | condensed_milk | other_dairy | package_price_only | 836 |
|  |  | sour_cream | exclude_non_dairy | exclude_non_dairy | 818 |
|  |  | cream | exclude_non_dairy | exclude_non_dairy | 517 |
|  |  | hard_cheese | other_dairy | package_price_only | 396 |
|  |  | drinking_milk | other_dairy | package_price_only | 384 |
|  |  | yogurt | yogurt | ok_uah_kg | 231 |
|  |  | butter | other_dairy | package_price_only | 217 |
|  |  | cream | other_dairy | package_price_only | 195 |
|  |  | hard_cheese | soft_cheese | ok_uah_kg | 192 |
|  |  | skim_milk_powder | drinking_milk | package_price_only | 162 |
|  |  | cottage_cheese | soft_cheese | package_price_only | 128 |
|  |  | sour_cream | other_dairy | package_price_only | 100 |
|  |  | other_dairy | drinking_milk | package_price_only | 96 |
|  |  | drinking_milk | drinking_milk | ok_uah_kg | 84 |
|  |  | drinking_milk | butter | package_price_only | 71 |

## Additional Model Families Added

The v2 rebuild adds Dynamic Ordinary Least Squares (DOLS), local projections, and a Loy-style threshold error-correction first-stage. These are used in addition to Error Correction Model (ECM), Vector Error Correction Model (VECM), Autoregressive Distributed Lag (ARDL), and Nonlinear Autoregressive Distributed Lag (NARDL) evidence from the old and new packages.
| model_family | rows |
| --- | --- |
| Threshold ECM (Loy-style) | 27 |
| DOLS | 15 |
| Local Projection h=1 month | 15 |
| Local Projection h=3 month | 15 |
| Local Projection h=6 month | 13 |
| Local Projection h=1 day | 12 |
| Local Projection h=7 day | 12 |
| Local Projection h=14 day | 12 |

## Integrated Reliability Screen

| integrated_reliability | rows |
| --- | --- |
| appendix or discard | 12375 |
| probable / supporting | 685 |
| main reliable | 214 |

## Selected Model Set

| hypothesis | link | product | source_block | model_family | n_obs | coef | pvalue | integrated_reliability | thesis_use |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| H1 | FarmGate -> ProZorro | butter | newmodel_v2 | Threshold ECM (Loy-style) | 34 | 1.376 | 2.451e-14 | appendix or discard | appendix only / do not headline |
| H1 | FarmGate -> ProZorro | condensed_milk | newmodel_v2 | Threshold ECM (Loy-style) | 32 | 0.4268 | 0.003922 | appendix or discard | appendix only / do not headline |
| H1 | FarmGate -> ProZorro | cottage_cheese | newmodel_v2 | Threshold ECM (Loy-style) | 34 | 0.2693 | 0.02589 | appendix or discard | appendix only / do not headline |
| H1 | FarmGate -> ProZorro | drinking_milk | newmodel_v2 | Threshold ECM (Loy-style) | 34 | 0.8067 | 4.867e-13 | appendix or discard | appendix only / do not headline |
| H1 | FarmGate -> ProZorro | hard_cheese | newmodel_v2 | Threshold ECM (Loy-style) | 34 | 0.8858 | 5.745e-10 | appendix or discard | appendix only / do not headline |
| H1 | FarmGate -> ProZorro | kefir | newmodel_v2 | Threshold ECM (Loy-style) | 32 | 0.5958 | 5.263e-06 | appendix or discard | appendix only / do not headline |
| H1 | FarmGate -> Processor | butter | newmodel_v2 | Threshold ECM (Loy-style) | 129 | 1.07 | 1.249e-110 | probable / supporting | short supporting block or appendix |
| H1 | FarmGate -> Processor | drinking_milk | newmodel_v2 | Threshold ECM (Loy-style) | 129 | 0.9446 | 5.805e-109 | main reliable | main text |
| H1 | FarmGate -> Processor | hard_cheese | newmodel_v2 | Threshold ECM (Loy-style) | 129 | 0.8742 | 7.034e-114 | main reliable | main text |
| H1 | FarmGate -> Processor | kefir | newmodel_v2 | Threshold ECM (Loy-style) | 129 | 0.9627 | 2.111e-110 | main reliable | main text |
| H1 | FarmGate -> Processor | skim_milk_powder | newmodel_v2 | Threshold ECM (Loy-style) | 129 | 0.7803 | 1.4e-67 | main reliable | main text |
| H1 | FarmGate -> Processor | sour_cream | newmodel_v2 | Threshold ECM (Loy-style) | 129 | 0.9227 | 7.308e-105 | main reliable | main text |
| H1 | FarmGate -> Procurement | butter | old_final_daily | NARDL | 274 | 2.312 | 7.889e-05 | main reliable | main text |
| H1 | FarmGate -> Procurement | cheese | old_final_daily | ECM | 268 | 1.478 | 5.132e-06 | main reliable | main text |
| H1 | FarmGate -> Procurement | condensed_milk | old_final_daily | ECM | 270 | -0.4487 | 2.947e-07 | main reliable | main text |
| H1 | FarmGate -> Procurement | cream | old_final_daily | ECM | 273 | 0.6482 | 3.155e-06 | main reliable | main text |
| H1 | FarmGate -> Procurement | milk | old_final_daily | ECM | 268 | 0.0455 | 2.667e-20 | main reliable | main text |
| H1 | FarmGate -> Procurement | sour_cream | old_final_daily | NARDL | 274 | 2.575 | 7.934e-08 | main reliable | main text |
| H1 | FarmGate -> Producer | butter | old_final_daily | NARDL | 1476 | -3.78 | 0.001156 | main reliable | main text |
| H1 | FarmGate -> Producer | cheese | old_final_daily | ECM | 1476 | 0.7669 | 0.002256 | main reliable | main text |
| H1 | FarmGate -> Producer | milk | old_final_daily | ECM | 1476 | 0.9691 | 0.002117 | main reliable | main text |
| H1 | FarmGate -> Producer | milk_powder | old_final_daily | ECM | 1475 | 0.2594 | 0.001385 | main reliable | main text |
| H1 | FarmGate -> Producer | sour_cream | old_final_daily | ECM | 1476 | 1.08 | 0.0001205 | main reliable | main text |
| H1 | FarmGateUA -> ProducerUA | butter | old_final_lp | LP_linear | 1476 | 1.063 | 1.824e-75 | main reliable | main text |
| H1 | FarmGateUA -> ProducerUA | cheese | old_final_lp | LP_linear | 1476 | 0.6316 | 4.322e-81 | main reliable | main text |
| H1 | FarmGateUA -> ProducerUA | hard_cheese | second_stage_lp | LP_linear | 1458 | 0.9384 | 7.054e-05 | main reliable | main text |
| H1 | FarmGateUA -> ProducerUA | milk | old_final_lp | LP_linear | 1476 | 0.5903 | 3.678e-164 | main reliable | main text |
| H1 | FarmGateUA -> ProducerUA | milk_powder | old_final_lp | LP_linear | 1476 | 0.6926 | 4.505e-48 | main reliable | main text |
| H1 | FarmGateUA -> ProducerUA | sour_cream | old_final_lp | LP_linear | 1476 | 0.6969 | 8.381e-51 | main reliable | main text |
| H1 | Index FarmGate -> Producer | aggregate | old_final_index | ECM | 210 | 0.8844 | 5.281e-05 | main reliable | main text |
| H1 | ProducerUA -> FarmGateUA | butter | old_final_lp | LP_linear | 1476 | 0.5304 | 4.368e-16 | appendix or discard | appendix only / do not headline |
| H1 | ProducerUA -> FarmGateUA | cheese | old_final_lp | LP_linear | 1476 | 0.8763 | 5.88e-11 | appendix or discard | appendix only / do not headline |
| H1 | ProducerUA -> FarmGateUA | hard_cheese | second_stage_lp | LP_linear | 1458 | 0.07222 | 0.004832 | appendix or discard | appendix only / do not headline |
| H1 | ProducerUA -> FarmGateUA | milk | old_final_lp | LP_linear | 1476 | 1.191 | 1.626e-21 | appendix or discard | appendix only / do not headline |
| H1 | ProducerUA -> FarmGateUA | milk_powder | old_final_lp | LP_linear | 1476 | 0.6857 | 1.664e-08 | appendix or discard | appendix only / do not headline |
| H1 | ProducerUA -> FarmGateUA | sour_cream | old_final_lp | LP_linear | 1476 | 0.6801 | 5.149e-10 | appendix or discard | appendix only / do not headline |
| H1 | producer_farmgate | butter | old_final_margin | old_final_margin | 1477 |  |  | appendix or discard | appendix only / do not headline |
| H1 | producer_farmgate | cheese | old_final_margin | old_final_margin | 1477 |  |  | appendix or discard | appendix only / do not headline |
| H1 | producer_farmgate | hard_cheese | second_stage_margin | second_stage_margin | 1459 |  |  | appendix or discard | appendix only / do not headline |
| H1 | producer_farmgate | milk | old_final_margin | old_final_margin | 1477 |  |  | appendix or discard | appendix only / do not headline |
| H1 | producer_farmgate | milk_powder | old_final_margin | old_final_margin | 1477 |  |  | appendix or discard | appendix only / do not headline |
| H1 | producer_farmgate | sour_cream | old_final_margin | old_final_margin | 1477 |  |  | appendix or discard | appendix only / do not headline |
| H1 |  |  | newmodel_v1_ecm_ardl_nardl | ECM |  | 1.18 |  | appendix or discard | appendix only / do not headline |
| H1/H2 | long equilibrium | hard_cheese | extra_long_equilibrium | extra_long_equilibrium | 209 | 0.9801 | 0 | probable / supporting | short supporting block or appendix |
| H1/H2 | long equilibrium | milk | extra_long_equilibrium | extra_long_equilibrium | 209 | 0.9741 | 0 | probable / supporting | short supporting block or appendix |
| H1/H2 | long equilibrium | sour_cream | extra_long_equilibrium | extra_long_equilibrium | 209 | 0.9948 | 0 | probable / supporting | short supporting block or appendix |
| H1/H2 | procurement bridge | hard_cheese | extra_procurement_bridge | extra_procurement_bridge | 37 | 1.314 | 0.4025 | appendix or discard | appendix only / do not headline |
| H1/H2 | procurement bridge | milk | extra_procurement_bridge | extra_procurement_bridge | 37 | 0.1456 | 0.937 | appendix or discard | appendix only / do not headline |
| H1/H2 | procurement bridge | sour_cream | extra_procurement_bridge | extra_procurement_bridge | 37 | 0.9101 | 0.839 | appendix or discard | appendix only / do not headline |
| H2 | FarmGate -> Retail combined | butter | old_final_daily | NARDL | 82 | -3.726 | 0.001154 | appendix or discard | appendix only / do not headline |
| H2 | FarmGate -> Retail combined | cheese | old_final_daily | NARDL | 83 | 15.69 | 0.07232 | appendix or discard | appendix only / do not headline |
| H2 | FarmGate -> Retail combined | condensed_milk | old_final_daily | NARDL | 82 | -0.3642 | 0.001919 | appendix or discard | appendix only / do not headline |
| H2 | FarmGate -> Retail combined | cream | old_final_daily | NARDL | 83 | -14.12 | 0.009315 | appendix or discard | appendix only / do not headline |
| H2 | FarmGate -> Retail combined | milk | old_final_daily | NARDL | 83 | -0.7248 | 0.01852 | appendix or discard | appendix only / do not headline |
| H2 | FarmGate -> Retail combined | other | old_final_daily | ECM | 80 | -3.092 | 0.2198 | appendix or discard | appendix only / do not headline |
| H2 | FarmGate -> Retail combined | sour_cream | old_final_daily | NARDL | 82 | -3.864 | 0.01743 | appendix or discard | appendix only / do not headline |
| H2 | FarmGate -> Retail combined | yogurt_dessert | old_final_daily | NARDL | 83 | 9.51 | 0.001147 | appendix or discard | appendix only / do not headline |
| H2 | FarmGateUA -> ProZorro | butter | second_stage_lp | LP_linear | 260 | -9.78 | 0.09383 | probable / supporting | short supporting block or appendix |
| H2 | FarmGateUA -> ProZorro | cheese | old_final_lp | LP_linear | 265 | 55.36 | 0.09266 | probable / supporting | short supporting block or appendix |
| H2 | FarmGateUA -> ProZorro | condensed_milk | old_final_lp | LP_linear | 266 | 18.52 | 0.03821 | probable / supporting | short supporting block or appendix |
| H2 | FarmGateUA -> ProZorro | cottage_cheese | second_stage_lp | LP_linear | 254 | 25.76 | 0.0004703 | probable / supporting | short supporting block or appendix |
| H2 | FarmGateUA -> ProZorro | cream | old_final_lp | LP_linear | 264 | 25.92 | 0.0554 | probable / supporting | short supporting block or appendix |
| H2 | FarmGateUA -> ProZorro | hard_cheese | second_stage_lp | LP_linear | 260 | -10.3 | 0.05772 | probable / supporting | short supporting block or appendix |
| H2 | FarmGateUA -> ProZorro | milk | old_final_lp | LP_linear | 268 | 0.4887 | 0.9118 | appendix or discard | appendix only / do not headline |
| H2 | FarmGateUA -> ProZorro | milk_powder | old_final_lp | LP_linear | 74 | 0.08651 | 0.5548 | appendix or discard | appendix only / do not headline |
| H2 | FarmGateUA -> ProZorro | sour_cream | old_final_lp | LP_linear | 268 | -22.25 | 0.07415 | probable / supporting | short supporting block or appendix |
| H2 | FarmGateUA -> Retail | butter | old_final_lp | LP_linear | 56 | -22.33 | 0.05251 | appendix or discard | appendix only / do not headline |
| H2 | FarmGateUA -> Retail | cheese | old_final_lp | LP_linear | 60 | -90.71 | 0.0001272 | appendix or discard | appendix only / do not headline |
| H2 | FarmGateUA -> Retail | condensed_milk | old_final_lp | LP_linear | 56 | 10.31 | 0.06629 | appendix or discard | appendix only / do not headline |
| H2 | FarmGateUA -> Retail | cottage_cheese | second_stage_lp | LP_linear | 58 | 7.131 | 0.0583 | appendix or discard | appendix only / do not headline |
| H2 | FarmGateUA -> Retail | cream | old_final_lp | LP_linear | 64 | 17.74 | 0.09549 | appendix or discard | appendix only / do not headline |
| H2 | FarmGateUA -> Retail | hard_cheese | second_stage_lp | LP_linear | 60 | -77 | 0.01517 | appendix or discard | appendix only / do not headline |
| H2 | FarmGateUA -> Retail | milk | old_final_lp | LP_linear | 66 | -1.447 | 0.8172 | appendix or discard | appendix only / do not headline |
| H2 | FarmGateUA -> Retail | milk_powder | old_final_lp | LP_linear | 42 | -93.06 | 0.009634 | appendix or discard | appendix only / do not headline |
| H2 | FarmGateUA -> Retail | other | old_final_lp | LP_linear | 58 | 23.6 | 0.08638 | appendix or discard | appendix only / do not headline |
| H2 | FarmGateUA -> Retail | sour_cream | old_final_lp | LP_linear | 58 | 17.06 | 0.000188 | appendix or discard | appendix only / do not headline |
| H2 | FarmGateUA -> Retail | yogurt_dessert | old_final_lp | LP_linear | 54 | 36.46 | 0.03875 | appendix or discard | appendix only / do not headline |
| H2 | FarmGateUA -> Retail optimal | butter | old_final_lp | LP_linear | 56 | -22.33 | 0.05251 | appendix or discard | appendix only / do not headline |
| H2 | FarmGateUA -> Retail optimal | cheese | old_final_lp | LP_linear | 60 | -90.71 | 0.0001272 | appendix or discard | appendix only / do not headline |
| H2 | FarmGateUA -> Retail optimal | condensed_milk | old_final_lp | LP_linear | 56 | 10.31 | 0.06629 | appendix or discard | appendix only / do not headline |

## Loy-Style Block

First-stage rows estimate pass-through speed and asymmetry. Second-stage rows regress those measures on discount intensity, SKU support, perishability, and retail-link indicators.
| hypothesis | link | product | n_obs | speed_measure | asymmetry_measure | discount_mean_x | discount_mean_y | sku_support_x | sku_support_y | perishable |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| H1 | FarmGate -> Processor | butter | 129 | 0.02612 | 0.04193 |  | 0.1941 |  | 114 | 0 |
| H1 | FarmGate -> Processor | drinking_milk | 129 | 0.04407 | 0.0222 |  | 0.2035 |  | 198 | 1 |
| H1 | FarmGate -> Processor | hard_cheese | 129 | 0.09375 | -0.1875 |  | 0 |  | 1 | 0 |
| H1 | FarmGate -> Processor | kefir | 129 | 0.01778 | 0.01042 |  | 0.2021 |  | 90 | 1 |
| H1 | FarmGate -> Processor | skim_milk_powder | 129 | 0.01289 | -0.02578 |  |  |  |  | 0 |
| H1 | FarmGate -> Processor | sour_cream | 129 | 0.06536 | 0.08175 |  | 0.2124 |  | 105 | 1 |
| H1 | FarmGate -> ProZorro | butter | 34 | 0.4889 | 0.4598 |  | 0.1941 |  | 114 | 0 |
| H1 | FarmGate -> ProZorro | condensed_milk | 32 | 0.799 | -0.2236 |  | 0.1903 |  | 31 | 0 |
| H1 | FarmGate -> ProZorro | cottage_cheese | 34 | 0.6929 | 0.2072 |  | 0.2081 |  | 70 | 0 |
| H1 | FarmGate -> ProZorro | drinking_milk | 34 | 0.4045 | 0.4801 |  | 0.2035 |  | 198 | 1 |
| H1 | FarmGate -> ProZorro | hard_cheese | 34 | 0.6951 | -0.7551 |  | 0 |  | 1 | 0 |
| H1 | FarmGate -> ProZorro | kefir | 32 | 0.7471 | -0.8564 |  | 0.2021 |  | 90 | 1 |
| H2 | Processor -> Consumer | drinking_milk | 109 | 0.06444 | -0.02787 |  | 0.2035 |  | 198 | 1 |
| H2 | Processor -> Consumer | sour_cream | 109 | 0.0133 | -0.0266 |  | 0.2124 |  | 105 | 1 |
| H2 | ProZorro -> Consumer | drinking_milk | 37 | 0.1473 | 0.2945 |  | 0.2035 |  | 198 | 1 |
| H2 | ProZorro -> Retail | butter | 46 | 0.7103 | 0.7298 | 0.2196 | 0.1941 | 114 | 114 | 0 |
| H2 | ProZorro -> Retail | condensed_milk | 46 | 1.206 | 0.2722 | 0.2084 | 0.1903 | 31 | 31 | 0 |
| H2 | ProZorro -> Retail | cottage_cheese | 46 | 1.031 | -0.5132 | 0.2363 | 0.2081 | 70 | 70 | 0 |
| H2 | ProZorro -> Retail | drinking_milk | 46 | 0.7249 | 0.006033 | 0.2431 | 0.2035 | 198 | 198 | 1 |
| H2 | ProZorro -> Retail | kefir | 46 | 0.694 | -0.1347 | 0.2282 | 0.2021 | 90 | 90 | 1 |
| H2 | ProZorro -> Retail | soft_cheese | 46 | 1.057 | 0.3889 | 0.315 | 0.2549 | 100 | 100.5 | 0 |
| H2 | ProZorro -> Retail | butter | 52 | 0.5099 | -0.07885 | 0.1941 | 0.1941 | 114 | 114 | 0 |
| H2 | ProZorro -> Retail | condensed_milk | 50 | 0.1581 | 0.3161 | 0.1903 | 0.1903 | 31 | 31 | 0 |
| H2 | ProZorro -> Retail | cottage_cheese | 52 | 0.4567 | 0.8665 | 0.2081 | 0.2081 | 70 | 70 | 0 |
| H2 | ProZorro -> Retail | drinking_milk | 55 | 1.67 | -0.2802 | 0.2035 | 0.2035 | 198 | 198 | 1 |
| H2 | ProZorro -> Retail | kefir | 52 | 0.5417 | 0.4036 | 0.2021 | 0.2021 | 90 | 90 | 1 |
| H2 | ProZorro -> Retail | soft_cheese | 53 | 0.4994 | -0.9988 | 0.2549 | 0.2549 | 100.5 | 100.5 | 0 |
| dependent | term | coef | pvalue | n_obs | r2 |
| --- | --- | --- | --- | --- | --- |
| speed_measure | const | 0.4029 | 0.0006983 | 27 | 0.1505 |
| speed_measure | perishable | -0.1495 | 0.3555 | 27 | 0.1505 |
| speed_measure | retail_link | 0.2991 | 0.0467 | 27 | 0.1505 |
| asymmetry_measure | const | -0.04423 | 0.7371 | 27 | 0.02922 |
| asymmetry_measure | perishable | -0.04284 | 0.8047 | 27 | 0.02922 |
| asymmetry_measure | retail_link | 0.1454 | 0.413 | 27 | 0.02922 |

## Figures Kept / Rebuilt

| file | title |
| --- | --- |
| /Users/getapple/Documents/KSE/Master Thesis/outputs/newmodel_deep_rebuild_v2/figures/v2_fig_01_h1_monthly_chain.png | H1 monthly farm-gate and processor prices |
| /Users/getapple/Documents/KSE/Master Thesis/outputs/newmodel_deep_rebuild_v2/figures/v2_fig_02_h2_official_bridge.png | H2 processor-consumer official bridge |
| /Users/getapple/Documents/KSE/Master Thesis/outputs/newmodel_deep_rebuild_v2/figures/v2_fig_03_selected_coefficients.png | Selected model coefficient map |
| /Users/getapple/Documents/KSE/Master Thesis/outputs/newmodel_deep_rebuild_v2/figures/v2_fig_04_reliability_screen.png | Integrated reliability screen |
| /Users/getapple/Documents/KSE/Master Thesis/outputs/newmodel_deep_rebuild_v2/figures/v2_fig_05_retail_discounts.png | Retail discount incidence |
| /Users/getapple/Documents/KSE/Master Thesis/outputs/newmodel_deep_rebuild_v2/figures/v2_fig_06_loy_first_stage.png | Loy-style first-stage pass-through measures |
| /Users/getapple/Documents/KSE/Master Thesis/outputs/newmodel_deep_rebuild_v2/figures/v2_fig_07_loy_second_stage.png | Loy-style second-stage correlates |

## DOCX QA

{
  "docx": "/Users/getapple/Documents/KSE/Master Thesis/output/doc/Maksym_Charniuk_MSc_thesis_market_power_deep_rebuild_v2.docx",
  "exists": true,
  "word_count": 13297,
  "paragraphs": 313,
  "tables": 5,
  "images": 6,
  "render": "no_pngs rc=1 stderr=ce -env:UserInstallation=file:///var/folders/rw/l18tb_lj1rx1h1dpt6fbzvs80000gn/T/soffice_profile_8o302y2_ --invisible --headless --norestore --convert-to odt --outdir /var/folders/rw/l18tb_lj1rx1h1dpt6fbzvs80000gn/T/soffice_convert_9687g02b /Users/getapple/Documents/KSE/Master Thesis/output/doc/Maksym_Charniuk_MSc_thesis_market_power_deep_rebuild_v2.docx\nEXIT: 134\nSTDERR:\n/opt/homebrew/bin/soffice: line 2:  6201 Abort trap: 6           '/Applications/LibreOffice.app/Contents/MacOS/soffice' \"$@\"\n",
  "render_pages": 0
}