# RW3 Full Modular Run Summary

## Interpretation Guide
- ADF p>0.05 and KPSS p<0.05 suggests I(1)-like behavior; use differences/cointegration frameworks.
- ADF p<0.05 and KPSS p>0.05 suggests stationarity; level models are more admissible.
- Ljung-Box p<0.05 indicates autocorrelation; include lag terms.
- BP/White p<0.05 indicates heteroskedasticity; use robust/HAC standard errors.
- JB p<0.05 indicates non-normality; rely on robust inference.
- Stability flag=1 indicates drift/break risk; use rolling or split-sample checks.
- Retail transmission should be interpreted with promo controls and without promo controls.

## Run Status
- steps: 19
- failed: 0
- artifact modules: 19

## Module Blocks

### graphs_brand_region

Interpretation:
- mean |coef|=20.3301 | positive share=0.44 | significance share (p<0.05)=0.18 | Interpret signs/magnitudes jointly with diagnostics and sample coverage.

- xlsx files: graphs_brand_region_output.xlsx
- pdf files: graphs_brand_region_report.pdf
- md files: graphs_brand_region_report.md
- png count: 3

### graphs_correlations_lags

Interpretation:
- No explicit test/model tables detected; interpret via module-specific descriptive outputs.

- xlsx files: graphs_correlations_lags_output.xlsx
- pdf files: graphs_correlations_lags_report.pdf
- md files: graphs_correlations_lags_report.md
- png count: 2

### graphs_decomposition

Interpretation:
- No explicit test/model tables detected; interpret via module-specific descriptive outputs.

- xlsx files: graphs_decomposition_output.xlsx
- pdf files: graphs_decomposition_report.pdf
- md files: graphs_decomposition_report.md
- png count: 24

### graphs_overlay_ln

Interpretation:
- No explicit test/model tables detected; interpret via module-specific descriptive outputs.

- xlsx files: graphs_overlay_ln_output.xlsx
- pdf files: graphs_overlay_ln_report.pdf
- md files: graphs_overlay_ln_report.md
- png count: 21

### model_ardl

Interpretation:
- mean |coef|=0.9400 | positive share=0.77 | significance share (p<0.05)=0.27 | Interpret signs/magnitudes jointly with diagnostics and sample coverage.

- xlsx files: model_ardl_output.xlsx
- pdf files: model_ardl_report.pdf
- md files: model_ardl_report.md
- png count: 1

### model_discounts

Interpretation:
- mean |coef|=1.8479 | positive share=0.50 | Interpret signs/magnitudes jointly with diagnostics and sample coverage.

- xlsx files: model_discounts_output.xlsx
- pdf files: model_discounts_report.pdf
- md files: model_discounts_report.md
- png count: 2

### model_ecm

Interpretation:
- mean |coef|=0.6234 | positive share=0.44 | significance share (p<0.05)=1.00 | Interpret signs/magnitudes jointly with diagnostics and sample coverage.

- xlsx files: model_ecm_output.xlsx
- pdf files: model_ecm_report.pdf
- md files: model_ecm_report.md
- png count: 1

### model_forecast_knn

Interpretation:
- mean |coef|=0.5000 | positive share=1.00 | Interpret signs/magnitudes jointly with diagnostics and sample coverage.

- xlsx files: model_forecast_knn_output.xlsx
- pdf files: model_forecast_knn_report.pdf
- md files: model_forecast_knn_report.md
- png count: 3

### model_intersection_bidirectional

Interpretation:
- mean |coef|=0.9493 | positive share=0.52 | significance share (p<0.05)=0.26 | Interpret signs/magnitudes jointly with diagnostics and sample coverage.

- xlsx files: model_intersection_bidirectional_output.xlsx
- pdf files: model_intersection_bidirectional_report.pdf
- md files: model_intersection_bidirectional_report.md
- png count: 2

### model_nardl

Interpretation:
- mean |coef|=0.3855 | positive share=0.50 | significance share (p<0.05)=0.32 | Interpret signs/magnitudes jointly with diagnostics and sample coverage.

- xlsx files: model_nardl_output.xlsx
- pdf files: model_nardl_report.pdf
- md files: model_nardl_report.md
- png count: 2

