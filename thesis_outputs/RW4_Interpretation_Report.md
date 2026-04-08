# RW4 Interpretation Report

This document explains the current RW4 output set without reproducing the raw tables or graphs. All values below are interpretive guideposts for the thesis write-up, not replacements for the original workbooks.

## Executive View

The current run completes **22** of **22** module steps with **0** recorded failures. Across the full output tree, Total Run bundles **331** tables and **226** graphs, while the active RW4 run-all summary indexes **117** current sheets across **22** modules. The active input stack is the farm-gate initial workbook, the farm-gate gap-filled workbook, and the full UAH source workbook located under /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research.

The category mix inside Total Run is dominated by **167** general supporting tables, **68** diagnostic tables, **36** coefficient tables, and **4** forecast tables. So the pipeline is already richer than a single regression appendix; it is a layered evidence system with diagnostics, coefficients, forecasts, and graph packs.

## Current RW4 Module Inventory

### sheet_FarmGateUA_initial

sheet_FarmGateUA_initial contains the initial daily farm-gate workbook for Ukrainian farm-gate prices. It currently writes **1** workbook(s), **1** PDF(s), **1** Markdown file(s), and **4** PNG figure(s).
The run-all summary reads this block as: I(1)-like share=1.00; cointegration-support share=0.00; inspect admissibility and reconstruction robustness before promoting findings. | significance share (p<0.05)=0.83.
The directly named figure files in this module begin with sheet farmgateua initial distribution, sheet farmgateua initial region trends, sheet farmgateua initial timeseries by product, sheet farmgateua initial timeseries by standardized type.

### sheet_FarmGateUA_filled

sheet_FarmGateUA_filled contains the gap-filled daily farm-gate workbook used as the alternative reconstruction source. It currently writes **1** workbook(s), **1** PDF(s), **1** Markdown file(s), and **4** PNG figure(s).
The run-all summary reads this block as: I(1)-like share=1.00; cointegration-support share=0.00; inspect admissibility and reconstruction robustness before promoting findings. | significance share (p<0.05)=0.67.
The directly named figure files in this module begin with sheet farmgateua filled distribution, sheet farmgateua filled region trends, sheet farmgateua filled timeseries by product, sheet farmgateua filled timeseries by standardized type.

### sheet_ProducerUA

sheet_ProducerUA contains domestic producer prices used as the first post-farm-gate downstream layer. It currently writes **1** workbook(s), **1** PDF(s), **1** Markdown file(s), and **3** PNG figure(s).
The run-all summary reads this block as: I(1)-like share=1.00; cointegration-support share=0.00; inspect admissibility and reconstruction robustness before promoting findings. | significance share (p<0.05)=0.67.
The directly named figure files in this module begin with sheet producerua distribution, sheet producerua timeseries by product, sheet producerua timeseries by standardized type.

### sheet_ConsumerUA

sheet_ConsumerUA contains official consumer-price benchmarks used as an external plausibility anchor. It currently writes **1** workbook(s), **1** PDF(s), **1** Markdown file(s), and **3** PNG figure(s).
The run-all summary reads this block as: I(1)-like share=1.00; cointegration-support share=0.00; inspect admissibility and reconstruction robustness before promoting findings. | significance share (p<0.05)=0.67.
The directly named figure files in this module begin with sheet consumerua distribution, sheet consumerua timeseries by product, sheet consumerua timeseries by standardized type.

### sheet_EU

sheet_EU contains EU benchmark prices used as an external international reference. It currently writes **1** workbook(s), **1** PDF(s), **1** Markdown file(s), and **3** PNG figure(s).
The run-all summary reads this block as: I(1)-like share=0.33; cointegration-support share=0.00; inspect admissibility and reconstruction robustness before promoting findings. | significance share (p<0.05)=0.50.
The directly named figure files in this module begin with sheet eu distribution, sheet eu timeseries by product, sheet eu timeseries by standardized type.

### sheet_ProZorro

sheet_ProZorro contains public procurement prices representing the institutional intermediary layer. It currently writes **1** workbook(s), **1** PDF(s), **1** Markdown file(s), and **4** PNG figure(s).
The run-all summary reads this block as: I(1)-like share=0.22; cointegration-support share=0.00; inspect admissibility and reconstruction robustness before promoting findings. | significance share (p<0.05)=0.25.
The directly named figure files in this module begin with sheet prozorro distribution, sheet prozorro region trends, sheet prozorro timeseries by product, sheet prozorro timeseries by standardized type.

### sheet_Silpo

sheet_Silpo contains Silpo retail prices and promo-state metadata. It currently writes **1** workbook(s), **1** PDF(s), **1** Markdown file(s), and **4** PNG figure(s).
The run-all summary reads this block as: I(1)-like share=0.00; cointegration-support share=0.00; inspect admissibility and reconstruction robustness before promoting findings. | Result table has no standard coefficient/p-value columns; interpret by table-specific fields..
The directly named figure files in this module begin with sheet silpo brand trends, sheet silpo distribution, sheet silpo timeseries by product, sheet silpo timeseries by standardized type.

### sheet_Novus

sheet_Novus contains Novus retail prices and brand-level assortment evidence. It currently writes **1** workbook(s), **1** PDF(s), **1** Markdown file(s), and **4** PNG figure(s).
The run-all summary reads this block as: I(1)-like share=0.00; cointegration-support share=0.00; inspect admissibility and reconstruction robustness before promoting findings. | Result table has no standard coefficient/p-value columns; interpret by table-specific fields..
The directly named figure files in this module begin with sheet novus brand trends, sheet novus distribution, sheet novus timeseries by product, sheet novus timeseries by standardized type.

### sheet_CME

sheet_CME contains commodity-market benchmark data used as an external check rather than an endogenous chain stage. It currently writes **1** workbook(s), **1** PDF(s), **1** Markdown file(s), and **3** PNG figure(s).
The run-all summary reads this block as: I(1)-like share=0.33; cointegration-support share=0.00; inspect admissibility and reconstruction robustness before promoting findings. | significance share (p<0.05)=0.50.
The directly named figure files in this module begin with sheet cme distribution, sheet cme timeseries by product, sheet cme timeseries by standardized type.

### model_short_chain_regional

model_short_chain_regional contains the consolidated RW4 chain workbook, which is the main analytical output for forward, reverse, brand, average, and robustness results. It currently writes **1** workbook(s), **1** PDF(s), **1** Markdown file(s), and **4** PNG figure(s).
The run-all summary reads this block as: I(1)-like share=0.00; cointegration-support share=0.00; inspect admissibility and reconstruction robustness before promoting findings. | mean |coef|=3.5293 | significance share (p<0.05)=0.41 | robust-across-reconstruction share=0.27 | core-finding share=0.09.
The directly named figure files in this module begin with farmgate direct heatmap, farmgate reverse corefinding, intersection stability, unified retail comparison.

### model_ardl

model_ardl contains the pooled ARDL evidence used as a linear distributed-lag benchmark. It currently writes **1** workbook(s), **1** PDF(s), **1** Markdown file(s), and **1** PNG figure(s).
The run-all summary reads this block as: I(1)-like share=0.00; cointegration-support share=0.00; inspect admissibility and reconstruction robustness before promoting findings. | mean |coef|=2.6492 | significance share (p<0.05)=0.33 | robust-across-reconstruction share=0.00 | core-finding share=0.00.
The directly named figure files in this module begin with ardl short run.

### model_ecm

model_ecm contains the ECM evidence used for explicit equilibrium-correction interpretation. It currently writes **1** workbook(s), **1** PDF(s), **1** Markdown file(s), and **1** PNG figure(s).
The run-all summary reads this block as: I(1)-like share=0.00; cointegration-support share=0.00; inspect admissibility and reconstruction robustness before promoting findings. | mean |coef|=0.7494 | significance share (p<0.05)=0.74 | robust-across-reconstruction share=0.90 | core-finding share=0.10.
The directly named figure files in this module begin with ecm ect.

### model_nardl

model_nardl contains the asymmetric distributed-lag evidence used to detect different responses to positive and negative shocks. It currently writes **1** workbook(s), **1** PDF(s), **1** Markdown file(s), and **2** PNG figure(s).
The run-all summary reads this block as: I(1)-like share=0.00; cointegration-support share=0.00; inspect admissibility and reconstruction robustness before promoting findings. | mean |coef|=4.1309 | significance share (p<0.05)=0.43 | robust-across-reconstruction share=0.81 | core-finding share=0.28.
The directly named figure files in this module begin with nardl long run, nardl short run.

### model_vecm

