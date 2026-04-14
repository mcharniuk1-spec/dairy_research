# Step-by-Step Results of FINAL_RESEARCH

This document consolidates the interpretable final outputs of the dairy price transmission project. Green highlights in the DOCX mark the most important retained or supportive results. Red highlights mark the most important non-significant or infeasible results in central parts of the thesis.

## Model reliability and diagnostic hierarchy

1. **Product-level weekly models | ECM**
Result: Product-level weekly models | ECM: rows 21, reliable 16, conditional 5.
**This block contributes retained evidence and can enter the final interpretation hierarchy.**

1. **Product-level weekly models | NARDL**
Result: Product-level weekly models | NARDL: rows 30, reliable 14, conditional 16.
**This block contributes retained evidence and can enter the final interpretation hierarchy.**

1. **Aggregate index models | ECM**
Result: Aggregate index models | ECM: rows 6, reliable 5, conditional 1.
**This block contributes retained evidence and can enter the final interpretation hierarchy.**

1. **Aggregate index models | NARDL**
Result: Aggregate index models | NARDL: rows 10, reliable 3, conditional 7.
**This block contributes retained evidence and can enter the final interpretation hierarchy.**

1. **Discount models | OLS-HAC**
Result: Discount models | OLS-HAC: rows 3, reliable 2, conditional 1.
**This block contributes retained evidence and can enter the final interpretation hierarchy.**

1. **Procurement-scale models | OLS-HAC**
Result: Procurement-scale models | OLS-HAC: rows 6, reliable 5, conditional 1.
**This block contributes retained evidence and can enter the final interpretation hierarchy.**

1. **Product-level VECM | VECM**
Result: Product-level VECM | VECM: rows 27, reliable 3, conditional 24.
**This block contributes retained evidence and can enter the final interpretation hierarchy.**

1. **Aggregate index VECM | VECM**
Result: Aggregate index VECM | VECM: rows 3, reliable 2, conditional 1.
**This block contributes retained evidence and can enter the final interpretation hierarchy.**

## Weekly pairwise transmission across the 21 directional links

1. **FarmGate -> Producer | ECM**
Result: FarmGate -> Producer: ECM, coef 1.481, ECT -0.039, reliability reliable.
**This link provides retained weekly evidence, but its economic weight depends on the overlap quality and the retained reliability label rather than on the coefficient alone.**

1. **Producer -> Procurement | NARDL**
Result: Producer -> Procurement: NARDL, coef 2.455, ECT -0.225, reliability reliable.
**This link provides retained weekly evidence, but its economic weight depends on the overlap quality and the retained reliability label rather than on the coefficient alone.**

1. **Procurement -> Retail (Novus) | None retained**
Result: Procurement -> Retail (Novus): no retained weekly coefficient; overlap weeks 9.
**The weekly overlap is too thin for a defensible retained equilibrium reading, so this link remains descriptive only.**

1. **Procurement -> Retail (Silpo) | None retained**
Result: Procurement -> Retail (Silpo): no retained weekly coefficient; overlap weeks 8.
**The weekly overlap is too thin for a defensible retained equilibrium reading, so this link remains descriptive only.**

1. **Procurement -> Retail combined | None retained**
Result: Procurement -> Retail combined: no retained weekly coefficient; overlap weeks 11.
**The weekly overlap is too thin for a defensible retained equilibrium reading, so this link remains descriptive only.**

1. **Producer -> Retail (Novus) | None retained**
Result: Producer -> Retail (Novus): no retained weekly coefficient; overlap weeks 9.
**The weekly overlap is too thin for a defensible retained equilibrium reading, so this link remains descriptive only.**

1. **Producer -> Retail (Silpo) | None retained**
Result: Producer -> Retail (Silpo): no retained weekly coefficient; overlap weeks 8.
**The weekly overlap is too thin for a defensible retained equilibrium reading, so this link remains descriptive only.**

1. **Producer -> Retail combined | None retained**
Result: Producer -> Retail combined: no retained weekly coefficient; overlap weeks 11.
**The weekly overlap is too thin for a defensible retained equilibrium reading, so this link remains descriptive only.**

1. **FarmGate -> Procurement | NARDL**
Result: FarmGate -> Procurement: NARDL, coef -5.536, ECT -1.722, reliability reliable.
**This link provides retained weekly evidence, but its economic weight depends on the overlap quality and the retained reliability label rather than on the coefficient alone.**

1. **FarmGate -> Retail (Novus) | None retained**
Result: FarmGate -> Retail (Novus): no retained weekly coefficient; overlap weeks 9.
**The weekly overlap is too thin for a defensible retained equilibrium reading, so this link remains descriptive only.**

1. **FarmGate -> Retail (Silpo) | None retained**
Result: FarmGate -> Retail (Silpo): no retained weekly coefficient; overlap weeks 8.
**The weekly overlap is too thin for a defensible retained equilibrium reading, so this link remains descriptive only.**

1. **FarmGate -> Retail combined | None retained**
Result: FarmGate -> Retail combined: no retained weekly coefficient; overlap weeks 11.
**The weekly overlap is too thin for a defensible retained equilibrium reading, so this link remains descriptive only.**

1. **Retail (Novus) -> Procurement | None retained**
Result: Retail (Novus) -> Procurement: no retained weekly coefficient; overlap weeks 9.
**The weekly overlap is too thin for a defensible retained equilibrium reading, so this link remains descriptive only.**

1. **Retail (Silpo) -> Procurement | None retained**
Result: Retail (Silpo) -> Procurement: no retained weekly coefficient; overlap weeks 8.
**The weekly overlap is too thin for a defensible retained equilibrium reading, so this link remains descriptive only.**

1. **Retail combined -> Procurement | None retained**
Result: Retail combined -> Procurement: no retained weekly coefficient; overlap weeks 11.
**The weekly overlap is too thin for a defensible retained equilibrium reading, so this link remains descriptive only.**

1. **Retail (Novus) -> Producer | None retained**
Result: Retail (Novus) -> Producer: no retained weekly coefficient; overlap weeks 9.
**The weekly overlap is too thin for a defensible retained equilibrium reading, so this link remains descriptive only.**

1. **Retail (Silpo) -> Producer | None retained**
Result: Retail (Silpo) -> Producer: no retained weekly coefficient; overlap weeks 8.
**The weekly overlap is too thin for a defensible retained equilibrium reading, so this link remains descriptive only.**

1. **Retail combined -> Producer | None retained**
Result: Retail combined -> Producer: no retained weekly coefficient; overlap weeks 11.
**The weekly overlap is too thin for a defensible retained equilibrium reading, so this link remains descriptive only.**

1. **Retail (Novus) -> FarmGate | None retained**
Result: Retail (Novus) -> FarmGate: no retained weekly coefficient; overlap weeks 9.
**The weekly overlap is too thin for a defensible retained equilibrium reading, so this link remains descriptive only.**

1. **Retail (Silpo) -> FarmGate | None retained**
Result: Retail (Silpo) -> FarmGate: no retained weekly coefficient; overlap weeks 8.
**The weekly overlap is too thin for a defensible retained equilibrium reading, so this link remains descriptive only.**

1. **Retail combined -> FarmGate | None retained**
Result: Retail combined -> FarmGate: no retained weekly coefficient; overlap weeks 11.
**The weekly overlap is too thin for a defensible retained equilibrium reading, so this link remains descriptive only.**

## Weekly retained core-chain model rows

1. **Butter | FarmGate -> Procurement | ECM | weekly_raw**
Result: Butter | FarmGate -> Procurement | ECM | weekly_raw: LR/SR coef 1.630, ECT -0.604, p <0.001, n 37.
**This weekly equation is reliable and the retained coefficient is strongly significant; it should be read as long-run evidence only if the diagnostics remain supportive.**

1. **Butter | FarmGate -> Procurement | NARDL | weekly_raw**
Result: Butter | FarmGate -> Procurement | NARDL | weekly_raw: LR/SR coef 3.579, ECT -0.760, p <0.001, n 37.
**This weekly equation is reliable and the retained coefficient is strongly significant; it should be read as long-run evidence only if the diagnostics remain supportive.**

1. **Butter | FarmGate -> Procurement | NARDL | weekly_smoothed**
Result: Butter | FarmGate -> Procurement | NARDL | weekly_smoothed: LR/SR coef 2.239, ECT -0.376, p <0.001, n 39.
**This weekly equation is reliable and the retained coefficient is strongly significant; it should be read as long-run evidence only if the diagnostics remain supportive.**

1. **Butter | FarmGate -> Producer | ECM | weekly_raw**
Result: Butter | FarmGate -> Producer | ECM | weekly_raw: LR/SR coef 1.481, ECT -0.046, p 0.002, n 208.
**This weekly equation is reliable and the retained coefficient is strongly significant; it should be read as long-run evidence only if the diagnostics remain supportive.**

1. **Butter | FarmGate -> Producer | ECM | weekly_smoothed**
Result: Butter | FarmGate -> Producer | ECM | weekly_smoothed: LR/SR coef 1.481, ECT -0.039, p 0.006, n 210.
**This weekly equation is reliable and the retained coefficient is strongly significant; it should be read as long-run evidence only if the diagnostics remain supportive.**

1. **Butter | FarmGate -> Producer | NARDL | weekly_raw**
Result: Butter | FarmGate -> Producer | NARDL | weekly_raw: LR/SR coef -1.170, ECT -0.057, p <0.001, n 210.
**This weekly equation is conditionally_usable and the retained coefficient is strongly significant; it should be read as long-run evidence only if the diagnostics remain supportive.**

1. **Butter | FarmGate -> Producer | NARDL | weekly_smoothed**
Result: Butter | FarmGate -> Producer | NARDL | weekly_smoothed: LR/SR coef -0.803, ECT -0.056, p <0.001, n 210.
**This weekly equation is conditionally_usable and the retained coefficient is strongly significant; it should be read as long-run evidence only if the diagnostics remain supportive.**

1. **Butter | Producer -> Procurement | NARDL | weekly_raw**
Result: Butter | Producer -> Procurement | NARDL | weekly_raw: LR/SR coef 0.222, ECT -0.793, p <0.001, n 37.
**This weekly equation is conditionally_usable and the retained coefficient is strongly significant; it should be read as long-run evidence only if the diagnostics remain supportive.**

1. **Butter | Producer -> Procurement | NARDL | weekly_smoothed**
Result: Butter | Producer -> Procurement | NARDL | weekly_smoothed: LR/SR coef 2.455, ECT -0.225, p 0.089, n 39.
**This weekly equation is reliable and the retained coefficient is marginally significant; it should be read as long-run evidence only if the diagnostics remain supportive.**

1. **CHEESE | FarmGate -> Procurement | ECM | weekly_raw**
Result: CHEESE | FarmGate -> Procurement | ECM | weekly_raw: LR/SR coef 1.894, ECT -1.497, p <0.001, n 36.
**This weekly equation is reliable and the retained coefficient is strongly significant; it should be read as long-run evidence only if the diagnostics remain supportive.**

1. **CHEESE | FarmGate -> Procurement | ECM | weekly_smoothed**
Result: CHEESE | FarmGate -> Procurement | ECM | weekly_smoothed: LR/SR coef 1.880, ECT -0.832, p <0.001, n 39.
**This weekly equation is reliable and the retained coefficient is strongly significant; it should be read as long-run evidence only if the diagnostics remain supportive.**

1. **CHEESE | FarmGate -> Procurement | NARDL | weekly_raw**
Result: CHEESE | FarmGate -> Procurement | NARDL | weekly_raw: LR/SR coef 4.078, ECT -1.346, p <0.001, n 37.
**This weekly equation is reliable and the retained coefficient is strongly significant; it should be read as long-run evidence only if the diagnostics remain supportive.**

1. **CHEESE | FarmGate -> Procurement | NARDL | weekly_smoothed**
Result: CHEESE | FarmGate -> Procurement | NARDL | weekly_smoothed: LR/SR coef 2.438, ECT -0.917, p <0.001, n 39.
**This weekly equation is reliable and the retained coefficient is strongly significant; it should be read as long-run evidence only if the diagnostics remain supportive.**

1. **CHEESE | FarmGate -> Producer | ECM | weekly_raw**
Result: CHEESE | FarmGate -> Producer | ECM | weekly_raw: LR/SR coef 0.766, ECT -0.064, p <0.001, n 210.
**This weekly equation is reliable and the retained coefficient is strongly significant; it should be read as long-run evidence only if the diagnostics remain supportive.**

1. **CHEESE | FarmGate -> Producer | ECM | weekly_smoothed**
Result: CHEESE | FarmGate -> Producer | ECM | weekly_smoothed: LR/SR coef 0.768, ECT -0.060, p <0.001, n 210.
**This weekly equation is reliable and the retained coefficient is strongly significant; it should be read as long-run evidence only if the diagnostics remain supportive.**

1. **CHEESE | FarmGate -> Producer | NARDL | weekly_raw**
Result: CHEESE | FarmGate -> Producer | NARDL | weekly_raw: LR/SR coef 0.234, ECT -0.063, p <0.001, n 210.
**This weekly equation is conditionally_usable and the retained coefficient is strongly significant; it should be read as long-run evidence only if the diagnostics remain supportive.**

1. **CHEESE | FarmGate -> Producer | NARDL | weekly_smoothed**
Result: CHEESE | FarmGate -> Producer | NARDL | weekly_smoothed: LR/SR coef 0.370, ECT -0.059, p <0.001, n 210.
**This weekly equation is conditionally_usable and the retained coefficient is strongly significant; it should be read as long-run evidence only if the diagnostics remain supportive.**

1. **CHEESE | Producer -> Procurement | ECM | weekly_smoothed**
Result: CHEESE | Producer -> Procurement | ECM | weekly_smoothed: LR/SR coef 0.380, ECT -0.454, p 0.003, n 39.
**This weekly equation is reliable and the retained coefficient is strongly significant; it should be read as long-run evidence only if the diagnostics remain supportive.**

1. **CHEESE | Producer -> Procurement | NARDL | weekly_raw**
Result: CHEESE | Producer -> Procurement | NARDL | weekly_raw: LR/SR coef 0.916, ECT -1.359, p <0.001, n 37.
**This weekly equation is reliable and the retained coefficient is strongly significant; it should be read as long-run evidence only if the diagnostics remain supportive.**

1. **CHEESE | Producer -> Procurement | NARDL | weekly_smoothed**
Result: CHEESE | Producer -> Procurement | NARDL | weekly_smoothed: LR/SR coef 1.102, ECT -0.964, p <0.001, n 39.
**This weekly equation is reliable and the retained coefficient is strongly significant; it should be read as long-run evidence only if the diagnostics remain supportive.**

1. **Condensed milk | FarmGate -> Procurement | ECM | weekly_smoothed**
Result: Condensed milk | FarmGate -> Procurement | ECM | weekly_smoothed: LR/SR coef -0.512, ECT -0.720, p <0.001, n 38.
**This weekly equation is reliable and the retained coefficient is strongly significant; it should be read as long-run evidence only if the diagnostics remain supportive.**

1. **Condensed milk | FarmGate -> Procurement | NARDL | weekly_raw**
Result: Condensed milk | FarmGate -> Procurement | NARDL | weekly_raw: LR/SR coef -5.536, ECT -1.722, p <0.001, n 34.
**This weekly equation is reliable and the retained coefficient is strongly significant; it should be read as long-run evidence only if the diagnostics remain supportive.**

1. **Condensed milk | FarmGate -> Procurement | NARDL | weekly_smoothed**
Result: Condensed milk | FarmGate -> Procurement | NARDL | weekly_smoothed: LR/SR coef -5.029, ECT -0.646, p <0.001, n 39.
**This weekly equation is reliable and the retained coefficient is strongly significant; it should be read as long-run evidence only if the diagnostics remain supportive.**

1. **Cream | FarmGate -> Procurement | NARDL | weekly_raw**
Result: Cream | FarmGate -> Procurement | NARDL | weekly_raw: LR/SR coef 3.723, ECT -1.376, p <0.001, n 37.
**This weekly equation is reliable and the retained coefficient is strongly significant; it should be read as long-run evidence only if the diagnostics remain supportive.**

1. **Cream | FarmGate -> Procurement | NARDL | weekly_smoothed**
Result: Cream | FarmGate -> Procurement | NARDL | weekly_smoothed: LR/SR coef 1.534, ECT -0.316, p 0.003, n 39.
**This weekly equation is conditionally_usable and the retained coefficient is strongly significant; it should be read as long-run evidence only if the diagnostics remain supportive.**

1. **Drinking milk / fermented milk | FarmGate -> Procurement | ECM | weekly_raw**
Result: Drinking milk / fermented milk | FarmGate -> Procurement | ECM | weekly_raw: LR/SR coef 0.050, ECT -0.618, p 0.009, n 36.
**This weekly equation is reliable and the retained coefficient is strongly significant; it should be read as long-run evidence only if the diagnostics remain supportive.**

1. **Drinking milk / fermented milk | FarmGate -> Procurement | ECM | weekly_smoothed**
Result: Drinking milk / fermented milk | FarmGate -> Procurement | ECM | weekly_smoothed: LR/SR coef 0.029, ECT -0.508, p 0.009, n 39.
**This weekly equation is reliable and the retained coefficient is strongly significant; it should be read as long-run evidence only if the diagnostics remain supportive.**

1. **Drinking milk / fermented milk | FarmGate -> Procurement | NARDL | weekly_raw**
Result: Drinking milk / fermented milk | FarmGate -> Procurement | NARDL | weekly_raw: LR/SR coef 1.036, ECT -1.156, p <0.001, n 37.
**This weekly equation is reliable and the retained coefficient is strongly significant; it should be read as long-run evidence only if the diagnostics remain supportive.**

1. **Drinking milk / fermented milk | FarmGate -> Procurement | NARDL | weekly_smoothed**
Result: Drinking milk / fermented milk | FarmGate -> Procurement | NARDL | weekly_smoothed: LR/SR coef 0.959, ECT -0.475, p 0.001, n 39.
**This weekly equation is conditionally_usable and the retained coefficient is strongly significant; it should be read as long-run evidence only if the diagnostics remain supportive.**

1. **Drinking milk / fermented milk | FarmGate -> Producer | ECM | weekly_raw**
Result: Drinking milk / fermented milk | FarmGate -> Producer | ECM | weekly_raw: LR/SR coef 0.971, ECT -0.044, p <0.001, n 210.
**This weekly equation is conditionally_usable and the retained coefficient is strongly significant; it should be read as long-run evidence only if the diagnostics remain supportive.**

1. **Drinking milk / fermented milk | FarmGate -> Producer | ECM | weekly_smoothed**
Result: Drinking milk / fermented milk | FarmGate -> Producer | ECM | weekly_smoothed: LR/SR coef 0.973, ECT -0.040, p <0.001, n 210.
**This weekly equation is conditionally_usable and the retained coefficient is strongly significant; it should be read as long-run evidence only if the diagnostics remain supportive.**

1. **Drinking milk / fermented milk | FarmGate -> Producer | NARDL | weekly_raw**
Result: Drinking milk / fermented milk | FarmGate -> Producer | NARDL | weekly_raw: LR/SR coef 0.073, ECT -0.050, p <0.001, n 210.
**This weekly equation is conditionally_usable and the retained coefficient is strongly significant; it should be read as long-run evidence only if the diagnostics remain supportive.**

1. **Drinking milk / fermented milk | FarmGate -> Producer | NARDL | weekly_smoothed**
Result: Drinking milk / fermented milk | FarmGate -> Producer | NARDL | weekly_smoothed: LR/SR coef 0.028, ECT -0.045, p <0.001, n 210.
**This weekly equation is conditionally_usable and the retained coefficient is strongly significant; it should be read as long-run evidence only if the diagnostics remain supportive.**

