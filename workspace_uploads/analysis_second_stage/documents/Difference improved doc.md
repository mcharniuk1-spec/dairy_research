# Difference improved doc

## Compared files
- `data_estiamtion_updated_conclusion.docx` is the broader RW4 estimation chapter built around ARDL/ECM/NARDL/VECM and the full rerun output tree.
- `analysis second stage/documents/second_stage_estimation_summary.docx` is the shorter second-stage robustness redesign built around deeper retail item harmonization, local projections, spread equations, discount controls, and the ConsumerUA-linked endpoint.

## Bottom-line difference
The old document is the main thesis-style estimation narrative. It treats equilibrium correction as the core evidence and uses the full RW4 model hierarchy. The new second-stage summary is narrower by design: it rechecks the same economic chain with a different identification logic and with deeper retailer-level preparation. Its value is not that it replaces the RW4 chapter, but that it stress-tests it with a different data build and a different model family.

## Data-preparation comparison
- Old RW4 chapter: retail is prepared mainly at the category and chain level, then extended into `Retail_combined` and `Retail_combined_core` with a ConsumerUA anchor. It emphasizes overlap, admissibility, benchmark alignment, and baseline-versus-observed retail prices.
- New second-stage summary: retail is prepared first at item level. Novus and Silpo products are harmonized by normalized brand, cleaned product name, standardized dairy type, discount state, fat field, and pack metadata before category aggregation.
- New second-stage improvement: effective price already includes the discount, but discount amount, discount type, discount dummy, markdown depth, baseline price, and unit-price variants are retained as separate modeling variables.
- New second-stage improvement: the combined retailer catalog now identifies 187 harmonized item keys observed in both shops, alongside 1263 Silpo-only and 980 Novus-only keys. This is materially deeper retailer cleaning than the old chapter describes explicitly.
- Same point across both documents: retail data must not be treated as a frictionless cost-plus series. Both documents read retail as a managed pricing layer.
- Interpretation difference: the old chapter frames ConsumerUA mainly as an external or anchored downstream environment; the second-stage summary keeps that caution but makes `Retail+Consumer` a formal robustness endpoint rather than the main retail definition.

## Model-by-model comparison
### 1. ARDL in the old chapter vs local projections in the second-stage summary
- Old RW4 approach: ARDL is used as a distributed-lag benchmark when a stable long-run relation is plausible. It is link-specific and coefficient-rich, with explicit short-run and long-run terms.
- New second-stage approach: local projections estimate cumulative downstream responses at horizons 0, 1, 3, 7, 14, and 21 days with HAC inference. This avoids committing each link to one lag-polynomial structure.
- Same interpretation: both approaches find that transmission is delayed, product-specific, and not well summarized by a same-day elasticity.
- Difference in interpretation: ARDL is read structurally, as a candidate long-run dynamic relation. The local-projection redesign is read more cautiously, as horizon-specific evidence on timing and directional response. In the second stage, 2082 linear LP equations are estimated and 465 pass the p<0.10 plus overlap screen (22.3%).

### 2. ECM in the old chapter vs spread adjustment in the second-stage summary
- Old RW4 approach: ECM is the core evidential model because negative and significant ECT terms are interpreted as equilibrium correction. The chapter explicitly treats speed of correction as the main economic object.
- New second-stage approach: vertical spread regressions replace explicit ECM leadership in the robustness run. The dependent variable is the change in the log spread between stages, with lagged spread and upstream shock terms.
- Same interpretation: both documents still say that the most meaningful evidence is adjustment over time, not a literal one-period pass-through coefficient.
- Difference in interpretation: the old chapter concludes with equilibrium re-anchoring language; the new summary translates that into market-power proxy language. Persistent or asymmetric spreads are treated as evidence consistent with timing control, category management, and margin smoothing rather than as direct proof of cointegrating equilibrium.
- Quantitative difference: the second stage reports 194 usable spread equations, with 38 persistent-margin flags and 111 asymmetric-margin flags.

### 3. NARDL in the old chapter vs asymmetric local projections in the second-stage summary
- Old RW4 approach: NARDL is used to test whether positive and negative upstream shocks have different short-run and long-run effects. It is central for claims about selective asymmetry, especially in hard cheese.
- New second-stage approach: asymmetry is checked in local projections by splitting current upstream shocks into positive and negative components at each horizon.
- Same interpretation: asymmetry is not universal. Both documents reject a simple market-wide rockets-and-feathers story and keep the reading product-specific.
- Difference in interpretation: the old chapter can make stronger long-run asymmetry statements because NARDL is an equilibrium model. The second-stage summary is more restrained and treats asymmetry as horizon-specific directional evidence inside a robustness redesign, not as the thesis main proof.