model_vecm contains the system-level VECM evidence used for multistage dynamics and impulse interpretation. It currently writes **1** workbook(s), **1** PDF(s), **1** Markdown file(s), and **1** PNG figure(s).
The run-all summary reads this block as: I(1)-like share=0.00; cointegration-support share=0.00; inspect admissibility and reconstruction robustness before promoting findings. | mean |coef|=11.6733 | significance share (p<0.05)=0.23 | robust-across-reconstruction share=0.00 | core-finding share=0.00.
The directly named figure files in this module begin with vecm alpha.

### model_discounts

model_discounts contains the retail-promo comparison module that contrasts observed and baseline price transmission. It currently writes **1** workbook(s), **1** PDF(s), **1** Markdown file(s), and **3** PNG figure(s).
The run-all summary reads this block as: mean |coef|=3.4146.
The directly named figure files in this module begin with discount delta eu, discount delta producer, discount delta short run.

### model_intersection_bidirectional

model_intersection_bidirectional contains the cross-retailer overlap module that tests shared Silpo-Novus evidence where overlap exists. It currently writes **1** workbook(s), **1** PDF(s), **1** Markdown file(s), and **2** PNG figure(s).
The run-all summary reads this block as: No explicit test/model tables detected; inspect module-specific outputs..
The directly named figure files in this module begin with bidirectional coef, intersection combo coef.

### model_forecast_knn

model_forecast_knn contains the forecasting and synthetic-retail module that projects producer and consumer paths. It currently writes **1** workbook(s), **1** PDF(s), **1** Markdown file(s), and **3** PNG figure(s).
The run-all summary reads this block as: mean |coef|=0.5000.
The directly named figure files in this module begin with consumer link coef, forecast producer consumer, synthetic retail top entity.

### model_secondary_synthetic_consumer

model_secondary_synthetic_consumer contains the secondary synthetic-consumer module that would link synthetic retail signals to consumer prices when enough overlap exists. It currently writes **1** workbook(s), **1** PDF(s), **1** Markdown file(s), and **0** PNG figure(s).
The run-all summary reads this block as: mean |coef|=0.4950 | significance share (p<0.05)=0.50.

### graphs_decomposition

graphs_decomposition contains the trend-seasonal decomposition graph pack. It currently writes **1** workbook(s), **1** PDF(s), **1** Markdown file(s), and **24** PNG figure(s).
The run-all summary reads this block as: No explicit test/model tables detected; inspect module-specific outputs..
The directly named figure files in this module begin with decomp observed trend 01, decomp observed trend 02, decomp observed trend 03, decomp observed trend 04, decomp observed trend 05, decomp observed trend 06, plus **18** more figure file(s).

### graphs_overlay_ln

graphs_overlay_ln contains the before/after log transformation and cross-source overlay graph pack. It currently writes **1** workbook(s), **1** PDF(s), **1** Markdown file(s), and **21** PNG figure(s).
The run-all summary reads this block as: No explicit test/model tables detected; inspect module-specific outputs..
The directly named figure files in this module begin with before after log 01, before after log 02, before after log 03, before after log 04, before after log 05, before after log 06, plus **15** more figure file(s).

### graphs_correlations_lags

graphs_correlations_lags contains the cross-source correlation and lag graph pack. It currently writes **1** workbook(s), **1** PDF(s), **1** Markdown file(s), and **2** PNG figure(s).
The run-all summary reads this block as: No explicit test/model tables detected; inspect module-specific outputs..
The directly named figure files in this module begin with corr matrix sources, lag best bar.

### graphs_brand_region

graphs_brand_region contains the brand concentration and ProZorro regional heterogeneity graph pack. It currently writes **1** workbook(s), **1** PDF(s), **1** Markdown file(s), and **3** PNG figure(s).
The run-all summary reads this block as: mean |coef|=27.5983 | significance share (p<0.05)=0.14.
The directly named figure files in this module begin with brand hhi, brand promo intensity, prozorro region median.

## Data And Preprocessing Interpretation

The source modules are not causal findings by themselves. They tell us whether each raw series behaves like a trending level series, whether simple level regressions are admissible, and whether the accompanying graphs suggest outliers, gaps, or region-specific irregularities.

### FarmGateUA_initial

FarmGateUA_initial records an I(1)-like share of **100.0%** across its diagnostic rows. This means the source behaves mostly like a trending level series whenever the share is high, so level regressions without cointegration logic would be risky. Its cointegration-support share is **0.0%**, which matters only as a screening signal, not as final evidence of pass-through. The compact run summary for this source is: significance share (p<0.05)=0.83. The module currently emits **4** graph(s), namely sheet farmgateua initial distribution, sheet farmgateua initial region trends, sheet farmgateua initial timeseries by product, sheet farmgateua initial timeseries by standardized type. The distribution plots diagnose tail risk and level dispersion, the product or type time-series plots show common trend breaks, and the region-trend figures, where present, are the fastest way to spot geographic discontinuities or missing-region artifacts.

### FarmGateUA_filled

FarmGateUA_filled records an I(1)-like share of **100.0%** across its diagnostic rows. This means the source behaves mostly like a trending level series whenever the share is high, so level regressions without cointegration logic would be risky. Its cointegration-support share is **0.0%**, which matters only as a screening signal, not as final evidence of pass-through. The compact run summary for this source is: significance share (p<0.05)=0.67. The module currently emits **4** graph(s), namely sheet farmgateua filled distribution, sheet farmgateua filled region trends, sheet farmgateua filled timeseries by product, sheet farmgateua filled timeseries by standardized type. The distribution plots diagnose tail risk and level dispersion, the product or type time-series plots show common trend breaks, and the region-trend figures, where present, are the fastest way to spot geographic discontinuities or missing-region artifacts.

### ProducerUA

ProducerUA records an I(1)-like share of **100.0%** across its diagnostic rows. This means the source behaves mostly like a trending level series whenever the share is high, so level regressions without cointegration logic would be risky. Its cointegration-support share is **0.0%**, which matters only as a screening signal, not as final evidence of pass-through. The compact run summary for this source is: significance share (p<0.05)=0.67. The module currently emits **3** graph(s), namely sheet producerua distribution, sheet producerua timeseries by product, sheet producerua timeseries by standardized type. The distribution plots diagnose tail risk and level dispersion, the product or type time-series plots show common trend breaks, and the region-trend figures, where present, are the fastest way to spot geographic discontinuities or missing-region artifacts.

### ConsumerUA

ConsumerUA records an I(1)-like share of **100.0%** across its diagnostic rows. This means the source behaves mostly like a trending level series whenever the share is high, so level regressions without cointegration logic would be risky. Its cointegration-support share is **0.0%**, which matters only as a screening signal, not as final evidence of pass-through. The compact run summary for this source is: significance share (p<0.05)=0.67. The module currently emits **3** graph(s), namely sheet consumerua distribution, sheet consumerua timeseries by product, sheet consumerua timeseries by standardized type. The distribution plots diagnose tail risk and level dispersion, the product or type time-series plots show common trend breaks, and the region-trend figures, where present, are the fastest way to spot geographic discontinuities or missing-region artifacts.

### EU

EU records an I(1)-like share of **33.3%** across its diagnostic rows. This means the source behaves mostly like a trending level series whenever the share is high, so level regressions without cointegration logic would be risky. Its cointegration-support share is **0.0%**, which matters only as a screening signal, not as final evidence of pass-through. The compact run summary for this source is: significance share (p<0.05)=0.50. The module currently emits **3** graph(s), namely sheet eu distribution, sheet eu timeseries by product, sheet eu timeseries by standardized type. The distribution plots diagnose tail risk and level dispersion, the product or type time-series plots show common trend breaks, and the region-trend figures, where present, are the fastest way to spot geographic discontinuities or missing-region artifacts.

### ProZorro

ProZorro records an I(1)-like share of **22.2%** across its diagnostic rows. This means the source behaves mostly like a trending level series whenever the share is high, so level regressions without cointegration logic would be risky. Its cointegration-support share is **0.0%**, which matters only as a screening signal, not as final evidence of pass-through. The compact run summary for this source is: significance share (p<0.05)=0.25. The module currently emits **4** graph(s), namely sheet prozorro distribution, sheet prozorro region trends, sheet prozorro timeseries by product, sheet prozorro timeseries by standardized type. The distribution plots diagnose tail risk and level dispersion, the product or type time-series plots show common trend breaks, and the region-trend figures, where present, are the fastest way to spot geographic discontinuities or missing-region artifacts.

### Silpo

