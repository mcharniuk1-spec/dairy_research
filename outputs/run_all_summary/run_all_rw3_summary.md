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
- Result table has no standard coefficient/p-value columns; interpret by table-specific fields. | Interpret signs/magnitudes jointly with diagnostics and sample coverage.

- xlsx files: model_ardl_output.xlsx
- pdf files: model_ardl_report.pdf
- md files: model_ardl_report.md
- png count: 1

### model_discounts

Interpretation:
- No explicit test/model tables detected; interpret via module-specific descriptive outputs.

- xlsx files: model_discounts_output.xlsx
- pdf files: model_discounts_report.pdf
- md files: model_discounts_report.md
- png count: 2

### model_ecm

Interpretation:
- Result table has no standard coefficient/p-value columns; interpret by table-specific fields. | Interpret signs/magnitudes jointly with diagnostics and sample coverage.

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
- No explicit test/model tables detected; interpret via module-specific descriptive outputs.

- xlsx files: model_intersection_bidirectional_output.xlsx
- pdf files: model_intersection_bidirectional_report.pdf
- md files: model_intersection_bidirectional_report.md
- png count: 2

### model_nardl

Interpretation:
- Result table has no standard coefficient/p-value columns; interpret by table-specific fields. | Interpret signs/magnitudes jointly with diagnostics and sample coverage.

- xlsx files: model_nardl_output.xlsx
- pdf files: model_nardl_report.pdf
- md files: model_nardl_report.md
- png count: 2

### model_short_chain_regional

Interpretation:
- I(1)-like share=0.00, stationary share=0.00, autocorr risk share=0.00, heterosk risk share=0.00, non-normal share=0.00, stability risk share=0.00. Model action: cointegration/differences + lag structure + robust/HAC + stability checks. | Result table has no standard coefficient/p-value columns; interpret by table-specific fields. | Interpret signs/magnitudes jointly with diagnostics and sample coverage.

- xlsx files: primary_chain_consolidated.xlsx
- pdf files: primary_chain_consolidated.pdf
- md files: primary_chain_consolidated.md
- png count: 0

### model_vecm

Interpretation:
- Result table has no standard coefficient/p-value columns; interpret by table-specific fields. | Interpret signs/magnitudes jointly with diagnostics and sample coverage.

- xlsx files: model_vecm_output.xlsx
- pdf files: model_vecm_report.pdf
- md files: model_vecm_report.md
- png count: 1

### sheet_CME

Interpretation:
- I(1)-like share=0.33, stationary share=0.00, autocorr risk share=0.33, heterosk risk share=0.00, non-normal share=0.33, stability risk share=0.33. Model action: cointegration/differences + lag structure + robust/HAC + stability checks. | significance share (p<0.05)=0.50 | Interpret signs/magnitudes jointly with diagnostics and sample coverage.

- xlsx files: sheet_cme_output.xlsx
- pdf files: sheet_cme_report.pdf
- md files: sheet_cme_report.md
- png count: 3

### sheet_ConsumerUA

Interpretation:
- I(1)-like share=1.00, stationary share=0.00, autocorr risk share=1.00, heterosk risk share=1.00, non-normal share=1.00, stability risk share=1.00. Model action: cointegration/differences + lag structure + robust/HAC + stability checks. | significance share (p<0.05)=0.67 | Interpret signs/magnitudes jointly with diagnostics and sample coverage.

- xlsx files: sheet_consumerua_output.xlsx
- pdf files: sheet_consumerua_report.pdf
- md files: sheet_consumerua_report.md
- png count: 3

### sheet_EU

Interpretation:
- I(1)-like share=0.33, stationary share=0.00, autocorr risk share=0.22, heterosk risk share=0.06, non-normal share=0.33, stability risk share=0.33. Model action: cointegration/differences + lag structure + robust/HAC + stability checks. | significance share (p<0.05)=0.50 | Interpret signs/magnitudes jointly with diagnostics and sample coverage.

- xlsx files: sheet_eu_output.xlsx
- pdf files: sheet_eu_report.pdf
- md files: sheet_eu_report.md
- png count: 3