1. **Drinking milk / fermented milk | Producer -> Procurement | ECM | weekly_raw**
Result: Drinking milk / fermented milk | Producer -> Procurement | ECM | weekly_raw: LR/SR coef 0.092, ECT -0.823, p <0.001, n 36.
**This weekly equation is reliable and the retained coefficient is strongly significant; it should be read as long-run evidence only if the diagnostics remain supportive.**

1. **Drinking milk / fermented milk | Producer -> Procurement | ECM | weekly_smoothed**
Result: Drinking milk / fermented milk | Producer -> Procurement | ECM | weekly_smoothed: LR/SR coef 0.082, ECT -0.438, p 0.003, n 39.
**This weekly equation is reliable and the retained coefficient is strongly significant; it should be read as long-run evidence only if the diagnostics remain supportive.**

1. **Drinking milk / fermented milk | Producer -> Procurement | NARDL | weekly_raw**
Result: Drinking milk / fermented milk | Producer -> Procurement | NARDL | weekly_raw: LR/SR coef 0.927, ECT -1.237, p <0.001, n 37.
**This weekly equation is reliable and the retained coefficient is strongly significant; it should be read as long-run evidence only if the diagnostics remain supportive.**

1. **Drinking milk / fermented milk | Producer -> Procurement | NARDL | weekly_smoothed**
Result: Drinking milk / fermented milk | Producer -> Procurement | NARDL | weekly_smoothed: LR/SR coef 1.016, ECT -0.541, p 0.002, n 39.
**This weekly equation is reliable and the retained coefficient is strongly significant; it should be read as long-run evidence only if the diagnostics remain supportive.**

1. **Milk powder | FarmGate -> Producer | ECM | weekly_raw**
Result: Milk powder | FarmGate -> Producer | ECM | weekly_raw: LR/SR coef 0.257, ECT -0.044, p <0.001, n 209.
**This weekly equation is conditionally_usable and the retained coefficient is strongly significant; it should be read as long-run evidence only if the diagnostics remain supportive.**

1. **Milk powder | FarmGate -> Producer | ECM | weekly_smoothed**
Result: Milk powder | FarmGate -> Producer | ECM | weekly_smoothed: LR/SR coef 0.257, ECT -0.039, p <0.001, n 208.
**This weekly equation is reliable and the retained coefficient is strongly significant; it should be read as long-run evidence only if the diagnostics remain supportive.**

1. **Milk powder | FarmGate -> Producer | NARDL | weekly_raw**
Result: Milk powder | FarmGate -> Producer | NARDL | weekly_raw: LR/SR coef 0.285, ECT -0.068, p <0.001, n 210.
**This weekly equation is conditionally_usable and the retained coefficient is strongly significant; it should be read as long-run evidence only if the diagnostics remain supportive.**

1. **Milk powder | FarmGate -> Producer | NARDL | weekly_smoothed**
Result: Milk powder | FarmGate -> Producer | NARDL | weekly_smoothed: LR/SR coef 0.120, ECT -0.065, p <0.001, n 210.
**This weekly equation is conditionally_usable and the retained coefficient is strongly significant; it should be read as long-run evidence only if the diagnostics remain supportive.**

1. **Sour cream | FarmGate -> Procurement | ECM | weekly_raw**
Result: Sour cream | FarmGate -> Procurement | ECM | weekly_raw: LR/SR coef 1.018, ECT -0.833, p <0.001, n 37.
**This weekly equation is reliable and the retained coefficient is strongly significant; it should be read as long-run evidence only if the diagnostics remain supportive.**

1. **Sour cream | FarmGate -> Procurement | NARDL | weekly_raw**
Result: Sour cream | FarmGate -> Procurement | NARDL | weekly_raw: LR/SR coef 4.823, ECT -0.769, p <0.001, n 37.
**This weekly equation is reliable and the retained coefficient is strongly significant; it should be read as long-run evidence only if the diagnostics remain supportive.**

1. **Sour cream | FarmGate -> Procurement | NARDL | weekly_smoothed**
Result: Sour cream | FarmGate -> Procurement | NARDL | weekly_smoothed: LR/SR coef 3.334, ECT -0.415, p <0.001, n 39.
**This weekly equation is conditionally_usable and the retained coefficient is strongly significant; it should be read as long-run evidence only if the diagnostics remain supportive.**

1. **Sour cream | FarmGate -> Producer | ECM | weekly_raw**
Result: Sour cream | FarmGate -> Producer | ECM | weekly_raw: LR/SR coef 1.081, ECT -0.058, p <0.001, n 210.
**This weekly equation is conditionally_usable and the retained coefficient is strongly significant; it should be read as long-run evidence only if the diagnostics remain supportive.**

1. **Sour cream | FarmGate -> Producer | ECM | weekly_smoothed**
Result: Sour cream | FarmGate -> Producer | ECM | weekly_smoothed: LR/SR coef 1.082, ECT -0.050, p <0.001, n 210.
**This weekly equation is conditionally_usable and the retained coefficient is strongly significant; it should be read as long-run evidence only if the diagnostics remain supportive.**

1. **Sour cream | FarmGate -> Producer | NARDL | weekly_raw**
Result: Sour cream | FarmGate -> Producer | NARDL | weekly_raw: LR/SR coef 0.299, ECT -0.071, p <0.001, n 210.
**This weekly equation is conditionally_usable and the retained coefficient is strongly significant; it should be read as long-run evidence only if the diagnostics remain supportive.**

1. **Sour cream | FarmGate -> Producer | NARDL | weekly_smoothed**
Result: Sour cream | FarmGate -> Producer | NARDL | weekly_smoothed: LR/SR coef 0.186, ECT -0.066, p <0.001, n 210.
**This weekly equation is conditionally_usable and the retained coefficient is strongly significant; it should be read as long-run evidence only if the diagnostics remain supportive.**

1. **Sour cream | Producer -> Procurement | ECM | weekly_raw**
Result: Sour cream | Producer -> Procurement | ECM | weekly_raw: LR/SR coef 0.635, ECT -0.598, p <0.001, n 37.
**This weekly equation is reliable and the retained coefficient is strongly significant; it should be read as long-run evidence only if the diagnostics remain supportive.**

1. **Sour cream | Producer -> Procurement | NARDL | weekly_raw**
Result: Sour cream | Producer -> Procurement | NARDL | weekly_raw: LR/SR coef 1.429, ECT -0.693, p <0.001, n 37.
**This weekly equation is conditionally_usable and the retained coefficient is strongly significant; it should be read as long-run evidence only if the diagnostics remain supportive.**

1. **Sour cream | Producer -> Procurement | NARDL | weekly_smoothed**
Result: Sour cream | Producer -> Procurement | NARDL | weekly_smoothed: LR/SR coef 0.784, ECT -0.294, p 0.006, n 39.
**This weekly equation is conditionally_usable and the retained coefficient is strongly significant; it should be read as long-run evidence only if the diagnostics remain supportive.**

## Daily local-projection results

1. **FarmGateUA -> ProZorro | procurement_price | Local projections**
Result: FarmGateUA -> ProZorro | horizon 0d | mean coef -2.078, median coef 0.179, sig share 0.143, core share 0.143, median n 268.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **FarmGateUA -> ProducerUA | processor_price | Local projections**
Result: FarmGateUA -> ProducerUA | horizon 0d | mean coef 0.929, median coef 0.949, sig share 1.000, core share 1.000, median n 1476.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **FarmGateUA -> Retail | retail_observed | Local projections**
Result: FarmGateUA -> Retail | horizon 0d | mean coef 9.843, median coef 4.084, sig share 0.167, core share 0.167, median n 60.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **FarmGateUA -> Retail optimal | retail_optimal_observed | Local projections**
Result: FarmGateUA -> Retail optimal | horizon 0d | mean coef 1.660, median coef 4.084, sig share 0.167, core share 0.167, median n 60.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **Novus -> ProZorro | novus_observed | Local projections**
Result: Novus -> ProZorro | horizon 0d | mean coef -0.988, median coef 0.002, sig share 0.250, core share 0.000, median n 42.
**This horizon shows some significant short-run movement, but the evidence is not strong enough to treat it as a stable core signal across products.**

1. **ProZorro -> Novus | novus_observed | Local projections**
Result: ProZorro -> Novus | horizon 0d | mean coef 0.015, median coef -0.003, sig share 0.250, core share 0.000, median n 42.
**This horizon shows some significant short-run movement, but the evidence is not strong enough to treat it as a stable core signal across products.**

1. **ProZorro -> ProducerUA | processor_price | Local projections**
Result: ProZorro -> ProducerUA | horizon 0d | mean coef 0.000, median coef -0.000, sig share 0.000, core share 0.000, median n 268.
**This horizon does not retain stable short-run evidence, which itself supports a delayed or weak transmission reading for this link.**

1. **ProZorro -> Retail | retail_baseline | Local projections**
Result: ProZorro -> Retail | horizon 0d | mean coef -0.061, median coef -0.043, sig share 0.000, core share 0.000, median n 62.
**This horizon does not retain stable short-run evidence, which itself supports a delayed or weak transmission reading for this link.**

1. **ProZorro -> Retail | retail_observed | Local projections**
Result: ProZorro -> Retail | horizon 0d | mean coef -0.068, median coef -0.039, sig share 0.000, core share 0.000, median n 62.
**This horizon does not retain stable short-run evidence, which itself supports a delayed or weak transmission reading for this link.**

1. **ProZorro -> Retail matched | retail_matched_baseline | Local projections**
Result: ProZorro -> Retail matched | horizon 0d | mean coef -0.210, median coef -0.037, sig share 0.167, core share 0.167, median n 54.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **ProZorro -> Retail matched | retail_matched_observed | Local projections**
Result: ProZorro -> Retail matched | horizon 0d | mean coef -0.205, median coef -0.036, sig share 0.167, core share 0.167, median n 54.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **ProZorro -> Retail optimal | retail_optimal_baseline | Local projections**
Result: ProZorro -> Retail optimal | horizon 0d | mean coef -0.061, median coef -0.043, sig share 0.000, core share 0.000, median n 62.
**This horizon does not retain stable short-run evidence, which itself supports a delayed or weak transmission reading for this link.**

1. **ProZorro -> Retail optimal | retail_optimal_observed | Local projections**
Result: ProZorro -> Retail optimal | horizon 0d | mean coef -0.068, median coef -0.039, sig share 0.000, core share 0.000, median n 62.
**This horizon does not retain stable short-run evidence, which itself supports a delayed or weak transmission reading for this link.**

1. **ProZorro -> Silpo | silpo_baseline | Local projections**
Result: ProZorro -> Silpo | horizon 0d | mean coef 0.005, median coef 0.007, sig share 0.000, core share 0.000, median n 47.
**This horizon does not retain stable short-run evidence, which itself supports a delayed or weak transmission reading for this link.**

1. **ProZorro -> Silpo | silpo_observed | Local projections**
Result: ProZorro -> Silpo | horizon 0d | mean coef 0.001, median coef 0.013, sig share 0.000, core share 0.000, median n 47.
**This horizon does not retain stable short-run evidence, which itself supports a delayed or weak transmission reading for this link.**

1. **ProducerUA -> FarmGateUA | processor_price | Local projections**
Result: ProducerUA -> FarmGateUA | horizon 0d | mean coef 0.646, median coef 0.626, sig share 1.000, core share 1.000, median n 1476.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **ProducerUA -> ProZorro | procurement_price | Local projections**
Result: ProducerUA -> ProZorro | horizon 0d | mean coef -2.325, median coef -0.343, sig share 0.100, core share 0.100, median n 268.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **Retail -> FarmGateUA | retail_observed | Local projections**
Result: Retail -> FarmGateUA | horizon 0d | mean coef 0.000, median coef 0.000, sig share 0.056, core share 0.056, median n 60.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **Retail -> ProZorro | retail_baseline | Local projections**
Result: Retail -> ProZorro | horizon 0d | mean coef -0.099, median coef -0.056, sig share 0.167, core share 0.167, median n 62.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **Retail -> ProZorro | retail_observed | Local projections**
Result: Retail -> ProZorro | horizon 0d | mean coef -0.054, median coef -0.064, sig share 0.167, core share 0.167, median n 62.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **Retail matched -> ProZorro | retail_matched_baseline | Local projections**
Result: Retail matched -> ProZorro | horizon 0d | mean coef -0.076, median coef -0.036, sig share 0.167, core share 0.167, median n 54.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **Retail matched -> ProZorro | retail_matched_observed | Local projections**
Result: Retail matched -> ProZorro | horizon 0d | mean coef -0.035, median coef -0.029, sig share 0.167, core share 0.167, median n 54.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **Retail optimal -> FarmGateUA | retail_optimal_observed | Local projections**
Result: Retail optimal -> FarmGateUA | horizon 0d | mean coef 0.000, median coef 0.000, sig share 0.056, core share 0.056, median n 60.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **Retail optimal -> ProZorro | retail_optimal_baseline | Local projections**
Result: Retail optimal -> ProZorro | horizon 0d | mean coef -0.099, median coef -0.056, sig share 0.167, core share 0.167, median n 62.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **Retail optimal -> ProZorro | retail_optimal_observed | Local projections**
Result: Retail optimal -> ProZorro | horizon 0d | mean coef -0.054, median coef -0.064, sig share 0.167, core share 0.167, median n 62.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **Silpo -> ProZorro | silpo_baseline | Local projections**
Result: Silpo -> ProZorro | horizon 0d | mean coef 0.038, median coef 0.106, sig share 0.000, core share 0.000, median n 47.
**This horizon does not retain stable short-run evidence, which itself supports a delayed or weak transmission reading for this link.**

1. **Silpo -> ProZorro | silpo_observed | Local projections**
Result: Silpo -> ProZorro | horizon 0d | mean coef -0.014, median coef 0.095, sig share 0.000, core share 0.000, median n 47.
**This horizon does not retain stable short-run evidence, which itself supports a delayed or weak transmission reading for this link.**

1. **FarmGateUA -> ProZorro | procurement_price | Local projections**
Result: FarmGateUA -> ProZorro | horizon 1d | mean coef 0.097, median coef 0.927, sig share 0.214, core share 0.214, median n 267.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **FarmGateUA -> ProducerUA | processor_price | Local projections**
Result: FarmGateUA -> ProducerUA | horizon 1d | mean coef 1.998, median coef 1.944, sig share 1.000, core share 1.000, median n 1475.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **FarmGateUA -> Retail | retail_observed | Local projections**
Result: FarmGateUA -> Retail | horizon 1d | mean coef 2.571, median coef 2.753, sig share 0.250, core share 0.250, median n 58.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **FarmGateUA -> Retail optimal | retail_optimal_observed | Local projections**
Result: FarmGateUA -> Retail optimal | horizon 1d | mean coef -20.787, median coef 2.753, sig share 0.361, core share 0.361, median n 58.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **Novus -> ProZorro | novus_observed | Local projections**
Result: Novus -> ProZorro | horizon 1d | mean coef -0.563, median coef -0.026, sig share 0.250, core share 0.000, median n 40.
**This horizon shows some significant short-run movement, but the evidence is not strong enough to treat it as a stable core signal across products.**

1. **ProZorro -> Novus | novus_observed | Local projections**
Result: ProZorro -> Novus | horizon 1d | mean coef 0.183, median coef 0.106, sig share 0.333, core share 0.333, median n 44.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **ProZorro -> ProducerUA | processor_price | Local projections**
Result: ProZorro -> ProducerUA | horizon 1d | mean coef 0.001, median coef -0.000, sig share 0.000, core share 0.000, median n 268.
**This horizon does not retain stable short-run evidence, which itself supports a delayed or weak transmission reading for this link.**

1. **ProZorro -> Retail | retail_baseline | Local projections**
Result: ProZorro -> Retail | horizon 1d | mean coef 0.044, median coef 0.027, sig share 0.167, core share 0.167, median n 60.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **ProZorro -> Retail | retail_observed | Local projections**
Result: ProZorro -> Retail | horizon 1d | mean coef 0.036, median coef 0.025, sig share 0.167, core share 0.167, median n 60.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **ProZorro -> Retail matched | retail_matched_baseline | Local projections**
Result: ProZorro -> Retail matched | horizon 1d | mean coef -0.178, median coef -0.002, sig share 0.167, core share 0.167, median n 51.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **ProZorro -> Retail matched | retail_matched_observed | Local projections**
Result: ProZorro -> Retail matched | horizon 1d | mean coef -0.200, median coef -0.023, sig share 0.167, core share 0.167, median n 51.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **ProZorro -> Retail optimal | retail_optimal_baseline | Local projections**
Result: ProZorro -> Retail optimal | horizon 1d | mean coef 0.044, median coef 0.027, sig share 0.167, core share 0.167, median n 60.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **ProZorro -> Retail optimal | retail_optimal_observed | Local projections**
Result: ProZorro -> Retail optimal | horizon 1d | mean coef 0.036, median coef 0.025, sig share 0.167, core share 0.167, median n 60.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **ProZorro -> Silpo | silpo_baseline | Local projections**
Result: ProZorro -> Silpo | horizon 1d | mean coef 0.011, median coef 0.027, sig share 0.000, core share 0.000, median n 45.
**This horizon does not retain stable short-run evidence, which itself supports a delayed or weak transmission reading for this link.**

1. **ProZorro -> Silpo | silpo_observed | Local projections**
Result: ProZorro -> Silpo | horizon 1d | mean coef -0.006, median coef 0.018, sig share 0.000, core share 0.000, median n 45.
**This horizon does not retain stable short-run evidence, which itself supports a delayed or weak transmission reading for this link.**

1. **ProducerUA -> FarmGateUA | processor_price | Local projections**
Result: ProducerUA -> FarmGateUA | horizon 1d | mean coef 1.394, median coef 1.293, sig share 1.000, core share 1.000, median n 1475.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **ProducerUA -> ProZorro | procurement_price | Local projections**
Result: ProducerUA -> ProZorro | horizon 1d | mean coef -3.375, median coef -2.558, sig share 0.200, core share 0.200, median n 267.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **Retail -> FarmGateUA | retail_observed | Local projections**
Result: Retail -> FarmGateUA | horizon 1d | mean coef 0.001, median coef 0.001, sig share 0.000, core share 0.000, median n 60.
**This horizon does not retain stable short-run evidence, which itself supports a delayed or weak transmission reading for this link.**

1. **Retail -> ProZorro | retail_baseline | Local projections**
Result: Retail -> ProZorro | horizon 1d | mean coef -0.031, median coef 0.008, sig share 0.000, core share 0.000, median n 62.
**This horizon does not retain stable short-run evidence, which itself supports a delayed or weak transmission reading for this link.**

1. **Retail -> ProZorro | retail_observed | Local projections**
Result: Retail -> ProZorro | horizon 1d | mean coef -0.044, median coef -0.023, sig share 0.000, core share 0.000, median n 62.
**This horizon does not retain stable short-run evidence, which itself supports a delayed or weak transmission reading for this link.**

1. **Retail matched -> ProZorro | retail_matched_baseline | Local projections**
Result: Retail matched -> ProZorro | horizon 1d | mean coef -0.123, median coef -0.076, sig share 0.167, core share 0.167, median n 54.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **Retail matched -> ProZorro | retail_matched_observed | Local projections**
Result: Retail matched -> ProZorro | horizon 1d | mean coef -0.100, median coef -0.093, sig share 0.167, core share 0.167, median n 54.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **Retail optimal -> FarmGateUA | retail_optimal_observed | Local projections**
Result: Retail optimal -> FarmGateUA | horizon 1d | mean coef 0.001, median coef 0.001, sig share 0.000, core share 0.000, median n 60.
**This horizon does not retain stable short-run evidence, which itself supports a delayed or weak transmission reading for this link.**

