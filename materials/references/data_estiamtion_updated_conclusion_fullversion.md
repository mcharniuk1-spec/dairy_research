# Chapter 5. Data

This chapter presents the integrated empirical architecture of the thesis and explains how the different raw sources are transformed into one economically coherent research design. The four-stage chain remains the same throughout the study, but the downstream block is now prepared more deeply at item level, so the empirical narrative no longer depends only on broad category pooling. The purpose of the revision is not to replace the original analytical logic, but to tighten it where the identification problem is hardest: retailer product naming, brand reconciliation, discount-aware pricing, and the choice of the most credible stage-4 retail endpoint.

The chapter therefore combines two tasks. First, it documents the institutional meaning of each price layer: raw-milk farm-gate conditions, processed-dairy producer prices, public procurement prices, and retailer-facing shelf prices do not represent the same market mechanism and should not be interpreted as if they did. Second, it shows how the deeper retail reconstruction improves comparability without breaking the broader vertical-transmission story developed in the thesis.

## 5.1 Data sources and datasets

All sources are expressed in a common hryvnia-based analytical environment and then transformed into modelling panels that correspond to distinct stages of price formation rather than to arbitrary storage tables. The research design keeps the chain visible: FarmGateUA provides the raw-milk benchmark, ProducerUA captures processor-level domestic prices for processed dairy categories, ProZorro captures procurement prices under tender and contract rules, and the retail block represents the consumer-facing shelf environment reconstructed from Silpo and Novus. External EU and CME benchmarks, together with ConsumerUA, remain important supporting layers because they help distinguish domestic chain behaviour from broader dairy-cycle movement.

### 5.1.1 FarmGateUA (raw-milk farm-gate benchmark and reconstructed daily layer).

The farm-gate layer retains its special role in the thesis. It is the only stage that starts from an official raw-milk benchmark rather than from processed-dairy or retail observations. Because the original benchmark is low-frequency, the study keeps both the initial and the gap-filled daily reconstructions, each in linear and shape-preserving form, so later inference can be checked against reconstruction sensitivity instead of hiding the issue inside one synthetic series.

Figure 5.1. Farm-gate raw-milk benchmark and reconstructed regional trends
![Figure 5.1. Farm-gate raw-milk benchmark and reconstructed regional trends](/Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/sheet_farmgateua_filled/sheet_farmgateua_filled_region_trends.png)
Source: author's calculations based on the integrated FarmGateUA reconstruction.

The technical quality of this layer is high even though its economic interpretation must remain cautious. The required-link audit keeps **709** FarmGateUA -> ProducerUA rows, **873** FarmGateUA -> ProZorro rows, and **1,883** FarmGateUA -> Retail rows. At the same time, only **8** of the FarmGateUA -> ProducerUA rows survive into the core-finding set, which is just **1.1%**. This confirms the central identification point: the farm-gate benchmark is useful as an upstream anchor and robustness dimension, but it is too aggregated to behave like a literal product-by-product pass-through series.

### 5.1.2 ProducerUA (processor-level domestic producer prices).

ProducerUA remains the cleanest domestic anchor for the processed part of the chain. The series represent processor-level domestic prices for standardized dairy categories and therefore stand between raw milk and procurement rather than duplicating the farm-gate benchmark. This layer is also the most naturally suited to error-correction reasoning because it is product-specific, persistent, and less distorted by retailer assortment management than the downstream stage.

Figure 5.2. Ukrainian producer prices by products
![Figure 5.2. Ukrainian producer prices by products](/Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/sheet_producerua/sheet_producerua_timeseries_by_standardized_type.png)
Source: author's calculations based on the ProducerUA layer.

In the benchmark-comparison table, the strongest average coherence appears in the producer layer, with the best benchmark pairings reaching mean absolute best-lag correlations of **0.730**, **0.584**, and **0.457**. Economically, this matters because the producer block is the first stage at which raw-milk conditions have already been translated into differentiated dairy products but have not yet been fully filtered by procurement rules or retail category management.

### 5.1.3 ProZorro.

The procurement layer is institutionally different from both the producer and retail stages. Contract prices in ProZorro move through tender timing, specification mix, fat content, packaging, and delivery terms rather than through continuous spot repricing. That is exactly why procurement must be modeled as its own layer: it is the first place where upstream cost pressure is translated into standardized transaction prices, yet it remains slower and more rule-bound than the retail shelf.

Figure 5.3. Ukrainian procurement prices by products
![Figure 5.3. Ukrainian procurement prices by products](/Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/sheet_prozorro/sheet_prozorro_timeseries_by_standardized_type.png)
Source: author's calculations based on the ProZorro layer.

The required-link validation retains **382** ProducerUA -> ProZorro rows and **64** core findings. That concentration of admissible and interpretable evidence is one of the main reasons why procurement is treated later as the key institutional transmission buffer rather than as a passive middle observation.

### 5.1.4 Retail (Silpo and Novus).

The most substantial data improvement in the integrated design concerns the retail block. Instead of relying only on broad category pooling, the downstream layer is rebuilt from item-level Silpo and Novus observations with cleaned product titles, cleaned brands, canonical item names, literal dairy-product typing, and explicit discount-aware prices. The effective shelf price already includes the markdown faced by the buyer, but the discount amount, discount type, discount dummy, and markdown depth are retained as separate variables. This allows the thesis to study both the transacted price and the promotional mechanism behind it.

After dairy-only reconciliation, the retail input contains **78,556** product-day observations, **361** normalized brand identifiers, and **13** literal dairy-product types. The literal mix is selective rather than generic: **Yogurt Dessert -> Yogurt (705 item keys); Hard Cheese -> Hard Cheese (592 item keys); Yogurt Dessert -> Dessert (318 item keys); Milk -> Milk (292 item keys); Butter -> Butter (163 item keys)**. This matters because the chain is more economically coherent when hard cheese, butter, milk, sour cream, condensed milk, and yogurt are not collapsed into one undifferentiated downstream average.

