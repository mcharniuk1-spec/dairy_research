# Second-Stage Estimation Summary

## Analytical Purpose
This second-stage run keeps the thesis chain as FarmGateUA -> ProducerUA -> ProZorro -> Retail, but estimates it with a different empirical design from the earlier RW4 ARDL/ECM/NARDL/VECM workflow. The aim is to check whether the same economic story survives when the model is rebuilt as a daily product-panel local-projection exercise and a vertical spread/discount market-power proxy exercise.

The model uses the active `full_uah.xlsx`, `farm_gate_daily.xlsx`, and `farm_gate_all_missing_filled_daily.xlsx` workbooks from the nested Charniuk dairy research project. Farm-gate variants remain explicit (`initial` and `filled`, each with `linear` and `pchip` reconstruction), while retail is separated into observed and baseline price paths to keep discount behavior visible.

## Data Coverage
The cleaned second-stage panel covers 9 standardized product groups. The strongest retail coverage remains in Silpo, while Novus is useful mainly as a thinner cross-retailer robustness layer. ProZorro is treated as an institutional procurement layer and is locally interpolated only across short gaps to avoid inventing long contract windows.

The retail-preparation block now works at item level before product-level aggregation. Silpo and Novus rows are harmonized with normalized brand names, canonical item names, standardized dairy product types, fat percentage, and pack-size fields. This produced 200 unique harmonized item keys observed in both shops, against 1229 Silpo-only keys and 947 Novus-only keys. Effective price keeps the discount inside the price, while discount amount, discount-type dummies, and markdown depth remain as separate covariates.

![Panel coverage](../figures/01_panel_coverage.png)

![Cross-shop match status](../figures/06_cross_shop_match_status.png)

## Model Design
The first model block uses local projections. For each admissible product and chain link, the cumulative change in the downstream log price over horizons 0, 1, 3, 7, 14, and 21 days is regressed on the current upstream log shock with HAC inference. A parallel asymmetric version separates positive and negative upstream shocks. This is intentionally different from the thesis draft's ECM/NARDL core and therefore functions as a robustness redesign rather than a simple rerun.

The second model block estimates vertical spread equations. The dependent variable is the change in the log spread between downstream and upstream stages; regressors include the lagged spread, positive and negative upstream shocks, and retail discount measures where they vary. This is a market-power proxy, not a direct structural proof of conduct: persistent or asymmetric spreads and discount-responsive retail margins are interpreted as evidence consistent with timing control and category management.

A new consumer-linked endpoint is also added. `Retail+Consumer` combines the harmonized merged-shop retail layer with ConsumerUA, so the rerun can test whether conclusions survive once the retailer-facing endpoint is blended with the official consumer-price environment instead of using retail-only prices alone.

## Main Local-Projection Results
The local-projection block estimated 3570 linear pass-through equations, of which 728 met the p<0.10 and overlap screen (20.4%). The strongest thesis-relevant 7/14-day signals, excluding the mechanically smooth reconstructed FarmGateUA-ProducerUA diagnostic, are: ProZorro -> Silpo (silpo_baseline, h=7): core share 42.9%, median coefficient -0.025; FarmGateUA -> Retail+Consumer (retail_consumer_observed, h=7): core share 41.7%, median coefficient -3.610; ProducerUA -> ProZorro (procurement_price, h=7): core share 40.0%, median coefficient 1.497; FarmGateUA -> Retail (retail_observed, h=7): core share 38.9%, median coefficient -2.996; Retail -> FarmGateUA (retail_observed, h=14): core share 38.9%, median coefficient 0.000.

The FarmGateUA -> ProducerUA and ProducerUA -> FarmGateUA local-projection rows are retained in the workbook, but they should not be promoted as headline causal evidence. Both sides are reconstructed over a long common daily horizon, so high fit can reflect shared smoothing and benchmark coherence rather than a clean product-level farm-to-processor response. This is consistent with the corrected-format draft's conservative farm-gate interpretation.

![Local-projection pass-through](../figures/02_lp_pass_through_horizons.png)

![Forward versus reverse evidence](../figures/03_forward_reverse_core_share.png)

## Market-Power And Discount Results
The spread model produced 280 usable margin equations. Persistent-margin flags appear in 24 rows and asymmetric-margin flags appear in 223 rows. These flags should be read as market-power proxies: they indicate where spreads do not quickly mean-revert or where upstream increases and decreases affect margins differently.

The discount model produced 4 usable product equations, with 2 discount-strategy signals. In this data structure, the discount result is strongest as a retail-pricing mechanism rather than as a farm-gate mechanism: discount variables are directly observed only for Silpo, while ProducerUA, ProZorro, and FarmGateUA do not contain comparable markdown variables.

![Vertical spread proxy](../figures/04_vertical_spread_proxy.png)

![Discount incidence](../figures/05_discount_incidence.png)

## Thesis Interpretation
The second-stage run supports a cautious but coherent interpretation. Vertical coordination remains visible, but it is not a single cost-plus coefficient. The local-projection redesign shows that short-horizon evidence is selective and product-dependent, while the spread regressions show where timing control, discount smoothing, and asymmetric margin behavior are plausible. This strengthens the thesis argument that downstream market power is better described as control over timing, visibility, and discount-mediated adjustment than as one static markup wedge.

Farm-gate results should still be written conservatively. The farm-gate benchmark is economically necessary as the raw-milk origin of the chain, but it is much smoother and less product-specific than the retail and procurement data. The second-stage results therefore use FarmGateUA as an upstream benchmark and robustness dimension, not as a literal product-level farm-to-shelf elasticity for every dairy category.

## Output Files
- `outputs/second_stage_model_outputs.xlsx` contains all model tables.
- `data/second_stage_daily_panel.csv` contains the cleaned daily panel used by the models.
- `data/retail_items_full_harmonized.csv` contains the full harmonized Silpo-Novus item list.
- `data/retail_match_audit.csv` contains the cross-shop item-match audit.
- `data/consumerua_clean_daily.csv` contains the cleaned ConsumerUA daily layer used in the consumer-linked rerun.
- `outputs/local_projection_coefficients.csv`, `outputs/margin_market_power_models.csv`, and `outputs/discount_strategy_models.csv` contain the main machine-readable estimates.