1. **Retail optimal -> ProZorro | retail_optimal_baseline | Local projections**
Result: Retail optimal -> ProZorro | horizon 1d | mean coef -0.031, median coef 0.008, sig share 0.000, core share 0.000, median n 62.
**This horizon does not retain stable short-run evidence, which itself supports a delayed or weak transmission reading for this link.**

1. **Retail optimal -> ProZorro | retail_optimal_observed | Local projections**
Result: Retail optimal -> ProZorro | horizon 1d | mean coef -0.044, median coef -0.023, sig share 0.000, core share 0.000, median n 62.
**This horizon does not retain stable short-run evidence, which itself supports a delayed or weak transmission reading for this link.**

1. **Silpo -> ProZorro | silpo_baseline | Local projections**
Result: Silpo -> ProZorro | horizon 1d | mean coef -0.080, median coef -0.050, sig share 0.000, core share 0.000, median n 47.
**This horizon does not retain stable short-run evidence, which itself supports a delayed or weak transmission reading for this link.**

1. **Silpo -> ProZorro | silpo_observed | Local projections**
Result: Silpo -> ProZorro | horizon 1d | mean coef -0.157, median coef -0.143, sig share 0.000, core share 0.000, median n 47.
**This horizon does not retain stable short-run evidence, which itself supports a delayed or weak transmission reading for this link.**

1. **FarmGateUA -> ProZorro | procurement_price | Local projections**
Result: FarmGateUA -> ProZorro | horizon 3d | mean coef 6.047, median coef 2.332, sig share 0.286, core share 0.286, median n 265.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **FarmGateUA -> ProducerUA | processor_price | Local projections**
Result: FarmGateUA -> ProducerUA | horizon 3d | mean coef 3.886, median coef 3.393, sig share 1.000, core share 1.000, median n 1473.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **FarmGateUA -> Retail | retail_observed | Local projections**
Result: FarmGateUA -> Retail | horizon 3d | mean coef 6.193, median coef 11.646, sig share 0.333, core share 0.333, median n 56.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **FarmGateUA -> Retail optimal | retail_optimal_observed | Local projections**
Result: FarmGateUA -> Retail optimal | horizon 3d | mean coef 5.976, median coef 8.002, sig share 0.333, core share 0.333, median n 56.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **Novus -> ProZorro | novus_observed | Local projections**
Result: Novus -> ProZorro | horizon 3d | mean coef 0.947, median coef -0.019, sig share 0.500, core share 0.250, median n 40.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **ProZorro -> Novus | novus_observed | Local projections**
Result: ProZorro -> Novus | horizon 3d | mean coef 0.377, median coef 0.403, sig share 0.333, core share 0.000, median n 42.
**This horizon shows some significant short-run movement, but the evidence is not strong enough to treat it as a stable core signal across products.**

1. **ProZorro -> ProducerUA | processor_price | Local projections**
Result: ProZorro -> ProducerUA | horizon 3d | mean coef 0.001, median coef -0.000, sig share 0.000, core share 0.000, median n 268.
**This horizon does not retain stable short-run evidence, which itself supports a delayed or weak transmission reading for this link.**

1. **ProZorro -> Retail | retail_baseline | Local projections**
Result: ProZorro -> Retail | horizon 3d | mean coef 0.161, median coef 0.122, sig share 0.167, core share 0.167, median n 58.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **ProZorro -> Retail | retail_observed | Local projections**
Result: ProZorro -> Retail | horizon 3d | mean coef 0.182, median coef 0.151, sig share 0.167, core share 0.167, median n 58.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **ProZorro -> Retail matched | retail_matched_baseline | Local projections**
Result: ProZorro -> Retail matched | horizon 3d | mean coef 0.101, median coef 0.057, sig share 0.167, core share 0.167, median n 48.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **ProZorro -> Retail matched | retail_matched_observed | Local projections**
Result: ProZorro -> Retail matched | horizon 3d | mean coef 0.148, median coef 0.084, sig share 0.000, core share 0.000, median n 48.
**This horizon does not retain stable short-run evidence, which itself supports a delayed or weak transmission reading for this link.**

1. **ProZorro -> Retail optimal | retail_optimal_baseline | Local projections**
Result: ProZorro -> Retail optimal | horizon 3d | mean coef 0.161, median coef 0.122, sig share 0.167, core share 0.167, median n 58.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **ProZorro -> Retail optimal | retail_optimal_observed | Local projections**
Result: ProZorro -> Retail optimal | horizon 3d | mean coef 0.182, median coef 0.151, sig share 0.167, core share 0.167, median n 58.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **ProZorro -> Silpo | silpo_baseline | Local projections**
Result: ProZorro -> Silpo | horizon 3d | mean coef -0.002, median coef -0.002, sig share 0.000, core share 0.000, median n 44.
**This horizon does not retain stable short-run evidence, which itself supports a delayed or weak transmission reading for this link.**

1. **ProZorro -> Silpo | silpo_observed | Local projections**
Result: ProZorro -> Silpo | horizon 3d | mean coef 0.029, median coef 0.022, sig share 0.000, core share 0.000, median n 44.
**This horizon does not retain stable short-run evidence, which itself supports a delayed or weak transmission reading for this link.**

1. **ProducerUA -> FarmGateUA | processor_price | Local projections**
Result: ProducerUA -> FarmGateUA | horizon 3d | mean coef 2.740, median coef 2.315, sig share 1.000, core share 1.000, median n 1473.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **ProducerUA -> ProZorro | procurement_price | Local projections**
Result: ProducerUA -> ProZorro | horizon 3d | mean coef 2.827, median coef 4.793, sig share 0.000, core share 0.000, median n 265.
**This horizon does not retain stable short-run evidence, which itself supports a delayed or weak transmission reading for this link.**

1. **Retail -> FarmGateUA | retail_observed | Local projections**
Result: Retail -> FarmGateUA | horizon 3d | mean coef 0.002, median coef 0.001, sig share 0.028, core share 0.028, median n 60.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **Retail -> ProZorro | retail_baseline | Local projections**
Result: Retail -> ProZorro | horizon 3d | mean coef -0.087, median coef 0.005, sig share 0.000, core share 0.000, median n 62.
**This horizon does not retain stable short-run evidence, which itself supports a delayed or weak transmission reading for this link.**

1. **Retail -> ProZorro | retail_observed | Local projections**
Result: Retail -> ProZorro | horizon 3d | mean coef -0.124, median coef -0.067, sig share 0.000, core share 0.000, median n 62.
**This horizon does not retain stable short-run evidence, which itself supports a delayed or weak transmission reading for this link.**

1. **Retail matched -> ProZorro | retail_matched_baseline | Local projections**
Result: Retail matched -> ProZorro | horizon 3d | mean coef 0.040, median coef 0.013, sig share 0.167, core share 0.167, median n 54.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **Retail matched -> ProZorro | retail_matched_observed | Local projections**
Result: Retail matched -> ProZorro | horizon 3d | mean coef 0.075, median coef 0.026, sig share 0.167, core share 0.167, median n 54.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **Retail optimal -> FarmGateUA | retail_optimal_observed | Local projections**
Result: Retail optimal -> FarmGateUA | horizon 3d | mean coef 0.002, median coef 0.001, sig share 0.028, core share 0.028, median n 60.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **Retail optimal -> ProZorro | retail_optimal_baseline | Local projections**
Result: Retail optimal -> ProZorro | horizon 3d | mean coef -0.087, median coef 0.005, sig share 0.000, core share 0.000, median n 62.
**This horizon does not retain stable short-run evidence, which itself supports a delayed or weak transmission reading for this link.**

1. **Retail optimal -> ProZorro | retail_optimal_observed | Local projections**
Result: Retail optimal -> ProZorro | horizon 3d | mean coef -0.124, median coef -0.067, sig share 0.000, core share 0.000, median n 62.
**This horizon does not retain stable short-run evidence, which itself supports a delayed or weak transmission reading for this link.**

1. **Silpo -> ProZorro | silpo_baseline | Local projections**
Result: Silpo -> ProZorro | horizon 3d | mean coef -0.115, median coef -0.075, sig share 0.000, core share 0.000, median n 47.
**This horizon does not retain stable short-run evidence, which itself supports a delayed or weak transmission reading for this link.**

1. **Silpo -> ProZorro | silpo_observed | Local projections**
Result: Silpo -> ProZorro | horizon 3d | mean coef -0.246, median coef -0.212, sig share 0.000, core share 0.000, median n 47.
**This horizon does not retain stable short-run evidence, which itself supports a delayed or weak transmission reading for this link.**

1. **FarmGateUA -> ProZorro | procurement_price | Local projections**
Result: FarmGateUA -> ProZorro | horizon 7d | mean coef 0.662, median coef -2.378, sig share 0.000, core share 0.000, median n 261.
**This horizon does not retain stable short-run evidence, which itself supports a delayed or weak transmission reading for this link.**

1. **FarmGateUA -> ProducerUA | processor_price | Local projections**
Result: FarmGateUA -> ProducerUA | horizon 7d | mean coef 5.181, median coef 4.643, sig share 1.000, core share 1.000, median n 1469.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **FarmGateUA -> Retail | retail_observed | Local projections**
Result: FarmGateUA -> Retail | horizon 7d | mean coef -7.937, median coef 0.746, sig share 0.361, core share 0.361, median n 55.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **FarmGateUA -> Retail optimal | retail_optimal_observed | Local projections**
Result: FarmGateUA -> Retail optimal | horizon 7d | mean coef -13.701, median coef 0.746, sig share 0.306, core share 0.306, median n 55.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **Novus -> ProZorro | novus_observed | Local projections**
Result: Novus -> ProZorro | horizon 7d | mean coef -0.515, median coef -0.018, sig share 0.000, core share 0.000, median n 40.
**This horizon does not retain stable short-run evidence, which itself supports a delayed or weak transmission reading for this link.**

1. **ProZorro -> Novus | novus_observed | Local projections**
Result: ProZorro -> Novus | horizon 7d | mean coef -0.370, median coef 0.008, sig share 0.333, core share 0.333, median n 42.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **ProZorro -> ProducerUA | processor_price | Local projections**
Result: ProZorro -> ProducerUA | horizon 7d | mean coef -0.010, median coef -0.002, sig share 0.000, core share 0.000, median n 268.
**This horizon does not retain stable short-run evidence, which itself supports a delayed or weak transmission reading for this link.**

1. **ProZorro -> Retail | retail_baseline | Local projections**
Result: ProZorro -> Retail | horizon 7d | mean coef -0.175, median coef -0.051, sig share 0.167, core share 0.167, median n 57.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **ProZorro -> Retail | retail_observed | Local projections**
Result: ProZorro -> Retail | horizon 7d | mean coef -0.188, median coef -0.063, sig share 0.167, core share 0.167, median n 57.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **ProZorro -> Retail matched | retail_matched_baseline | Local projections**
Result: ProZorro -> Retail matched | horizon 7d | mean coef -0.189, median coef -0.055, sig share 0.167, core share 0.167, median n 48.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **ProZorro -> Retail matched | retail_matched_observed | Local projections**
Result: ProZorro -> Retail matched | horizon 7d | mean coef -0.206, median coef -0.052, sig share 0.167, core share 0.167, median n 48.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **ProZorro -> Retail optimal | retail_optimal_baseline | Local projections**
Result: ProZorro -> Retail optimal | horizon 7d | mean coef -0.175, median coef -0.051, sig share 0.167, core share 0.167, median n 57.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **ProZorro -> Retail optimal | retail_optimal_observed | Local projections**
Result: ProZorro -> Retail optimal | horizon 7d | mean coef -0.188, median coef -0.063, sig share 0.167, core share 0.167, median n 57.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **ProZorro -> Silpo | silpo_baseline | Local projections**
Result: ProZorro -> Silpo | horizon 7d | mean coef -0.008, median coef -0.011, sig share 0.500, core share 0.500, median n 42.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **ProZorro -> Silpo | silpo_observed | Local projections**
Result: ProZorro -> Silpo | horizon 7d | mean coef -0.022, median coef -0.036, sig share 0.333, core share 0.333, median n 42.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **ProducerUA -> FarmGateUA | processor_price | Local projections**
Result: ProducerUA -> FarmGateUA | horizon 7d | mean coef 3.744, median coef 3.238, sig share 1.000, core share 1.000, median n 1469.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **ProducerUA -> ProZorro | procurement_price | Local projections**
Result: ProducerUA -> ProZorro | horizon 7d | mean coef 0.582, median coef 1.618, sig share 0.200, core share 0.200, median n 261.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **Retail -> FarmGateUA | retail_observed | Local projections**
Result: Retail -> FarmGateUA | horizon 7d | mean coef 0.005, median coef 0.003, sig share 0.111, core share 0.111, median n 60.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **Retail -> ProZorro | retail_baseline | Local projections**
Result: Retail -> ProZorro | horizon 7d | mean coef -0.143, median coef -0.033, sig share 0.167, core share 0.167, median n 62.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **Retail -> ProZorro | retail_observed | Local projections**
Result: Retail -> ProZorro | horizon 7d | mean coef -0.104, median coef -0.035, sig share 0.167, core share 0.167, median n 62.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **Retail matched -> ProZorro | retail_matched_baseline | Local projections**
Result: Retail matched -> ProZorro | horizon 7d | mean coef -0.058, median coef -0.059, sig share 0.000, core share 0.000, median n 54.
**This horizon does not retain stable short-run evidence, which itself supports a delayed or weak transmission reading for this link.**

1. **Retail matched -> ProZorro | retail_matched_observed | Local projections**
Result: Retail matched -> ProZorro | horizon 7d | mean coef -0.014, median coef -0.000, sig share 0.167, core share 0.167, median n 54.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **Retail optimal -> FarmGateUA | retail_optimal_observed | Local projections**
Result: Retail optimal -> FarmGateUA | horizon 7d | mean coef 0.005, median coef 0.003, sig share 0.111, core share 0.111, median n 60.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **Retail optimal -> ProZorro | retail_optimal_baseline | Local projections**
Result: Retail optimal -> ProZorro | horizon 7d | mean coef -0.143, median coef -0.033, sig share 0.167, core share 0.167, median n 62.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **Retail optimal -> ProZorro | retail_optimal_observed | Local projections**
Result: Retail optimal -> ProZorro | horizon 7d | mean coef -0.104, median coef -0.035, sig share 0.167, core share 0.167, median n 62.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **Silpo -> ProZorro | silpo_baseline | Local projections**
Result: Silpo -> ProZorro | horizon 7d | mean coef -0.174, median coef -0.144, sig share 0.167, core share 0.167, median n 47.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **Silpo -> ProZorro | silpo_observed | Local projections**
Result: Silpo -> ProZorro | horizon 7d | mean coef -0.117, median coef -0.152, sig share 0.167, core share 0.167, median n 47.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **FarmGateUA -> ProZorro | procurement_price | Local projections**
Result: FarmGateUA -> ProZorro | horizon 14d | mean coef -16.945, median coef -2.707, sig share 0.357, core share 0.286, median n 254.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **FarmGateUA -> ProducerUA | processor_price | Local projections**
Result: FarmGateUA -> ProducerUA | horizon 14d | mean coef 5.148, median coef 4.776, sig share 1.000, core share 1.000, median n 1462.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **FarmGateUA -> Retail | retail_observed | Local projections**
Result: FarmGateUA -> Retail | horizon 14d | mean coef -19.211, median coef -11.836, sig share 0.250, core share 0.250, median n 49.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **FarmGateUA -> Retail optimal | retail_optimal_observed | Local projections**
Result: FarmGateUA -> Retail optimal | horizon 14d | mean coef -17.936, median coef -11.836, sig share 0.250, core share 0.250, median n 49.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **Novus -> ProZorro | novus_observed | Local projections**
Result: Novus -> ProZorro | horizon 14d | mean coef -0.079, median coef -0.070, sig share 0.250, core share 0.250, median n 38.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **ProZorro -> Novus | novus_observed | Local projections**
Result: ProZorro -> Novus | horizon 14d | mean coef 0.120, median coef 0.308, sig share 0.333, core share 0.000, median n 35.
**This horizon shows some significant short-run movement, but the evidence is not strong enough to treat it as a stable core signal across products.**

1. **ProZorro -> ProducerUA | processor_price | Local projections**
Result: ProZorro -> ProducerUA | horizon 14d | mean coef -0.054, median coef -0.002, sig share 0.000, core share 0.000, median n 261.
**This horizon does not retain stable short-run evidence, which itself supports a delayed or weak transmission reading for this link.**

1. **ProZorro -> Retail | retail_baseline | Local projections**
Result: ProZorro -> Retail | horizon 14d | mean coef -0.030, median coef 0.035, sig share 0.000, core share 0.000, median n 50.
**This horizon does not retain stable short-run evidence, which itself supports a delayed or weak transmission reading for this link.**

1. **ProZorro -> Retail | retail_observed | Local projections**
Result: ProZorro -> Retail | horizon 14d | mean coef -0.003, median coef 0.044, sig share 0.000, core share 0.000, median n 50.
**This horizon does not retain stable short-run evidence, which itself supports a delayed or weak transmission reading for this link.**

1. **ProZorro -> Retail matched | retail_matched_baseline | Local projections**
Result: ProZorro -> Retail matched | horizon 14d | mean coef -0.051, median coef 0.001, sig share 0.000, core share 0.000, median n 44.
**This horizon does not retain stable short-run evidence, which itself supports a delayed or weak transmission reading for this link.**

1. **ProZorro -> Retail matched | retail_matched_observed | Local projections**
Result: ProZorro -> Retail matched | horizon 14d | mean coef -0.038, median coef 0.008, sig share 0.167, core share 0.167, median n 44.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **ProZorro -> Retail optimal | retail_optimal_baseline | Local projections**
Result: ProZorro -> Retail optimal | horizon 14d | mean coef -0.030, median coef 0.035, sig share 0.000, core share 0.000, median n 50.
**This horizon does not retain stable short-run evidence, which itself supports a delayed or weak transmission reading for this link.**

1. **ProZorro -> Retail optimal | retail_optimal_observed | Local projections**
Result: ProZorro -> Retail optimal | horizon 14d | mean coef -0.003, median coef 0.044, sig share 0.000, core share 0.000, median n 50.
**This horizon does not retain stable short-run evidence, which itself supports a delayed or weak transmission reading for this link.**

1. **ProZorro -> Silpo | silpo_baseline | Local projections**
Result: ProZorro -> Silpo | horizon 14d | mean coef -0.023, median coef -0.014, sig share 0.167, core share 0.167, median n 35.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **ProZorro -> Silpo | silpo_observed | Local projections**
Result: ProZorro -> Silpo | horizon 14d | mean coef -0.001, median coef -0.013, sig share 0.167, core share 0.167, median n 35.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **ProducerUA -> FarmGateUA | processor_price | Local projections**
Result: ProducerUA -> FarmGateUA | horizon 14d | mean coef 3.806, median coef 3.373, sig share 1.000, core share 1.000, median n 1462.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **ProducerUA -> ProZorro | procurement_price | Local projections**
Result: ProducerUA -> ProZorro | horizon 14d | mean coef 4.616, median coef -3.202, sig share 0.200, core share 0.200, median n 254.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **Retail -> FarmGateUA | retail_observed | Local projections**
Result: Retail -> FarmGateUA | horizon 14d | mean coef 0.005, median coef 0.004, sig share 0.222, core share 0.222, median n 60.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **Retail -> ProZorro | retail_baseline | Local projections**
Result: Retail -> ProZorro | horizon 14d | mean coef 0.087, median coef 0.110, sig share 0.167, core share 0.167, median n 60.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **Retail -> ProZorro | retail_observed | Local projections**
Result: Retail -> ProZorro | horizon 14d | mean coef -0.007, median coef 0.034, sig share 0.167, core share 0.167, median n 60.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **Retail matched -> ProZorro | retail_matched_baseline | Local projections**
Result: Retail matched -> ProZorro | horizon 14d | mean coef 0.063, median coef 0.037, sig share 0.000, core share 0.000, median n 52.
**This horizon does not retain stable short-run evidence, which itself supports a delayed or weak transmission reading for this link.**