Figure 5.4. Retail literal-product mix after dairy-only reconciliation
![Figure 5.4. Retail literal-product mix after dairy-only reconciliation](/Users/getapple/Documents/KSE/Master Thesis/analysis second stage/figures/07_retail_literal_mix.png)
Source: author's calculations based on the harmonized Silpo-Novus item catalog.

The harmonized item-key audit identifies **200** cross-shop matches, **1,229** Silpo-only keys, and **947** Novus-only keys. Within the matched group, **106** items also align on the stricter pack-and-fat diagnostic key. This shows that the naming problem is not cosmetic. A large part of the downstream identification problem comes from real assortment asymmetry across retailers, not only from spelling or formatting noise.

Figure 5.5. Cross-shop retail item harmonisation status
![Figure 5.5. Cross-shop retail item harmonisation status](/Users/getapple/Documents/KSE/Master Thesis/analysis second stage/figures/06_cross_shop_match_status.png)
Source: author's calculations based on the cross-shop item-key audit.

The brand-support table reinforces that interpretation: **Butter in Novus: unbranded/generic label (5 item keys, 1 day); Butter in Silpo: лавка традицій (23 item keys, 48 days); Condensed Milk in Novus: ічня (6 item keys, 4 days); Condensed Milk in Silpo: первомайський мкк (4 item keys, 48 days); Cottage Cheese in Novus: звени гора (7 item keys, 2 days); Cottage Cheese in Silpo: unbranded/generic label (19 item keys, 48 days); Cream in Novus: hochland (7 item keys, 4 days); Cream in Silpo: галичина (7 item keys, 48 days)**. The downstream stage is therefore not a flat retail average. It is a layered environment where category design, brand structure, and promotion routines coexist with price transmission.

Figure 5.6. Dominant retailer-brand support by dairy product
![Figure 5.6. Dominant retailer-brand support by dairy product](/Users/getapple/Documents/KSE/Master Thesis/analysis second stage/figures/08_dominant_brand_support.png)
Source: author's calculations based on retailer-brand support in the harmonized retail panel.

### 5.1.5 External benchmarks (EU and CME).

EU dairy price monitoring and CME Class III milk futures remain supporting benchmark layers rather than structural stages of the domestic chain. Their role is to help distinguish chain-specific movements from broader regional or global dairy cycles and to support the high-frequency reconstruction of the farm-gate benchmark.

Figure 5.7. U.S. CME Class III milk prices distribution
![Figure 5.7. U.S. CME Class III milk prices distribution](/Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/sheet_cme/sheet_cme_distribution.png)
Source: author's calculations based on the CME benchmark layer.

Figure 5.8. EU dairy products prices by products
![Figure 5.8. EU dairy products prices by products](/Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/sheet_eu/sheet_eu_timeseries_by_standardized_type.png)
Source: author's calculations based on the EU benchmark layer.

These series are not interpreted as domestic transmission stages, but they remain valuable for judging whether a given Ukrainian episode is likely to reflect wider dairy-cycle movement or a more local institutional pricing response.

### 5.1.6 ConsumerUA (domestic consumer layer).

ConsumerUA remains a supporting downstream environment rather than a replacement for retailer data. It is useful where retailer coverage is thin, where a consumer-facing anchor helps extend the downstream horizon, and where the plausibility of the broader market timing needs to be checked against official consumer-price movement.

Figure 5.9. Ukrainian consumer prices by products
![Figure 5.9. Ukrainian consumer prices by products](/Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/sheet_consumerua/sheet_consumerua_timeseries_by_standardized_type.png)
Source: author's calculations based on the ConsumerUA layer.

In the integrated retail diagnostics, consumer support is non-zero only for **3** product groups, and the median consumer weight in the anchored downstream panel remains **0.000**. This means the consumer layer helps continuity and plausibility, but it does not erase retailer information.

## 5.2 Data construction and transformation

The data-construction pipeline is deliberately conservative. It passes each source through product harmonization, unit harmonization, and frequency alignment before the prices are allowed to enter the econometric analysis. The objective is not to maximize raw sample length at any cost, but to retain windows in which the compared prices are economically similar enough for dynamic interpretation.

The product-mapping audit covers **3,728** mapped label groups. Exact matches account for **59.7%**, multi-match cases account for **33.2%**, and unmatched rows account for **7.1%**. At the same time, the economically comparable share remains **92.9%**. The implication is that the major problem is not general labeling chaos, but the smaller set of economically awkward cases in which pack size, product definition, or institutional wording does not line up cleanly across stages.

Retail preparation now adds a fourth gate that did not exist at the same depth before: item-level cross-shop reconciliation. The harmonized item key combines the thesis product group, cleaned brand, and canonicalized product name stripped of redundant fat and pack tokens. This greatly improves the downstream stage because Novus and Silpo often carry the same economic item under different wording, while other items are truly unique to only one chain and should not be forced into a false common sample.

Figure 5.10. Integrated panel coverage by product and source
![Figure 5.10. Integrated panel coverage by product and source](/Users/getapple/Documents/KSE/Master Thesis/analysis second stage/figures/01_panel_coverage.png)
Source: author's calculations based on the combined daily panel.

Frequency alignment follows the same economic logic as in the methodology chapter. Retail observations are daily, procurement observations remain irregular but are converted into comparable daily sequences within overlap windows, and the farm-gate benchmark is reconstructed to higher frequency in multiple admissible variants. Those variants are not treated as hidden technical steps; they are retained explicitly so later inference can be judged against interpolation and reconstruction robustness.