### sheet_Novus

Interpretation:
- I(1)-like share=0.00, stationary share=0.00, autocorr risk share=0.00, heterosk risk share=0.00, non-normal share=0.00, stability risk share=0.00. Model action: cointegration/differences + lag structure + robust/HAC + stability checks. | Result table has no standard coefficient/p-value columns; interpret by table-specific fields. | Interpret signs/magnitudes jointly with diagnostics and sample coverage.

- xlsx files: sheet_novus_output.xlsx
- pdf files: sheet_novus_report.pdf
- md files: sheet_novus_report.md
- png count: 4

### sheet_ProZorro

Interpretation:
- I(1)-like share=0.19, stationary share=0.10, autocorr risk share=0.10, heterosk risk share=0.00, non-normal share=0.05, stability risk share=0.29. Model action: cointegration/differences + lag structure + robust/HAC + stability checks. | significance share (p<0.05)=0.21 | Interpret signs/magnitudes jointly with diagnostics and sample coverage.

- xlsx files: sheet_prozorro_output.xlsx
- pdf files: sheet_prozorro_report.pdf
- md files: sheet_prozorro_report.md
- png count: 4

### sheet_ProducerUA

Interpretation:
- I(1)-like share=1.00, stationary share=0.00, autocorr risk share=1.00, heterosk risk share=1.00, non-normal share=1.00, stability risk share=1.00. Model action: cointegration/differences + lag structure + robust/HAC + stability checks. | significance share (p<0.05)=0.67 | Interpret signs/magnitudes jointly with diagnostics and sample coverage.

- xlsx files: sheet_producerua_output.xlsx
- pdf files: sheet_producerua_report.pdf
- md files: sheet_producerua_report.md
- png count: 3

### sheet_Silpo

Interpretation:
- I(1)-like share=0.00, stationary share=0.00, autocorr risk share=0.00, heterosk risk share=0.00, non-normal share=0.00, stability risk share=0.00. Model action: cointegration/differences + lag structure + robust/HAC + stability checks. | Result table has no standard coefficient/p-value columns; interpret by table-specific fields. | Interpret signs/magnitudes jointly with diagnostics and sample coverage.

- xlsx files: sheet_silpo_output.xlsx
- pdf files: sheet_silpo_report.pdf
- md files: sheet_silpo_report.md
- png count: 4

## Tests Summary

- model_short_chain_regional | primary_chain_consolidated.xlsx | Consolidated_PreTests: I(1)-like share=0.00, stationary share=0.00, autocorr risk share=0.00, heterosk risk share=0.00, non-normal share=0.00, stability risk share=0.00. Model action: cointegration/differences + lag structure + robust/HAC + stability checks.
- model_short_chain_regional | primary_chain_consolidated.xlsx | Consolidated_ResidualDiagnostic: I(1)-like share=0.00, stationary share=0.00, autocorr risk share=0.00, heterosk risk share=0.00, non-normal share=0.00, stability risk share=0.00. Model action: cointegration/differences + lag structure + robust/HAC + stability checks.
- sheet_CME | sheet_cme_output.xlsx | tests: I(1)-like share=0.33, stationary share=0.00, autocorr risk share=0.33, heterosk risk share=0.00, non-normal share=0.33, stability risk share=0.33. Model action: cointegration/differences + lag structure + robust/HAC + stability checks.
- sheet_ConsumerUA | sheet_consumerua_output.xlsx | tests: I(1)-like share=1.00, stationary share=0.00, autocorr risk share=1.00, heterosk risk share=1.00, non-normal share=1.00, stability risk share=1.00. Model action: cointegration/differences + lag structure + robust/HAC + stability checks.
- sheet_EU | sheet_eu_output.xlsx | tests: I(1)-like share=0.33, stationary share=0.00, autocorr risk share=0.22, heterosk risk share=0.06, non-normal share=0.33, stability risk share=0.33. Model action: cointegration/differences + lag structure + robust/HAC + stability checks.
- sheet_Novus | sheet_novus_output.xlsx | tests: I(1)-like share=0.00, stationary share=0.00, autocorr risk share=0.00, heterosk risk share=0.00, non-normal share=0.00, stability risk share=0.00. Model action: cointegration/differences + lag structure + robust/HAC + stability checks.
- sheet_ProZorro | sheet_prozorro_output.xlsx | tests: I(1)-like share=0.19, stationary share=0.10, autocorr risk share=0.10, heterosk risk share=0.00, non-normal share=0.05, stability risk share=0.29. Model action: cointegration/differences + lag structure + robust/HAC + stability checks.
- sheet_ProducerUA | sheet_producerua_output.xlsx | tests: I(1)-like share=1.00, stationary share=0.00, autocorr risk share=1.00, heterosk risk share=1.00, non-normal share=1.00, stability risk share=1.00. Model action: cointegration/differences + lag structure + robust/HAC + stability checks.
- sheet_Silpo | sheet_silpo_output.xlsx | tests: I(1)-like share=0.00, stationary share=0.00, autocorr risk share=0.00, heterosk risk share=0.00, non-normal share=0.00, stability risk share=0.00. Model action: cointegration/differences + lag structure + robust/HAC + stability checks.