1. **Retail matched -> ProZorro | retail_matched_observed | Local projections**
Result: Retail matched -> ProZorro | horizon 14d | mean coef 0.080, median coef 0.062, sig share 0.000, core share 0.000, median n 52.
**This horizon does not retain stable short-run evidence, which itself supports a delayed or weak transmission reading for this link.**

1. **Retail optimal -> FarmGateUA | retail_optimal_observed | Local projections**
Result: Retail optimal -> FarmGateUA | horizon 14d | mean coef 0.005, median coef 0.003, sig share 0.222, core share 0.222, median n 60.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **Retail optimal -> ProZorro | retail_optimal_baseline | Local projections**
Result: Retail optimal -> ProZorro | horizon 14d | mean coef 0.087, median coef 0.110, sig share 0.167, core share 0.167, median n 60.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **Retail optimal -> ProZorro | retail_optimal_observed | Local projections**
Result: Retail optimal -> ProZorro | horizon 14d | mean coef -0.007, median coef 0.034, sig share 0.167, core share 0.167, median n 60.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **Silpo -> ProZorro | silpo_baseline | Local projections**
Result: Silpo -> ProZorro | horizon 14d | mean coef -0.078, median coef -0.054, sig share 0.000, core share 0.000, median n 47.
**This horizon does not retain stable short-run evidence, which itself supports a delayed or weak transmission reading for this link.**

1. **Silpo -> ProZorro | silpo_observed | Local projections**
Result: Silpo -> ProZorro | horizon 14d | mean coef -0.054, median coef -0.080, sig share 0.167, core share 0.167, median n 47.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **FarmGateUA -> ProZorro | procurement_price | Local projections**
Result: FarmGateUA -> ProZorro | horizon 21d | mean coef 4.522, median coef 4.418, sig share 0.167, core share 0.167, median n 247.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **FarmGateUA -> ProducerUA | processor_price | Local projections**
Result: FarmGateUA -> ProducerUA | horizon 21d | mean coef 4.699, median coef 4.212, sig share 1.000, core share 1.000, median n 1455.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **FarmGateUA -> Retail | retail_observed | Local projections**
Result: FarmGateUA -> Retail | horizon 21d | mean coef -48.188, median coef -20.049, sig share 0.111, core share 0.000, median n 45.
**This horizon shows some significant short-run movement, but the evidence is not strong enough to treat it as a stable core signal across products.**

1. **FarmGateUA -> Retail optimal | retail_optimal_observed | Local projections**
Result: FarmGateUA -> Retail optimal | horizon 21d | mean coef -86.631, median coef -20.049, sig share 0.111, core share 0.000, median n 45.
**This horizon shows some significant short-run movement, but the evidence is not strong enough to treat it as a stable core signal across products.**

1. **Novus -> ProZorro | novus_observed | Local projections**
Result: Novus -> ProZorro | horizon 21d | mean coef -0.062, median coef -0.039, sig share 0.000, core share 0.000, median n 37.
**This horizon does not retain stable short-run evidence, which itself supports a delayed or weak transmission reading for this link.**

1. **ProZorro -> Novus | novus_observed | Local projections**
Result: ProZorro -> Novus | horizon 21d | mean coef 0.479, median coef 0.443, sig share 0.667, core share 0.333, median n 31.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **ProZorro -> ProducerUA | processor_price | Local projections**
Result: ProZorro -> ProducerUA | horizon 21d | mean coef -0.148, median coef -0.003, sig share 0.100, core share 0.100, median n 254.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **ProZorro -> Retail | retail_baseline | Local projections**
Result: ProZorro -> Retail | horizon 21d | mean coef -0.001, median coef -0.067, sig share 0.167, core share 0.167, median n 46.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **ProZorro -> Retail | retail_observed | Local projections**
Result: ProZorro -> Retail | horizon 21d | mean coef -0.014, median coef -0.047, sig share 0.167, core share 0.167, median n 46.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **ProZorro -> Retail matched | retail_matched_baseline | Local projections**
Result: ProZorro -> Retail matched | horizon 21d | mean coef -0.003, median coef -0.008, sig share 0.167, core share 0.167, median n 38.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **ProZorro -> Retail matched | retail_matched_observed | Local projections**
Result: ProZorro -> Retail matched | horizon 21d | mean coef -0.001, median coef -0.002, sig share 0.167, core share 0.167, median n 38.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **ProZorro -> Retail optimal | retail_optimal_baseline | Local projections**
Result: ProZorro -> Retail optimal | horizon 21d | mean coef -0.001, median coef -0.067, sig share 0.167, core share 0.167, median n 46.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **ProZorro -> Retail optimal | retail_optimal_observed | Local projections**
Result: ProZorro -> Retail optimal | horizon 21d | mean coef -0.014, median coef -0.047, sig share 0.167, core share 0.167, median n 46.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **ProZorro -> Silpo | silpo_baseline | Local projections**
Result: ProZorro -> Silpo | horizon 21d | mean coef -0.023, median coef -0.026, sig share 0.333, core share 0.000, median n 28.
**This horizon shows some significant short-run movement, but the evidence is not strong enough to treat it as a stable core signal across products.**

1. **ProZorro -> Silpo | silpo_observed | Local projections**
Result: ProZorro -> Silpo | horizon 21d | mean coef -0.029, median coef -0.021, sig share 0.333, core share 0.000, median n 28.
**This horizon shows some significant short-run movement, but the evidence is not strong enough to treat it as a stable core signal across products.**

1. **ProducerUA -> FarmGateUA | processor_price | Local projections**
Result: ProducerUA -> FarmGateUA | horizon 21d | mean coef 3.658, median coef 3.212, sig share 1.000, core share 1.000, median n 1455.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **ProducerUA -> ProZorro | procurement_price | Local projections**
Result: ProducerUA -> ProZorro | horizon 21d | mean coef -2.096, median coef -0.954, sig share 0.125, core share 0.125, median n 247.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **Retail -> FarmGateUA | retail_observed | Local projections**
Result: Retail -> FarmGateUA | horizon 21d | mean coef 0.002, median coef 0.003, sig share 0.111, core share 0.111, median n 58.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **Retail -> ProZorro | retail_baseline | Local projections**
Result: Retail -> ProZorro | horizon 21d | mean coef -0.205, median coef -0.110, sig share 0.333, core share 0.333, median n 56.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **Retail -> ProZorro | retail_observed | Local projections**
Result: Retail -> ProZorro | horizon 21d | mean coef -0.075, median coef -0.087, sig share 0.333, core share 0.333, median n 56.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **Retail matched -> ProZorro | retail_matched_baseline | Local projections**
Result: Retail matched -> ProZorro | horizon 21d | mean coef -0.184, median coef -0.159, sig share 0.500, core share 0.500, median n 51.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **Retail matched -> ProZorro | retail_matched_observed | Local projections**
Result: Retail matched -> ProZorro | horizon 21d | mean coef -0.143, median coef -0.173, sig share 0.500, core share 0.500, median n 51.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **Retail optimal -> FarmGateUA | retail_optimal_observed | Local projections**
Result: Retail optimal -> FarmGateUA | horizon 21d | mean coef 0.001, median coef 0.000, sig share 0.111, core share 0.111, median n 58.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **Retail optimal -> ProZorro | retail_optimal_baseline | Local projections**
Result: Retail optimal -> ProZorro | horizon 21d | mean coef -0.205, median coef -0.110, sig share 0.333, core share 0.333, median n 56.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **Retail optimal -> ProZorro | retail_optimal_observed | Local projections**
Result: Retail optimal -> ProZorro | horizon 21d | mean coef -0.075, median coef -0.087, sig share 0.333, core share 0.333, median n 56.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **Silpo -> ProZorro | silpo_baseline | Local projections**
Result: Silpo -> ProZorro | horizon 21d | mean coef -0.345, median coef -0.438, sig share 0.167, core share 0.167, median n 47.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

1. **Silpo -> ProZorro | silpo_observed | Local projections**
Result: Silpo -> ProZorro | horizon 21d | mean coef -0.260, median coef -0.149, sig share 0.167, core share 0.167, median n 47.
**This horizon retains short-run timing evidence, so it helps identify when pass-through becomes visible even if weekly equilibrium support is thin.**

## Spread and market-power proxy results

1. **Butter | producer_farmgate | Spread / margin**
Result: Butter | ProducerUA / FarmGateUA | linear: lag-spread -0.001 (p 0.680), upstream+ 0.116 (p 0.125), upstream- 0.119 (p 0.496), asym p 0.986, R2 0.008.
**This spread does not deliver strong margin-management evidence in statistical terms, so it should be treated as weak or descriptive.**

1. **Butter | retail_farmgate_observed | Spread / margin**
Result: Butter | Retail observed / FarmGateUA | linear: lag-spread -0.413 (p <0.001), upstream+ 18.276 (p 0.107), upstream- 12.151 (p 0.140), asym p 0.576, R2 0.439.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **Butter | retail_farmgate_baseline | Spread / margin**
Result: Butter | Retail baseline / FarmGateUA | linear: lag-spread -0.419 (p <0.001), upstream+ 19.269 (p 0.071), upstream- 10.558 (p 0.178), asym p 0.355, R2 0.419.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **Butter | producer_farmgate | Spread / margin**
Result: Butter | ProducerUA / FarmGateUA | linear: lag-spread -0.002 (p 0.199), upstream+ 0.769 (p <0.001), upstream- -0.301 (p 0.150), asym p <0.001, R2 0.084.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Butter | retail_farmgate_observed | Spread / margin**
Result: Butter | Retail observed / FarmGateUA | linear: lag-spread -0.424 (p <0.001), upstream+ 20.962 (p 0.210), upstream- 26.807 (p 0.101), asym p 0.735, R2 0.441.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **Butter | retail_farmgate_baseline | Spread / margin**
Result: Butter | Retail baseline / FarmGateUA | linear: lag-spread -0.432 (p <0.001), upstream+ 21.841 (p 0.136), upstream- 23.017 (p 0.133), asym p 0.938, R2 0.423.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **Butter | procurement_producer | Spread / margin**
Result: Butter | ProZorro / ProducerUA | linear: lag-spread -0.528 (p <0.001), upstream+ -13.434 (p 0.004), upstream- -2.644 (p 0.489), asym p 0.019, R2 0.278.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Butter | retail_procurement_observed | Spread / margin**
Result: Butter | Retail observed / ProZorro | linear: lag-spread -0.379 (p <0.001), upstream+ -0.815 (p <0.001), upstream- 0.649 (p <0.001), asym p <0.001, R2 0.699.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Butter | retail_procurement_baseline | Spread / margin**
Result: Butter | Retail baseline / ProZorro | linear: lag-spread -0.371 (p <0.001), upstream+ -0.856 (p <0.001), upstream- 0.605 (p <0.001), asym p <0.001, R2 0.705.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Butter | retail_matched_procurement_observed | Spread / margin**
Result: Butter | Retail matched observed / ProZorro | linear: lag-spread -0.353 (p 0.001), upstream+ -0.758 (p 0.001), upstream- 0.845 (p <0.001), asym p <0.001, R2 0.556.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Butter | retail_matched_procurement_baseline | Spread / margin**
Result: Butter | Retail matched baseline / ProZorro | linear: lag-spread -0.346 (p <0.001), upstream+ -0.916 (p <0.001), upstream- 0.775 (p <0.001), asym p <0.001, R2 0.644.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Butter | silpo_procurement_observed | Spread / margin**
Result: Butter | Silpo observed / ProZorro | linear: lag-spread -0.241 (p <0.001), upstream+ -0.866 (p <0.001), upstream- 0.790 (p 0.001), asym p <0.001, R2 0.728.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Butter | silpo_procurement_baseline | Spread / margin**
Result: Butter | Silpo baseline / ProZorro | linear: lag-spread -0.225 (p <0.001), upstream+ -0.936 (p <0.001), upstream- 0.725 (p 0.001), asym p <0.001, R2 0.769.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Butter | retail_optimal_procurement_observed | Spread / margin**
Result: Butter | Retail optimal observed / ProZorro | linear: lag-spread -0.379 (p <0.001), upstream+ -0.815 (p <0.001), upstream- 0.649 (p <0.001), asym p <0.001, R2 0.699.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Butter | retail_optimal_procurement_baseline | Spread / margin**
Result: Butter | Retail optimal baseline / ProZorro | linear: lag-spread -0.371 (p <0.001), upstream+ -0.856 (p <0.001), upstream- 0.605 (p <0.001), asym p <0.001, R2 0.705.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Butter | producer_farmgate | Spread / margin**
Result: Butter | ProducerUA / FarmGateUA | pchip: lag-spread -0.001 (p 0.673), upstream+ 0.104 (p 0.187), upstream- 0.099 (p 0.548), asym p 0.978, R2 0.007.
**This spread does not deliver strong margin-management evidence in statistical terms, so it should be treated as weak or descriptive.**