Silpo records an I(1)-like share of **0.0%** across its diagnostic rows. This means the source behaves mostly like a trending level series whenever the share is high, so level regressions without cointegration logic would be risky. Its cointegration-support share is **0.0%**, which matters only as a screening signal, not as final evidence of pass-through. The compact run summary for this source is: Result table has no standard coefficient/p-value columns; interpret by table-specific fields.. The module currently emits **4** graph(s), namely sheet silpo brand trends, sheet silpo distribution, sheet silpo timeseries by product, sheet silpo timeseries by standardized type. The distribution plots diagnose tail risk and level dispersion, the product or type time-series plots show common trend breaks, and the region-trend figures, where present, are the fastest way to spot geographic discontinuities or missing-region artifacts.

### Novus

Novus records an I(1)-like share of **0.0%** across its diagnostic rows. This means the source behaves mostly like a trending level series whenever the share is high, so level regressions without cointegration logic would be risky. Its cointegration-support share is **0.0%**, which matters only as a screening signal, not as final evidence of pass-through. The compact run summary for this source is: Result table has no standard coefficient/p-value columns; interpret by table-specific fields.. The module currently emits **4** graph(s), namely sheet novus brand trends, sheet novus distribution, sheet novus timeseries by product, sheet novus timeseries by standardized type. The distribution plots diagnose tail risk and level dispersion, the product or type time-series plots show common trend breaks, and the region-trend figures, where present, are the fastest way to spot geographic discontinuities or missing-region artifacts.

### CME

CME records an I(1)-like share of **33.3%** across its diagnostic rows. This means the source behaves mostly like a trending level series whenever the share is high, so level regressions without cointegration logic would be risky. Its cointegration-support share is **0.0%**, which matters only as a screening signal, not as final evidence of pass-through. The compact run summary for this source is: significance share (p<0.05)=0.50. The module currently emits **3** graph(s), namely sheet cme distribution, sheet cme timeseries by product, sheet cme timeseries by standardized type. The distribution plots diagnose tail risk and level dispersion, the product or type time-series plots show common trend breaks, and the region-trend figures, where present, are the fastest way to spot geographic discontinuities or missing-region artifacts.

### Reconstruction, Mapping, And Unit Admissibility

The mapping audit covers **3,728** mapped label groups. Exact matches account for **59.7%**, multi-match cases account for **33.2%**, and explicit unmatched rows account for **7.1%**. Economic comparability remains high at **92.9%**, while lexical anomalies are nearly absent at **0.0%**. This means the weak points are not broad text noise; they are mostly concentrated in sources whose unit normalization is intrinsically imperfect.

Reconstruction diagnostics show that FarmGateUA_filled has mean absolute variant gap **0.013**, worst-case variant gap **0.185**, and mean monthly reaggregation gap **0.003**; FarmGateUA_initial has mean absolute variant gap **0.012**, worst-case variant gap **0.279**, and mean monthly reaggregation gap **0.003**; ProducerUA has mean absolute variant gap **0.075**, worst-case variant gap **1.660**, and mean monthly reaggregation gap **0.024**. In practice, this says producer reconstructions are smooth but still non-identical, while the farm-gate regional rebuild remains sensitive enough that robustness filtering is necessary.

The unit-admissibility table confirms that most active sources remain model-usable after normalization. FarmGateUA_initial retains admissible-share **100.0%** under reason 'uah_per_kg'; FarmGateUA_filled retains admissible-share **100.0%** under reason 'uah_per_kg'; ProducerUA retains admissible-share **100.0%** under reason 'uah_per_kg'; ConsumerUA retains admissible-share **100.0%** under reason 'uah_per_kg'; EU retains admissible-share **0.0%** under reason 'missing_price'; EU retains admissible-share **100.0%** under reason 'uah_per_kg'; ProZorro retains admissible-share **0.0%** under reason 'missing_unit_normalized_price'; ProZorro retains admissible-share **100.0%** under reason 'normalized_unit_price'; Silpo retains admissible-share **100.0%** under reason 'unit_price_or_pack_normalized'; Novus retains admissible-share **0.0%** under reason 'liter_not_comparable_for_product_family'; Novus retains admissible-share **100.0%** under reason 'unit_price_or_pack_normalized'; CME retains admissible-share **100.0%** under reason 'uah_per_kg'. The important exceptions are EU missing-price rows, ProZorro rows without normalized unit price, and a thin Novus liter-based fragment that should not be forced into mass-style product comparisons.

## RW4 Chain Interpretation

The consolidated forward-chain table contains **10,141** rows across **7** model families. Models finish with status 'ok' in **51.9%**, while **48.1%** of rows are still flagged unreliable and only **8.7%** survive into the core-finding layer. The pretests show cointegration-support share **50.5%** and an integration mix of I(0) **1,824**, I(1) **1,508**, I(2) **535**, and ambiguous **445**. So the mathematically safe reading is that the data are heterogeneous enough to require admissibility screening, not a one-model-fits-all shortcut.

Recorded NO_FIT rows total **1,236**. The two dominant reasons are i2_series_blocked at **940** rows and insufficient_overlap at **296** rows. These rows are analytically useful because they tell us where the pipeline refused to fabricate coefficients on mathematically weak samples.

Cross-variant robustness remains limited. Linear-versus-pchip robustness averages **62.3%**, interpolation sensitivity is flagged in **51.7%**, and farm-gate-source robustness averages only **48.9%**. That means coefficients should only be promoted when they survive both reconstruction and source comparisons.

### Coverage Validation

Forward FarmGateUA -> ProducerUA has **709** total rows, **361** preferred-family rows, and **8** core findings.
Forward ProducerUA -> ProZorro has **382** total rows, **178** preferred-family rows, and **64** core findings.
Forward ProZorro -> Retail has **896** total rows, **352** preferred-family rows, and **204** core findings.
Forward FarmGateUA -> ProZorro has **873** total rows, **525** preferred-family rows, and **42** core findings.
Forward ProducerUA -> Retail has **850** total rows, **378** preferred-family rows, and **56** core findings.
Forward FarmGateUA -> Retail has **1,883** total rows, **799** preferred-family rows, and **42** core findings.
Reverse Retail -> ProZorro has **636** total rows, **324** preferred-family rows, and **228** core findings.
Reverse ProZorro -> ProducerUA has **402** total rows, **198** preferred-family rows, and **80** core findings.
Reverse Retail -> ProducerUA has **606** total rows, **294** preferred-family rows, and **36** core findings.
Reverse ProducerUA -> FarmGateUA has **712** total rows, **364** preferred-family rows, and **17** core findings.
Reverse ProZorro -> FarmGateUA has **735** total rows, **387** preferred-family rows, and **54** core findings.
Reverse Retail -> FarmGateUA has **1,457** total rows, **825** preferred-family rows, and **48** core findings.
The brand-panel coverage audit records **44** panel definitions, **371** preferred-family rows, and **55** core findings.

### Forward And Reverse Transmission

The strongest forward evidence appears in Retail -> ProZorro, where core findings reach **35.8%** across **636** rows. The weakest required forward link is FarmGateUA -> ProducerUA, where core findings stay at **1.1%**. In this run that pattern means downstream transmission is easier to confirm than the earliest farm-gate step.
Reverse-flow evidence is non-trivial. Retail -> ProZorro reaches core-finding share **35.8%**, which is stronger than several forward upstream links. This does not prove literal reverse causality by itself, but it does show that downstream pricing carries information back into the rest of the chain.

One thesis-level warning is that FarmGateUA -> ProducerUA has coverage but no core findings: **8** core findings out of **709** total rows. So the current national farm-gate series remains too blunt to explain producer prices cleanly, even though midstream and retail layers do transmit to one another.

### Raw-Milk, Average, Brand, And Benchmark Layers

The direct raw-milk-to-product layer is weak. Its best stage-to target is ProZorro with core-finding share only **4.8%**, so the direct bypass interpretation should be treated as mostly unsupported on the present sample.
The average-price layer is more stable than many product-specific links. Its strongest pair is Retail -> ProZorro with core-finding share **36.4%**, which suggests aggregation removes some product-level noise and exposes a smoother retail-procurement signal.
Brand-level transmission remains much thinner than product-level transmission. The brand table has **962** rows, but brand labels are missing in **39.7%** of them and the overall core-finding share is only **5.7%**. Most surviving brand evidence comes from Silpo rather than Novus, which means any cross-retailer brand conclusions should still be framed as asymmetric in data support.
By retailer, Novus contributes **144** rows with core-finding share **0.0%**; Silpo contributes **818** rows with core-finding share **6.7%**.
Benchmark-comparison tables show how the RW4 layers line up with external anchors. CME versus retail has mean absolute best-lag correlation **0.584**; CME versus farm_gate has mean absolute best-lag correlation **0.457**; ConsumerUA versus producer has mean absolute best-lag correlation **0.730**; ConsumerUA versus farm_gate has mean absolute best-lag correlation **0.422**; ConsumerUA versus retail has mean absolute best-lag correlation **0.224**; ConsumerUA versus prozorro has mean absolute best-lag correlation **0.164**. The strongest benchmark coherence is at the producer layer, especially against ConsumerUA for milk and sour-cream style products.