## Results Summary

- graphs_brand_region | graphs_brand_region_output.xlsx | Brand_Economic_Metrics: mean |coef|=20.3301 | positive share=0.44 | significance share (p<0.05)=0.18 | Interpret signs/magnitudes jointly with diagnostics and sample coverage.
- model_ardl | model_ardl_output.xlsx | ARDL_Summary: Result table has no standard coefficient/p-value columns; interpret by table-specific fields. | Interpret signs/magnitudes jointly with diagnostics and sample coverage.
- model_ecm | model_ecm_output.xlsx | ECM_Summary: Result table has no standard coefficient/p-value columns; interpret by table-specific fields. | Interpret signs/magnitudes jointly with diagnostics and sample coverage.
- model_forecast_knn | model_forecast_knn_output.xlsx | Synthetic_Influence_Coefficient: mean |coef|=0.5000 | positive share=1.00 | Interpret signs/magnitudes jointly with diagnostics and sample coverage.
- model_forecast_knn | model_forecast_knn_output.xlsx | Synthetic_to_Consumer_Link: mean |coef|=0.9907 | positive share=0.33 | significance share (p<0.05)=0.00 | Interpret signs/magnitudes jointly with diagnostics and sample coverage.
- model_nardl | model_nardl_output.xlsx | NARDL_Summary: Result table has no standard coefficient/p-value columns; interpret by table-specific fields. | Interpret signs/magnitudes jointly with diagnostics and sample coverage.
- model_short_chain_regional | primary_chain_consolidated.xlsx | Consolidated_ModelCoefficients: Result table has no standard coefficient/p-value columns; interpret by table-specific fields. | Interpret signs/magnitudes jointly with diagnostics and sample coverage.
- model_short_chain_regional | primary_chain_consolidated.xlsx | Consolidated_PreTests: Result table has no standard coefficient/p-value columns; interpret by table-specific fields. | Interpret signs/magnitudes jointly with diagnostics and sample coverage.
- model_short_chain_regional | primary_chain_consolidated.xlsx | Consolidated_ResidualDiagnostic: Result table has no standard coefficient/p-value columns; interpret by table-specific fields. | Interpret signs/magnitudes jointly with diagnostics and sample coverage.
- model_vecm | model_vecm_output.xlsx | VECM_Summary: Result table has no standard coefficient/p-value columns; interpret by table-specific fields. | Interpret signs/magnitudes jointly with diagnostics and sample coverage.
- sheet_CME | sheet_cme_output.xlsx | tests: significance share (p<0.05)=0.50 | Interpret signs/magnitudes jointly with diagnostics and sample coverage.
- sheet_ConsumerUA | sheet_consumerua_output.xlsx | tests: significance share (p<0.05)=0.67 | Interpret signs/magnitudes jointly with diagnostics and sample coverage.
- sheet_EU | sheet_eu_output.xlsx | tests: significance share (p<0.05)=0.50 | Interpret signs/magnitudes jointly with diagnostics and sample coverage.
- sheet_Novus | sheet_novus_output.xlsx | tests: Result table has no standard coefficient/p-value columns; interpret by table-specific fields. | Interpret signs/magnitudes jointly with diagnostics and sample coverage.
- sheet_ProZorro | sheet_prozorro_output.xlsx | tests: significance share (p<0.05)=0.21 | Interpret signs/magnitudes jointly with diagnostics and sample coverage.
- sheet_ProducerUA | sheet_producerua_output.xlsx | tests: significance share (p<0.05)=0.67 | Interpret signs/magnitudes jointly with diagnostics and sample coverage.
- sheet_Silpo | sheet_silpo_output.xlsx | tests: Result table has no standard coefficient/p-value columns; interpret by table-specific fields. | Interpret signs/magnitudes jointly with diagnostics and sample coverage.

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
- model_ardl | model_ardl_output.xlsx | ARDL_Summary | rows=0 cols=20
- model_discounts | model_discounts_output.xlsx | Silpo_Discounts_Depth | rows=1 cols=1
- model_discounts | model_discounts_output.xlsx | Silpo_Discounts_Occurrence | rows=1 cols=1
- model_discounts | model_discounts_output.xlsx | Silpo_Transmission_PromoCtrl | rows=1 cols=1
- model_ecm | model_ecm_output.xlsx | ECM_Summary | rows=0 cols=20
- model_forecast_knn | model_forecast_knn_output.xlsx | Forecast_Predictions | rows=540 cols=6
- model_forecast_knn | model_forecast_knn_output.xlsx | Forecast_Summary | rows=9 cols=7
- model_forecast_knn | model_forecast_knn_output.xlsx | Synthetic_Influence_Coefficient | rows=28 cols=7
- model_forecast_knn | model_forecast_knn_output.xlsx | Synthetic_Retail_Series | rows=91758 cols=8
- model_forecast_knn | model_forecast_knn_output.xlsx | Synthetic_to_Consumer_Link | rows=3 cols=7
- model_forecast_knn | model_forecast_knn_output.xlsx | Ultimate_Consumer_Price | rows=145 cols=5
- model_intersection_bidirectional | model_intersection_bidirectional_output.xlsx | Bidirectional_Granger | rows=1 cols=1
- model_intersection_bidirectional | model_intersection_bidirectional_output.xlsx | Bidirectional_Results | rows=1 cols=1
- model_intersection_bidirectional | model_intersection_bidirectional_output.xlsx | CrossTable_Correlations | rows=77 cols=10
- model_intersection_bidirectional | model_intersection_bidirectional_output.xlsx | Intersection_Combination_Detail | rows=0 cols=0
- model_intersection_bidirectional | model_intersection_bidirectional_output.xlsx | Intersection_Combination_Summar | rows=1 cols=1
- model_nardl | model_nardl_output.xlsx | NARDL_Summary | rows=0 cols=20
- model_short_chain_regional | primary_chain_consolidated.xlsx | Consolidated_Eligibility | rows=48 cols=9
- model_short_chain_regional | primary_chain_consolidated.xlsx | Consolidated_ModelCoefficients | rows=48 cols=20
- model_short_chain_regional | primary_chain_consolidated.xlsx | Consolidated_PreTests | rows=144 cols=12
- model_short_chain_regional | primary_chain_consolidated.xlsx | Consolidated_ResidualDiagnostic | rows=48 cols=11
- model_short_chain_regional | primary_chain_consolidated.xlsx | Rule_Documentation | rows=1 cols=6
- model_vecm | model_vecm_output.xlsx | VECM_Summary | rows=0 cols=20
- sheet_CME | sheet_cme_output.xlsx | clean | rows=1023 cols=9
- sheet_CME | sheet_cme_output.xlsx | daily_variants | rows=1486 cols=12
- sheet_CME | sheet_cme_output.xlsx | descriptive_stats | rows=3 cols=21
- sheet_CME | sheet_cme_output.xlsx | raw | rows=1023 cols=2
- sheet_CME | sheet_cme_output.xlsx | series_long | rows=1023 cols=11
- sheet_CME | sheet_cme_output.xlsx | tests | rows=3 cols=23
- sheet_ConsumerUA | sheet_consumerua_output.xlsx | clean | rows=5463 cols=12
- sheet_ConsumerUA | sheet_consumerua_output.xlsx | daily_variants | rows=5463 cols=12
- sheet_ConsumerUA | sheet_consumerua_output.xlsx | descriptive_stats | rows=9 cols=21
- sheet_ConsumerUA | sheet_consumerua_output.xlsx | raw | rows=5463 cols=11
- sheet_ConsumerUA | sheet_consumerua_output.xlsx | series_long | rows=16389 cols=11
- sheet_ConsumerUA | sheet_consumerua_output.xlsx | tests | rows=9 cols=23
- sheet_EU | sheet_eu_output.xlsx | clean | rows=111299 cols=9
- sheet_EU | sheet_eu_output.xlsx | daily_variants | rows=8868 cols=12
- sheet_EU | sheet_eu_output.xlsx | descriptive_stats | rows=18 cols=21
- sheet_EU | sheet_eu_output.xlsx | raw | rows=111299 cols=6
- sheet_EU | sheet_eu_output.xlsx | series_long | rows=6336 cols=11
- sheet_EU | sheet_eu_output.xlsx | tests | rows=18 cols=23
- sheet_Novus | sheet_novus_output.xlsx | clean | rows=1530 cols=22
- sheet_Novus | sheet_novus_output.xlsx | daily_variants | rows=8790 cols=12
- sheet_Novus | sheet_novus_output.xlsx | descriptive_stats | rows=36 cols=21
- sheet_Novus | sheet_novus_output.xlsx | raw | rows=1530 cols=19
- sheet_Novus | sheet_novus_output.xlsx | series_long | rows=755 cols=11
- sheet_Novus | sheet_novus_output.xlsx | tests | rows=36 cols=23
- sheet_ProZorro | sheet_prozorro_output.xlsx | clean | rows=10927 cols=18
- sheet_ProZorro | sheet_prozorro_output.xlsx | daily_variants | rows=40843 cols=12
- sheet_ProZorro | sheet_prozorro_output.xlsx | descriptive_stats | rows=21 cols=21
- sheet_ProZorro | sheet_prozorro_output.xlsx | raw | rows=10927 cols=12
- sheet_ProZorro | sheet_prozorro_output.xlsx | series_long | rows=7613 cols=11
- sheet_ProZorro | sheet_prozorro_output.xlsx | tests | rows=21 cols=23
- sheet_ProducerUA | sheet_producerua_output.xlsx | clean | rows=10758 cols=12
- sheet_ProducerUA | sheet_producerua_output.xlsx | daily_variants | rows=10758 cols=12
- sheet_ProducerUA | sheet_producerua_output.xlsx | descriptive_stats | rows=18 cols=21
- sheet_ProducerUA | sheet_producerua_output.xlsx | raw | rows=10758 cols=11
- sheet_ProducerUA | sheet_producerua_output.xlsx | series_long | rows=32274 cols=11
- sheet_ProducerUA | sheet_producerua_output.xlsx | tests | rows=18 cols=23
- sheet_Silpo | sheet_silpo_output.xlsx | clean | rows=86765 cols=23
- sheet_Silpo | sheet_silpo_output.xlsx | daily_variants | rows=23691 cols=12
- sheet_Silpo | sheet_silpo_output.xlsx | descriptive_stats | rows=36 cols=21
- sheet_Silpo | sheet_silpo_output.xlsx | raw | rows=86765 cols=19
- sheet_Silpo | sheet_silpo_output.xlsx | series_long | rows=20933 cols=11
- sheet_Silpo | sheet_silpo_output.xlsx | tests | rows=36 cols=23