1. **Butter | retail_farmgate_observed | Spread / margin**
Result: Butter | Retail observed / FarmGateUA | pchip: lag-spread -0.416 (p <0.001), upstream+ 14.125 (p 0.073), upstream- 11.543 (p 0.133), asym p 0.694, R2 0.438.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **Butter | retail_farmgate_baseline | Spread / margin**
Result: Butter | Retail baseline / FarmGateUA | pchip: lag-spread -0.421 (p <0.001), upstream+ 10.617 (p 0.138), upstream- 8.681 (p 0.219), asym p 0.731, R2 0.410.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **Butter | producer_farmgate | Spread / margin**
Result: Butter | ProducerUA / FarmGateUA | pchip: lag-spread -0.002 (p 0.212), upstream+ 0.755 (p <0.001), upstream- -0.325 (p 0.104), asym p <0.001, R2 0.087.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Butter | retail_farmgate_observed | Spread / margin**
Result: Butter | Retail observed / FarmGateUA | pchip: lag-spread -0.426 (p <0.001), upstream+ 17.506 (p 0.121), upstream- 25.527 (p 0.094), asym p 0.546, R2 0.442.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **Butter | retail_farmgate_baseline | Spread / margin**
Result: Butter | Retail baseline / FarmGateUA | pchip: lag-spread -0.434 (p <0.001), upstream+ 13.213 (p 0.197), upstream- 18.932 (p 0.181), asym p 0.627, R2 0.416.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **Butter | procurement_producer | Spread / margin**
Result: Butter | ProZorro / ProducerUA | pchip: lag-spread -0.518 (p <0.001), upstream+ -10.936 (p 0.006), upstream- -0.331 (p 0.917), asym p 0.010, R2 0.271.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Butter | retail_procurement_observed | Spread / margin**
Result: Butter | Retail observed / ProZorro | pchip: lag-spread -0.379 (p <0.001), upstream+ -0.815 (p <0.001), upstream- 0.649 (p <0.001), asym p <0.001, R2 0.699.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Butter | retail_procurement_baseline | Spread / margin**
Result: Butter | Retail baseline / ProZorro | pchip: lag-spread -0.371 (p <0.001), upstream+ -0.856 (p <0.001), upstream- 0.605 (p <0.001), asym p <0.001, R2 0.705.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Butter | retail_matched_procurement_observed | Spread / margin**
Result: Butter | Retail matched observed / ProZorro | pchip: lag-spread -0.353 (p 0.001), upstream+ -0.758 (p 0.001), upstream- 0.845 (p <0.001), asym p <0.001, R2 0.556.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Butter | retail_matched_procurement_baseline | Spread / margin**
Result: Butter | Retail matched baseline / ProZorro | pchip: lag-spread -0.346 (p <0.001), upstream+ -0.916 (p <0.001), upstream- 0.775 (p <0.001), asym p <0.001, R2 0.644.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Butter | silpo_procurement_observed | Spread / margin**
Result: Butter | Silpo observed / ProZorro | pchip: lag-spread -0.241 (p <0.001), upstream+ -0.866 (p <0.001), upstream- 0.790 (p 0.001), asym p <0.001, R2 0.728.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Butter | silpo_procurement_baseline | Spread / margin**
Result: Butter | Silpo baseline / ProZorro | pchip: lag-spread -0.225 (p <0.001), upstream+ -0.936 (p <0.001), upstream- 0.725 (p 0.001), asym p <0.001, R2 0.769.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Butter | retail_optimal_procurement_observed | Spread / margin**
Result: Butter | Retail optimal observed / ProZorro | pchip: lag-spread -0.379 (p <0.001), upstream+ -0.815 (p <0.001), upstream- 0.649 (p <0.001), asym p <0.001, R2 0.699.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Butter | retail_optimal_procurement_baseline | Spread / margin**
Result: Butter | Retail optimal baseline / ProZorro | pchip: lag-spread -0.371 (p <0.001), upstream+ -0.856 (p <0.001), upstream- 0.605 (p <0.001), asym p <0.001, R2 0.705.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **CHEESE | producer_farmgate | Spread / margin**
Result: CHEESE | ProducerUA / FarmGateUA | linear: lag-spread -0.000 (p 0.901), upstream+ -0.266 (p <0.001), upstream- 0.676 (p <0.001), asym p <0.001, R2 0.158.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **CHEESE | retail_farmgate_observed | Spread / margin**
Result: CHEESE | Retail observed / FarmGateUA | linear: lag-spread -0.673 (p <0.001), upstream+ -8.984 (p 0.816), upstream- -27.283 (p 0.323), asym p 0.452, R2 0.492.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **CHEESE | retail_farmgate_baseline | Spread / margin**
Result: CHEESE | Retail baseline / FarmGateUA | linear: lag-spread -0.665 (p <0.001), upstream+ -18.136 (p 0.626), upstream- -25.765 (p 0.345), asym p 0.742, R2 0.469.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **CHEESE | producer_farmgate | Spread / margin**
Result: CHEESE | ProducerUA / FarmGateUA | linear: lag-spread -0.001 (p 0.692), upstream+ 0.132 (p 0.159), upstream- 0.544 (p 0.007), asym p 0.049, R2 0.061.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **CHEESE | retail_farmgate_observed | Spread / margin**
Result: CHEESE | Retail observed / FarmGateUA | linear: lag-spread -0.683 (p <0.001), upstream+ -34.122 (p 0.588), upstream- -94.643 (p 0.253), asym p 0.227, R2 0.497.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **CHEESE | retail_farmgate_baseline | Spread / margin**
Result: CHEESE | Retail baseline / FarmGateUA | linear: lag-spread -0.677 (p <0.001), upstream+ -46.479 (p 0.448), upstream- -94.301 (p 0.249), asym p 0.331, R2 0.477.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **CHEESE | procurement_producer | Spread / margin**
Result: CHEESE | ProZorro / ProducerUA | linear: lag-spread -0.720 (p <0.001), upstream+ 11.486 (p 0.159), upstream- 16.549 (p 0.026), asym p 0.522, R2 0.363.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **CHEESE | retail_procurement_observed | Spread / margin**
Result: CHEESE | Retail observed / ProZorro | linear: lag-spread -0.599 (p <0.001), upstream+ -0.821 (p <0.001), upstream- 0.754 (p <0.001), asym p <0.001, R2 0.649.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **CHEESE | retail_procurement_baseline | Spread / margin**
Result: CHEESE | Retail baseline / ProZorro | linear: lag-spread -0.592 (p <0.001), upstream+ -0.831 (p <0.001), upstream- 0.758 (p <0.001), asym p <0.001, R2 0.644.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **CHEESE | retail_matched_procurement_observed | Spread / margin**
Result: CHEESE | Retail matched observed / ProZorro | linear: lag-spread -0.417 (p 0.030), upstream+ -0.513 (p 0.007), upstream- 0.928 (p <0.001), asym p <0.001, R2 0.760.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **CHEESE | retail_matched_procurement_baseline | Spread / margin**
Result: CHEESE | Retail matched baseline / ProZorro | linear: lag-spread -0.395 (p 0.022), upstream+ -0.663 (p <0.001), upstream- 0.954 (p <0.001), asym p <0.001, R2 0.825.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **CHEESE | silpo_procurement_observed | Spread / margin**
Result: CHEESE | Silpo observed / ProZorro | linear: lag-spread -0.147 (p 0.122), upstream+ -0.807 (p <0.001), upstream- 0.948 (p <0.001), asym p <0.001, R2 0.914.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **CHEESE | silpo_procurement_baseline | Spread / margin**
Result: CHEESE | Silpo baseline / ProZorro | linear: lag-spread -0.123 (p 0.046), upstream+ -0.882 (p <0.001), upstream- 0.959 (p <0.001), asym p <0.001, R2 0.943.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **CHEESE | novus_procurement_observed | Spread / margin**
Result: CHEESE | Novus observed / ProZorro | linear: lag-spread -0.518 (p <0.001), upstream+ -1.142 (p 0.016), upstream- 0.843 (p 0.006), asym p <0.001, R2 0.403.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **CHEESE | retail_optimal_procurement_observed | Spread / margin**
Result: CHEESE | Retail optimal observed / ProZorro | linear: lag-spread -0.599 (p <0.001), upstream+ -0.821 (p <0.001), upstream- 0.754 (p <0.001), asym p <0.001, R2 0.649.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **CHEESE | retail_optimal_procurement_baseline | Spread / margin**
Result: CHEESE | Retail optimal baseline / ProZorro | linear: lag-spread -0.592 (p <0.001), upstream+ -0.831 (p <0.001), upstream- 0.758 (p <0.001), asym p <0.001, R2 0.644.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **CHEESE | producer_farmgate | Spread / margin**
Result: CHEESE | ProducerUA / FarmGateUA | pchip: lag-spread -0.000 (p 0.893), upstream+ -0.281 (p <0.001), upstream- 0.646 (p <0.001), asym p <0.001, R2 0.163.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **CHEESE | retail_farmgate_observed | Spread / margin**
Result: CHEESE | Retail observed / FarmGateUA | pchip: lag-spread -0.668 (p <0.001), upstream+ -15.118 (p 0.660), upstream- -25.313 (p 0.199), asym p 0.706, R2 0.491.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **CHEESE | retail_farmgate_baseline | Spread / margin**
Result: CHEESE | Retail baseline / FarmGateUA | pchip: lag-spread -0.660 (p <0.001), upstream+ -23.435 (p 0.487), upstream- -23.871 (p 0.221), asym p 0.987, R2 0.470.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **CHEESE | producer_farmgate | Spread / margin**
Result: CHEESE | ProducerUA / FarmGateUA | pchip: lag-spread -0.001 (p 0.677), upstream+ 0.113 (p 0.211), upstream- 0.498 (p 0.007), asym p 0.053, R2 0.059.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **CHEESE | retail_farmgate_observed | Spread / margin**
Result: CHEESE | Retail observed / FarmGateUA | pchip: lag-spread -0.678 (p <0.001), upstream+ -47.481 (p 0.457), upstream- -96.178 (p 0.181), asym p 0.339, R2 0.502.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **CHEESE | retail_farmgate_baseline | Spread / margin**
Result: CHEESE | Retail baseline / FarmGateUA | pchip: lag-spread -0.671 (p <0.001), upstream+ -57.864 (p 0.352), upstream- -94.720 (p 0.182), asym p 0.453, R2 0.483.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **CHEESE | procurement_producer | Spread / margin**
Result: CHEESE | ProZorro / ProducerUA | pchip: lag-spread -0.722 (p <0.001), upstream+ 10.257 (p 0.214), upstream- 15.761 (p 0.022), asym p 0.493, R2 0.362.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **CHEESE | retail_procurement_observed | Spread / margin**
Result: CHEESE | Retail observed / ProZorro | pchip: lag-spread -0.599 (p <0.001), upstream+ -0.821 (p <0.001), upstream- 0.754 (p <0.001), asym p <0.001, R2 0.649.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **CHEESE | retail_procurement_baseline | Spread / margin**
Result: CHEESE | Retail baseline / ProZorro | pchip: lag-spread -0.592 (p <0.001), upstream+ -0.831 (p <0.001), upstream- 0.758 (p <0.001), asym p <0.001, R2 0.644.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **CHEESE | retail_matched_procurement_observed | Spread / margin**
Result: CHEESE | Retail matched observed / ProZorro | pchip: lag-spread -0.417 (p 0.030), upstream+ -0.513 (p 0.007), upstream- 0.928 (p <0.001), asym p <0.001, R2 0.760.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **CHEESE | retail_matched_procurement_baseline | Spread / margin**
Result: CHEESE | Retail matched baseline / ProZorro | pchip: lag-spread -0.395 (p 0.022), upstream+ -0.663 (p <0.001), upstream- 0.954 (p <0.001), asym p <0.001, R2 0.825.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **CHEESE | silpo_procurement_observed | Spread / margin**
Result: CHEESE | Silpo observed / ProZorro | pchip: lag-spread -0.147 (p 0.122), upstream+ -0.807 (p <0.001), upstream- 0.948 (p <0.001), asym p <0.001, R2 0.914.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **CHEESE | silpo_procurement_baseline | Spread / margin**
Result: CHEESE | Silpo baseline / ProZorro | pchip: lag-spread -0.123 (p 0.046), upstream+ -0.882 (p <0.001), upstream- 0.959 (p <0.001), asym p <0.001, R2 0.943.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **CHEESE | novus_procurement_observed | Spread / margin**
Result: CHEESE | Novus observed / ProZorro | pchip: lag-spread -0.518 (p <0.001), upstream+ -1.142 (p 0.016), upstream- 0.843 (p 0.006), asym p <0.001, R2 0.403.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **CHEESE | retail_optimal_procurement_observed | Spread / margin**
Result: CHEESE | Retail optimal observed / ProZorro | pchip: lag-spread -0.599 (p <0.001), upstream+ -0.821 (p <0.001), upstream- 0.754 (p <0.001), asym p <0.001, R2 0.649.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **CHEESE | retail_optimal_procurement_baseline | Spread / margin**
Result: CHEESE | Retail optimal baseline / ProZorro | pchip: lag-spread -0.592 (p <0.001), upstream+ -0.831 (p <0.001), upstream- 0.758 (p <0.001), asym p <0.001, R2 0.644.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Condensed milk | retail_farmgate_observed | Spread / margin**
Result: Condensed milk | Retail observed / FarmGateUA | linear: lag-spread -0.593 (p <0.001), upstream+ -14.562 (p 0.051), upstream- -29.508 (p 0.003), asym p 0.026, R2 0.656.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Condensed milk | retail_farmgate_baseline | Spread / margin**
Result: Condensed milk | Retail baseline / FarmGateUA | linear: lag-spread -0.601 (p <0.001), upstream+ -12.407 (p 0.111), upstream- -30.579 (p <0.001), asym p 0.008, R2 0.687.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Condensed milk | retail_farmgate_observed | Spread / margin**
Result: Condensed milk | Retail observed / FarmGateUA | linear: lag-spread -0.629 (p <0.001), upstream+ -7.630 (p 0.432), upstream- -57.086 (p 0.009), asym p 0.010, R2 0.665.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Condensed milk | retail_farmgate_baseline | Spread / margin**
Result: Condensed milk | Retail baseline / FarmGateUA | linear: lag-spread -0.638 (p <0.001), upstream+ -2.438 (p 0.815), upstream- -56.857 (p 0.005), asym p 0.003, R2 0.694.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Condensed milk | retail_procurement_observed | Spread / margin**
Result: Condensed milk | Retail observed / ProZorro | linear: lag-spread -0.163 (p <0.001), upstream+ -1.254 (p <0.001), upstream- 0.874 (p <0.001), asym p <0.001, R2 0.841.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Condensed milk | retail_procurement_baseline | Spread / margin**
Result: Condensed milk | Retail baseline / ProZorro | linear: lag-spread -0.149 (p <0.001), upstream+ -1.205 (p <0.001), upstream- 0.927 (p <0.001), asym p <0.001, R2 0.869.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Condensed milk | retail_matched_procurement_observed | Spread / margin**
Result: Condensed milk | Retail matched observed / ProZorro | linear: lag-spread -0.723 (p <0.001), upstream+ -2.061 (p 0.012), upstream- 1.267 (p 0.074), asym p <0.001, R2 0.520.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Condensed milk | retail_matched_procurement_baseline | Spread / margin**
Result: Condensed milk | Retail matched baseline / ProZorro | linear: lag-spread -0.775 (p <0.001), upstream+ -1.899 (p 0.015), upstream- 1.160 (p 0.102), asym p <0.001, R2 0.521.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Condensed milk | silpo_procurement_observed | Spread / margin**
Result: Condensed milk | Silpo observed / ProZorro | linear: lag-spread -0.186 (p <0.001), upstream+ -1.219 (p <0.001), upstream- 0.884 (p <0.001), asym p <0.001, R2 0.846.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Condensed milk | silpo_procurement_baseline | Spread / margin**
Result: Condensed milk | Silpo baseline / ProZorro | linear: lag-spread -0.166 (p <0.001), upstream+ -1.129 (p <0.001), upstream- 0.950 (p <0.001), asym p <0.001, R2 0.871.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Condensed milk | retail_optimal_procurement_observed | Spread / margin**
Result: Condensed milk | Retail optimal observed / ProZorro | linear: lag-spread -0.163 (p <0.001), upstream+ -1.254 (p <0.001), upstream- 0.874 (p <0.001), asym p <0.001, R2 0.841.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Condensed milk | retail_optimal_procurement_baseline | Spread / margin**
Result: Condensed milk | Retail optimal baseline / ProZorro | linear: lag-spread -0.149 (p <0.001), upstream+ -1.205 (p <0.001), upstream- 0.927 (p <0.001), asym p <0.001, R2 0.869.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Condensed milk | retail_farmgate_observed | Spread / margin**
Result: Condensed milk | Retail observed / FarmGateUA | pchip: lag-spread -0.589 (p <0.001), upstream+ -13.159 (p 0.037), upstream- -25.845 (p 0.002), asym p 0.061, R2 0.648.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Condensed milk | retail_farmgate_baseline | Spread / margin**
Result: Condensed milk | Retail baseline / FarmGateUA | pchip: lag-spread -0.595 (p <0.001), upstream+ -9.853 (p 0.122), upstream- -25.776 (p 0.002), asym p 0.014, R2 0.670.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Condensed milk | retail_farmgate_observed | Spread / margin**
Result: Condensed milk | Retail observed / FarmGateUA | pchip: lag-spread -0.630 (p <0.001), upstream+ -10.063 (p 0.250), upstream- -52.731 (p 0.005), asym p 0.011, R2 0.664.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Condensed milk | retail_farmgate_baseline | Spread / margin**
Result: Condensed milk | Retail baseline / FarmGateUA | pchip: lag-spread -0.635 (p <0.001), upstream+ -3.652 (p 0.679), upstream- -50.758 (p 0.006), asym p 0.003, R2 0.686.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Condensed milk | retail_procurement_observed | Spread / margin**
Result: Condensed milk | Retail observed / ProZorro | pchip: lag-spread -0.163 (p <0.001), upstream+ -1.254 (p <0.001), upstream- 0.874 (p <0.001), asym p <0.001, R2 0.841.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Condensed milk | retail_procurement_baseline | Spread / margin**
Result: Condensed milk | Retail baseline / ProZorro | pchip: lag-spread -0.149 (p <0.001), upstream+ -1.205 (p <0.001), upstream- 0.927 (p <0.001), asym p <0.001, R2 0.869.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Condensed milk | retail_matched_procurement_observed | Spread / margin**
Result: Condensed milk | Retail matched observed / ProZorro | pchip: lag-spread -0.723 (p <0.001), upstream+ -2.061 (p 0.012), upstream- 1.267 (p 0.074), asym p <0.001, R2 0.520.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Condensed milk | retail_matched_procurement_baseline | Spread / margin**
Result: Condensed milk | Retail matched baseline / ProZorro | pchip: lag-spread -0.775 (p <0.001), upstream+ -1.899 (p 0.015), upstream- 1.160 (p 0.102), asym p <0.001, R2 0.521.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Condensed milk | silpo_procurement_observed | Spread / margin**
Result: Condensed milk | Silpo observed / ProZorro | pchip: lag-spread -0.186 (p <0.001), upstream+ -1.219 (p <0.001), upstream- 0.884 (p <0.001), asym p <0.001, R2 0.846.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Condensed milk | silpo_procurement_baseline | Spread / margin**
Result: Condensed milk | Silpo baseline / ProZorro | pchip: lag-spread -0.166 (p <0.001), upstream+ -1.129 (p <0.001), upstream- 0.950 (p <0.001), asym p <0.001, R2 0.871.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Condensed milk | retail_optimal_procurement_observed | Spread / margin**
Result: Condensed milk | Retail optimal observed / ProZorro | pchip: lag-spread -0.163 (p <0.001), upstream+ -1.254 (p <0.001), upstream- 0.874 (p <0.001), asym p <0.001, R2 0.841.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Condensed milk | retail_optimal_procurement_baseline | Spread / margin**
Result: Condensed milk | Retail optimal baseline / ProZorro | pchip: lag-spread -0.149 (p <0.001), upstream+ -1.205 (p <0.001), upstream- 0.927 (p <0.001), asym p <0.001, R2 0.869.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Cream | retail_farmgate_observed | Spread / margin**
Result: Cream | Retail observed / FarmGateUA | linear: lag-spread -0.243 (p <0.001), upstream+ -18.916 (p 0.124), upstream- -9.642 (p 0.243), asym p 0.328, R2 0.240.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **Cream | retail_farmgate_baseline | Spread / margin**
Result: Cream | Retail baseline / FarmGateUA | linear: lag-spread -0.230 (p <0.001), upstream+ -12.269 (p 0.308), upstream- -3.227 (p 0.700), asym p 0.327, R2 0.237.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **Cream | retail_farmgate_observed | Spread / margin**
Result: Cream | Retail observed / FarmGateUA | linear: lag-spread -0.246 (p <0.001), upstream+ -17.689 (p 0.297), upstream- -22.041 (p 0.293), asym p 0.754, R2 0.244.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **Cream | retail_farmgate_baseline | Spread / margin**
Result: Cream | Retail baseline / FarmGateUA | linear: lag-spread -0.235 (p <0.001), upstream+ -12.962 (p 0.428), upstream- -10.369 (p 0.632), asym p 0.860, R2 0.243.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **Cream | retail_procurement_observed | Spread / margin**
Result: Cream | Retail observed / ProZorro | linear: lag-spread -0.149 (p 0.010), upstream+ -1.032 (p <0.001), upstream- 0.814 (p <0.001), asym p <0.001, R2 0.825.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Cream | retail_procurement_baseline | Spread / margin**
Result: Cream | Retail baseline / ProZorro | linear: lag-spread -0.147 (p 0.011), upstream+ -1.006 (p <0.001), upstream- 0.766 (p <0.001), asym p <0.001, R2 0.827.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Cream | retail_matched_procurement_observed | Spread / margin**
Result: Cream | Retail matched observed / ProZorro | linear: lag-spread -0.183 (p <0.001), upstream+ -1.032 (p <0.001), upstream- 0.626 (p <0.001), asym p <0.001, R2 0.807.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Cream | retail_matched_procurement_baseline | Spread / margin**
Result: Cream | Retail matched baseline / ProZorro | linear: lag-spread -0.190 (p <0.001), upstream+ -1.050 (p <0.001), upstream- 0.645 (p <0.001), asym p <0.001, R2 0.815.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Cream | silpo_procurement_observed | Spread / margin**
Result: Cream | Silpo observed / ProZorro | linear: lag-spread -0.101 (p 0.055), upstream+ -1.014 (p <0.001), upstream- 0.934 (p <0.001), asym p <0.001, R2 0.934.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Cream | silpo_procurement_baseline | Spread / margin**
Result: Cream | Silpo baseline / ProZorro | linear: lag-spread -0.059 (p 0.019), upstream+ -0.981 (p <0.001), upstream- 0.939 (p <0.001), asym p <0.001, R2 0.950.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Cream | novus_procurement_observed | Spread / margin**
Result: Cream | Novus observed / ProZorro | linear: lag-spread -0.261 (p 0.002), upstream+ -0.796 (p <0.001), upstream- 0.914 (p <0.001), asym p <0.001, R2 0.644.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Cream | retail_optimal_procurement_observed | Spread / margin**
Result: Cream | Retail optimal observed / ProZorro | linear: lag-spread -0.149 (p 0.010), upstream+ -1.032 (p <0.001), upstream- 0.814 (p <0.001), asym p <0.001, R2 0.825.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Cream | retail_optimal_procurement_baseline | Spread / margin**
Result: Cream | Retail optimal baseline / ProZorro | linear: lag-spread -0.147 (p 0.011), upstream+ -1.006 (p <0.001), upstream- 0.766 (p <0.001), asym p <0.001, R2 0.827.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Cream | retail_farmgate_observed | Spread / margin**
Result: Cream | Retail observed / FarmGateUA | pchip: lag-spread -0.223 (p <0.001), upstream+ -3.109 (p 0.708), upstream- 2.810 (p 0.596), asym p 0.438, R2 0.231.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **Cream | retail_farmgate_baseline | Spread / margin**
Result: Cream | Retail baseline / FarmGateUA | pchip: lag-spread -0.217 (p <0.001), upstream+ -0.625 (p 0.936), upstream- 4.681 (p 0.372), asym p 0.455, R2 0.235.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **Cream | retail_farmgate_observed | Spread / margin**
Result: Cream | Retail observed / FarmGateUA | pchip: lag-spread -0.230 (p <0.001), upstream+ -4.211 (p 0.756), upstream- 0.337 (p 0.982), asym p 0.665, R2 0.235.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **Cream | retail_farmgate_baseline | Spread / margin**
Result: Cream | Retail baseline / FarmGateUA | pchip: lag-spread -0.226 (p <0.001), upstream+ -2.746 (p 0.831), upstream- 3.193 (p 0.830), asym p 0.566, R2 0.239.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **Cream | retail_procurement_observed | Spread / margin**
Result: Cream | Retail observed / ProZorro | pchip: lag-spread -0.149 (p 0.010), upstream+ -1.032 (p <0.001), upstream- 0.814 (p <0.001), asym p <0.001, R2 0.825.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Cream | retail_procurement_baseline | Spread / margin**
Result: Cream | Retail baseline / ProZorro | pchip: lag-spread -0.147 (p 0.011), upstream+ -1.006 (p <0.001), upstream- 0.766 (p <0.001), asym p <0.001, R2 0.827.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Cream | retail_matched_procurement_observed | Spread / margin**
Result: Cream | Retail matched observed / ProZorro | pchip: lag-spread -0.183 (p <0.001), upstream+ -1.032 (p <0.001), upstream- 0.626 (p <0.001), asym p <0.001, R2 0.807.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Cream | retail_matched_procurement_baseline | Spread / margin**
Result: Cream | Retail matched baseline / ProZorro | pchip: lag-spread -0.190 (p <0.001), upstream+ -1.050 (p <0.001), upstream- 0.645 (p <0.001), asym p <0.001, R2 0.815.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Cream | silpo_procurement_observed | Spread / margin**
Result: Cream | Silpo observed / ProZorro | pchip: lag-spread -0.101 (p 0.055), upstream+ -1.014 (p <0.001), upstream- 0.934 (p <0.001), asym p <0.001, R2 0.934.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Cream | silpo_procurement_baseline | Spread / margin**
Result: Cream | Silpo baseline / ProZorro | pchip: lag-spread -0.059 (p 0.019), upstream+ -0.981 (p <0.001), upstream- 0.939 (p <0.001), asym p <0.001, R2 0.950.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Cream | novus_procurement_observed | Spread / margin**
Result: Cream | Novus observed / ProZorro | pchip: lag-spread -0.261 (p 0.002), upstream+ -0.796 (p <0.001), upstream- 0.914 (p <0.001), asym p <0.001, R2 0.644.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Cream | retail_optimal_procurement_observed | Spread / margin**
Result: Cream | Retail optimal observed / ProZorro | pchip: lag-spread -0.149 (p 0.010), upstream+ -1.032 (p <0.001), upstream- 0.814 (p <0.001), asym p <0.001, R2 0.825.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Cream | retail_optimal_procurement_baseline | Spread / margin**
Result: Cream | Retail optimal baseline / ProZorro | pchip: lag-spread -0.147 (p 0.011), upstream+ -1.006 (p <0.001), upstream- 0.766 (p <0.001), asym p <0.001, R2 0.827.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Drinking milk / fermented milk | producer_farmgate | Spread / margin**
Result: Drinking milk / fermented milk | ProducerUA / FarmGateUA | linear: lag-spread 0.002 (p 0.258), upstream+ -0.360 (p <0.001), upstream- 0.437 (p <0.001), asym p <0.001, R2 0.259.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Drinking milk / fermented milk | retail_farmgate_observed | Spread / margin**
Result: Drinking milk / fermented milk | Retail observed / FarmGateUA | linear: lag-spread -0.705 (p <0.001), upstream+ -0.794 (p 0.944), upstream- 10.023 (p 0.492), asym p 0.224, R2 0.363.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **Drinking milk / fermented milk | retail_farmgate_baseline | Spread / margin**
Result: Drinking milk / fermented milk | Retail baseline / FarmGateUA | linear: lag-spread -0.742 (p <0.001), upstream+ -4.768 (p 0.685), upstream- 8.411 (p 0.588), asym p 0.152, R2 0.385.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **Drinking milk / fermented milk | producer_farmgate | Spread / margin**
Result: Drinking milk / fermented milk | ProducerUA / FarmGateUA | linear: lag-spread -0.001 (p 0.709), upstream+ 0.045 (p 0.647), upstream- 0.256 (p 0.012), asym p 0.081, R2 0.024.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Drinking milk / fermented milk | retail_farmgate_observed | Spread / margin**
Result: Drinking milk / fermented milk | Retail observed / FarmGateUA | linear: lag-spread -0.742 (p <0.001), upstream+ -3.778 (p 0.843), upstream- 15.458 (p 0.654), asym p 0.429, R2 0.382.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **Drinking milk / fermented milk | retail_farmgate_baseline | Spread / margin**
Result: Drinking milk / fermented milk | Retail baseline / FarmGateUA | linear: lag-spread -0.778 (p <0.001), upstream+ -8.361 (p 0.665), upstream- 11.341 (p 0.754), asym p 0.442, R2 0.405.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **Drinking milk / fermented milk | procurement_producer | Spread / margin**
Result: Drinking milk / fermented milk | ProZorro / ProducerUA | linear: lag-spread -0.556 (p <0.001), upstream+ -6.522 (p 0.366), upstream- 2.138 (p 0.767), asym p 0.166, R2 0.278.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **Drinking milk / fermented milk | retail_procurement_observed | Spread / margin**
Result: Drinking milk / fermented milk | Retail observed / ProZorro | linear: lag-spread -0.662 (p <0.001), upstream+ -0.343 (p 0.205), upstream- 1.192 (p 0.004), asym p <0.001, R2 0.504.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Drinking milk / fermented milk | retail_procurement_baseline | Spread / margin**
Result: Drinking milk / fermented milk | Retail baseline / ProZorro | linear: lag-spread -0.701 (p <0.001), upstream+ -0.328 (p 0.210), upstream- 1.161 (p 0.006), asym p <0.001, R2 0.516.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Drinking milk / fermented milk | retail_matched_procurement_observed | Spread / margin**
Result: Drinking milk / fermented milk | Retail matched observed / ProZorro | linear: lag-spread -0.642 (p 0.002), upstream+ -0.253 (p 0.462), upstream- 1.112 (p <0.001), asym p <0.001, R2 0.534.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Drinking milk / fermented milk | retail_matched_procurement_baseline | Spread / margin**
Result: Drinking milk / fermented milk | Retail matched baseline / ProZorro | linear: lag-spread -0.704 (p <0.001), upstream+ -0.244 (p 0.434), upstream- 1.176 (p <0.001), asym p <0.001, R2 0.562.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Drinking milk / fermented milk | silpo_procurement_observed | Spread / margin**
Result: Drinking milk / fermented milk | Silpo observed / ProZorro | linear: lag-spread -0.050 (p 0.298), upstream+ -0.886 (p <0.001), upstream- 1.052 (p <0.001), asym p <0.001, R2 0.870.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Drinking milk / fermented milk | silpo_procurement_baseline | Spread / margin**
Result: Drinking milk / fermented milk | Silpo baseline / ProZorro | linear: lag-spread -0.050 (p 0.288), upstream+ -0.836 (p <0.001), upstream- 1.038 (p <0.001), asym p <0.001, R2 0.881.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Drinking milk / fermented milk | novus_procurement_observed | Spread / margin**
Result: Drinking milk / fermented milk | Novus observed / ProZorro | linear: lag-spread -0.579 (p <0.001), upstream+ 0.316 (p 0.398), upstream- 2.040 (p 0.002), asym p <0.001, R2 0.407.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Drinking milk / fermented milk | retail_optimal_procurement_observed | Spread / margin**
Result: Drinking milk / fermented milk | Retail optimal observed / ProZorro | linear: lag-spread -0.662 (p <0.001), upstream+ -0.343 (p 0.205), upstream- 1.192 (p 0.004), asym p <0.001, R2 0.504.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Drinking milk / fermented milk | retail_optimal_procurement_baseline | Spread / margin**
Result: Drinking milk / fermented milk | Retail optimal baseline / ProZorro | linear: lag-spread -0.701 (p <0.001), upstream+ -0.328 (p 0.210), upstream- 1.161 (p 0.006), asym p <0.001, R2 0.516.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Drinking milk / fermented milk | producer_farmgate | Spread / margin**
Result: Drinking milk / fermented milk | ProducerUA / FarmGateUA | pchip: lag-spread 0.002 (p 0.265), upstream+ -0.363 (p <0.001), upstream- 0.450 (p <0.001), asym p <0.001, R2 0.279.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Drinking milk / fermented milk | retail_farmgate_observed | Spread / margin**
Result: Drinking milk / fermented milk | Retail observed / FarmGateUA | pchip: lag-spread -0.703 (p <0.001), upstream+ -6.378 (p 0.591), upstream- 6.126 (p 0.677), asym p 0.216, R2 0.362.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **Drinking milk / fermented milk | retail_farmgate_baseline | Spread / margin**
Result: Drinking milk / fermented milk | Retail baseline / FarmGateUA | pchip: lag-spread -0.739 (p <0.001), upstream+ -9.990 (p 0.419), upstream- 4.694 (p 0.761), asym p 0.161, R2 0.384.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **Drinking milk / fermented milk | producer_farmgate | Spread / margin**
Result: Drinking milk / fermented milk | ProducerUA / FarmGateUA | pchip: lag-spread -0.001 (p 0.724), upstream+ 0.035 (p 0.710), upstream- 0.265 (p 0.007), asym p 0.059, R2 0.026.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Drinking milk / fermented milk | retail_farmgate_observed | Spread / margin**
Result: Drinking milk / fermented milk | Retail observed / FarmGateUA | pchip: lag-spread -0.742 (p <0.001), upstream+ -8.430 (p 0.642), upstream- 11.557 (p 0.740), asym p 0.460, R2 0.382.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **Drinking milk / fermented milk | retail_farmgate_baseline | Spread / margin**
Result: Drinking milk / fermented milk | Retail baseline / FarmGateUA | pchip: lag-spread -0.778 (p <0.001), upstream+ -12.812 (p 0.481), upstream- 8.018 (p 0.825), asym p 0.459, R2 0.406.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **Drinking milk / fermented milk | procurement_producer | Spread / margin**
Result: Drinking milk / fermented milk | ProZorro / ProducerUA | pchip: lag-spread -0.552 (p <0.001), upstream+ -2.974 (p 0.700), upstream- 4.465 (p 0.500), asym p 0.188, R2 0.275.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **Drinking milk / fermented milk | retail_procurement_observed | Spread / margin**
Result: Drinking milk / fermented milk | Retail observed / ProZorro | pchip: lag-spread -0.662 (p <0.001), upstream+ -0.343 (p 0.205), upstream- 1.192 (p 0.004), asym p <0.001, R2 0.504.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Drinking milk / fermented milk | retail_procurement_baseline | Spread / margin**
Result: Drinking milk / fermented milk | Retail baseline / ProZorro | pchip: lag-spread -0.701 (p <0.001), upstream+ -0.328 (p 0.210), upstream- 1.161 (p 0.006), asym p <0.001, R2 0.516.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Drinking milk / fermented milk | retail_matched_procurement_observed | Spread / margin**
Result: Drinking milk / fermented milk | Retail matched observed / ProZorro | pchip: lag-spread -0.642 (p 0.002), upstream+ -0.253 (p 0.462), upstream- 1.112 (p <0.001), asym p <0.001, R2 0.534.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Drinking milk / fermented milk | retail_matched_procurement_baseline | Spread / margin**
Result: Drinking milk / fermented milk | Retail matched baseline / ProZorro | pchip: lag-spread -0.704 (p <0.001), upstream+ -0.244 (p 0.434), upstream- 1.176 (p <0.001), asym p <0.001, R2 0.562.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Drinking milk / fermented milk | silpo_procurement_observed | Spread / margin**
Result: Drinking milk / fermented milk | Silpo observed / ProZorro | pchip: lag-spread -0.050 (p 0.298), upstream+ -0.886 (p <0.001), upstream- 1.052 (p <0.001), asym p <0.001, R2 0.870.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Drinking milk / fermented milk | silpo_procurement_baseline | Spread / margin**
Result: Drinking milk / fermented milk | Silpo baseline / ProZorro | pchip: lag-spread -0.050 (p 0.288), upstream+ -0.836 (p <0.001), upstream- 1.038 (p <0.001), asym p <0.001, R2 0.881.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Drinking milk / fermented milk | novus_procurement_observed | Spread / margin**
Result: Drinking milk / fermented milk | Novus observed / ProZorro | pchip: lag-spread -0.579 (p <0.001), upstream+ 0.316 (p 0.398), upstream- 2.040 (p 0.002), asym p <0.001, R2 0.407.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Drinking milk / fermented milk | retail_optimal_procurement_observed | Spread / margin**
Result: Drinking milk / fermented milk | Retail optimal observed / ProZorro | pchip: lag-spread -0.662 (p <0.001), upstream+ -0.343 (p 0.205), upstream- 1.192 (p 0.004), asym p <0.001, R2 0.504.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Drinking milk / fermented milk | retail_optimal_procurement_baseline | Spread / margin**
Result: Drinking milk / fermented milk | Retail optimal baseline / ProZorro | pchip: lag-spread -0.701 (p <0.001), upstream+ -0.328 (p 0.210), upstream- 1.161 (p 0.006), asym p <0.001, R2 0.516.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Milk powder | producer_farmgate | Spread / margin**
Result: Milk powder | ProducerUA / FarmGateUA | linear: lag-spread -0.002 (p 0.436), upstream+ -0.191 (p 0.298), upstream- 0.761 (p <0.001), asym p <0.001, R2 0.104.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Milk powder | retail_farmgate_observed | Spread / margin**
Result: Milk powder | Retail observed / FarmGateUA | linear: lag-spread -0.912 (p <0.001), upstream+ 11.564 (p 0.644), upstream- -32.257 (p 0.188), asym p 0.148, R2 0.520.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **Milk powder | retail_farmgate_baseline | Spread / margin**
Result: Milk powder | Retail baseline / FarmGateUA | linear: lag-spread -0.934 (p <0.001), upstream+ 23.424 (p 0.349), upstream- -26.028 (p 0.281), asym p 0.131, R2 0.516.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **Milk powder | producer_farmgate | Spread / margin**
Result: Milk powder | ProducerUA / FarmGateUA | linear: lag-spread -0.002 (p 0.490), upstream+ 0.212 (p 0.536), upstream- 0.737 (p 0.001), asym p 0.096, R2 0.041.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Milk powder | retail_farmgate_observed | Spread / margin**
Result: Milk powder | Retail observed / FarmGateUA | linear: lag-spread -0.916 (p <0.001), upstream+ 50.122 (p 0.174), upstream- -36.823 (p 0.417), asym p 0.095, R2 0.512.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Milk powder | retail_farmgate_baseline | Spread / margin**
Result: Milk powder | Retail baseline / FarmGateUA | linear: lag-spread -0.937 (p <0.001), upstream+ 65.725 (p 0.078), upstream- -19.985 (p 0.649), asym p 0.107, R2 0.511.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **Milk powder | procurement_producer | Spread / margin**
Result: Milk powder | ProZorro / ProducerUA | linear: lag-spread -0.004 (p 0.825), upstream+ 1.611 (p 0.765), upstream- 5.656 (p 0.202), asym p 0.020, R2 0.071.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Milk powder | producer_farmgate | Spread / margin**
Result: Milk powder | ProducerUA / FarmGateUA | pchip: lag-spread -0.002 (p 0.482), upstream+ -0.243 (p 0.138), upstream- 0.695 (p <0.001), asym p <0.001, R2 0.106.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Milk powder | retail_farmgate_observed | Spread / margin**
Result: Milk powder | Retail observed / FarmGateUA | pchip: lag-spread -0.908 (p <0.001), upstream+ 11.899 (p 0.562), upstream- -24.872 (p 0.386), asym p 0.191, R2 0.514.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **Milk powder | retail_farmgate_baseline | Spread / margin**
Result: Milk powder | Retail baseline / FarmGateUA | pchip: lag-spread -0.927 (p <0.001), upstream+ 33.137 (p 0.090), upstream- -13.751 (p 0.632), asym p 0.117, R2 0.512.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **Milk powder | producer_farmgate | Spread / margin**
Result: Milk powder | ProducerUA / FarmGateUA | pchip: lag-spread -0.002 (p 0.520), upstream+ 0.140 (p 0.652), upstream- 0.649 (p 0.002), asym p 0.100, R2 0.037.
**This spread does not deliver strong margin-management evidence in statistical terms, so it should be treated as weak or descriptive.**