The revised downstream block also no longer assumes that one retail series is universally optimal for every product. Instead, the study tests several candidate stage-4 endpoints: the merged full-list retail panel, the stricter matched cross-shop panel, Silpo-only and Novus-only panels, and a retail-plus-ConsumerUA variant. These candidates are compared product by product using a composite score that reflects coverage, procurement alignment, consumer alignment, item support, and discount variation.

Figure 5.11. Candidate downstream retail scores by product
![Figure 5.11. Candidate downstream retail scores by product](/Users/getapple/Documents/KSE/Master Thesis/analysis second stage/figures/09_retail_level_scores.png)
Source: author's calculations based on the retail-level comparison table.

Figure 5.12. Chosen downstream retail level by product
![Figure 5.12. Chosen downstream retail level by product](/Users/getapple/Documents/KSE/Master Thesis/analysis second stage/figures/10_optimal_retail_level.png)
Source: author's calculations based on the selected downstream hierarchy.

The selected hierarchy chooses the merged full retail list for **7** of the **9** thesis product groups, the Retail plus ConsumerUA endpoint for **1** group, and the matched cross-shop panel for **1** group. Hard cheese is the clearest case where the downstream extension benefits from the consumer-linked endpoint, while milk powder is the clearest case where the stricter matched panel is preferable to a broad pooled average.

## 5.3 Diagnostic tests and interpretation

Before estimation, every candidate link is screened through stationarity and admissibility diagnostics. The pretest block combines ADF and KPSS evidence, overlap rules, residual diagnostics, and explicit no-fit classification. This matters substantively: the models are not treated as automatic coefficient generators, but as conditional tools whose interpretation depends on whether the underlying data support a long-run relation, a correction mechanism, or only a reduced-form short-run response.

The integrated pretests confirm that the environment is heterogeneous rather than uniformly I(1). The dependent series is classified as I(0) in **1,824** cases, I(1) in **1,508**, I(2) in **535**, and ambiguous in **445**. Cointegration support appears in **50.5%**. This is substantial enough to motivate error-correction models, but not enough to justify forcing every link into the same dynamic form.

The consolidated coefficient table contains **10,141** rows. Of these, **51.9%** finish with status 'ok', **48.1%** remain unreliable, and only **8.7%** survive into the core-finding layer. There are **1,236** explicit no-fit rows, dominated by **940** I(2)-blocked cases and **296** insufficient-overlap cases. This is analytically important because it shows that the code excludes weak or non-comparable estimates instead of hiding them.

Figure 5.13. Before/after log transformation (illustrative)
![Figure 5.13. Before/after log transformation (illustrative)](/Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/graphs_overlay_ln/before_after_ln_01.png)
Source: author's calculations based on the log-transformation diagnostics.

Figure 5.14. Best-lag correlation scan across stages
![Figure 5.14. Best-lag correlation scan across stages](/Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/graphs_correlations_lags/lag_best_bar.png)
Source: author's calculations based on the lag-profile diagnostics.

The lag structure also remains central for interpretation. The strongest best-lag examples in the descriptive scan include ProducerUA -> ConsumerUA for Сметана at lag **1** with correlation **0.994**, ProducerUA -> ConsumerUA for Сир твердий at lag **1** with correlation **0.986**, and ProducerUA -> ConsumerUA for Молоко питне at lag **1** with correlation **0.907**. This pattern confirms that delayed adjustment, rather than same-day co-movement, is the economically relevant object in the dairy chain.

## 5.4 Market-structure and regional heterogeneity diagnostics

The empirical design does not rely on time-series structure alone. It also incorporates market-structure diagnostics because bargaining power, assortment design, and regional contract conditions shape how price shocks are filtered across the chain. This is especially important downstream, where promotions and category management can alter the observed timing of transmission even when the long-run relation is preserved.

Figure 5.15. Retail brand concentration over time
![Figure 5.15. Retail brand concentration over time](/Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/graphs_brand_region/brand_hhi.png)
Source: author's calculations based on the retail brand-structure diagnostics.

The concentration block shows that retailer power is not evenly distributed across products. The highest HHI episodes in the current sample appear in Novus butter at **1.000**, Novus other at **0.500**, and Novus yogurt_dessert at **0.202**. These values must still be read together with SKU support, but they confirm that concentration is a real feature of parts of the retail environment rather than an abstract theoretical concern.

Figure 5.16. Regional procurement-price dispersion by product type
![Figure 5.16. Regional procurement-price dispersion by product type](/Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/graphs_brand_region/prozorro_region_median.png)
Source: author's calculations based on the ProZorro regional diagnostics.

Regional procurement dispersion is equally important. The highest coefficients of variation appear in Чернівецька milk at **1.744**, Харківська cottage_cheese at **0.919**, and Запорізька milk at **0.683**. That dispersion helps explain why procurement is best interpreted as an institutional transmission buffer rather than as one homogeneous national middle layer.

Figure 5.17. Retail discount environment by product and retailer
![Figure 5.17. Retail discount environment by product and retailer](/Users/getapple/Documents/KSE/Master Thesis/analysis second stage/figures/12_discount_environment.png)
Source: author's calculations based on the harmonized Silpo-Novus retail panel.

The integrated discount environment shows the same point from a different angle. Promotions are not random statistical noise attached to a true price that lies somewhere behind the shelf. They are part of how the shelf path itself is managed, especially in high-frequency retailer data.

## 5.5 Product-level retail price movements in the consumer basket

The product-level retail evidence deserves separate discussion before the estimation chapter because it is the point at which the thesis comes closest to the way households actually experience dairy inflation. As the introduction stresses, dairy products are purchased frequently, are immediately visible in the day-to-day consumer basket, and become salient not because one category alone dominates household spending, but because several staple categories move in front of consumers repeatedly. That intuition is exactly why the item-level Silpo-Novus reconstruction matters: it allows the chapter to compare visible shelf movements product by product against the corresponding producer, procurement, and consumer layers rather than treating retail as one abstract average.