### 4. VECM in the old chapter vs no multivariate system core in the second-stage summary
- Old RW4 approach: VECM appears as a multivariate robustness check around the core chain logic.
- New second-stage approach: there is no direct VECM replacement. The redesign chooses simpler, more interpretable blocks: local projections, spread equations, and discount regressions.
- Same interpretation: both documents preserve the vertical chain logic.
- Difference in interpretation: the old chapter uses multivariate system evidence as a robustness layer for cointegration logic, while the new summary deliberately prioritizes transparent retailer-sensitive robustness over full-system estimation.

### 5. Old discount module vs new discount modeling
- Old RW4 approach: the discount module compares observed and baseline retail paths and concludes that promotions often work like a shock-absorption mechanism. It reports observed-versus-baseline coefficient differences and pseudo-asymmetry in 55.1% of rows.
- New second-stage approach: discount variables are embedded directly into the retail build and into the second-stage regressions. Effective price includes the markdown, but baseline price, discount amount, discount share, markdown depth, and discount-type dummies remain visible in the models.
- Same interpretation: both documents say discounts are part of the downstream adjustment mechanism rather than random noise.
- Difference in interpretation: the old chapter gives stronger discount evidence and reads promotions as an important smoothing mechanism in the RW4 system. The second-stage summary finds a weaker signal at this stage: only 4 usable discount equations and 0 formal discount-strategy signals. So the improved data preparation is stronger, but the reduced-form evidence is more cautious.

### 6. Old downstream endpoint vs new matched-retail and Retail+Consumer endpoint
- Old RW4 approach: downstream analysis relies on retailer-specific panels plus pooled retail and the anchored `Retail_combined` / `Retail_combined_core` constructs.
- New second-stage approach: the downstream side is rebuilt from the harmonized Novus-Silpo item catalog, then aggregated into retail observed, retail baseline, matched-cross-shop retail, and `Retail+Consumer` variants.
- Same interpretation: downstream evidence remains the part of the chain where market power and category management matter most.
- Difference in interpretation: the old chapter emphasizes pooled retailer panels and anchor design; the new summary adds explicit cross-shop item matching and a cleaner distinction between retailer-only support and consumer-linked support. Coverage now shows non-zero matched-retail support across all 9 product groups, typically around 48 to 56 daily observations per product in the overlap window.

## Link-level interpretation: what remains the same
- Both documents keep the chain logic `FarmGateUA -> ProducerUA -> ProZorro -> Retail` and both reject the idea of one universal pass-through coefficient.
- Both documents treat procurement as an institutional buffer rather than a frictionless conduit.
- Both documents argue that downstream power is expressed mainly through timing, smoothing, category management, and selective asymmetry.
- Both documents keep farm-gate interpretation conservative and reject strong literal product-level farm-to-shelf claims.

## Link-level interpretation: what changes in detail
- ProducerUA -> ProZorro: the old chapter makes stronger structural claims because ECM/NARDL repeatedly recover significant error-correction terms for butter, cream, and hard cheese. The second-stage summary still finds this link important, but now the evidence is framed through local-projection timing and spread persistence rather than through one equilibrium-correction coefficient.
- ProZorro -> Retail: the old chapter highlights product-level ECM/NARDL cases such as milk and pooled butter. The second-stage summary still supports downstream linkage, but it leans more heavily on selective 7- and 14-day LP responses and on margin behavior.
- Retail reverse-flow evidence: both documents see reverse information flow, but the second-stage summary makes that point even more explicit in the LP ranking, where `Retail -> FarmGateUA` and `Retail+Consumer -> FarmGateUA` appear among the strongest screened signals. That strengthens the retailer-mediated coordination reading, although it should still not be called literal causal reverse transmission.
- Farm-gate evidence: both documents remain cautious. The old chapter stresses that FarmGateUA is broad and variant-sensitive; the second-stage summary repeats that caution and explicitly warns that high farm-gate LP fit may reflect shared reconstruction smoothness rather than clean causal transmission.

## Practical reading for the thesis
- Use the old RW4 conclusion chapter as the main estimation narrative because it is fuller, model-richer, and more tightly connected to the thesis chapter structure.
- Use the new second-stage summary as the improvement and robustness narrative: it shows that after deeper Novus-Silpo product cleaning and explicit discount-aware retail construction, the main economic story still survives.
- Do not merge the two documents mechanically. Their strength is complementary: the old chapter gives the core structural story; the new second-stage summary shows that the story is not an artifact of one modeling family or one retail aggregation routine.

## Most important substantive improvement in the second stage
The clearest substantive upgrade is not that the second-stage summary produces stronger coefficients. It is that the downstream data-generating process is cleaner. Product names and brands are harmonized across Novus and Silpo at item level, discounts are carried inside price while also modeled explicitly, matched cross-shop retail support is identified directly, and ConsumerUA is added as a transparent robustness endpoint rather than hidden inside a broad downstream aggregate. That makes the second-stage results methodologically different, more retailer-grounded, and easier to defend as a robustness exercise.