1. **Milk powder | retail_farmgate_observed | Spread / margin**
Result: Milk powder | Retail observed / FarmGateUA | pchip: lag-spread -0.900 (p <0.001), upstream+ 52.363 (p 0.099), upstream- -19.651 (p 0.692), asym p 0.162, R2 0.509.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **Milk powder | retail_farmgate_baseline | Spread / margin**
Result: Milk powder | Retail baseline / FarmGateUA | pchip: lag-spread -0.919 (p <0.001), upstream+ 75.198 (p 0.011), upstream- 5.626 (p 0.907), asym p 0.182, R2 0.512.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **Milk powder | procurement_producer | Spread / margin**
Result: Milk powder | ProZorro / ProducerUA | pchip: lag-spread -0.004 (p 0.852), upstream+ 1.001 (p 0.825), upstream- 4.321 (p 0.165), asym p 0.074, R2 0.062.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Other | retail_farmgate_observed | Spread / margin**
Result: Other | Retail observed / FarmGateUA | linear: lag-spread -0.284 (p 0.019), upstream+ -21.160 (p 0.373), upstream- -27.058 (p 0.262), asym p 0.748, R2 0.198.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **Other | retail_farmgate_baseline | Spread / margin**
Result: Other | Retail baseline / FarmGateUA | linear: lag-spread -0.277 (p 0.022), upstream+ -18.844 (p 0.415), upstream- -22.855 (p 0.310), asym p 0.817, R2 0.202.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **Other | retail_farmgate_observed | Spread / margin**
Result: Other | Retail observed / FarmGateUA | linear: lag-spread -0.286 (p 0.016), upstream+ -12.326 (p 0.697), upstream- -52.343 (p 0.301), asym p 0.330, R2 0.203.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **Other | retail_farmgate_baseline | Spread / margin**
Result: Other | Retail baseline / FarmGateUA | linear: lag-spread -0.279 (p 0.019), upstream+ -12.437 (p 0.680), upstream- -45.983 (p 0.337), asym p 0.377, R2 0.209.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **Other | retail_farmgate_observed | Spread / margin**
Result: Other | Retail observed / FarmGateUA | pchip: lag-spread -0.284 (p 0.020), upstream+ -23.227 (p 0.245), upstream- -24.183 (p 0.279), asym p 0.953, R2 0.198.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **Other | retail_farmgate_baseline | Spread / margin**
Result: Other | Retail baseline / FarmGateUA | pchip: lag-spread -0.276 (p 0.023), upstream+ -20.434 (p 0.289), upstream- -18.273 (p 0.395), asym p 0.887, R2 0.201.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **Other | retail_farmgate_observed | Spread / margin**
Result: Other | Retail observed / FarmGateUA | pchip: lag-spread -0.285 (p 0.017), upstream+ -18.549 (p 0.470), upstream- -49.268 (p 0.300), asym p 0.433, R2 0.203.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **Other | retail_farmgate_baseline | Spread / margin**
Result: Other | Retail baseline / FarmGateUA | pchip: lag-spread -0.278 (p 0.020), upstream+ -17.041 (p 0.492), upstream- -38.675 (p 0.404), asym p 0.560, R2 0.208.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **Sour cream | producer_farmgate | Spread / margin**
Result: Sour cream | ProducerUA / FarmGateUA | linear: lag-spread 0.001 (p 0.641), upstream+ -0.280 (p <0.001), upstream- 0.325 (p 0.002), asym p <0.001, R2 0.087.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Sour cream | retail_farmgate_observed | Spread / margin**
Result: Sour cream | Retail observed / FarmGateUA | linear: lag-spread -0.366 (p <0.001), upstream+ 0.016 (p 0.996), upstream- -4.351 (p 0.264), asym p 0.279, R2 0.264.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **Sour cream | retail_farmgate_baseline | Spread / margin**
Result: Sour cream | Retail baseline / FarmGateUA | linear: lag-spread -0.459 (p <0.001), upstream+ -6.069 (p 0.147), upstream- -4.888 (p 0.168), asym p 0.758, R2 0.270.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **Sour cream | producer_farmgate | Spread / margin**
Result: Sour cream | ProducerUA / FarmGateUA | linear: lag-spread -0.000 (p 0.900), upstream+ 0.109 (p 0.261), upstream- 0.150 (p 0.331), asym p 0.810, R2 0.004.
**This spread does not deliver strong margin-management evidence in statistical terms, so it should be treated as weak or descriptive.**