NARDL dynamic multipliers remain directionally informative even when single coefficients are unstable. Across saved multiplier rows, average positive-path multiplier is **1.243** and average negative-path multiplier is **1.984**. A large gap between those paths is the practical signal of asymmetry.

The saved VECM impulse-style outputs span **3,744** rows, and the largest absolute response among explicit IRF columns is **3,104.5**. Because the system-level VECM block has low overall significance support, these IRFs should be read as structural diagnostics rather than headline elasticities.

## Model-Specific Interpretation

### model_ardl

model_ardl currently summarizes **1,383** rows. mean |coef|=2.6492 | significance share (p<0.05)=0.33 | robust-across-reconstruction share=0.00 | core-finding share=0.00. The diagnostic screen for this block reads I(1)-like share=0.00; cointegration-support share=0.00; inspect admissibility and reconstruction robustness before promoting findings..

### model_ecm

model_ecm currently summarizes **286** rows. mean |coef|=0.7494 | significance share (p<0.05)=0.74 | robust-across-reconstruction share=0.90 | core-finding share=0.10. The diagnostic screen for this block reads I(1)-like share=0.00; cointegration-support share=0.00; inspect admissibility and reconstruction robustness before promoting findings.. ECM is the most interpretable correction-style block here, but the sample is tiny and should be treated as confirmatory only where it agrees with the consolidated chain.

### model_nardl

model_nardl currently summarizes **3,028** rows. mean |coef|=4.1309 | significance share (p<0.05)=0.43 | robust-across-reconstruction share=0.81 | core-finding share=0.28. The diagnostic screen for this block reads I(1)-like share=0.00; cointegration-support share=0.00; inspect admissibility and reconstruction robustness before promoting findings.. NARDL remains the richest block for asymmetric pass-through, but it also contains many of the largest unstable coefficients, so core-filtering matters.

### model_vecm

model_vecm currently summarizes **288** rows. mean |coef|=11.6733 | significance share (p<0.05)=0.23 | robust-across-reconstruction share=0.00 | core-finding share=0.00. The diagnostic screen for this block reads I(1)-like share=0.00; cointegration-support share=0.00; inspect admissibility and reconstruction robustness before promoting findings.. The VECM system is structurally informative, yet its significance density is low, so system coefficients should not outrank simpler robust links.

### model_discounts

The discount module is analytically useful, but the explicit promo-state equations are not estimable on the present sample. Incidence, type, and depth each contain **1**, **1**, and **1** placeholder row(s) rather than fitted coefficient tables. That is an honest mathematical outcome: the data do not provide enough stable within-panel variation or convergence support for those nonlinear equations right now.

The plain-language synthesis table currently says Do promotions behave like equilibrium correction? = **yes**; Does pseudo-asymmetry weaken after promo control? = **yes**; Do effective prices adjust faster than baseline prices? = **mixed**; Does discount depth react to upstream shocks? = **mixed**; Do retail shocks transmit materially to farm-gate prices? = **yes**; Is the retail-to-farmgate conclusion stable across farm-gate reconstructions? = **yes**; Is transmission stronger for product-specific panels than for all-products averages? = **yes**; Do specific retailer brands show stronger or weaker transmission? = **yes**. The correct interpretation is that promotions matter for reading transmission, but the exact promo-state probability mechanism still needs a different data structure.

### model_forecast_knn

The forecast block is one of the cleaner empirical components. Producer holdout RMSE ranges from **0.003** to **0.004**, consumer holdout RMSE ranges from **0.006** to **0.008**, and training R-squared stays in the **84.6%** to **85.8%** range. So forecasting is working as a smoothing and plausibility tool even where causal transmission remains ambiguous.

Within the synthetic-to-consumer link table, the significant results are Сметана has synthetic-to-consumer coefficient **0.929** at p-value **0.000**. This makes sour cream the clearest case where the synthetic retail proxy is carrying independent information.

### model_intersection_bidirectional And model_secondary_synthetic_consumer

The intersection module currently resolves to explicit insufficiency notes rather than regressions: 'Insufficient Silpo-Novus overlap for bidirectional regressions.', 'Insufficient overlap for Silpo-Novus Granger tests.', and 'Insufficient overlap for combined secondary model.'. This does not prove the absence of cross-retailer interaction; it proves that the shared Silpo-Novus sample is not long or dense enough to estimate that interaction credibly.

The secondary synthetic-consumer module is still empty, with **3** rows in Synthetic_Consumer_Link and **166** rows in Synthetic_Consumer_Predictions. That should be read as unfinished data support rather than as a negative substantive result.

## Graph Interpretation

This section explains what the graph families are telling us without reproducing the figures themselves. The main rule is that graphs are strongest as pattern checks and plausibility screens; they are not substitutes for the robustness-filtered coefficient tables.

### Source-Sheet Graphs

FarmGateUA_initial contributes **4** source graphs: sheet farmgateua initial distribution, sheet farmgateua initial region trends, sheet farmgateua initial timeseries by product, sheet farmgateua initial timeseries by standardized type. The distribution charts diagnose outliers and heavy tails, the product and standardized-type time-series charts show whether categories move together, and the region-trend charts reveal geographic discontinuities that may later show up as weak or unstable pass-through.

FarmGateUA_filled contributes **4** source graphs: sheet farmgateua filled distribution, sheet farmgateua filled region trends, sheet farmgateua filled timeseries by product, sheet farmgateua filled timeseries by standardized type. The distribution charts diagnose outliers and heavy tails, the product and standardized-type time-series charts show whether categories move together, and the region-trend charts reveal geographic discontinuities that may later show up as weak or unstable pass-through.

ProducerUA contributes **3** source graphs: sheet producerua distribution, sheet producerua timeseries by product, sheet producerua timeseries by standardized type. The distribution charts diagnose outliers and heavy tails, the product and standardized-type time-series charts show whether categories move together, and the region-trend charts reveal geographic discontinuities that may later show up as weak or unstable pass-through.

ConsumerUA contributes **3** source graphs: sheet consumerua distribution, sheet consumerua timeseries by product, sheet consumerua timeseries by standardized type. The distribution charts diagnose outliers and heavy tails, the product and standardized-type time-series charts show whether categories move together, and the region-trend charts reveal geographic discontinuities that may later show up as weak or unstable pass-through.

EU contributes **3** source graphs: sheet eu distribution, sheet eu timeseries by product, sheet eu timeseries by standardized type. The distribution charts diagnose outliers and heavy tails, the product and standardized-type time-series charts show whether categories move together, and the region-trend charts reveal geographic discontinuities that may later show up as weak or unstable pass-through.

ProZorro contributes **4** source graphs: sheet prozorro distribution, sheet prozorro region trends, sheet prozorro timeseries by product, sheet prozorro timeseries by standardized type. The distribution charts diagnose outliers and heavy tails, the product and standardized-type time-series charts show whether categories move together, and the region-trend charts reveal geographic discontinuities that may later show up as weak or unstable pass-through.

Silpo contributes **4** source graphs: sheet silpo brand trends, sheet silpo distribution, sheet silpo timeseries by product, sheet silpo timeseries by standardized type. The distribution charts diagnose outliers and heavy tails, the product and standardized-type time-series charts show whether categories move together, and the region-trend charts reveal geographic discontinuities that may later show up as weak or unstable pass-through.

Novus contributes **4** source graphs: sheet novus brand trends, sheet novus distribution, sheet novus timeseries by product, sheet novus timeseries by standardized type. The distribution charts diagnose outliers and heavy tails, the product and standardized-type time-series charts show whether categories move together, and the region-trend charts reveal geographic discontinuities that may later show up as weak or unstable pass-through.

CME contributes **3** source graphs: sheet cme distribution, sheet cme timeseries by product, sheet cme timeseries by standardized type. The distribution charts diagnose outliers and heavy tails, the product and standardized-type time-series charts show whether categories move together, and the region-trend charts reveal geographic discontinuities that may later show up as weak or unstable pass-through.

### Decomposition Graphs