The retail window covers mostly the period from **2025-10-21** to **2026-01-08**. Within that interval, the densest daily category support appears in yogurt/dessert with median **649** retail item keys and **77** brands, milk/fermented milk with **275** item keys and **71** brands, butter with **108** item keys and **36** brands, sour cream with **57** item keys and **35** brands, and hard cheese with **55** item keys and **21** brands. This ranking matches the economic logic of the consumer basket quite closely: the everyday categories that households notice most are also the categories for which the downstream panel is most densely observed.

Figure 5.18. Novus retail-level prices by product
![Figure 5.18. Novus retail-level prices by product](/Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/sheet_novus/sheet_novus_timeseries_by_standardized_type.png)
Source: author's calculations based on the Novus retail panel.

Figure 5.19. Silpo retail-level prices by product
![Figure 5.19. Silpo retail-level prices by product](/Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/sheet_silpo/sheet_silpo_timeseries_by_standardized_type.png)
Source: author's calculations based on the Silpo retail panel.

The preparation results already show why retailer-level construction cannot be separated from later model interpretation. In several categories Silpo carries the dense part of the item universe, while Novus contributes a much thinner but still informative reference line. Milk is built on a median **275** Silpo item keys and **72** brands, but only **1** Novus key and **1** brand; butter shows **108** Silpo keys against **1** Novus key; sour cream shows **57** against **1**; and even hard cheese, which is one of the richer comparison categories, has only **2** median Novus keys against **55** in Silpo. This means that cross-shop comparison is economically useful, but it should not be read as if both chains contribute the same product depth in every category.

Milk and butter are the clearest examples of visible basket categories that move more smoothly on the shelf than upstream prices would suggest. Over the observed retail window of **61** days for milk, Silpo milk changes by **+5.0%**, while Novus milk changes by **-2.4%**; over the same interval the producer series falls by **-22.92%**, ProZorro rises by **+11.84%**, and the consumer layer rises by **+2.2%**. The mean absolute Silpo-Novus gap in milk is only **15.68** UAH, which is small compared with the same-category gap in hard cheese. In butter, over **54** days, Silpo changes by **-5.4%** and Novus by **+0.4%**, while the producer layer falls by **-24.06%** and procurement still rises slightly by **+1.7%**. These are also heavily promoted Silpo categories, with mean discount shares of **25.6%** for milk and **22.9%** for butter, while the average absolute cross-chain gap remains **82.97** UAH in butter. Economically, this is a strong sign of downstream smoothing: the products that matter most in the daily basket do not mirror upstream shocks one-for-one, even when those upstream shocks are substantial.

Sour cream sits close to the same everyday-basket logic. Silpo sour cream changes by **-3.5%**, while Novus changes by **+3.4%**. At the same time, the producer layer falls by **-22.41%**, procurement falls by **-8.8%**, and the consumer layer still rises by **+2.0%**. With median support of **57** retail item keys, **35** brands, an average Silpo discount share of **23.9%**, and a mean Silpo-Novus gap of only **4.850** UAH, sour cream behaves like a typical visible shelf category: it stays inside a comparatively narrow retail corridor even when other parts of the chain move more sharply.

Hard cheese is the clearest contrast. Over the same window, Silpo hard-cheese prices rise by **+12.71%**, while Novus falls by **-54.34%**. The producer series falls by **-21.08%**, procurement rises by **+15.54%**, and the consumer layer rises by **+3.4%**. The category still has a substantial Silpo discount share of **22.1%**, but its average cross-chain gap reaches **247.5** UAH and the maximum observed gap reaches **864.1** UAH. This is not the pattern of a homogeneous downstream category. It is the pattern of a strategically managed category in which retailer assortment, brand mix, imported and premium lines, and product differentiation matter enough to produce materially different shelf paths across chains.

The thinner and more differentiated categories reinforce the same point in a more selective way. Condensed milk is observed over **52** days and shows Silpo at **-8.2%** against Novus at **+20.55%**, while procurement rises by **+49.55%**; cottage cheese shows Silpo at **+8.4%** against Novus at **-3.9%**, while procurement rises by **+56.75%**; and cream shows Silpo at **+3.3%** against Novus at **-27.78%**, while procurement falls by **-11.07%**. These are all categories where Novus support remains very thin, usually **1** key in condensed milk, **1** key in cottage cheese, and **1** key in cream, so the Novus path should be treated as a focused chain signal rather than a broad market average. Yogurt/dessert remains one of the densest shelf categories, with **649** median item keys and **77** brands, yet even there Silpo changes by only **-5.5%** while Novus changes by **-18.89%**. Milk powder is the thinnest category, with only **3** median retail item keys and **2** median Novus keys, which is why its very large Silpo increase of **+78.33%** and mean discount share of **36.1%** should be read more cautiously than the staple-basket categories.

From the viewpoint of data preparation, these comparisons justify the later modelling hierarchy. A strict matched cross-shop retail panel is valuable when the same economic item truly exists in both chains, but it is not always the best analytical endpoint when one retailer contributes only one or two matched observations inside a category with otherwise rich shelf turnover. For staple categories, the broader merged retail panel preserves the visible consumer basket better; for categories with thinner and more specialized retail support, the matched or consumer-linked variants can be more credible. This is why product-level preparation is not a separate descriptive appendix to the thesis, but the mechanism through which the stage-4 price object becomes economically interpretable.