### model_short_chain_regional

Interpretation:
- mean |coef|=2.6086 | positive share=0.58 | significance share (p<0.05)=0.04 | Interpret signs/magnitudes jointly with diagnostics and sample coverage.

- xlsx files: model_short_chain_regional_output.xlsx
- pdf files: model_short_chain_regional_report.pdf
- md files: model_short_chain_regional_report.md
- png count: 1

### model_vecm

Interpretation:
- mean cointegration rank=2.33 | Interpret signs/magnitudes jointly with diagnostics and sample coverage.

- xlsx files: model_vecm_output.xlsx
- pdf files: model_vecm_report.pdf
- md files: model_vecm_report.md
- png count: 1

### sheet_cme

Interpretation:
- I(1)-like share=0.33, stationary share=0.00, autocorr risk share=0.33, heterosk risk share=0.00, non-normal share=0.33, stability risk share=0.33. Model action: cointegration/differences + lag structure + robust/HAC + stability checks. | significance share (p<0.05)=0.50 | Interpret signs/magnitudes jointly with diagnostics and sample coverage.

- xlsx files: sheet_cme_output.xlsx
- pdf files: sheet_cme_report.pdf
- md files: sheet_cme_report.md
- png count: 3

### sheet_consumerua

Interpretation:
- I(1)-like share=1.00, stationary share=0.00, autocorr risk share=1.00, heterosk risk share=1.00, non-normal share=1.00, stability risk share=1.00. Model action: cointegration/differences + lag structure + robust/HAC + stability checks. | significance share (p<0.05)=0.67 | Interpret signs/magnitudes jointly with diagnostics and sample coverage.

- xlsx files: sheet_consumerua_output.xlsx
- pdf files: sheet_consumerua_report.pdf
- md files: sheet_consumerua_report.md
- png count: 3

### sheet_eu

Interpretation:
- I(1)-like share=0.33, stationary share=0.00, autocorr risk share=0.22, heterosk risk share=0.06, non-normal share=0.33, stability risk share=0.33. Model action: cointegration/differences + lag structure + robust/HAC + stability checks. | significance share (p<0.05)=0.50 | Interpret signs/magnitudes jointly with diagnostics and sample coverage.

- xlsx files: sheet_eu_output.xlsx
- pdf files: sheet_eu_report.pdf
- md files: sheet_eu_report.md
- png count: 3

### sheet_novus

Interpretation:
- I(1)-like share=0.00, stationary share=0.00, autocorr risk share=0.00, heterosk risk share=0.00, non-normal share=0.00, stability risk share=0.00. Model action: cointegration/differences + lag structure + robust/HAC + stability checks. | Result table has no standard coefficient/p-value columns; interpret by table-specific fields. | Interpret signs/magnitudes jointly with diagnostics and sample coverage.

- xlsx files: sheet_novus_output.xlsx
- pdf files: sheet_novus_report.pdf
- md files: sheet_novus_report.md
- png count: 4

### sheet_producerua

Interpretation:
- I(1)-like share=1.00, stationary share=0.00, autocorr risk share=1.00, heterosk risk share=1.00, non-normal share=1.00, stability risk share=1.00. Model action: cointegration/differences + lag structure + robust/HAC + stability checks. | significance share (p<0.05)=0.67 | Interpret signs/magnitudes jointly with diagnostics and sample coverage.

- xlsx files: sheet_producerua_output.xlsx
- pdf files: sheet_producerua_report.pdf
- md files: sheet_producerua_report.md
- png count: 3

### sheet_prozorro

Interpretation:
- I(1)-like share=0.19, stationary share=0.10, autocorr risk share=0.10, heterosk risk share=0.00, non-normal share=0.05, stability risk share=0.29. Model action: cointegration/differences + lag structure + robust/HAC + stability checks. | significance share (p<0.05)=0.21 | Interpret signs/magnitudes jointly with diagnostics and sample coverage.

- xlsx files: sheet_prozorro_output.xlsx
- pdf files: sheet_prozorro_report.pdf
- md files: sheet_prozorro_report.md
- png count: 4

### sheet_silpo