The decomposition pack contains **12** observed-versus-trend figures and **12** seasonal-versus-residual figures. These plots show that upstream series are largely trend-driven, while some retail families carry visibly stronger seasonal structure. The strongest seasonal signatures in the summary table are Novus Сир твердий with seasonal strength **0.457**; Silpo Інше/невідомо with seasonal strength **0.422**; Silpo Йогурт with seasonal strength **0.409**; Silpo Сир кисломолочний with seasonal strength **0.400**; ProZorro Сметана with seasonal strength **0.366**. That means seasonality is mostly a retail-category issue rather than a farm-gate issue.

### Overlay And Log-Transformation Graphs

The overlay pack contains **12** before/after-log figures and **9** cross-source overlay figures. The log figures answer whether scale compression makes dynamics more comparable across products; the overlay figures answer whether different sources co-move in their common windows. The overlay index spans **9** product windows, while the before/after index spans **36** source-product combinations.

### Correlation And Lag Graphs

The correlation-and-lag graphs are the quickest visual check on timing. The strongest positive best-lag relationships are ProducerUA -> ConsumerUA for Сметана at lag **1** with correlation **0.994**; ProducerUA -> ConsumerUA for Сир твердий at lag **1** with correlation **0.986**; ProducerUA -> ConsumerUA for Молоко питне at lag **1** with correlation **0.907**; EU -> ProducerUA for Вершки at lag **1** with correlation **0.727**; EU -> ProducerUA for Сир твердий at lag **27** with correlation **0.686**. The strongest negative best-lag relationships are EU -> ProZorro for Інше/невідомо at lag **21** with correlation **-0.924**; EU -> Silpo for Вершки at lag **10** with correlation **-0.604**; ProducerUA -> Silpo for Молоко питне at lag **15** with correlation **-0.525**; EU -> Silpo for Молоко питне at lag **8** with correlation **-0.522**; Novus -> Silpo for Сир твердий at lag **7** with correlation **-0.493**. Large negative lag peaks are not automatically errors, but they are the first place to look for mismatch, opposite seasonal timing, or unit-composition drift.

### Brand And Regional Graphs

The brand-region pack contains three direct figure files: brand HHI, brand promo intensity, and ProZorro regional median. Those graphs should be interpreted together with the tables: concentration spikes are meaningful only when SKU counts are not trivially small, and regional volatility is meaningful only when it persists beyond one-off outliers. The highest concentration cases are Novus butter in 2025-11-01 with HHI **1.000** on **1** SKU(s); Novus other in 2025-12-01 with HHI **0.500** on **2** SKU(s); Novus yogurt_dessert in 2025-12-01 with HHI **0.202** on **23** SKU(s); Novus sour_cream in 2026-01-01 with HHI **0.180** on **20** SKU(s); Novus cottage_cheese in 2026-01-01 with HHI **0.133** on **33** SKU(s). The most volatile regional ProZorro pockets are Чернівецька Молоко питне with CV **1.744**; Харківська Сир кисломолочний with CV **0.919**; Запорізька Молоко питне with CV **0.683**; Київська Інше/невідомо with CV **0.660**; Харківська Молоко питне with CV **0.651**.

### Model-Family Figures

ardl_short_run.png: shows the pooled short-run ARDL effects and should be read against the low overall ARDL significance density.
ecm_ect.png: shows the equilibrium-correction coefficients, where more negative values mean faster error correction.
nardl_short_run.png: shows short-run asymmetry and should be paired with the multiplier tables.
nardl_long_run.png: shows long-run asymmetry and is useful only when the corresponding models remain admissible.
vecm_alpha.png: shows system adjustment coefficients and is more diagnostic than headline-causal in this run.
chain_retail_from_producer.png: summarizes the shorter producer-to-retail regional relationship.
discount_delta_short_run.png: shows how observed-vs-baseline short-run retail transmission differs.
discount_delta_producer.png: shows how producer-linked discount effects differ between observed and baseline pricing.
discount_delta_eu.png: shows how EU-linked discount effects differ between observed and baseline pricing.
forecast_producer_consumer.png: visualizes holdout forecasting quality for producer and consumer series.
consumer_link_coef.png: visualizes the consumer-link coefficients from the synthetic-retail module.
synthetic_retail_top_entity.png: shows the dominant entities inside the synthetic-retail construction.
bidirectional_coef.png: would show cross-retailer bidirectional coefficients, but on this run it is mainly a placeholder context plot because overlap is thin.
intersection_combo_coef.png: would show combination-model coefficients, but again the current overlap is too weak for strong inference.

### Legacy Product-Retailer Graph Packs

The output tree still contains **25** legacy product-retailer workbooks spanning products butter, cottage_cheese, cream, hard_cheese, milk, other, sour_cream, yogurt_dessert and retailer panels novus, silpo, silpo_novus. Their graph inventory includes **48** time-series figures, **40** lag-profile figures, **32** NARDL-multiplier figures, and **6** ECM-adjustment figures. These packs are still useful as panel-level diagnostics, but they are not the authoritative RW4 chain summary anymore because they follow the older product-retailer reporting structure.

## Detailed Workbook Map

The lines below explain every current run-all workbook sheet without reproducing the output itself. Row and column counts are included so it is easy to tell whether a sheet is substantive, sparse, or just an index.

### sheet_FarmGateUA_initial

This module writes workbook(s) sheet_farmgateua_initial_output.xlsx and the main output directory currently contains **4** PNG figure(s).
the initial daily farm-gate workbook for Ukrainian farm-gate prices.

Workbook sheet_farmgateua_initial_output.xlsx:
Sheet clean has **32,620** rows and **30** columns. It is supporting output sheet that should be interpreted in conjunction with its module context.
Sheet daily_variants has **32,620** rows and **25** columns. It is supporting output sheet that should be interpreted in conjunction with its module context.
Sheet descriptive_stats has **3** rows and **21** columns. It is supporting output sheet that should be interpreted in conjunction with its module context.
Sheet raw has **32,620** rows and **6** columns. It is supporting output sheet that should be interpreted in conjunction with its module context.
Sheet series_long has **97,860** rows and **16** columns. It is supporting output sheet that should be interpreted in conjunction with its module context.
Sheet tests has **3** rows and **23** columns. It is diagnostic output focused on integration, residual, or admissibility testing. Current compact interpretation: I(1)-like share=1.00; cointegration-support share=0.00; inspect admissibility and reconstruction robustness before promoting findings. significance share (p<0.05)=0.83

### sheet_FarmGateUA_filled

This module writes workbook(s) sheet_farmgateua_filled_output.xlsx and the main output directory currently contains **4** PNG figure(s).
the gap-filled daily farm-gate workbook used as the alternative reconstruction source.

Workbook sheet_farmgateua_filled_output.xlsx:
Sheet clean has **38,012** rows and **30** columns. It is supporting output sheet that should be interpreted in conjunction with its module context.
Sheet daily_variants has **38,012** rows and **25** columns. It is supporting output sheet that should be interpreted in conjunction with its module context.
Sheet descriptive_stats has **3** rows and **21** columns. It is supporting output sheet that should be interpreted in conjunction with its module context.
Sheet raw has **38,012** rows and **6** columns. It is supporting output sheet that should be interpreted in conjunction with its module context.
Sheet series_long has **114,036** rows and **16** columns. It is supporting output sheet that should be interpreted in conjunction with its module context.
Sheet tests has **3** rows and **23** columns. It is diagnostic output focused on integration, residual, or admissibility testing. Current compact interpretation: I(1)-like share=1.00; cointegration-support share=0.00; inspect admissibility and reconstruction robustness before promoting findings. significance share (p<0.05)=0.67

### sheet_ProducerUA

This module writes workbook(s) sheet_producerua_output.xlsx and the main output directory currently contains **3** PNG figure(s).
domestic producer prices used as the first post-farm-gate downstream layer.

Workbook sheet_producerua_output.xlsx:
Sheet clean has **10,758** rows and **30** columns. It is supporting output sheet that should be interpreted in conjunction with its module context.
Sheet daily_variants has **8,965** rows and **25** columns. It is supporting output sheet that should be interpreted in conjunction with its module context.
Sheet descriptive_stats has **15** rows and **21** columns. It is supporting output sheet that should be interpreted in conjunction with its module context.
Sheet raw has **10,758** rows and **11** columns. It is supporting output sheet that should be interpreted in conjunction with its module context.
Sheet series_long has **26,895** rows and **16** columns. It is supporting output sheet that should be interpreted in conjunction with its module context.
Sheet tests has **15** rows and **23** columns. It is diagnostic output focused on integration, residual, or admissibility testing. Current compact interpretation: I(1)-like share=1.00; cointegration-support share=0.00; inspect admissibility and reconstruction robustness before promoting findings. significance share (p<0.05)=0.67