Read together, these product-level comparisons tighten the thesis story before the formal estimation begins. The visible basket categories, especially milk, butter, and sour cream, show dense retail support and comparatively bounded shelf movement relative to larger upstream shifts, which is consistent with markdown smoothing and retail timing control. The more differentiated categories, especially hard cheese, cream, and some condensed-milk and cottage-cheese lines, show wider retailer divergence and therefore provide a more natural setting for asymmetric adjustment and category-management effects. This is exactly the distinction that the estimation chapter must then take seriously: not all dairy products transmit shocks in the same way, and the product level is not detail around the model but part of the model's economic meaning.

## 5.6 What data remain after preparation - datasets in models

After filtering and standardization, the integrated modelling universe contains **688** panel definitions: **500** pairwise-product panels, **100** product panels, **44** brand panels, **28** average panels, and **16** comparison panels. This is a large empirical universe, but it remains economically uneven because overlap and admissibility differ sharply by link and by product.

The required-link coverage makes that unevenness visible. FarmGateUA -> ProducerUA contributes **709** rows with **8** core findings; ProducerUA -> ProZorro contributes **382** rows with **64** core findings; ProZorro -> Retail contributes **896** rows with **204** core findings; Retail -> ProZorro contributes **636** rows with **228** core findings; and the brand block adds **44** brand panels with **55** core findings. The integrated retail reconstruction improves the stage-4 interpretation substantially, but it does not remove the basic fact that some products and some links remain much better identified than others.

The direct farm-gate block is especially important to interpret correctly. Its core-finding share is **1.1%** for ProducerUA, **4.8%** for ProZorro, and **2.2%** for Retail. This corrected ranking matters because it shows that the strongest direct extreme-points evidence is farm-gate to procurement, not farm-gate to processor. The raw-milk benchmark is therefore informative, but it works best where the downstream stage is still relatively standardized.

# Chapter 6. Estimation results

The estimation chapter asks where along the dairy chain price adjustment is fast, where it is buffered, and where it is reshaped by downstream commercial conduct. The core structural evidence still comes from the chain ProducerUA -> ProZorro -> Retail because this remains the clearest sequence through which an upstream cost signal can be traced into procurement and then to the shelf. The deeper retail reconstruction does not replace that logic. It strengthens it by making the stage-4 measurement more transparent and by checking whether the main economic interpretation survives under alternative retailer-grounded downstream definitions.

## 6.1 Model strategy and what the families contribute

The model families are deliberately complementary rather than redundant. ARDL remains the distributed-lag benchmark when a stable long-run relation is plausible. ECM turns that relation into an explicit speed-of-adjustment object. NARDL tests whether positive and negative shocks are processed differently. VECM remains a multivariate robustness layer. To deepen the downstream interpretation, the study also adds local projections, vertical spread equations, and focused discount regressions built on the item-level retail reconstruction. These additional models are not substitutes for the structural stack; they are retailer-sensitive robustness layers that clarify timing, endpoint choice, and the role of promotions.

Across the integrated coefficient table, the study estimates **10,141** coefficients: **3,028** NARDL rows, **1,383** ARDL rows, **286** ECM rows, **288** VECM rows, and the remainder in OLS-HAC stress-test families or explicit no-fit cases. Crucially, **879** out of **879** core findings sit in the NARDL or ECM families. That is why the thesis treats equilibrium correction and asymmetry, rather than one-period coefficients, as the main evidential objects.

Figure 6.1. Short-run ARDL coefficient dispersion across active links
![Figure 6.1. Short-run ARDL coefficient dispersion across active links](/Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/model_ardl/ardl_short_run.png)
Source: author's calculations based on the integrated ARDL summary output.

Figure 6.2. Long-run adjustment signals across links
![Figure 6.2. Long-run adjustment signals across links](/Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/model_ecm/ecm_ect.png)
Source: author's calculations based on the integrated ECM summary output.

Figure 6.3. Asymmetric long-run transmission evidence
![Figure 6.3. Asymmetric long-run transmission evidence](/Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/model_nardl/nardl_long_run.png)
Source: author's calculations based on the integrated NARDL summary output.

The additional retailer-sensitive block estimates **3,570** local-projection equations and retains **728** screened horizon responses. The vertical spread block adds **280** usable equations, while the focused discount block adds **4** direct discount equations. These models are deliberately simpler than the structural ARDL-ECM-NARDL system, but they are informative because they stress-test the same economic story with a data build that is much more explicit about item-level retail construction.

## 6.2 Producers to procurement (processors) transmission

The upstream link remains the clearest part of the chain. Procurement does not behave like a frictionless conduit, but it repeatedly re-anchors to producer conditions. This is the stage at which cost pressure is translated into standardized transaction prices, yet contracting and specification rules still smooth part of the short-run noise.

In the required-link audit, ProducerUA -> ProZorro contributes **382** rows and **64** core findings. The product-level NARDL block shows especially clear correction for butter with ECT **-0.808**, cream with ECT **-1.003**, and hard cheese with ECT **-0.704**, all with very small p-values. This is exactly the kind of repeated equilibrium re-anchoring one would expect when procurement is institutionally slower than the producer layer but cannot remain detached from it for long.

The timing evidence supports the same interpretation. In the pooled butter panel, the strongest producer-to-procurement lag appears at **25** days; in hard cheese it appears at **27** days. In the horizon-based robustness block, ProducerUA -> ProZorro reaches a screened 7-day core share of **40.0%**. So the evidence is not only statistically present; it is also consistent with delayed but real institutional repricing.

What matters economically is not a literal one-to-one long-run markup coefficient. The more important result is that procurement repeatedly corrects disequilibrium with the producer stage, which is precisely what gives the middle of the chain its buffering role. Procurement absorbs, delays, and regularizes shocks; it does not sever the link.

## 6.3 Procurement to retail transmission and retailer heterogeneity