Interpretation:
- I(1)-like share=0.00, stationary share=0.00, autocorr risk share=0.00, heterosk risk share=0.00, non-normal share=0.00, stability risk share=0.00. Model action: cointegration/differences + lag structure + robust/HAC + stability checks. | Result table has no standard coefficient/p-value columns; interpret by table-specific fields. | Interpret signs/magnitudes jointly with diagnostics and sample coverage.

- xlsx files: sheet_silpo_output.xlsx
- pdf files: sheet_silpo_report.pdf
- md files: sheet_silpo_report.md
- png count: 4

## Tests Summary

- sheet_cme | sheet_cme_output.xlsx | tests: I(1)-like share=0.33, stationary share=0.00, autocorr risk share=0.33, heterosk risk share=0.00, non-normal share=0.33, stability risk share=0.33. Model action: cointegration/differences + lag structure + robust/HAC + stability checks.
- sheet_consumerua | sheet_consumerua_output.xlsx | tests: I(1)-like share=1.00, stationary share=0.00, autocorr risk share=1.00, heterosk risk share=1.00, non-normal share=1.00, stability risk share=1.00. Model action: cointegration/differences + lag structure + robust/HAC + stability checks.
- sheet_eu | sheet_eu_output.xlsx | tests: I(1)-like share=0.33, stationary share=0.00, autocorr risk share=0.22, heterosk risk share=0.06, non-normal share=0.33, stability risk share=0.33. Model action: cointegration/differences + lag structure + robust/HAC + stability checks.
- sheet_novus | sheet_novus_output.xlsx | tests: I(1)-like share=0.00, stationary share=0.00, autocorr risk share=0.00, heterosk risk share=0.00, non-normal share=0.00, stability risk share=0.00. Model action: cointegration/differences + lag structure + robust/HAC + stability checks.
- sheet_producerua | sheet_producerua_output.xlsx | tests: I(1)-like share=1.00, stationary share=0.00, autocorr risk share=1.00, heterosk risk share=1.00, non-normal share=1.00, stability risk share=1.00. Model action: cointegration/differences + lag structure + robust/HAC + stability checks.
- sheet_prozorro | sheet_prozorro_output.xlsx | tests: I(1)-like share=0.19, stationary share=0.10, autocorr risk share=0.10, heterosk risk share=0.00, non-normal share=0.05, stability risk share=0.29. Model action: cointegration/differences + lag structure + robust/HAC + stability checks.
- sheet_silpo | sheet_silpo_output.xlsx | tests: I(1)-like share=0.00, stationary share=0.00, autocorr risk share=0.00, heterosk risk share=0.00, non-normal share=0.00, stability risk share=0.00. Model action: cointegration/differences + lag structure + robust/HAC + stability checks.

## Results Summary