### sheet_ConsumerUA

This module writes workbook(s) sheet_consumerua_output.xlsx and the main output directory currently contains **3** PNG figure(s).
official consumer-price benchmarks used as an external plausibility anchor.

Workbook sheet_consumerua_output.xlsx:
Sheet clean has **5,463** rows and **30** columns. It is supporting output sheet that should be interpreted in conjunction with its module context.
Sheet daily_variants has **5,463** rows and **25** columns. It is supporting output sheet that should be interpreted in conjunction with its module context.
Sheet descriptive_stats has **9** rows and **21** columns. It is supporting output sheet that should be interpreted in conjunction with its module context.
Sheet raw has **5,463** rows and **11** columns. It is supporting output sheet that should be interpreted in conjunction with its module context.
Sheet series_long has **16,389** rows and **16** columns. It is supporting output sheet that should be interpreted in conjunction with its module context.
Sheet tests has **9** rows and **23** columns. It is diagnostic output focused on integration, residual, or admissibility testing. Current compact interpretation: I(1)-like share=1.00; cointegration-support share=0.00; inspect admissibility and reconstruction robustness before promoting findings. significance share (p<0.05)=0.67

### sheet_EU

This module writes workbook(s) sheet_eu_output.xlsx and the main output directory currently contains **3** PNG figure(s).
EU benchmark prices used as an external international reference.

Workbook sheet_eu_output.xlsx:
Sheet clean has **111,299** rows and **27** columns. It is supporting output sheet that should be interpreted in conjunction with its module context.
Sheet daily_variants has **7,390** rows and **25** columns. It is supporting output sheet that should be interpreted in conjunction with its module context.
Sheet descriptive_stats has **15** rows and **21** columns. It is supporting output sheet that should be interpreted in conjunction with its module context.
Sheet raw has **111,299** rows and **6** columns. It is supporting output sheet that should be interpreted in conjunction with its module context.
Sheet series_long has **5,280** rows and **16** columns. It is supporting output sheet that should be interpreted in conjunction with its module context.
Sheet tests has **15** rows and **23** columns. It is diagnostic output focused on integration, residual, or admissibility testing. Current compact interpretation: I(1)-like share=0.33; cointegration-support share=0.00; inspect admissibility and reconstruction robustness before promoting findings. significance share (p<0.05)=0.50

### sheet_ProZorro

This module writes workbook(s) sheet_prozorro_output.xlsx and the main output directory currently contains **4** PNG figure(s).
public procurement prices representing the institutional intermediary layer.

Workbook sheet_prozorro_output.xlsx:
Sheet clean has **10,927** rows and **37** columns. It is supporting output sheet that should be interpreted in conjunction with its module context.
Sheet daily_variants has **35,275** rows and **25** columns. It is supporting output sheet that should be interpreted in conjunction with its module context.
Sheet descriptive_stats has **18** rows and **21** columns. It is supporting output sheet that should be interpreted in conjunction with its module context.
Sheet raw has **10,927** rows and **12** columns. It is supporting output sheet that should be interpreted in conjunction with its module context.
Sheet series_long has **7,239** rows and **16** columns. It is supporting output sheet that should be interpreted in conjunction with its module context.
Sheet tests has **18** rows and **23** columns. It is diagnostic output focused on integration, residual, or admissibility testing. Current compact interpretation: I(1)-like share=0.22; cointegration-support share=0.00; inspect admissibility and reconstruction robustness before promoting findings. significance share (p<0.05)=0.25

### sheet_Silpo

This module writes workbook(s) sheet_silpo_output.xlsx and the main output directory currently contains **4** PNG figure(s).
Silpo retail prices and promo-state metadata.

Workbook sheet_silpo_output.xlsx:
Sheet clean has **86,765** rows and **53** columns. It is supporting output sheet that should be interpreted in conjunction with its module context.
Sheet daily_variants has **22,120** rows and **25** columns. It is supporting output sheet that should be interpreted in conjunction with its module context.
Sheet descriptive_stats has **24** rows and **21** columns. It is supporting output sheet that should be interpreted in conjunction with its module context.
Sheet raw has **86,765** rows and **19** columns. It is supporting output sheet that should be interpreted in conjunction with its module context.
Sheet series_long has **19,508** rows and **16** columns. It is supporting output sheet that should be interpreted in conjunction with its module context.
Sheet tests has **24** rows and **23** columns. It is diagnostic output focused on integration, residual, or admissibility testing. Current compact interpretation: I(1)-like share=0.00; cointegration-support share=0.00; inspect admissibility and reconstruction robustness before promoting findings. Result table has no standard coefficient/p-value columns; interpret by table-specific fields.

### sheet_Novus

This module writes workbook(s) sheet_novus_output.xlsx and the main output directory currently contains **4** PNG figure(s).
Novus retail prices and brand-level assortment evidence.

Workbook sheet_novus_output.xlsx:
Sheet clean has **1,530** rows and **53** columns. It is supporting output sheet that should be interpreted in conjunction with its module context.
Sheet daily_variants has **8,654** rows and **25** columns. It is supporting output sheet that should be interpreted in conjunction with its module context.
Sheet descriptive_stats has **27** rows and **21** columns. It is supporting output sheet that should be interpreted in conjunction with its module context.
Sheet raw has **1,530** rows and **19** columns. It is supporting output sheet that should be interpreted in conjunction with its module context.
Sheet series_long has **747** rows and **16** columns. It is supporting output sheet that should be interpreted in conjunction with its module context.
Sheet tests has **27** rows and **23** columns. It is diagnostic output focused on integration, residual, or admissibility testing. Current compact interpretation: I(1)-like share=0.00; cointegration-support share=0.00; inspect admissibility and reconstruction robustness before promoting findings. Result table has no standard coefficient/p-value columns; interpret by table-specific fields.

### sheet_CME

This module writes workbook(s) sheet_cme_output.xlsx and the main output directory currently contains **3** PNG figure(s).
commodity-market benchmark data used as an external check rather than an endogenous chain stage.

Workbook sheet_cme_output.xlsx:
Sheet clean has **1,023** rows and **27** columns. It is supporting output sheet that should be interpreted in conjunction with its module context.
Sheet daily_variants has **1,486** rows and **25** columns. It is supporting output sheet that should be interpreted in conjunction with its module context.
Sheet descriptive_stats has **3** rows and **21** columns. It is supporting output sheet that should be interpreted in conjunction with its module context.
Sheet raw has **1,023** rows and **2** columns. It is supporting output sheet that should be interpreted in conjunction with its module context.
Sheet series_long has **1,023** rows and **16** columns. It is supporting output sheet that should be interpreted in conjunction with its module context.
Sheet tests has **3** rows and **23** columns. It is diagnostic output focused on integration, residual, or admissibility testing. Current compact interpretation: I(1)-like share=0.33; cointegration-support share=0.00; inspect admissibility and reconstruction robustness before promoting findings. significance share (p<0.05)=0.50

### model_short_chain_regional

This module writes workbook(s) primary_chain_consolidated.xlsx and the main output directory currently contains **4** PNG figure(s).
the consolidated RW4 chain workbook, which is the main analytical output for forward, reverse, brand, average, and robustness results.

