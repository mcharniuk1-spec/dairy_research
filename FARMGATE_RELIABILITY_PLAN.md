# Farm-Gate And Extreme-Points Reliability Plan

## Goal

Strengthen the reliability of:

- `FarmGateUA -> ProducerUA`
- `FarmGateUA -> ProZorro`
- `FarmGateUA -> Retail`
- reverse links from `Retail` to upstream stages

The target is not to maximize the number of estimated coefficients. The target is to identify which farm-gate and downstream extreme-point effects are mathematically stable, economically interpretable, and robust across reconstruction choices.

## Why This Is Needed

Current RW4 outputs show that direct farm-gate effects are estimated, but they are variant-sensitive.

- `FarmGateUA -> ProducerUA` has broad coverage but no current core findings.
- `FarmGateUA -> ProZorro` has some core findings, but the signal is concentrated in a narrow subset of specifications.
- `FarmGateUA -> Retail` also has core findings, mainly in selected `ECM` and `NARDL` cases.
- Reverse links from `Retail` to `ProZorro` and `ProducerUA` are materially stronger than the direct farm-gate block, which suggests that downstream information and category management matter more than the current direct raw-milk proxy can capture.

This means the next iteration should be a structured reliability program.

## Main Improvement Axes

### 1. Compare all farm-gate source variants directly

Run the extreme-point chain separately for:

- `farm_gate_daily.xlsx`
- `farm_gate_all_missing_filled_daily.xlsx`

For each source, estimate:

- direct links to `ProducerUA`
- direct links to `ProZorro`
- direct links to `Retail`
- reverse links back to `FarmGateUA`

Required output:

- one comparison table with coefficient stability, `ECT`, `ECT p-value`, diagnostics, and core-finding flags by farm-gate source
- one summary chart that shows which source generates the most stable direct and reverse links

### 2. Compare interpolation methods systematically

Every direct and reverse farm-gate panel should be run under both:

- `linear`
- `pchip`

Required checks:

- coefficient sign stability
- `ECT` sign stability
- core-finding stability
- overlap loss from each interpolation method

Required output:

- one interpolation-robustness table for each stage pair
- one aggregate “stable in both interpolations / stable only in one / unstable in both” summary

### 3. Compare full and not-full farm-gate datasets

The no-empty and gap-filled farm-gate variants should be treated as distinct empirical environments, not just preprocessing options.

Key question:

- does filling missing farm-gate data improve identification, or does it create smoother but less credible direct pass-through?

Required checks:

- compare `n_obs`
- compare integration-classification outcomes
- compare bounds/cointegration evidence
- compare core-finding share

### 4. Build a unified retail price layer

Create a unified retail downstream target using:

- `Silpo`
- `Novus`
- `ConsumerUA`

This should be built in at least three forms:

- simple pooled category average
- overlap-weighted average
- variance-weighted or coverage-weighted unified retail index

Purpose:

- test whether direct `FarmGateUA -> Retail` becomes more stable when the downstream target is a unified consumer-facing price environment rather than a single retailer panel
- test whether reverse `Retail -> upstream` effects remain strong after downstream aggregation

Required outputs:

- methodology note for the unified retail index
- comparison workbook for retailer-specific vs unified-retail results
- explicit diagnostics on whether aggregation improves or weakens cointegration and adjustment

### 5. Expand intersection-based estimation

Check all combinations of overlap/intersection rules:

- strict common overlap
- relaxed overlap with minimum coverage threshold
- brand-clean subset
- category-average subset
- retailer-specific subset
- pooled-retailer subset

Reason:

- the direct farm-gate effect is likely sensitive to overlap construction because the upstream series is much smoother than the downstream product panels

Required output:

- intersection matrix showing which overlap rule yields the most reliable direct and reverse results

### 6. Re-estimate all direct and reverse links with a stricter model ladder

For each candidate panel:

1. pretest integration and overlap
2. try `ARDL`
3. if admissible, estimate `ECM`
4. estimate `NARDL`
5. estimate `VECM` when multivariate structure is appropriate
6. keep `OLS-HAC` only as reduced-form stress test, not as primary evidence

Model interpretation rules:

- prioritize negative and significant `ECT`
- treat large short-run or long-run coefficients cautiously if diagnostics or overlap are weak
- do not elevate a direct effect unless it is stable across at least two construction variants

### 7. Add direct farm-gate reliability diagnostics to outputs

Add dedicated output sheets:

- `FarmGate_Direct_Summary`
- `FarmGate_Reverse_Summary`
- `FarmGate_Variant_Stability`
- `Unified_Retail_Comparison`
- `Intersection_Stability`

Add graphs:

- direct farm-gate effect heatmap by stage pair and variant
- `ECT` stability chart across variants
- direct-vs-reverse core-finding share chart
- unified-retail vs single-retailer comparison chart

## Concrete Coding Tasks

### Data layer

- formalize farm-gate source identifiers across all generated panels
- keep `initial` and `all_missing_filled` as first-class analysis dimensions
- keep interpolation method as a first-class dimension in all direct-link summaries
- implement unified-retail panel builder

### Model layer

- add a reusable farm-gate experiment runner for all source/interpolation/intersection combinations
- add stability scoring for coefficient sign, `ECT`, and core-finding consistency
- make direct and reverse extreme-point summaries part of `run_all_rw4` and `total_run`

### Reporting layer

- surface farm-gate direct-effect evidence explicitly in the consolidated workbook
- surface unified-retail evidence explicitly in `Total_Run.xlsx`
- add a thesis-ready table for the strongest direct farm-gate and reverse retail cases

## Success Criteria

The next model iteration is successful if it can show at least one of the following with clear robustness:

- a stable direct `FarmGateUA -> ProZorro` effect across multiple variants
- a stable direct `FarmGateUA -> Retail` effect using unified retail
- a stable reverse `Retail -> upstream` effect that survives aggregation and intersection changes
- a transparent explanation for why `FarmGateUA -> ProducerUA` remains weak even after the design improvements

## Recommended Execution Order

1. Implement unified retail panel construction.
2. Build a farm-gate experiment matrix over source x interpolation x overlap rule.
3. Re-run direct and reverse extreme-point models with the stricter model ladder.
4. Score robustness and write dedicated summary sheets.
5. Upgrade the thesis chapter only after the new stability evidence is available.
