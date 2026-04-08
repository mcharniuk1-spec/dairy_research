# RW4 Synthetic Consumer

## Interpretation Guide
- ADF p>0.05 and KPSS p<0.05 -> likely I(1)-like; prefer differences/cointegration models.
- ADF p<0.05 and KPSS p>0.05 -> stationary; level models are more admissible.
- Ljung-Box p<0.05 -> autocorrelation; add lag structure.
- BP/White p<0.05 -> heteroskedasticity; use robust or HAC standard errors.
- JB p<0.05 -> non-normality; use robust inference and avoid strict normality assumptions.
- Stability flag=1 -> potential breaks/drift; use rolling or split-sample robustness.
- For retail transmission, compare no-promo vs promo-controlled estimates.

## Notes
- link_rows=3
- RW4 domestic vertical chain is FarmGateUA -> ProducerUA -> ProZorro -> Retail, estimated with both forward and reverse-flow pairs. Farm-gate enters from two alternative reconstruction workbooks and both linear/pchip interpolation variants are carried end-to-end. Retail_combined is the anchored downstream index built from Silpo effective prices, Novus observed prices, and a level-aligned ConsumerUA anchor, while Retail_combined_core keeps the strict retailer-only overlap for robustness.

## Tables

### Synthetic_Consumer_Link

| product | standardized_type | n_obs | coef_retail | p_retail | coef_producer | p_producer | r2 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Молоко питне | milk | 56 | 0.0006170987828229427 | 0.5777992398736067 | 0.943225223379526 | 7.577082686107432e-29 | 0.8723404713710914 |
| Сир твердий | hard_cheese | 56 | 0.00020376027608469318 | 0.3489522548733358 | 0.9255256838346126 | 0.0 | 0.9791246197782543 |
| Сметана | sour_cream | 51 | -0.0002863434322670274 | 0.8956552864195457 | 1.1003703971747334 | 3.991164062063931e-230 | 0.988665326159806 |