Workbook primary_chain_consolidated.xlsx:
Sheet AveragePrice_Chain_Transmission has **749** rows and **41** columns. It is average-price panels that smooth product detail and show chain behavior at a more aggregated level. Current compact interpretation: I(1)-like share=0.00; cointegration-support share=0.00; inspect admissibility and reconstruction robustness before promoting findings. mean |coef|=2.9094 | significance share (p<0.05)=0.31 | robust-across-reconstruction share=0.26 | core-finding share=0.11
Sheet Benchmark_Comparison has **1,992** rows and **18** columns. It is best-lag benchmark correlations against ConsumerUA and EU anchors.
Sheet Consolidated_ModelCoefficients has **10,141** rows and **41** columns. It is the main forward-chain coefficient table across panel definitions, reconstruction variants, farm-gate sources, and model families. Current compact interpretation: I(1)-like share=0.00; cointegration-support share=0.00; inspect admissibility and reconstruction robustness before promoting findings. mean |coef|=3.5293 | significance share (p<0.05)=0.41 | robust-across-reconstruction share=0.27 | core-finding share=0.09
Sheet Consolidated_PreTests has **4,312** rows and **22** columns. It is pair-level integration and cointegration pretests used to decide whether level or correction-type models are admissible. Current compact interpretation: I(1)-like share=0.00; cointegration-support share=0.51; inspect admissibility and reconstruction robustness before promoting findings. significance share (p<0.05)=0.49
Sheet Coverage_Validation has **13** rows and **7** columns. It is coverage audit that verifies every required RW4 link has estimable rows and shows how many core findings survive.
Sheet FarmGate_Direct_Summary has **163** rows and **16** columns. It is summary sheet that condenses the module's main outputs. Current compact interpretation: mean |coef|=8.5959
Sheet FarmGate_Reverse_Summary has **146** rows and **16** columns. It is summary sheet that condenses the module's main outputs. Current compact interpretation: mean |coef|=0.1189
Sheet FarmGate_Source_Comparison has **2,379** rows and **13** columns. It is cross-source stability table comparing the initial and gap-filled farm-gate inputs. Current compact interpretation: robust-across-reconstruction share=0.49
Sheet FarmGate_Variant_Stability has **309** rows and **15** columns. It is supporting output sheet that should be interpreted in conjunction with its module context.
Sheet Intersection_Stability has **276** rows and **10** columns. It is supporting output sheet that should be interpreted in conjunction with its module context.
Sheet Mapping_Audit has **3,728** rows and **11** columns. It is mapping-quality audit from raw labels into product families and admissible units.
Sheet NARDL_Multipliers has **63,588** rows and **8** columns. It is dynamic multiplier paths for asymmetric NARDL models.
Sheet Panel_Index has **688** rows and **16** columns. It is catalog of the active product, comparison, and brand panels used in the consolidated RW4 chain.
Sheet RawMilk_To_Product_Transmission has **3,465** rows and **41** columns. It is direct farm-gate to downstream product links used to check whether raw-milk information bypasses intermediate stages. Current compact interpretation: I(1)-like share=0.00; cointegration-support share=0.00; inspect admissibility and reconstruction robustness before promoting findings. mean |coef|=8.1330 | significance share (p<0.05)=0.39 | robust-across-reconstruction share=0.24 | core-finding share=0.03
Sheet Reconstruction_Diagnostics has **55** rows and **14** columns. It is source-by-region diagnostics for interpolation gaps, spikes, reaggregation gaps, and imputation shares.
Sheet Retail_Combined_Diagnostics has **18** rows and **18** columns. It is supporting output sheet that should be interpreted in conjunction with its module context.
Sheet Retail_Combined_Methodology has **2** rows and **9** columns. It is supporting output sheet that should be interpreted in conjunction with its module context.
Sheet Retailer_Brand_Transmission has **962** rows and **41** columns. It is brand-level transmission table, mostly for Silpo, that checks whether brand segmentation changes pass-through. Current compact interpretation: I(1)-like share=0.00; cointegration-support share=0.00; inspect admissibility and reconstruction robustness before promoting findings. mean |coef|=8.4973 | significance share (p<0.05)=0.27 | robust-across-reconstruction share=0.13 | core-finding share=0.06
Sheet ReverseFlow_ModelCoefficients has **4,548** rows and **41** columns. It is reverse-flow estimates that test whether downstream retail shocks transmit back through the chain. Current compact interpretation: I(1)-like share=0.00; cointegration-support share=0.00; inspect admissibility and reconstruction robustness before promoting findings. mean |coef|=0.3376 | significance share (p<0.05)=0.44 | robust-across-reconstruction share=0.29 | core-finding share=0.10
Sheet Rule_Documentation has **1** rows and **9** columns. It is brief description of the admissibility and panel-construction rules used in RW4.
Sheet Unified_Retail_Comparison has **212** rows and **16** columns. It is supporting output sheet that should be interpreted in conjunction with its module context.
Sheet Unit_Admissibility has **12** rows and **5** columns. It is summary of which source-unit combinations are economically comparable enough to be modeled.
Sheet VECM_IRF has **3,744** rows and **8** columns. It is impulse-response style outputs from the system models.
Sheet Variant_Robustness has **2,449** rows and **17** columns. It is cross-variant stability table that compares linear and pchip reconstruction choices.

### model_ardl

This module writes workbook(s) model_ardl_output.xlsx and the main output directory currently contains **1** PNG figure(s).
the pooled ARDL evidence used as a linear distributed-lag benchmark.

Workbook model_ardl_output.xlsx:
Sheet ARDL_Summary has **1,383** rows and **41** columns. It is summary sheet that condenses the module's main outputs. Current compact interpretation: I(1)-like share=0.00; cointegration-support share=0.00; inspect admissibility and reconstruction robustness before promoting findings. mean |coef|=2.6492 | significance share (p<0.05)=0.33 | robust-across-reconstruction share=0.00 | core-finding share=0.00

### model_ecm

This module writes workbook(s) model_ecm_output.xlsx and the main output directory currently contains **1** PNG figure(s).
the ECM evidence used for explicit equilibrium-correction interpretation.

Workbook model_ecm_output.xlsx:
Sheet ECM_Summary has **286** rows and **41** columns. It is summary sheet that condenses the module's main outputs. Current compact interpretation: I(1)-like share=0.00; cointegration-support share=0.00; inspect admissibility and reconstruction robustness before promoting findings. mean |coef|=0.7494 | significance share (p<0.05)=0.74 | robust-across-reconstruction share=0.90 | core-finding share=0.10

### model_nardl

This module writes workbook(s) model_nardl_output.xlsx and the main output directory currently contains **2** PNG figure(s).
the asymmetric distributed-lag evidence used to detect different responses to positive and negative shocks.

Workbook model_nardl_output.xlsx:
Sheet NARDL_Summary has **3,028** rows and **41** columns. It is summary sheet that condenses the module's main outputs. Current compact interpretation: I(1)-like share=0.00; cointegration-support share=0.00; inspect admissibility and reconstruction robustness before promoting findings. mean |coef|=4.1309 | significance share (p<0.05)=0.43 | robust-across-reconstruction share=0.81 | core-finding share=0.28

### model_vecm

This module writes workbook(s) model_vecm_output.xlsx and the main output directory currently contains **1** PNG figure(s).
the system-level VECM evidence used for multistage dynamics and impulse interpretation.

Workbook model_vecm_output.xlsx:
Sheet VECM_Summary has **288** rows and **41** columns. It is summary sheet that condenses the module's main outputs. Current compact interpretation: I(1)-like share=0.00; cointegration-support share=0.00; inspect admissibility and reconstruction robustness before promoting findings. mean |coef|=11.6733 | significance share (p<0.05)=0.23 | robust-across-reconstruction share=0.00 | core-finding share=0.00

### model_discounts

This module writes workbook(s) model_discounts_output.xlsx and the main output directory currently contains **3** PNG figure(s).
the retail-promo comparison module that contrasts observed and baseline price transmission.

Workbook model_discounts_output.xlsx:
Sheet Asymmetry_Observed_vs_Baseline has **1,322** rows and **20** columns. It is comparison table between observed retail transmission and promo-controlled baseline transmission. Current compact interpretation: mean |coef|=3.4146
Sheet Discount_Strategy_Synthesis has **8** rows and **3** columns. It is plain-language summary of the discount-module conclusions.
Sheet Promo_State_Depth has **1** rows and **5** columns. It is conditional markdown-depth model output or an explicit placeholder when the model is not estimable.
Sheet Promo_State_Incidence has **1** rows and **5** columns. It is binary promo-incidence model output or an explicit placeholder when the model is not estimable.
Sheet Promo_State_Type has **1** rows and **5** columns. It is multinomial promo-state model output or an explicit placeholder when the model is not estimable.
Sheet Silpo_Discounts_Depth has **1** rows and **5** columns. It is legacy-compatible alias for the promo-depth output.
Sheet Silpo_Discounts_Occurrence has **1** rows and **5** columns. It is legacy-compatible alias for the promo-incidence output.
Sheet Silpo_Transmission_PromoCtrl has **1,322** rows and **20** columns. It is legacy-compatible alias for the observed-vs-baseline comparison table. Current compact interpretation: mean |coef|=3.4146

### model_intersection_bidirectional

This module writes workbook(s) model_intersection_bidirectional_output.xlsx and the main output directory currently contains **2** PNG figure(s).
the cross-retailer overlap module that tests shared Silpo-Novus evidence where overlap exists.

Workbook model_intersection_bidirectional_output.xlsx:
Sheet Bidirectional_Granger has **1** rows and **1** columns. It is Granger-type overlap test or an explanatory note when overlap is insufficient.
Sheet Bidirectional_Results has **1** rows and **1** columns. It is main bidirectional-regression result or an explanatory note when overlap is insufficient.
Sheet CrossTable_Correlations has **68** rows and **10** columns. It is cross-retailer and cross-source overlap correlations used to diagnose whether bidirectional estimation is even feasible.
Sheet Intersection_Combination_Detail has **0** rows and **0** columns. It is detail table for the combined-secondary model when such a model is estimable.
Sheet Intersection_Combination_Summar has **1** rows and **1** columns. It is combined-secondary-model summary or an explanatory note when overlap is insufficient.

