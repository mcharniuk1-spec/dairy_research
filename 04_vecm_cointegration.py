# =============================================================================
# MASTER THESIS DAIRY PRICE TRANSMISSION ANALYSIS
# Part 4: Cointegration Analysis and VECM Models
# =============================================================================

import pandas as pd
import numpy as np
from statsmodels.tsa.vector_ar.vecm import coint_johansen, VECM, select_order, select_coint_rank
from statsmodels.tsa.stattools import grangercausalitytests
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

BASE_PATH = '/Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/'

# =============================================================================
# JOHANSEN COINTEGRATION TEST
# =============================================================================

def johansen_cointegration_test(data, columns, det_order=1, k_ar_diff=1):
    """
    Johansen cointegration test for multiple time series
    
    det_order:
    - -1: no deterministic terms
    - 0: constant term in cointegration relation
    - 1: constant and trend in cointegration relation
    
    Returns number of cointegrating relationships
    """
    print(f"\n{'='*80}")
    print("JOHANSEN COINTEGRATION TEST")
    print(f"{'='*80}")
    
    # Select data
    y = data[columns].dropna()
    
    print(f"\nTesting variables: {columns}")
    print(f"Sample size: {len(y)}")
    print(f"Lag order: {k_ar_diff}")
    
    # Run Johansen test
    result = coint_johansen(y, det_order=det_order, k_ar_diff=k_ar_diff)
    
    # Trace statistic
    print(f"\n{'='*80}")
    print("TRACE STATISTIC TEST")
    print(f"{'='*80}")
    print(f"{'Rank':<10}{'Test Stat':<15}{'90% Crit':<15}{'95% Crit':<15}{'99% Crit':<15}")
    print("-" * 80)
    
    for i in range(len(columns)):
        print(f"{i:<10}{result.lr1[i]:<15.3f}{result.cvt[i, 0]:<15.3f}"
              f"{result.cvt[i, 1]:<15.3f}{result.cvt[i, 2]:<15.3f}")
    
    # Eigenvalue statistic
    print(f"\n{'='*80}")
    print("MAX EIGENVALUE STATISTIC TEST")
    print(f"{'='*80}")
    print(f"{'Rank':<10}{'Test Stat':<15}{'90% Crit':<15}{'95% Crit':<15}{'99% Crit':<15}")
    print("-" * 80)
    
    for i in range(len(columns)):
        print(f"{i:<10}{result.lr2[i]:<15.3f}{result.cvm[i, 0]:<15.3f}"
              f"{result.cvm[i, 1]:<15.3f}{result.cvm[i, 2]:<15.3f}")
    
    # Determine number of cointegrating vectors at 95% level
    trace_rank = np.sum(result.lr1 > result.cvt[:, 1])
    eigen_rank = np.sum(result.lr2 > result.cvm[:, 1])
    
    print(f"\n{'='*80}")
    print(f"CONCLUSION (95% significance level)")
    print(f"{'='*80}")
    print(f"Trace test suggests {trace_rank} cointegrating equation(s)")
    print(f"Max eigenvalue test suggests {eigen_rank} cointegrating equation(s)")
    
    # Eigenvectors (cointegrating vectors)
    print(f"\n{'='*80}")
    print("COINTEGRATING VECTORS (Eigenvectors)")
    print(f"{'='*80}")
    print(pd.DataFrame(result.evec, index=columns, 
                      columns=[f'CE{i+1}' for i in range(len(columns))]))
    
    return result, max(trace_rank, eigen_rank)


# =============================================================================
# VECM ESTIMATION
# =============================================================================

def estimate_vecm(data, columns, coint_rank, k_ar_diff=1, deterministic='ci'):
    """
    Estimate Vector Error Correction Model
    
    deterministic options:
    - 'nc': no constant
    - 'co': constant outside cointegration relation
    - 'ci': constant inside cointegration relation
    - 'lo': linear trend outside
    - 'li': linear trend inside
    - 'cili': constant and trend inside
    """
    print(f"\n{'='*80}")
    print("VECM ESTIMATION")
    print(f"{'='*80}")
    
    y = data[columns].dropna()
    
    print(f"\nVariables: {columns}")
    print(f"Cointegrating rank: {coint_rank}")
    print(f"Lag order: {k_ar_diff}")
    print(f"Deterministic terms: {deterministic}")
    
    # Estimate VECM
    model = VECM(y, k_ar_diff=k_ar_diff, coint_rank=coint_rank, 
                deterministic=deterministic)
    results = model.fit()
    
    print(f"\n{results.summary()}")
    
    # Extract key parameters
    print(f"\n{'='*80}")
    print("COINTEGRATING VECTOR(S)")
    print(f"{'='*80}")
    print(results.beta)  # Cointegrating vectors
    
    print(f"\n{'='*80}")
    print("ADJUSTMENT COEFFICIENTS (Alpha)")
    print(f"{'='*80}")
    print(pd.DataFrame(results.alpha, 
                      index=columns,
                      columns=[f'CE{i+1}' for i in range(coint_rank)]))
    
    print(f"\nInterpretation:")
    print("- Negative alpha → variable adjusts to restore long-run equilibrium")
    print("- Larger |alpha| → faster adjustment speed")
    
    # Granger causality
    print(f"\n{'='*80}")
    print("GRANGER CAUSALITY WITHIN VECM")
    print(f"{'='*80}")
    print(results.test_granger_causality(caused=columns[0]))
    
    return results


# =============================================================================
# IMPULSE RESPONSE FUNCTIONS
# =============================================================================

