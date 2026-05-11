# Model Execution Protocol for H1 and H2

## H1

H1 tests whether market power exists between farm-gate raw milk producers and processors. The main models use observed monthly Ukrainian national data. The dependent variables are processor-level prices. The upstream variable is farm-gate raw milk price.

Execution order:

1. Harmonize all prices to UAH/kg.
2. Keep Ukraine national data for headline models.
3. Test stationarity with Augmented Dickey-Fuller (ADF) and Kwiatkowski-Phillips-Schmidt-Shin (KPSS).
4. Estimate long-run relation and Error Correction Model (ECM).
5. Use Autoregressive Distributed Lag (ARDL) lag selection as support.
6. Estimate Nonlinear Autoregressive Distributed Lag (NARDL) only as a mechanism test.
7. Use Vector Error Correction Model (VECM) only for three-layer monthly systems with enough observations.

## H2

H2 tests whether market power exists between processors/procurement and downstream retail actors. The main official benchmark is processor-level to official consumer price. ProZorro and retail SKU/day models explain institutional and promotional mechanisms.

Execution order:

1. Estimate processor to official consumer monthly ECM/NARDL models.
2. Aggregate ProZorro by product and date/week/month.
3. Build retail Stock Keeping Unit (SKU) panel after product reclassification.
4. Estimate short retail mechanism models only after overlap checks.
5. Treat discount incidence and discount depth as H2 mechanisms.

## Reliability

Main-text models must be economically interpretable, have enough observations, and pass core diagnostics. Weak models are retained only in appendix notes.