### model_forecast_knn

This module writes workbook(s) model_forecast_knn_output.xlsx and the main output directory currently contains **3** PNG figure(s).
the forecasting and synthetic-retail module that projects producer and consumer paths.

Workbook model_forecast_knn_output.xlsx:
Sheet Forecast_Predictions has **480** rows and **6** columns. It is holdout predictions versus realized values for the forecast module.
Sheet Forecast_Summary has **8** rows and **7** columns. It is accuracy summary for the KNN-based producer and consumer forecasts.
Sheet Synthetic_Influence_Coefficient has **31** rows and **7** columns. It is coefficients linking synthetic retail signals to downstream outcomes. Current compact interpretation: mean |coef|=0.5000
Sheet Synthetic_Retail_Series has **91,711** rows and **8** columns. It is synthetic-retail panel created from the forecast module.
Sheet Synthetic_to_Consumer_Link has **3** rows and **7** columns. It is consumer-link regressions that test whether synthetic retail contains extra consumer information. Current compact interpretation: mean |coef|=0.8160 | significance share (p<0.05)=0.17
Sheet Ultimate_Consumer_Price has **143** rows and **5** columns. It is implied consumer price path based on the synthetic-retail exercise.

### model_secondary_synthetic_consumer

This module writes workbook(s) secondary_synthetic_consumer_output.xlsx and the main output directory currently contains **0** PNG figure(s).
the secondary synthetic-consumer module that would link synthetic retail signals to consumer prices when enough overlap exists.

Workbook secondary_synthetic_consumer_output.xlsx:
Sheet Synthetic_Consumer_Link has **3** rows and **8** columns. It is supporting output sheet that should be interpreted in conjunction with its module context. Current compact interpretation: mean |coef|=0.4950 | significance share (p<0.05)=0.50
Sheet Synthetic_Consumer_Predictions has **166** rows and **9** columns. It is supporting output sheet that should be interpreted in conjunction with its module context.

### graphs_decomposition

This module writes workbook(s) graphs_decomposition_output.xlsx and the main output directory currently contains **24** PNG figure(s).
the trend-seasonal decomposition graph pack.

Workbook graphs_decomposition_output.xlsx:
Sheet Decomposition_All has **25,346** rows and **9** columns. It is long-form data behind the decomposition charts.
Sheet Decomposition_Index has **31** rows and **4** columns. It is index of the decomposition chart set.
Sheet Decomposition_Summary has **31** rows and **8** columns. It is summary statistics for trend, seasonal, and residual variance shares.

### graphs_overlay_ln

This module writes workbook(s) graphs_overlay_ln_output.xlsx and the main output directory currently contains **21** PNG figure(s).
the before/after log transformation and cross-source overlay graph pack.

Workbook graphs_overlay_ln_output.xlsx:
Sheet BeforeAfterLN_All has **25,452** rows and **8** columns. It is long-form data behind the before/after log charts.
Sheet BeforeAfterLN_Index has **36** rows and **4** columns. It is index of the before/after log-transformation charts.
Sheet Overlay_All has **11,867** rows and **12** columns. It is long-form data behind the cross-source overlay charts.
Sheet Overlay_Index has **9** rows and **4** columns. It is index of the cross-source overlay charts.

### graphs_correlations_lags

This module writes workbook(s) graphs_correlations_lags_output.xlsx and the main output directory currently contains **2** PNG figure(s).
the cross-source correlation and lag graph pack.

Workbook graphs_correlations_lags_output.xlsx:
Sheet Corr_Matrix has **9** rows and **10** columns. It is matrix view of cross-source same-window correlations.
Sheet Correlations has **296** rows and **10** columns. It is pairwise correlation table across sources, frequencies, and lag choices.
Sheet Lag_Best has **31** rows and **7** columns. It is best lag per pair and product according to the lag-profile search.
Sheet Lag_Profiles has **872** rows and **7** columns. It is full lag-profile table behind the lag charts.

### graphs_brand_region

This module writes workbook(s) graphs_brand_region_output.xlsx and the main output directory currently contains **3** PNG figure(s).
the brand concentration and ProZorro regional heterogeneity graph pack.

Workbook graphs_brand_region_output.xlsx:
Sheet Brand_Economic_Metrics has **1,808** rows and **10** columns. It is brand premium, promo intensity, volatility, and brand-specific pass-through evidence. Current compact interpretation: mean |coef|=27.5983 | significance share (p<0.05)=0.14
Sheet Brand_IO_Metrics has **43** rows and **8** columns. It is brand concentration and private-label mix table by month and product family.
Sheet Prozorro_ByRegion has **147** rows and **20** columns. It is regional distribution diagnostics for ProZorro prices.

## Mismatches, Non-Logical Results, And How To Fix Them

1. Promo-state incidence, type, and depth are not mathematically estimable on the current sample. Each sheet is a placeholder row rather than a fitted model. To fix this, widen the overlap window, aggregate promo states to weekly frequency, reduce the state space, or use regularized classification models after checking class balance.
2. Brand rows miss explicit brand labels in **39.7%** of the brand-transmission table. The missing-label pattern is concentrated in empty-brand Silpo cream panels. To fix this, drop empty normalized brands before panel construction, require a minimum non-empty brand share, and re-run the brand panel builder only on supported brand names.
3. FarmGateUA -> ProducerUA has **8** core findings out of **709** covered rows. That is a substantive mismatch between economic intuition and the present proxy quality. To reduce it, replace or supplement the national farm-gate average with product-resolved procurement or raw-milk contract data.
4. Some statistically fitted coefficients are economically implausible in magnitude even when the row is not mechanically marked unreliable. Examples include brand::Silpo::alpro::sour_cream::observed::all_missing_filled::pchip on farmgate_producer_prozorro_retail_system reaches maximum absolute coefficient **296.3**; brand::Silpo::alpro::sour_cream::baseline::all_missing_filled::pchip on farmgate_producer_prozorro_retail_system reaches maximum absolute coefficient **279.7**; pairwise::producer_retail::Вершки::Silpo::baseline::initial::pchip on farmgateua_to_producerua reaches maximum absolute coefficient **247.3**; pairwise::producer_retail::Вершки::Silpo::observed::initial::pchip on farmgateua_to_producerua reaches maximum absolute coefficient **247.3**; comparison::silpo_baseline_vs_novus_observed::initial::pchip on farmgateua_to_prozorro reaches maximum absolute coefficient **237.3**. To get rid of this, impose minimum overlap and variance thresholds, winsorize or robustify extreme panels, and add coefficient-plausibility filters before promoting results.
5. Reconstruction robustness is still limited, so mathematically significant results can disappear when interpolation or farm-gate source changes. The fix is to report only doubly-robust findings, tighten interpolation anchors, and surface robustness flags directly in the thesis narrative rather than only in appendices.
6. Regional ProZorro outliers remain strong in places such as Чернівецька Молоко питне with CV **1.744**; Харківська Сир кисломолочний with CV **0.919**; Запорізька Молоко питне with CV **0.683**. These can create non-logical pass-through estimates if left untouched. The fix is to audit regional outliers, trim extreme procurement spikes, or run robust regional medians before aggregation.
7. Cross-retailer overlap is too thin for the bidirectional intersection module, and the secondary synthetic-consumer module is still empty. The fix is straightforward but data-heavy: extend the shared Silpo-Novus time window, standardize retailer calendar alignment, and only then re-run those modules.
8. Legacy three-stage product-retailer packs are still present inside the output tree and therefore remain visible in Total Run. If the thesis appendix should be RW4-only, move these legacy folders into an archive subtree or exclude them in the Total Run builder.

## Further Changes

1. Clean brand normalization and rerun brand panels so the brand table no longer carries empty-brand rows.
2. Rebuild promo-state estimation on a pooled or weekly panel so promo incidence, type, and depth become genuinely estimable rather than placeholders.
3. Tighten admissibility filters with coefficient-plausibility screens and minimum support thresholds before calling anything a core finding.
4. Add a farm-gate data upgrade step, ideally using product-linked procurement or raw-milk contractual information, because the first chain link is the current bottleneck.
5. Separate authoritative RW4 outputs from legacy diagnostic packs in Total Run so the final thesis bundle is easier to defend and easier to read.
6. Re-run the final thesis narrative only on links that survive both interpolation robustness and farm-gate-source robustness, with brand and regional caveats attached explicitly.