The downstream link is harder to interpret because retail price is not only a function of upstream cost. It is also a function of assortment design, markdown policy, category management, and the retailer's ability to choose when a procurement shock becomes visible on the shelf. That is why retailer heterogeneity matters more downstream than upstream.

Butter remains the clearest example of managed but real downstream linkage. In the pooled retail panel, ARDL gives a short-run coefficient of **0.381** and a long-run coefficient of **5.038**. ECM then sharpens the interpretation with ECT **-0.584** at p-value **0.008**, while NARDL also yields a strong correction term of **-0.935**. The stable conclusion is not a literal long-run markup; it is that the pooled butter category re-anchors after procurement shocks, but does so through a managed shelf path rather than through one-step repricing.

Figure 6.4. Butter, pooled retail, observed category series
![Figure 6.4. Butter, pooled retail, observed category series](/Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/butter/silpo_novus/time_series_observed.png)
Source: author's calculations based on the integrated butter retail-procurement panel.

Figure 6.5. Butter, pooled retail, ECM adjustment
![Figure 6.5. Butter, pooled retail, ECM adjustment](/Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/butter/silpo_novus/ecm_adjustment_observed.png)
Source: author's calculations based on the integrated butter ECM output.

Milk in Silpo remains the clearest fast-adjustment case. ECM gives a short-run coefficient of **0.038**, a long-run coefficient of **0.080**, and ECT **-0.900**. NARDL produces the same qualitative result, with ECT **-1.149**. The lag profile places the strongest procurement-to-retail relation at **26** days with correlation **0.346**. This is economically consistent with a high-turnover product category in which disequilibrium is removed relatively quickly.

Figure 6.6. Milk, Silpo, observed category series
![Figure 6.6. Milk, Silpo, observed category series](/Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/milk/silpo/time_series_observed.png)
Source: author's calculations based on the integrated milk Silpo panel.

Figure 6.7. Milk, Silpo, ECM adjustment
![Figure 6.7. Milk, Silpo, ECM adjustment](/Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/milk/silpo/ecm_adjustment_observed.png)
Source: author's calculations based on the integrated milk ECM output.

Hard cheese is different again. The pooled ARDL coefficient is short-run **-1.331** and long-run **-3.323**, while the pooled NARDL gives short-run **-0.287**, long-run **-7.005**, and ECT **-0.586**. The category also shows one of the strongest delayed patterns, with the procurement-to-retail lag peak at **13** days and the producer-to-procurement peak at **27**. This is the strongest downstream case for strategic category management and asymmetric treatment of cost pressure.

Figure 6.8. Hard cheese, pooled retail, NARDL multipliers
![Figure 6.8. Hard cheese, pooled retail, NARDL multipliers](/Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/hard_cheese/silpo_novus/nardl_multipliers_observed.png)
Source: author's calculations based on the integrated hard-cheese NARDL output.

Sour cream sits between the milk and hard-cheese cases. Its pooled NARDL gives short-run **-0.198**, long-run **0.141**, and ECT **-0.851**. The category clearly corrects, but it remains more strategically managed than plain drinking milk.

The deeper retail reconstruction clarifies this heterogeneity further because it allows the stage-4 endpoint to vary by product instead of being imposed mechanically. In the horizon-based downstream comparison, the strongest procurement-to-retail evidence appears for Silpo, where the best screened ProZorro -> Silpo specification reaches a 7-day core share of **42.9%**. Novus follows with **33.3%**, the matched cross-shop panel with **16.7%**, and the broad retail pool with **14.3%**. This ranking is economically useful because it shows that more coverage is not always more informative: the broader pooled panel is longer, but the retailer-specific endpoint can carry a cleaner timing signal.

Figure 6.9. Procurement-to-retail evidence across downstream endpoint candidates
![Figure 6.9. Procurement-to-retail evidence across downstream endpoint candidates](/Users/getapple/Documents/KSE/Master Thesis/analysis second stage/figures/11_candidate_downstream_core_share.png)
Source: author's calculations based on 7- and 14-day local-projection screening across candidate retail endpoints.

Figure 6.10. Local-projection pass-through by horizon
![Figure 6.10. Local-projection pass-through by horizon](/Users/getapple/Documents/KSE/Master Thesis/analysis second stage/figures/02_lp_pass_through_horizons.png)
Source: author's calculations based on the integrated local-projection summary.

The local-projection evidence should still be interpreted carefully. It is intentionally less structural than ECM or NARDL. Its value lies in showing whether the timing of the response survives when the lag structure is not imposed parametrically. In that role, it supports the same conclusion as the structural models: transmission is delayed, product-specific, and sensitive to how the downstream stage is measured.

## 6.4 Discounts, retail design, and market-power signals

Discounts are not treated here as an afterthought. The retail item-level reconstruction makes them explicit in two ways at once: the effective price already contains the markdown, but the discount state remains visible through the baseline price, discount amount, discount type, discount dummy, and markdown depth. That design matters because retailers can absorb part of the short-run pressure by changing the promotional regime while leaving the broader shelf path comparatively smooth.

The structural discount comparison confirms that observed and baseline retail paths are not equivalent. Across **1,322** observations in the observed-versus-baseline table, the mean absolute difference equals **2.888** in short-run coefficients, **1.218** in long-run coefficients, and **0.551** in adjustment terms. Pseudo-asymmetry is flagged in **55.1%** of rows. This is much more consistent with tactical price smoothing than with a clean one-price retail regime.

Figure 6.11. Observed-versus-baseline discount effect in short-run transmission
![Figure 6.11. Observed-versus-baseline discount effect in short-run transmission](/Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/model_discounts/discount_delta_short_run.png)
Source: author's calculations based on the integrated discount-comparison output.