1. **Sour cream | retail_farmgate_observed | Spread / margin**
Result: Sour cream | Retail observed / FarmGateUA | linear: lag-spread -0.424 (p <0.001), upstream+ 3.265 (p 0.488), upstream- -10.972 (p 0.140), asym p 0.044, R2 0.321.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Sour cream | retail_farmgate_baseline | Spread / margin**
Result: Sour cream | Retail baseline / FarmGateUA | linear: lag-spread -0.518 (p <0.001), upstream+ -3.505 (p 0.534), upstream- -11.757 (p 0.118), asym p 0.241, R2 0.334.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **Sour cream | procurement_producer | Spread / margin**
Result: Sour cream | ProZorro / ProducerUA | linear: lag-spread -0.519 (p <0.001), upstream+ -1.290 (p 0.760), upstream- 6.389 (p 0.170), asym p 0.215, R2 0.261.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **Sour cream | retail_procurement_observed | Spread / margin**
Result: Sour cream | Retail observed / ProZorro | linear: lag-spread -0.097 (p 0.004), upstream+ -0.942 (p <0.001), upstream- 0.983 (p <0.001), asym p <0.001, R2 0.953.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Sour cream | retail_procurement_baseline | Spread / margin**
Result: Sour cream | Retail baseline / ProZorro | linear: lag-spread -0.101 (p 0.001), upstream+ -0.940 (p <0.001), upstream- 1.028 (p <0.001), asym p <0.001, R2 0.951.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Sour cream | retail_matched_procurement_observed | Spread / margin**
Result: Sour cream | Retail matched observed / ProZorro | linear: lag-spread -0.211 (p <0.001), upstream+ -0.852 (p <0.001), upstream- 1.085 (p <0.001), asym p <0.001, R2 0.857.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Sour cream | retail_matched_procurement_baseline | Spread / margin**
Result: Sour cream | Retail matched baseline / ProZorro | linear: lag-spread -0.207 (p 0.003), upstream+ -0.853 (p <0.001), upstream- 1.122 (p <0.001), asym p <0.001, R2 0.879.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Sour cream | silpo_procurement_observed | Spread / margin**
Result: Sour cream | Silpo observed / ProZorro | linear: lag-spread -0.068 (p 0.032), upstream+ -0.948 (p <0.001), upstream- 0.987 (p <0.001), asym p <0.001, R2 0.943.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Sour cream | silpo_procurement_baseline | Spread / margin**
Result: Sour cream | Silpo baseline / ProZorro | linear: lag-spread -0.092 (p <0.001), upstream+ -0.947 (p <0.001), upstream- 1.015 (p <0.001), asym p <0.001, R2 0.934.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Sour cream | retail_optimal_procurement_observed | Spread / margin**
Result: Sour cream | Retail optimal observed / ProZorro | linear: lag-spread -0.097 (p 0.004), upstream+ -0.942 (p <0.001), upstream- 0.983 (p <0.001), asym p <0.001, R2 0.953.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Sour cream | retail_optimal_procurement_baseline | Spread / margin**
Result: Sour cream | Retail optimal baseline / ProZorro | linear: lag-spread -0.101 (p 0.001), upstream+ -0.940 (p <0.001), upstream- 1.028 (p <0.001), asym p <0.001, R2 0.951.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Sour cream | producer_farmgate | Spread / margin**
Result: Sour cream | ProducerUA / FarmGateUA | pchip: lag-spread 0.001 (p 0.680), upstream+ -0.281 (p <0.001), upstream- 0.325 (p 0.002), asym p <0.001, R2 0.091.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Sour cream | retail_farmgate_observed | Spread / margin**
Result: Sour cream | Retail observed / FarmGateUA | pchip: lag-spread -0.368 (p <0.001), upstream+ -5.066 (p 0.076), upstream- -7.816 (p 0.011), asym p 0.383, R2 0.298.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **Sour cream | retail_farmgate_baseline | Spread / margin**
Result: Sour cream | Retail baseline / FarmGateUA | pchip: lag-spread -0.469 (p <0.001), upstream+ -7.970 (p 0.022), upstream- -6.402 (p 0.004), asym p 0.642, R2 0.290.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **Sour cream | producer_farmgate | Spread / margin**
Result: Sour cream | ProducerUA / FarmGateUA | pchip: lag-spread -0.000 (p 0.880), upstream+ 0.110 (p 0.256), upstream- 0.135 (p 0.374), asym p 0.881, R2 0.004.
**This spread does not deliver strong margin-management evidence in statistical terms, so it should be treated as weak or descriptive.**

1. **Sour cream | retail_farmgate_observed | Spread / margin**
Result: Sour cream | Retail observed / FarmGateUA | pchip: lag-spread -0.425 (p <0.001), upstream+ -1.244 (p 0.768), upstream- -17.097 (p <0.001), asym p 0.004, R2 0.350.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Sour cream | retail_farmgate_baseline | Spread / margin**
Result: Sour cream | Retail baseline / FarmGateUA | pchip: lag-spread -0.522 (p <0.001), upstream+ -4.862 (p 0.376), upstream- -13.611 (p 0.003), asym p 0.122, R2 0.346.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **Sour cream | procurement_producer | Spread / margin**
Result: Sour cream | ProZorro / ProducerUA | pchip: lag-spread -0.524 (p <0.001), upstream+ 1.058 (p 0.744), upstream- 7.630 (p 0.044), asym p 0.210, R2 0.262.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **Sour cream | retail_procurement_observed | Spread / margin**
Result: Sour cream | Retail observed / ProZorro | pchip: lag-spread -0.097 (p 0.004), upstream+ -0.942 (p <0.001), upstream- 0.983 (p <0.001), asym p <0.001, R2 0.953.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Sour cream | retail_procurement_baseline | Spread / margin**
Result: Sour cream | Retail baseline / ProZorro | pchip: lag-spread -0.101 (p 0.001), upstream+ -0.940 (p <0.001), upstream- 1.028 (p <0.001), asym p <0.001, R2 0.951.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Sour cream | retail_matched_procurement_observed | Spread / margin**
Result: Sour cream | Retail matched observed / ProZorro | pchip: lag-spread -0.211 (p <0.001), upstream+ -0.852 (p <0.001), upstream- 1.085 (p <0.001), asym p <0.001, R2 0.857.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Sour cream | retail_matched_procurement_baseline | Spread / margin**
Result: Sour cream | Retail matched baseline / ProZorro | pchip: lag-spread -0.207 (p 0.003), upstream+ -0.853 (p <0.001), upstream- 1.122 (p <0.001), asym p <0.001, R2 0.879.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Sour cream | silpo_procurement_observed | Spread / margin**
Result: Sour cream | Silpo observed / ProZorro | pchip: lag-spread -0.068 (p 0.032), upstream+ -0.948 (p <0.001), upstream- 0.987 (p <0.001), asym p <0.001, R2 0.943.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Sour cream | silpo_procurement_baseline | Spread / margin**
Result: Sour cream | Silpo baseline / ProZorro | pchip: lag-spread -0.092 (p <0.001), upstream+ -0.947 (p <0.001), upstream- 1.015 (p <0.001), asym p <0.001, R2 0.934.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Sour cream | retail_optimal_procurement_observed | Spread / margin**
Result: Sour cream | Retail optimal observed / ProZorro | pchip: lag-spread -0.097 (p 0.004), upstream+ -0.942 (p <0.001), upstream- 0.983 (p <0.001), asym p <0.001, R2 0.953.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Sour cream | retail_optimal_procurement_baseline | Spread / margin**
Result: Sour cream | Retail optimal baseline / ProZorro | pchip: lag-spread -0.101 (p 0.001), upstream+ -0.940 (p <0.001), upstream- 1.028 (p <0.001), asym p <0.001, R2 0.951.
**This spread behaves asymmetrically, which is consistent with managed downstream adjustment rather than a purely passive markup.**

1. **Yogurt / dessert | retail_farmgate_observed | Spread / margin**
Result: Yogurt / dessert | Retail observed / FarmGateUA | linear: lag-spread -0.344 (p <0.001), upstream+ -2.864 (p 0.595), upstream- 2.556 (p 0.555), asym p 0.310, R2 0.257.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **Yogurt / dessert | retail_farmgate_baseline | Spread / margin**
Result: Yogurt / dessert | Retail baseline / FarmGateUA | linear: lag-spread -0.406 (p <0.001), upstream+ -3.388 (p 0.590), upstream- 4.772 (p 0.361), asym p 0.242, R2 0.367.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **Yogurt / dessert | retail_farmgate_observed | Spread / margin**
Result: Yogurt / dessert | Retail observed / FarmGateUA | linear: lag-spread -0.339 (p <0.001), upstream+ -1.643 (p 0.847), upstream- 4.341 (p 0.677), asym p 0.493, R2 0.257.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **Yogurt / dessert | retail_farmgate_baseline | Spread / margin**
Result: Yogurt / dessert | Retail baseline / FarmGateUA | linear: lag-spread -0.400 (p <0.001), upstream+ -4.250 (p 0.657), upstream- 6.549 (p 0.570), asym p 0.324, R2 0.372.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **Yogurt / dessert | retail_farmgate_observed | Spread / margin**
Result: Yogurt / dessert | Retail observed / FarmGateUA | pchip: lag-spread -0.346 (p <0.001), upstream+ -4.175 (p 0.328), upstream- 2.284 (p 0.468), asym p 0.173, R2 0.259.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **Yogurt / dessert | retail_farmgate_baseline | Spread / margin**
Result: Yogurt / dessert | Retail baseline / FarmGateUA | pchip: lag-spread -0.408 (p <0.001), upstream+ -4.131 (p 0.411), upstream- 4.659 (p 0.266), asym p 0.165, R2 0.369.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **Yogurt / dessert | retail_farmgate_observed | Spread / margin**
Result: Yogurt / dessert | Retail observed / FarmGateUA | pchip: lag-spread -0.343 (p <0.001), upstream+ -1.624 (p 0.845), upstream- 6.240 (p 0.512), asym p 0.309, R2 0.259.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

1. **Yogurt / dessert | retail_farmgate_baseline | Spread / margin**
Result: Yogurt / dessert | Retail baseline / FarmGateUA | pchip: lag-spread -0.405 (p <0.001), upstream+ -2.906 (p 0.749), upstream- 9.906 (p 0.378), asym p 0.223, R2 0.375.
**This spread mean-reverts significantly, so the margin adjusts systematically even without strong asymmetry.**

## Silpo discount-strategy results

1. **CHEESE | Silpo discount strategy**
Result: CHEESE: discount share 0.008, lag discount 0.042 (p 0.643), retail-consumer gap -0.251 (p <0.001), Silpo-Novus gap -0.006 (p 0.504), R2 0.829.
**This product shows a retained discount-strategy signal, meaning markdown policy helps explain how visible retail pass-through is managed.**

1. **Drinking milk / fermented milk | Silpo discount strategy**
Result: Drinking milk / fermented milk: discount share 0.008, lag discount 0.250 (p 0.053), retail-consumer gap 0.444 (p <0.001), Silpo-Novus gap 0.041 (p 0.002), R2 0.841.
**This product shows a retained discount-strategy signal, meaning markdown policy helps explain how visible retail pass-through is managed.**

1. **Yogurt / dessert | Silpo discount strategy**
Result: Yogurt / dessert: discount share 0.009, lag discount 0.601 (p <0.001), retail-consumer gap  (p ), Silpo-Novus gap 0.018 (p 0.265), R2 0.360.
**This product does not retain a full discount-strategy signal, so discounting is present but not strongly systematic in the final specification.**

## Procurement-scale results

1. **Butter | Procurement scale**
Result: Butter: lag price -0.443 (p <0.001), d producer -1.066 (p 0.032), d expected -0.560 (p <0.001), d sum initial 0.657 (p 0.020), d sum current -0.124 (p 0.529), R2 0.525.
**This product retains a procurement-scale signal, meaning contract scale modifies procurement price adjustment rather than merely accompanying it.**

1. **CHEESE | Procurement scale**
Result: CHEESE: lag price -0.957 (p <0.001), d producer -1.520 (p 0.240), d expected -0.103 (p 0.392), d sum initial -0.110 (p 0.721), d sum current 0.199 (p 0.432), R2 0.487.
**This product does not retain a strong procurement-scale signal, so the trade-scale variables remain informative but not decisive here.**

1. **Condensed milk | Procurement scale**
Result: Condensed milk: lag price -1.363 (p <0.001), d producer  (p ), d expected -0.436 (p 0.014), d sum initial 0.385 (p 0.497), d sum current 0.040 (p 0.934), R2 0.691.
**This product retains a procurement-scale signal, meaning contract scale modifies procurement price adjustment rather than merely accompanying it.**

1. **Cream | Procurement scale**
Result: Cream: lag price -0.612 (p <0.001), d producer  (p ), d expected 0.045 (p 0.805), d sum initial -0.239 (p 0.129), d sum current 0.184 (p 0.058), R2 0.405.
**This product retains a procurement-scale signal, meaning contract scale modifies procurement price adjustment rather than merely accompanying it.**

1. **Drinking milk / fermented milk | Procurement scale**
Result: Drinking milk / fermented milk: lag price -0.931 (p <0.001), d producer 0.176 (p 0.837), d expected -0.408 (p <0.001), d sum initial 0.446 (p <0.001), d sum current -0.047 (p 0.485), R2 0.732.
**This product retains a procurement-scale signal, meaning contract scale modifies procurement price adjustment rather than merely accompanying it.**

1. **Sour cream | Procurement scale**
Result: Sour cream: lag price -0.541 (p <0.001), d producer 0.066 (p 0.926), d expected -0.475 (p 0.003), d sum initial 1.268 (p <0.001), d sum current -0.771 (p <0.001), R2 0.640.
**This product retains a procurement-scale signal, meaning contract scale modifies procurement price adjustment rather than merely accompanying it.**

## Aggregate dairy-index robustness results

1. **Index FarmGate -> Producer | Aggregate index ECM**
Result: Index FarmGate -> Producer | ECM | weekly_raw: coef 0.883, ECT -0.049, p <0.001, reliability conditionally_usable.
**This aggregate-index equation is a robustness check on system-wide dairy dynamics rather than the main identification result, but it helps verify whether the broad transmission story survives aggregation.**

1. **Index FarmGate -> Producer | Aggregate index NARDL**
Result: Index FarmGate -> Producer | NARDL | weekly_raw: coef -0.132, ECT -0.052, p 0.001, reliability conditionally_usable.
**This aggregate-index equation is a robustness check on system-wide dairy dynamics rather than the main identification result, but it helps verify whether the broad transmission story survives aggregation.**

1. **Index FarmGate -> Producer | Aggregate index ECM**
Result: Index FarmGate -> Producer | ECM | weekly_smoothed: coef 0.884, ECT -0.046, p <0.001, reliability reliable.
**This aggregate-index equation is a robustness check on system-wide dairy dynamics rather than the main identification result, but it helps verify whether the broad transmission story survives aggregation.**

1. **Index FarmGate -> Producer | Aggregate index NARDL**
Result: Index FarmGate -> Producer | NARDL | weekly_smoothed: coef -0.069, ECT -0.047, p <0.001, reliability conditionally_usable.
**This aggregate-index equation is a robustness check on system-wide dairy dynamics rather than the main identification result, but it helps verify whether the broad transmission story survives aggregation.**

1. **Index Producer -> Procurement | Aggregate index ECM**
Result: Index Producer -> Procurement | ECM | weekly_raw: coef 0.883, ECT -1.315, p <0.001, reliability reliable.
**This aggregate-index equation is a robustness check on system-wide dairy dynamics rather than the main identification result, but it helps verify whether the broad transmission story survives aggregation.**

1. **Index Producer -> Procurement | Aggregate index NARDL**
Result: Index Producer -> Procurement | NARDL | weekly_raw: coef 1.271, ECT -1.601, p <0.001, reliability reliable.
**This aggregate-index equation is a robustness check on system-wide dairy dynamics rather than the main identification result, but it helps verify whether the broad transmission story survives aggregation.**

1. **Index Producer -> Procurement | Aggregate index ECM**
Result: Index Producer -> Procurement | ECM | weekly_smoothed: coef 0.866, ECT -0.566, p <0.001, reliability reliable.
**This aggregate-index equation is a robustness check on system-wide dairy dynamics rather than the main identification result, but it helps verify whether the broad transmission story survives aggregation.**

1. **Index Producer -> Procurement | Aggregate index NARDL**
Result: Index Producer -> Procurement | NARDL | weekly_smoothed: coef 1.427, ECT -0.694, p <0.001, reliability reliable.
**This aggregate-index equation is a robustness check on system-wide dairy dynamics rather than the main identification result, but it helps verify whether the broad transmission story survives aggregation.**

1. **Index FarmGate -> Downstream extension | Aggregate index ECM**
Result: Index FarmGate -> Downstream extension | ECM | weekly_raw: coef 1.156, ECT -0.213, p 0.006, reliability reliable.
**This aggregate-index equation is a robustness check on system-wide dairy dynamics rather than the main identification result, but it helps verify whether the broad transmission story survives aggregation.**

1. **Index FarmGate -> Downstream extension | Aggregate index NARDL**
Result: Index FarmGate -> Downstream extension | NARDL | weekly_raw: coef 1.422, ECT -0.277, p 0.085, reliability conditionally_usable.
**This aggregate-index equation is a robustness check on system-wide dairy dynamics rather than the main identification result, but it helps verify whether the broad transmission story survives aggregation.**

1. **Index FarmGate -> Downstream extension | Aggregate index ECM**
Result: Index FarmGate -> Downstream extension | ECM | weekly_smoothed: coef 1.159, ECT -0.153, p 0.007, reliability reliable.
**This aggregate-index equation is a robustness check on system-wide dairy dynamics rather than the main identification result, but it helps verify whether the broad transmission story survives aggregation.**

1. **Index FarmGate -> Downstream extension | Aggregate index NARDL**
Result: Index FarmGate -> Downstream extension | NARDL | weekly_smoothed: coef 0.636, ECT -0.161, p 0.054, reliability conditionally_usable.
**This aggregate-index equation is a robustness check on system-wide dairy dynamics rather than the main identification result, but it helps verify whether the broad transmission story survives aggregation.**

1. **Index Producer -> Downstream extension | Aggregate index NARDL**
Result: Index Producer -> Downstream extension | NARDL | weekly_raw: coef 1.531, ECT -0.345, p 0.036, reliability reliable.
**This aggregate-index equation is a robustness check on system-wide dairy dynamics rather than the main identification result, but it helps verify whether the broad transmission story survives aggregation.**

1. **Index Producer -> Downstream extension | Aggregate index NARDL**
Result: Index Producer -> Downstream extension | NARDL | weekly_smoothed: coef 1.419, ECT -0.240, p 0.051, reliability conditionally_usable.
**This aggregate-index equation is a robustness check on system-wide dairy dynamics rather than the main identification result, but it helps verify whether the broad transmission story survives aggregation.**

1. **Index Procurement -> Downstream extension | Aggregate index NARDL**
Result: Index Procurement -> Downstream extension | NARDL | weekly_raw: coef -1.254, ECT -0.671, p 0.011, reliability conditionally_usable.
**This aggregate-index equation is a robustness check on system-wide dairy dynamics rather than the main identification result, but it helps verify whether the broad transmission story survives aggregation.**

1. **Index Procurement -> Downstream extension | Aggregate index NARDL**
Result: Index Procurement -> Downstream extension | NARDL | weekly_smoothed: coef -1.205, ECT -0.534, p 0.001, reliability conditionally_usable.
**This aggregate-index equation is a robustness check on system-wide dairy dynamics rather than the main identification result, but it helps verify whether the broad transmission story survives aggregation.**

## VECM and system-feasibility results