- graphs_brand_region | graphs_brand_region_output.xlsx | Brand_Economic_Metrics: mean |coef|=20.3301 | positive share=0.44 | significance share (p<0.05)=0.18 | Interpret signs/magnitudes jointly with diagnostics and sample coverage.
- model_ardl | model_ardl_output.xlsx | ARDL_Summary: mean |coef|=0.9400 | positive share=0.77 | significance share (p<0.05)=0.27 | Interpret signs/magnitudes jointly with diagnostics and sample coverage.
- model_discounts | model_discounts_output.xlsx | Silpo_Transmission_PromoCtrl: mean |coef|=1.8479 | positive share=0.50 | Interpret signs/magnitudes jointly with diagnostics and sample coverage.
- model_ecm | model_ecm_output.xlsx | ARDL_Summary: mean |coef|=0.9400 | positive share=0.77 | significance share (p<0.05)=0.27 | Interpret signs/magnitudes jointly with diagnostics and sample coverage.
- model_ecm | model_ecm_output.xlsx | ECM_Summary: mean |coef|=0.6234 | positive share=0.44 | significance share (p<0.05)=1.00 | Interpret signs/magnitudes jointly with diagnostics and sample coverage.
- model_forecast_knn | model_forecast_knn_output.xlsx | Synthetic_Influence_Coefficient: mean |coef|=0.5000 | positive share=1.00 | Interpret signs/magnitudes jointly with diagnostics and sample coverage.
- model_forecast_knn | model_forecast_knn_output.xlsx | Synthetic_to_Consumer_Link: mean |coef|=0.9907 | positive share=0.33 | significance share (p<0.05)=0.00 | Interpret signs/magnitudes jointly with diagnostics and sample coverage.
- model_intersection_bidirectional | model_intersection_bidirectional_output.xlsx | Bidirectional_Results: mean |coef|=0.9493 | positive share=0.52 | significance share (p<0.05)=0.26 | Interpret signs/magnitudes jointly with diagnostics and sample coverage.
- model_intersection_bidirectional | model_intersection_bidirectional_output.xlsx | Intersection_Combination_Detail: mean |coef|=4.5334 | positive share=0.50 | significance share (p<0.05)=0.69 | Interpret signs/magnitudes jointly with diagnostics and sample coverage.
- model_intersection_bidirectional | model_intersection_bidirectional_output.xlsx | Intersection_Combination_Summar: mean |coef|=3.1201 | positive share=0.33 | significance share (p<0.05)=0.69 | Interpret signs/magnitudes jointly with diagnostics and sample coverage.
- model_nardl | model_nardl_output.xlsx | NARDL_Summary: mean |coef|=0.3855 | positive share=0.50 | significance share (p<0.05)=0.32 | Interpret signs/magnitudes jointly with diagnostics and sample coverage.
- model_short_chain_regional | model_short_chain_regional_output.xlsx | Chain_Effects_Details: mean |coef|=2.6086 | positive share=0.58 | significance share (p<0.05)=0.04 | Interpret signs/magnitudes jointly with diagnostics and sample coverage.
- model_short_chain_regional | model_short_chain_regional_output.xlsx | Chain_Effects_Summary: mean |coef|=2.6086 | positive share=0.58 | significance share (p<0.05)=0.04 | Interpret signs/magnitudes jointly with diagnostics and sample coverage.
- model_vecm | model_vecm_output.xlsx | VECM_Summary: mean cointegration rank=2.33 | Interpret signs/magnitudes jointly with diagnostics and sample coverage.
- sheet_cme | sheet_cme_output.xlsx | tests: significance share (p<0.05)=0.50 | Interpret signs/magnitudes jointly with diagnostics and sample coverage.
- sheet_consumerua | sheet_consumerua_output.xlsx | tests: significance share (p<0.05)=0.67 | Interpret signs/magnitudes jointly with diagnostics and sample coverage.
- sheet_eu | sheet_eu_output.xlsx | tests: significance share (p<0.05)=0.50 | Interpret signs/magnitudes jointly with diagnostics and sample coverage.
- sheet_novus | sheet_novus_output.xlsx | tests: Result table has no standard coefficient/p-value columns; interpret by table-specific fields. | Interpret signs/magnitudes jointly with diagnostics and sample coverage.
- sheet_producerua | sheet_producerua_output.xlsx | tests: significance share (p<0.05)=0.67 | Interpret signs/magnitudes jointly with diagnostics and sample coverage.
- sheet_prozorro | sheet_prozorro_output.xlsx | tests: significance share (p<0.05)=0.21 | Interpret signs/magnitudes jointly with diagnostics and sample coverage.
- sheet_silpo | sheet_silpo_output.xlsx | tests: Result table has no standard coefficient/p-value columns; interpret by table-specific fields. | Interpret signs/magnitudes jointly with diagnostics and sample coverage.

## Sheet Index