def plot_irf(results, periods=12, var_names=None):
    """
    Plot Impulse Response Functions from VECM
    """
    irf = results.irf(periods=periods)
    
    fig = irf.plot(impulse=var_names, response=var_names, 
                   figsize=(14, 10), subplot_params={'fontsize': 10})
    
    plt.tight_layout()
    plt.savefig(BASE_PATH + 'plots/vecm_impulse_response.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"\nImpulse response function plot saved")


def plot_forecast_error_variance_decomposition(results, periods=12, var_names=None):
    """
    Plot Forecast Error Variance Decomposition
    """
    fevd = results.fevd(periods=periods)
    
    fig = fevd.plot(figsize=(14, 8))
    plt.tight_layout()
    plt.savefig(BASE_PATH + 'plots/vecm_fevd.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"\nFEVD plot saved")


# =============================================================================
# DIAGNOSTIC TESTS
# =============================================================================

def vecm_diagnostics(results):
    """
    Run diagnostic tests on VECM residuals
    """
    print(f"\n{'='*80}")
    print("VECM RESIDUAL DIAGNOSTICS")
    print(f"{'='*80}")
    
    # 1. Portmanteau test (autocorrelation)
    print(f"\n1. PORTMANTEAU TEST (Autocorrelation)")
    print(results.test_whiteness(nlags=10))
    
    # 2. Normality test
    print(f"\n2. JARQUE-BERA NORMALITY TEST")
    print(results.test_normality())
    
    # 3. Plot residuals
    fig, axes = plt.subplots(results.neqs, 1, figsize=(12, 3 * results.neqs))
    if results.neqs == 1:
        axes = [axes]
    
    for i, ax in enumerate(axes):
        ax.plot(results.resid[:, i])
        ax.axhline(0, color='black', linestyle='--', linewidth=1)
        ax.set_title(f'Residuals: {results.names[i]}', fontsize=12, fontweight='bold')
        ax.set_xlabel('Time')
        ax.set_ylabel('Residual')
        ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(BASE_PATH + 'plots/vecm_residuals.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"\nResidual plots saved")


# =============================================================================
# MAIN VECM ANALYSIS
# =============================================================================

def run_vecm_analysis():
    """
    Run full VECM analysis pipeline
    """
    
    # Load processed data
    print("Loading processed datasets...")
    
    class3_monthly = pd.read_csv(BASE_PATH + 'processed/class3_monthly.csv')
    class3_monthly['Date'] = pd.to_datetime(class3_monthly['Date'])
    class3_monthly = class3_monthly.set_index('Date')
    
    novus_monthly = pd.read_csv(BASE_PATH + 'processed/novus_monthly.csv')
    novus_monthly['Date'] = pd.to_datetime(novus_monthly['Date'])
    novus_monthly = novus_monthly.set_index('Date')
    
    # Merge datasets on date
    # Note: This requires overlapping time periods
    merged = pd.merge(class3_monthly[['ln_Price']], 
                     novus_monthly[['ln_unit_price']], 
                     left_index=True, right_index=True, how='inner')
    
    merged.columns = ['ln_Class3', 'ln_Novus']
    
    print(f"\nMerged dataset shape: {merged.shape}")
    print(f"Date range: {merged.index.min()} to {merged.index.max()}")
    
    if len(merged) < 30:
        print("\n⚠ WARNING: Very short time series. Results may be unreliable.")
        print("Consider collecting more data or using different frequency.")
        return
    
    # =========================================================================
    # MODEL 1: Class III → Novus (Vertical Price Transmission)
    # =========================================================================
    
    print(f"\n{'='*80}")
    print("MODEL 1: VERTICAL PRICE TRANSMISSION (Class III → Novus)")
    print(f"{'='*80}")
    
    # Step 1: Determine lag order
    lag_order = select_order(merged[['ln_Class3', 'ln_Novus']], 
                            maxlags=12, deterministic='ci')
    print(f"\nOptimal lag order (AIC): {lag_order.aic}")
    print(f"Optimal lag order (BIC): {lag_order.bic}")
    
    selected_lag = min(lag_order.aic, 6)  # Cap at 6 for small samples
    
    # Step 2: Johansen cointegration test
    johansen_result, coint_rank = johansen_cointegration_test(
        merged, ['ln_Class3', 'ln_Novus'], 
        det_order=1, k_ar_diff=selected_lag
    )
    
    if coint_rank == 0:
        print("\n⚠ No cointegration found. Consider VAR in differences instead.")
    else:
        # Step 3: Estimate VECM
        vecm_results = estimate_vecm(merged, ['ln_Class3', 'ln_Novus'],
                                    coint_rank=coint_rank, 
                                    k_ar_diff=selected_lag,
                                    deterministic='ci')
        
        # Step 4: Diagnostics
        vecm_diagnostics(vecm_results)
        
        # Step 5: Impulse responses
        plot_irf(vecm_results, periods=12, 
                var_names=['ln_Class3', 'ln_Novus'])
        
        # Step 6: FEVD
        plot_forecast_error_variance_decomposition(vecm_results, periods=12,
                                                   var_names=['ln_Class3', 'ln_Novus'])
        
        # Save results
        with open(BASE_PATH + 'results/vecm_model1_summary.txt', 'w') as f:
            f.write(str(vecm_results.summary()))
    
    print(f"\n{'='*80}")
    print("VECM ANALYSIS COMPLETE")
    print(f"{'='*80}")


if __name__ == "__main__":
    run_vecm_analysis()