1. **Butter | full_chain | VECM feasibility**
Result: Butter | full_chain: status infeasible, reason too_short, n 0.
**This system is not feasible on the corrected overlap, which is itself a substantive result limiting any full-chain equilibrium claim at product level.**

1. **Butter | full_chain_smoothed | VECM feasibility**
Result: Butter | full_chain_smoothed: status infeasible, reason too_short, n 0.
**This system is not feasible on the corrected overlap, which is itself a substantive result limiting any full-chain equilibrium claim at product level.**

1. **Butter | staged_chain | VECM feasibility**
Result: Butter | staged_chain: status infeasible, reason too_short, n 11.
**This system is not feasible on the corrected overlap, which is itself a substantive result limiting any full-chain equilibrium claim at product level.**

1. **CHEESE | full_chain | VECM feasibility**
Result: CHEESE | full_chain: status infeasible, reason too_short, n 11.
**This system is not feasible on the corrected overlap, which is itself a substantive result limiting any full-chain equilibrium claim at product level.**

1. **CHEESE | full_chain_smoothed | VECM feasibility**
Result: CHEESE | full_chain_smoothed: status ok, reason , n 41.
**This system is feasible and can be used as interdependent chain evidence, although it still remains secondary to the retained pairwise design.**

1. **CHEESE | staged_chain | VECM feasibility**
Result: CHEESE | staged_chain: status infeasible, reason too_short, n 11.
**This system is not feasible on the corrected overlap, which is itself a substantive result limiting any full-chain equilibrium claim at product level.**

1. **Condensed milk | full_chain | VECM feasibility**
Result: Condensed milk | full_chain: status infeasible, reason too_short, n 0.
**This system is not feasible on the corrected overlap, which is itself a substantive result limiting any full-chain equilibrium claim at product level.**

1. **Condensed milk | full_chain_smoothed | VECM feasibility**
Result: Condensed milk | full_chain_smoothed: status infeasible, reason too_short, n 0.
**This system is not feasible on the corrected overlap, which is itself a substantive result limiting any full-chain equilibrium claim at product level.**

1. **Condensed milk | staged_chain | VECM feasibility**
Result: Condensed milk | staged_chain: status infeasible, reason too_short, n 0.
**This system is not feasible on the corrected overlap, which is itself a substantive result limiting any full-chain equilibrium claim at product level.**

1. **Cream | full_chain | VECM feasibility**
Result: Cream | full_chain: status infeasible, reason too_short, n 0.
**This system is not feasible on the corrected overlap, which is itself a substantive result limiting any full-chain equilibrium claim at product level.**

1. **Cream | full_chain_smoothed | VECM feasibility**
Result: Cream | full_chain_smoothed: status infeasible, reason too_short, n 0.
**This system is not feasible on the corrected overlap, which is itself a substantive result limiting any full-chain equilibrium claim at product level.**

1. **Cream | staged_chain | VECM feasibility**
Result: Cream | staged_chain: status infeasible, reason too_short, n 0.
**This system is not feasible on the corrected overlap, which is itself a substantive result limiting any full-chain equilibrium claim at product level.**

1. **Drinking milk / fermented milk | full_chain | VECM feasibility**
Result: Drinking milk / fermented milk | full_chain: status infeasible, reason too_short, n 11.
**This system is not feasible on the corrected overlap, which is itself a substantive result limiting any full-chain equilibrium claim at product level.**

1. **Drinking milk / fermented milk | full_chain_smoothed | VECM feasibility**
Result: Drinking milk / fermented milk | full_chain_smoothed: status ok, reason , n 41.
**This system is feasible and can be used as interdependent chain evidence, although it still remains secondary to the retained pairwise design.**

1. **Drinking milk / fermented milk | staged_chain | VECM feasibility**
Result: Drinking milk / fermented milk | staged_chain: status infeasible, reason too_short, n 11.
**This system is not feasible on the corrected overlap, which is itself a substantive result limiting any full-chain equilibrium claim at product level.**

1. **Milk powder | full_chain | VECM feasibility**
Result: Milk powder | full_chain: status infeasible, reason too_short, n 0.
**This system is not feasible on the corrected overlap, which is itself a substantive result limiting any full-chain equilibrium claim at product level.**

1. **Milk powder | full_chain_smoothed | VECM feasibility**
Result: Milk powder | full_chain_smoothed: status infeasible, reason too_short, n 0.
**This system is not feasible on the corrected overlap, which is itself a substantive result limiting any full-chain equilibrium claim at product level.**

1. **Milk powder | staged_chain | VECM feasibility**
Result: Milk powder | staged_chain: status infeasible, reason too_short, n 2.
**This system is not feasible on the corrected overlap, which is itself a substantive result limiting any full-chain equilibrium claim at product level.**

1. **Other | full_chain | VECM feasibility**
Result: Other | full_chain: status infeasible, reason too_short, n 0.
**This system is not feasible on the corrected overlap, which is itself a substantive result limiting any full-chain equilibrium claim at product level.**

1. **Other | full_chain_smoothed | VECM feasibility**
Result: Other | full_chain_smoothed: status infeasible, reason too_short, n 0.
**This system is not feasible on the corrected overlap, which is itself a substantive result limiting any full-chain equilibrium claim at product level.**

1. **Other | staged_chain | VECM feasibility**
Result: Other | staged_chain: status infeasible, reason too_short, n 0.
**This system is not feasible on the corrected overlap, which is itself a substantive result limiting any full-chain equilibrium claim at product level.**

1. **Sour cream | full_chain | VECM feasibility**
Result: Sour cream | full_chain: status infeasible, reason too_short, n 11.
**This system is not feasible on the corrected overlap, which is itself a substantive result limiting any full-chain equilibrium claim at product level.**

1. **Sour cream | full_chain_smoothed | VECM feasibility**
Result: Sour cream | full_chain_smoothed: status ok, reason , n 41.
**This system is feasible and can be used as interdependent chain evidence, although it still remains secondary to the retained pairwise design.**

1. **Sour cream | staged_chain | VECM feasibility**
Result: Sour cream | staged_chain: status infeasible, reason too_short, n 11.
**This system is not feasible on the corrected overlap, which is itself a substantive result limiting any full-chain equilibrium claim at product level.**

1. **Yogurt / dessert | full_chain | VECM feasibility**
Result: Yogurt / dessert | full_chain: status infeasible, reason too_short, n 0.
**This system is not feasible on the corrected overlap, which is itself a substantive result limiting any full-chain equilibrium claim at product level.**

1. **Yogurt / dessert | full_chain_smoothed | VECM feasibility**
Result: Yogurt / dessert | full_chain_smoothed: status infeasible, reason too_short, n 0.
**This system is not feasible on the corrected overlap, which is itself a substantive result limiting any full-chain equilibrium claim at product level.**

1. **Yogurt / dessert | staged_chain | VECM feasibility**
Result: Yogurt / dessert | staged_chain: status infeasible, reason too_short, n 0.
**This system is not feasible on the corrected overlap, which is itself a substantive result limiting any full-chain equilibrium claim at product level.**

## Figures used in FINAL_RESEARCH

### Project-level figure inventory

![01_panel_coverage.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/01_panel_coverage.png)
**This figure forms part of the final empirical evidence set and should be read together with the chapter interpretation.**

![02_lp_pass_through_horizons.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/02_lp_pass_through_horizons.png)
**This figure forms part of the final empirical evidence set and should be read together with the chapter interpretation.**

![03_forward_reverse_core_share.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/03_forward_reverse_core_share.png)
**This figure forms part of the final empirical evidence set and should be read together with the chapter interpretation.**

![04_vertical_spread_proxy.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/04_vertical_spread_proxy.png)
**This figure forms part of the final empirical evidence set and should be read together with the chapter interpretation.**

![05_discount_incidence.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/05_discount_incidence.png)
**This figure forms part of the final empirical evidence set and should be read together with the chapter interpretation.**

![06_cross_shop_match_status.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/06_cross_shop_match_status.png)
**This figure forms part of the final empirical evidence set and should be read together with the chapter interpretation.**

![07_retail_literal_mix.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/07_retail_literal_mix.png)
**This figure forms part of the final empirical evidence set and should be read together with the chapter interpretation.**

![08_dominant_brand_support.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/08_dominant_brand_support.png)
**This figure forms part of the final empirical evidence set and should be read together with the chapter interpretation.**

![09_retail_level_scores.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/09_retail_level_scores.png)
**This figure forms part of the final empirical evidence set and should be read together with the chapter interpretation.**

![10_optimal_retail_level.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/10_optimal_retail_level.png)
**This figure forms part of the final empirical evidence set and should be read together with the chapter interpretation.**

![11_candidate_downstream_core_share.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/11_candidate_downstream_core_share.png)
**This figure forms part of the final empirical evidence set and should be read together with the chapter interpretation.**

![12_discount_environment.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/12_discount_environment.png)
**This figure forms part of the final empirical evidence set and should be read together with the chapter interpretation.**

![13_weekly_chain_overlay.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/13_weekly_chain_overlay.png)
**This figure forms part of the final empirical evidence set and should be read together with the chapter interpretation.**

![14_weekly_corr_scan.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/14_weekly_corr_scan.png)
**This figure forms part of the final empirical evidence set and should be read together with the chapter interpretation.**

![15_core_model_coefficients.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/15_core_model_coefficients.png)
**This figure forms part of the final empirical evidence set and should be read together with the chapter interpretation.**

![16_vecm_feasibility.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/16_vecm_feasibility.png)
**This figure forms part of the final empirical evidence set and should be read together with the chapter interpretation.**

![17_procurement_scale_effects.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/17_procurement_scale_effects.png)
**This figure forms part of the final empirical evidence set and should be read together with the chapter interpretation.**

![18_dataset_product_lines_and_indices.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/18_dataset_product_lines_and_indices.png)
**This figure forms part of the final empirical evidence set and should be read together with the chapter interpretation.**

![19_aggregate_chain_indices.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/19_aggregate_chain_indices.png)
**This figure forms part of the final empirical evidence set and should be read together with the chapter interpretation.**

![20_prozorro_region_profile.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/20_prozorro_region_profile.png)
**This figure forms part of the final empirical evidence set and should be read together with the chapter interpretation.**

![21_link21_status_matrix.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/21_link21_status_matrix.png)
**This figure forms part of the final empirical evidence set and should be read together with the chapter interpretation.**

![22_ecm_speed_of_adjustment.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/22_ecm_speed_of_adjustment.png)
**This figure forms part of the final empirical evidence set and should be read together with the chapter interpretation.**

![23_nardl_asymmetry.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/23_nardl_asymmetry.png)
**This figure forms part of the final empirical evidence set and should be read together with the chapter interpretation.**

![24_discount_coefficient_map.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/24_discount_coefficient_map.png)
**This figure forms part of the final empirical evidence set and should be read together with the chapter interpretation.**

![25_spread_levels.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/25_spread_levels.png)
**This figure forms part of the final empirical evidence set and should be read together with the chapter interpretation.**

![26_spread_volatility.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/26_spread_volatility.png)
**This figure forms part of the final empirical evidence set and should be read together with the chapter interpretation.**

![27_reliability_overview.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/27_reliability_overview.png)
**This figure forms part of the final empirical evidence set and should be read together with the chapter interpretation.**

![28_aggregate_index_overlay.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/28_aggregate_index_overlay.png)
**This figure forms part of the final empirical evidence set and should be read together with the chapter interpretation.**

![29_aggregate_index_model_coefficients.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/29_aggregate_index_model_coefficients.png)
**This figure forms part of the final empirical evidence set and should be read together with the chapter interpretation.**

![30_farmgate_to_chain_normalized.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/30_farmgate_to_chain_normalized.png)
**This figure forms part of the final empirical evidence set and should be read together with the chapter interpretation.**

![31_farmgate_lag_map.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/31_farmgate_lag_map.png)
**This figure forms part of the final empirical evidence set and should be read together with the chapter interpretation.**

![32_farmgate_chain_coefficients.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/32_farmgate_chain_coefficients.png)
**This figure forms part of the final empirical evidence set and should be read together with the chapter interpretation.**

### Chapter 5 figures

![01_raw_government_layers.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/chapter5_data/01_raw_government_layers.png)
**This figure establishes the corrected national governmental price paths before any modelling transformation.**

![02_raw_retail_observed_series.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/chapter5_data/02_raw_retail_observed_series.png)
**This figure shows observed retail package prices and makes the downstream price object explicit.**

![03_raw_external_benchmarks.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/chapter5_data/03_raw_external_benchmarks.png)
**This figure places the Ukrainian dairy chain against European and CME benchmark dynamics.**

![04_dataset_product_lines_and_indices.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/chapter5_data/04_dataset_product_lines_and_indices.png)
**This figure connects product-level series with aggregate dairy indices.**

![05_aggregate_chain_indices.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/chapter5_data/05_aggregate_chain_indices.png)
**This figure shows the latent chain-level dairy indices used as system robustness checks.**

![06_panel_coverage.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/chapter5_data/06_panel_coverage.png)
**This figure summarizes how much aligned support exists for each chain stage before estimation.**

![07_cross_shop_match_status.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/chapter5_data/07_cross_shop_match_status.png)
**This figure shows how much of the retail universe can be matched across Silpo and Novus.**

![07_retail_product_distribution.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/chapter5_data/07_retail_product_distribution.png)
**This figure shows the product distribution across the two retailers.**

![08_retail_brand_distribution.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/chapter5_data/08_retail_brand_distribution.png)
**This figure shows how brand support is distributed across Silpo and Novus.**

![10_prozorro_region_profile.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/chapter5_data/10_prozorro_region_profile.png)
**This figure shows regional procurement concentration inside ProZorro.**

![11_silpo_discount_environment.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/chapter5_data/11_silpo_discount_environment.png)
**This figure isolates the explicit Silpo markdown environment.**

![12_weekly_chain_overlay.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/chapter5_data/12_weekly_chain_overlay.png)
**This figure shows the weekly median chain paths for the main dairy products.**

![13_farmgate_benchmark_block.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/chapter5_data/13_farmgate_benchmark_block.png)
**This figure compares farm-gate raw milk with chain-level dairy indices.**

![13_retail_level_scores.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/chapter5_data/13_retail_level_scores.png)
**This figure forms part of the final empirical evidence set and should be read together with the chapter interpretation.**

![14_benchmark_correlations.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/chapter5_data/14_benchmark_correlations.png)
**This figure forms part of the final empirical evidence set and should be read together with the chapter interpretation.**

![14_optimal_retail_level.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/chapter5_data/14_optimal_retail_level.png)
**This figure forms part of the final empirical evidence set and should be read together with the chapter interpretation.**

![15_farmgate_to_chain_normalized.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/chapter5_data/15_farmgate_to_chain_normalized.png)
**This figure forms part of the final empirical evidence set and should be read together with the chapter interpretation.**

### Chapter 6 figures

![01_weekly_corr_scan.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/chapter6_results/01_weekly_corr_scan.png)
**This figure summarizes the strongest lag-correlation signals before weekly model retention.**

![02_link21_status_matrix.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/chapter6_results/02_link21_status_matrix.png)
**This figure synthesizes the full 21-link directional model design.**

![03_core_model_coefficients.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/chapter6_results/03_core_model_coefficients.png)
**This figure compares retained weekly coefficients across model families and products.**

![04_ecm_speed_of_adjustment.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/chapter6_results/04_ecm_speed_of_adjustment.png)
**This figure shows how quickly retained ECM equations move back toward equilibrium.**

![05_nardl_asymmetry.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/chapter6_results/05_nardl_asymmetry.png)
**This figure shows asymmetric long-run evidence in retained weekly NARDL models.**

![06_lp_pass_through_horizons.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/chapter6_results/06_lp_pass_through_horizons.png)
**This figure summarizes daily pass-through by response horizon.**

![07_forward_reverse_core_share.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/chapter6_results/07_forward_reverse_core_share.png)
**This figure compares forward and reverse daily timing evidence.**

![08_candidate_downstream_core_share.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/chapter6_results/08_candidate_downstream_core_share.png)
**This figure compares downstream endpoint candidates on daily core evidence.**

![08_spread_levels.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/chapter6_results/08_spread_levels.png)
**This figure shows average vertical spread levels across chain segments.**

![09_spread_volatility.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/chapter6_results/09_spread_volatility.png)
**This figure shows volatility differences across chain spreads.**

![10_vecm_feasibility.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/chapter6_results/10_vecm_feasibility.png)
**This figure reports the feasibility boundary for VECM system estimation.**

![10_vertical_spread_proxy.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/chapter6_results/10_vertical_spread_proxy.png)
**This figure summarizes the market-power proxy evidence from spread equations.**

![11_aggregate_index_overlay.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/chapter6_results/11_aggregate_index_overlay.png)
**This figure overlays the aggregate dairy indices used in the system-robustness block.**

![11_discount_incidence.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/chapter6_results/11_discount_incidence.png)
**This figure shows discount incidence by product where markdown states are observed.**

![12_discount_coefficient_map.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/chapter6_results/12_discount_coefficient_map.png)
**This figure summarizes the retained discount-model coefficients.**

![13_procurement_scale_effects.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/chapter6_results/13_procurement_scale_effects.png)
**This figure visualizes the procurement-scale coefficient block.**

![14_aggregate_index_model_coefficients.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/chapter6_results/14_aggregate_index_model_coefficients.png)
**This figure summarizes aggregate-index model coefficients.**

![15_reliability_overview.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/chapter6_results/15_reliability_overview.png)
**This figure shows the reliability distribution across model blocks.**

![16_farmgate_lag_map.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/chapter6_results/16_farmgate_lag_map.png)
**This figure forms part of the final empirical evidence set and should be read together with the chapter interpretation.**

![17_farmgate_chain_coefficients.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/chapter6_results/17_farmgate_chain_coefficients.png)
**This figure forms part of the final empirical evidence set and should be read together with the chapter interpretation.**

### Execution-sequence figures

![01_raw_government_layers.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/sequence/01_raw_government_layers.png)
**This figure establishes the corrected national governmental price paths before any modelling transformation.**

![02_raw_retail_observed_series.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/sequence/02_raw_retail_observed_series.png)
**This figure shows observed retail package prices and makes the downstream price object explicit.**

![03_raw_external_benchmarks.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/sequence/03_raw_external_benchmarks.png)
**This figure places the Ukrainian dairy chain against European and CME benchmark dynamics.**

![05_transformed_weekly_chain_overlay.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/sequence/05_transformed_weekly_chain_overlay.png)
**This figure forms part of the final empirical evidence set and should be read together with the chapter interpretation.**

![06_weekly_lag_correlation_scan.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/sequence/06_weekly_lag_correlation_scan.png)
**This figure forms part of the final empirical evidence set and should be read together with the chapter interpretation.**

![08_core_weekly_model_coefficients.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/sequence/08_core_weekly_model_coefficients.png)
**This figure forms part of the final empirical evidence set and should be read together with the chapter interpretation.**

![09_vecm_system_feasibility.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/sequence/09_vecm_system_feasibility.png)
**This figure forms part of the final empirical evidence set and should be read together with the chapter interpretation.**

![12_procurement_scale_effects.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/sequence/12_procurement_scale_effects.png)
**This figure forms part of the final empirical evidence set and should be read together with the chapter interpretation.**

![13_farmgate_benchmark_block.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/sequence/13_farmgate_benchmark_block.png)
**This figure compares farm-gate raw milk with chain-level dairy indices.**

![14_benchmark_correlations.png](/Users/getapple/Documents/KSE/Master Thesis/FINAL_RESEARCH/figures/sequence/14_benchmark_correlations.png)
**This figure forms part of the final empirical evidence set and should be read together with the chapter interpretation.**