- graphs_brand_region | graphs_brand_region_output.xlsx | Brand_Economic_Metrics | rows=1880 cols=10
- graphs_brand_region | graphs_brand_region_output.xlsx | Brand_IO_Metrics | rows=48 cols=8
- graphs_brand_region | graphs_brand_region_output.xlsx | Prozorro_ByRegion | rows=171 cols=20
- graphs_correlations_lags | graphs_correlations_lags_output.xlsx | Corr_Matrix | rows=7 cols=8
- graphs_correlations_lags | graphs_correlations_lags_output.xlsx | Correlations | rows=273 cols=10
- graphs_correlations_lags | graphs_correlations_lags_output.xlsx | Lag_Best | rows=39 cols=7
- graphs_correlations_lags | graphs_correlations_lags_output.xlsx | Lag_Profiles | rows=1025 cols=7
- graphs_decomposition | graphs_decomposition_output.xlsx | Decomposition_All | rows=25658 cols=9
- graphs_decomposition | graphs_decomposition_output.xlsx | Decomposition_Index | rows=36 cols=4
- graphs_decomposition | graphs_decomposition_output.xlsx | Decomposition_Summary | rows=36 cols=8
- graphs_overlay_ln | graphs_overlay_ln_output.xlsx | BeforeAfterLN_All | rows=25774 cols=8
- graphs_overlay_ln | graphs_overlay_ln_output.xlsx | BeforeAfterLN_Index | rows=42 cols=4
- graphs_overlay_ln | graphs_overlay_ln_output.xlsx | Overlay_All | rows=13399 cols=10
- graphs_overlay_ln | graphs_overlay_ln_output.xlsx | Overlay_Index | rows=12 cols=4
- model_ardl | model_ardl_output.xlsx | ARDL_Summary | rows=11 cols=12
- model_ardl | model_ardl_output.xlsx | Model_Series | rows=3765 cols=4
- model_discounts | model_discounts_output.xlsx | Silpo_Discounts_Depth | rows=1 cols=4
- model_discounts | model_discounts_output.xlsx | Silpo_Discounts_Occurrence | rows=1 cols=4
- model_discounts | model_discounts_output.xlsx | Silpo_Transmission_PromoCtrl | rows=4 cols=11
- model_ecm | model_ecm_output.xlsx | ARDL_Summary | rows=11 cols=12
- model_ecm | model_ecm_output.xlsx | ECM_Summary | rows=3 cols=12
- model_forecast_knn | model_forecast_knn_output.xlsx | Forecast_Predictions | rows=540 cols=6
- model_forecast_knn | model_forecast_knn_output.xlsx | Forecast_Summary | rows=9 cols=7
- model_forecast_knn | model_forecast_knn_output.xlsx | Synthetic_Influence_Coefficient | rows=28 cols=7
- model_forecast_knn | model_forecast_knn_output.xlsx | Synthetic_Retail_Series | rows=91758 cols=8
- model_forecast_knn | model_forecast_knn_output.xlsx | Synthetic_to_Consumer_Link | rows=3 cols=7
- model_intersection_bidirectional | model_intersection_bidirectional_output.xlsx | Bidirectional_Granger | rows=38 cols=7
- model_intersection_bidirectional | model_intersection_bidirectional_output.xlsx | Bidirectional_Results | rows=47 cols=11
- model_intersection_bidirectional | model_intersection_bidirectional_output.xlsx | CrossTable_Correlations | rows=159 cols=10
- model_intersection_bidirectional | model_intersection_bidirectional_output.xlsx | Intersection_Combination_Detail | rows=16 cols=8
- model_intersection_bidirectional | model_intersection_bidirectional_output.xlsx | Intersection_Combination_Summar | rows=8 cols=36
- model_nardl | model_nardl_output.xlsx | NARDL_Summary | rows=11 cols=12
- model_short_chain_regional | model_short_chain_regional_output.xlsx | Chain_Effects_Details | rows=60 cols=6
- model_short_chain_regional | model_short_chain_regional_output.xlsx | Chain_Effects_Summary | rows=12 cols=14
- model_short_chain_regional | model_short_chain_regional_output.xlsx | LagMatrix_ByProduct | rows=39 cols=7
- model_short_chain_regional | model_short_chain_regional_output.xlsx | LagProfiles_ByProduct | rows=1025 cols=7
- model_short_chain_regional | model_short_chain_regional_output.xlsx | Models_ShortRun_Summary | rows=0 cols=0
- model_short_chain_regional | model_short_chain_regional_output.xlsx | Prozorro_Regional_Effects_Matri | rows=171 cols=7
- model_short_chain_regional | model_short_chain_regional_output.xlsx | Prozorro_Regional_Models | rows=0 cols=0
- model_short_chain_regional | model_short_chain_regional_output.xlsx | ShortRun_Details | rows=0 cols=0
- model_vecm | model_vecm_output.xlsx | VECM_Summary | rows=3 cols=12
- sheet_cme | sheet_cme_output.xlsx | clean | rows=1023 cols=9
- sheet_cme | sheet_cme_output.xlsx | daily_variants | rows=1486 cols=12
- sheet_cme | sheet_cme_output.xlsx | descriptive_stats | rows=3 cols=21
- sheet_cme | sheet_cme_output.xlsx | raw | rows=1023 cols=2
- sheet_cme | sheet_cme_output.xlsx | series_long | rows=1023 cols=11
- sheet_cme | sheet_cme_output.xlsx | tests | rows=3 cols=23
- sheet_consumerua | sheet_consumerua_output.xlsx | clean | rows=5463 cols=12
- sheet_consumerua | sheet_consumerua_output.xlsx | daily_variants | rows=5463 cols=12
- sheet_consumerua | sheet_consumerua_output.xlsx | descriptive_stats | rows=9 cols=21
- sheet_consumerua | sheet_consumerua_output.xlsx | raw | rows=5463 cols=11
- sheet_consumerua | sheet_consumerua_output.xlsx | series_long | rows=16389 cols=11
- sheet_consumerua | sheet_consumerua_output.xlsx | tests | rows=9 cols=23
- sheet_eu | sheet_eu_output.xlsx | clean | rows=111299 cols=9
- sheet_eu | sheet_eu_output.xlsx | daily_variants | rows=8868 cols=12
- sheet_eu | sheet_eu_output.xlsx | descriptive_stats | rows=18 cols=21
- sheet_eu | sheet_eu_output.xlsx | raw | rows=111299 cols=6
- sheet_eu | sheet_eu_output.xlsx | series_long | rows=6336 cols=11
- sheet_eu | sheet_eu_output.xlsx | tests | rows=18 cols=23
- sheet_novus | sheet_novus_output.xlsx | clean | rows=1530 cols=22
- sheet_novus | sheet_novus_output.xlsx | daily_variants | rows=8790 cols=12
- sheet_novus | sheet_novus_output.xlsx | descriptive_stats | rows=36 cols=21
- sheet_novus | sheet_novus_output.xlsx | raw | rows=1530 cols=19
- sheet_novus | sheet_novus_output.xlsx | series_long | rows=755 cols=11
- sheet_novus | sheet_novus_output.xlsx | tests | rows=36 cols=23
- sheet_producerua | sheet_producerua_output.xlsx | clean | rows=10758 cols=12
- sheet_producerua | sheet_producerua_output.xlsx | daily_variants | rows=10758 cols=12
- sheet_producerua | sheet_producerua_output.xlsx | descriptive_stats | rows=18 cols=21
- sheet_producerua | sheet_producerua_output.xlsx | raw | rows=10758 cols=11
- sheet_producerua | sheet_producerua_output.xlsx | series_long | rows=32274 cols=11
- sheet_producerua | sheet_producerua_output.xlsx | tests | rows=18 cols=23
- sheet_prozorro | sheet_prozorro_output.xlsx | clean | rows=10927 cols=18
- sheet_prozorro | sheet_prozorro_output.xlsx | daily_variants | rows=40843 cols=12
- sheet_prozorro | sheet_prozorro_output.xlsx | descriptive_stats | rows=21 cols=21
- sheet_prozorro | sheet_prozorro_output.xlsx | raw | rows=10927 cols=12
- sheet_prozorro | sheet_prozorro_output.xlsx | series_long | rows=7613 cols=11
- sheet_prozorro | sheet_prozorro_output.xlsx | tests | rows=21 cols=23
- sheet_silpo | sheet_silpo_output.xlsx | clean | rows=86765 cols=23
- sheet_silpo | sheet_silpo_output.xlsx | daily_variants | rows=23691 cols=12
- sheet_silpo | sheet_silpo_output.xlsx | descriptive_stats | rows=36 cols=21
- sheet_silpo | sheet_silpo_output.xlsx | raw | rows=86765 cols=19
- sheet_silpo | sheet_silpo_output.xlsx | series_long | rows=20933 cols=11
- sheet_silpo | sheet_silpo_output.xlsx | tests | rows=36 cols=23