The retailer-sensitive robustness block sharpens the same point from a different direction. The vertical spread module estimates **280** usable equations, of which **24** indicate persistent spreads and **223** indicate asymmetric adjustment. These spread results are not direct legal proof of market power, but they are highly consistent with timing control, selective margin adjustment, and category management.

Figure 6.12. Vertical spread and margin-adjustment proxy across chain segments
![Figure 6.12. Vertical spread and margin-adjustment proxy across chain segments](/Users/getapple/Documents/KSE/Master Thesis/analysis second stage/figures/04_vertical_spread_proxy.png)
Source: author's calculations based on the integrated spread-model summary.

The focused discount model is intentionally narrower and therefore more cautious. It yields **4** usable equations and **2** explicit discount-strategy signals, notably in butter and milk. This does not weaken the economic role of promotions. It clarifies it. Promotions appear to matter most as part of the downstream data-generating process itself rather than as a stand-alone structural driver that dominates every category.

Figure 6.13. Retail discount incidence by product
![Figure 6.13. Retail discount incidence by product](/Users/getapple/Documents/KSE/Master Thesis/analysis second stage/figures/05_discount_incidence.png)
Source: author's calculations based on the integrated discount-model outputs.

Taken together, the main and retailer-sensitive discount blocks lead to the same interpretation. Discounts help retailers control the timing and visibility of transmission. They do not eliminate the upstream link, but they do alter how quickly and how visibly that link reaches the shelf.

### 6.4.1 Farm-gate transmission and whole-chain interpretation

The direct farm-gate question remains the most difficult part of the thesis because it compresses several institutional transformations into one relationship. The issue is not whether the farm-gate benchmark exists in the data. It does. The issue is how much of that benchmark can be recovered once one national raw-milk series is asked to explain processed-dairy categories, procurement prices, and retailer-controlled shelf prices.

The corrected direct-summary shares make the ranking clear. FarmGateUA -> ProducerUA contributes **8** core findings out of **709**, or **1.1%**. FarmGateUA -> ProZorro contributes **42** core findings out of **873**, or **4.8%**. FarmGateUA -> Retail contributes **42** core findings out of **1,883**, or **2.2%**. The strongest direct block is therefore farm-gate to procurement, not farm-gate to processor.

Figure 6.14. Direct farm-gate evidence by downstream stage and downstream panel
![Figure 6.14. Direct farm-gate evidence by downstream stage and downstream panel](/Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/primary_chain_summary/farmgate_direct_heatmap.png)
Source: author's calculations based on the integrated primary-chain farm-gate summary.

In the pairwise NARDL comparison, the strongest FarmGateUA -> ProZorro route reaches a core-finding share of **38.9%**, with reconstruction robustness of **77.8%** and interpolation robustness of **100.0%**. For the anchored broad retail panel, the comparable FarmGateUA -> Retail share is **3.3%** with median overlap **189**; for the stricter retailer-core panel it is **4.9%** with median overlap **54**. This is the central trade-off of the full-chain design: the broader downstream endpoint lengthens the horizon, while the retailer-core endpoint is shorter but economically cleaner.

Figure 6.15. Comparison of broad and retailer-core downstream panels in the full chain
![Figure 6.15. Comparison of broad and retailer-core downstream panels in the full chain](/Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/primary_chain_summary/unified_retail_comparison.png)
Source: author's calculations based on the integrated downstream-panel comparison output.

The reverse-flow evidence is equally important for interpretation. In the pairwise NARDL block, the broad downstream panel reaches **6.7%** core support in Retail -> FarmGateUA, while the retailer-core panel reaches **17.6%**. The broader reverse-flow table also retains **228** core findings out of **636** for Retail -> ProZorro, or **35.8%**. In the pooled Retail -> ProducerUA comparison panel, the strongest NARDL specification yields short-run **1.800**, long-run **1.318**, and ECT **-1.375**. This does not prove simple reverse causality in every period. It shows something more interesting: downstream pricing decisions contain information that travels back through the chain.

Figure 6.16. Bidirectional coefficient evidence across upstream and downstream intersection panels
![Figure 6.16. Bidirectional coefficient evidence across upstream and downstream intersection panels](/Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/Charniuk_Dairy_Research/outputs/model_intersection_bidirectional/bidirectional_coef.png)
Source: author's calculations based on the integrated bidirectional model summary.

The whole-chain interpretation is therefore more precise than a simple forward pass-through statement. Forward transmission remains the dominant structural story. Procurement still re-anchors to producer conditions, and retail still responds to procurement shocks. But the integrated evidence also shows that the downstream stage is informative in its own right. Retailers are not only receivers of shocks; they are coordinators of how those shocks are timed, displayed, and partially fed back into the broader price environment.

### 6.4.2 Comparative synthesis of model results

To keep the empirical story economically coherent, the final step before the conclusion is to place all estimation blocks into one comparative matrix. The purpose of the table is not to mechanically rank estimators, but to show what each model family contributes, which numeric results carry the interpretation, and how the same chain story changes when the price object, lag structure, or downstream measurement rule changes.

Table 6.1. Integrated comparative summary of the estimated model blocks

