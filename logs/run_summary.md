# FINAL_RESEARCH Run Summary

## Execution order
- Load corrected full_uah_final.xlsx.
- Run product-definition audit across government, procurement, and retail sources.
- Build corrected daily panel with retail combined, Silpo, and Novus downstream variants.
- Construct weekly median panels and controlled smoothing variants.
- Score intersections and admissibility before core estimation.
- Run the first strict weekly model pass.
- Activate post-test adaptation where strict weekly links remain too thin, keeping adapted evidence labelled separately.
- Estimate weekly ARDL, ECM, NARDL, and VECM system models.
- Estimate daily local projections, margin models, discount models, and procurement-scale models.
- Generate figures, workbooks, and thesis-style Chapter 5-6 outputs.
- Save separate compact results, diagnostics, and notes for individual retained models.

## Key counts
- Product dictionary rows: 28
- Strong intersections: 1
- Acceptable intersections: 4
- Weak-extension intersections: 10
- Reliable core models: 30
- Conditionally usable core models: 21
- Feasible VECM systems: 3
- Discount strategy signals: 2
- Procurement-scale signals: 5

## Retained weekly model families
- NARDL: 30
- ECM: 21
- ARDL was screened in the weekly pass but no ARDL row met the retained reporting standard on corrected data.

## Strongest lag signal
- Sour cream | FarmGate -> Producer | corr 0.932 | lag 0 weeks