| Model or screen | Estimated output | Main numeric result | Timing or correlation signal | Upstream reading | Downstream and chain reading |
| --- | --- | --- | --- | --- | --- |
| Lagged correlation scan | 31 pair-product lag scans | Top corr 0.994 for ProducerUA -> ConsumerUA (Сметана); next 0.986. | Producer-to-procurement peaks at 25-27 days; procurement-to-retail at 13-26 days. | Supports delayed repricing rather than same-day pass-through. | Motivates product-specific distributed-lag and retail-endpoint specifications. |
| ARDL | 1,383 equations; median n 49; ok share 68.9%. | Butter retail SR 0.381, LR 5.038; hard cheese retail SR -1.331, LR -3.323. | Benchmark distributed-lag structure when a long-run relation remains plausible. | Shows gradual producer-to-procurement incorporation without forcing asymmetry. | Useful sign and magnitude benchmark, but long-run retail coefficients are not read literally. |
| ECM | 286 equations; 29 core findings; median n 1,456. | ECTs: butter retail -0.584, milk retail -0.900, cream upstream -1.003. | Negative ECTs show how fast disequilibrium is removed after shocks. | Strongest evidence that procurement re-anchors toward producer conditions. | Milk is the fastest downstream correction case; butter also corrects under managed shelf pricing. |
| NARDL | 3,028 equations; 850 core findings; median n 46. | ECTs: butter -0.935, milk -1.149, sour cream -0.851; hard-cheese LR -7.005. | Separates positive and negative shock processing and retains the core asymmetry evidence. | Butter, cream, and hard cheese show clear procurement correction under nonlinear adjustment. | Hard cheese remains the clearest asymmetric downstream category; retailer management matters most here. |
| VECM | 288 system equations; 0 retained core findings; median n 47. | Median system adjustment term 0.112. | Multivariate consistency check only; short overlapping samples limit retained evidence. | Confirms that system-wide modelling is possible, but not the main identification base in this sample. | Used as robustness rather than as the headline estimator for retail transmission. |
| OLS-HAC shock | 3,076 reduced-form equations; median n 46. | Median absolute short-run coefficient 0.084. | Shock-dummy stress test without long-run equilibrium structure. | Captures event sensitivity around the chain without imposing cointegration. | Helpful for robustness, but not read as structural pass-through. |
| OLS-HAC retail controls | 844 reduced-form promo-control equations; median n 40. | Median absolute short-run coefficient 1.864; observed-vs-baseline delta SR 2.888; pseudo-asymmetry 55.1%. | Tests whether promotions and baseline construction reshape measured pass-through. | Not an upstream anchor; it is a downstream measurement check. | Shows that discount-aware retail preparation changes the observed coefficient surface materially. |
| Local projections | 3,570 horizon equations; 728 screened responses. | Best downstream screen: ProZorro -> Silpo with core share 42.9% at horizon 7; overall best FarmGateUA -> ProducerUA at horizon 7. | Non-parametric horizon responses preserve timing without imposing one lag polynomial. | Shows where producer and farm-gate shocks appear earliest in the chain. | Confirms that Silpo often carries the cleanest short-horizon procurement-to-retail response. |
| Vertical spread models | 280 usable equations; 24 persistent-margin flags; 223 asymmetric-margin flags. | Best spread case Milk / fermented milk (Silpo baseline / ProZorro) with R2 0.887 and discount-share coef 0.005. | Spread persistence and asymmetry proxy selective margin adjustment across stages. | Shows where procurement and farm-gate gaps remain persistent after upstream shocks. | Supports a category-management reading of downstream market power rather than one static markup wedge. |
| Discount models | 4 direct discount equations; 2 strategy signals. | Butter lag discount 0.631; milk lag discount 0.805; best R2 0.765. | Discount state is more persistent than spread state in staple categories. | Producer and procurement shocks enter discount behavior selectively, not uniformly. | Discounts act as tactical smoothing instruments, especially in milk and butter. |

Source: author's calculations based on the integrated primary-chain outputs, local-projection outputs, spread models, and discount models.

## 6.5 Conclusion and economic implications

The integrated empirical conclusion is that the Ukrainian dairy market is vertically coordinated, but that coordination is neither frictionless nor uniform. The study does not support one universal pass-through coefficient. Instead, it reveals a layered chain in which different institutional stages bear different parts of the adjustment burden and in which the downstream stage has its own strategic logic rather than behaving like a passive residual of upstream cost.

The most persuasive structural evidence remains equilibrium correction. Procurement repeatedly re-anchors to producer prices; retail categories repeatedly re-anchor to procurement conditions; and the strongest product-level results appear where the category is economically coherent enough for disequilibrium to be observed and then removed. Milk is the clearest high-frequency downstream correction case, butter is the clearest managed-but-linked case, and hard cheese is the clearest strategic category-management case.

The deeper retail reconstruction strengthens that conclusion rather than overturning it. Once Novus and Silpo are harmonized at item level, discounts are kept inside the effective price but modeled separately, and the downstream endpoint is allowed to vary by product, the main story survives. The shelf does not behave like a pure cost-plus series. It behaves like a managed adjustment layer in which timing, brand structure, discount policy, and assortment design reshape how upstream shocks become visible to consumers.

This integrated result is economically valuable at several levels. For processors and procurement managers, it shows that disequilibrium tends to be corrected, but not at the same speed across products. For retailers, it quantifies how category management and promotions can soften or delay the shelf response without fully severing the upstream link. For competition and policy analysis, it suggests that downstream market power is best understood not as one static markup wedge, but as control over the timing, visibility, and selectivity of transmission.

The difficult coefficients are also informative when read correctly. Large negative long-run values, selective asymmetry, and weak direct farm-gate coefficients concentrate where economic granularity is coarse, where overlap is thin, or where retailer assortment is structurally uneven across chains. The correct response is therefore not to smooth those results away, but to acknowledge where the chain is well identified and where it remains sensitive to data design.

On that standard, the present version is materially stronger than before. The retail stage is better grounded in item-level evidence, the farm-gate interpretation is more accurately delimited, the core structural models and the retailer-sensitive robustness layers now tell the same economic story, and the thesis can state its main claim more confidently: vertical price transmission in the Ukrainian dairy chain is real, procurement acts as an institutional transmission buffer, and downstream market power appears primarily through category management, discount smoothing, and selective asymmetry rather than through one mechanical pass-through coefficient.
