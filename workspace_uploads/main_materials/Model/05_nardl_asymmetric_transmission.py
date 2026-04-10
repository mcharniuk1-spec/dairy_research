# =============================================================================
# MASTER THESIS DAIRY PRICE TRANSMISSION ANALYSIS
# Part 5: NARDL Model (Asymmetric Price Transmission)
# Following Biloshytska (2020) methodology
# =============================================================================

import pandas as pd
import numpy as np
from statsmodels.regression.linear_model import OLS
from statsmodels.stats.diagnostic import acorr_ljungbox, het_breuschpagan
from statsmodels.stats.stattools import durbin_watson
from scipy import stats
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

BASE_PATH = '/Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/'

# =============================================================================
# NARDL HELPER FUNCTIONS
# =============================================================================

def decompose_price_changes(series):
    """
    Decompose price series into positive and negative partial sums
    
    Following Shin, Yu, and Greenwood-Nimmo (2014):
    x_t^+ = Σ max(Δx_i, 0)  for i from 1 to t
    x_t^- = Σ min(Δx_i, 0)  for i from 1 to t
    """
    # First difference
    delta_x = series.diff()
    
    # Positive changes
    pos_changes = delta_x.where(delta_x > 0, 0)
    x_pos = pos_changes.cumsum()
    
    # Negative changes
    neg_changes = delta_x.where(delta_x < 0, 0)
    x_neg = neg_changes.cumsum()
    
    return x_pos, x_neg, delta_x


def create_nardl_data(dependent, independent, p_lags=4, q_lags=4):
    """
    Create dataset for NARDL regression
    
    NARDL(p, q) specification:
    Δy_t = α₀ + ρ_y·y_{t-1} + θ⁺·x⁺_{t-1} + θ⁻·x⁻_{t-1}
           + Σ(i=1 to p-1) γ_i·Δy_{t-i}
           + Σ(i=0 to q-1) (π_i⁺·Δx⁺_{t-i} + π_i⁻·Δx⁻_{t-i})
           + ε_t
    """
    # Decompose independent variable
    x_pos, x_neg, delta_x = decompose_price_changes(independent)
    
    # Create dataframe
    df = pd.DataFrame({
        'y': dependent,
        'x': independent,
        'x_pos': x_pos,
        'x_neg': x_neg
    })
    
    # First difference of dependent
    df['delta_y'] = df['y'].diff()
    
    # Lagged levels
    df['y_lag1'] = df['y'].shift(1)
    df['x_pos_lag1'] = df['x_pos'].shift(1)
    df['x_neg_lag1'] = df['x_neg'].shift(1)
    
    # Lagged differences of dependent variable (p lags)
    for i in range(1, p_lags):
        df[f'delta_y_lag{i}'] = df['delta_y'].shift(i)
    
    # Lagged differences of decomposed independent (q lags)
    df['delta_x_pos'] = df['x_pos'].diff()
    df['delta_x_neg'] = df['x_neg'].diff()
    
    for i in range(0, q_lags):
        df[f'delta_x_pos_lag{i}'] = df['delta_x_pos'].shift(i)
        df[f'delta_x_neg_lag{i}'] = df['delta_x_neg'].shift(i)
    
    # Drop missing values
    df = df.dropna()
    
    return df


def estimate_nardl(df, p_lags=4, q_lags=4):
    """
    Estimate NARDL model using OLS
    """
    # Build formula
    exog_vars = ['y_lag1', 'x_pos_lag1', 'x_neg_lag1']
    
    # Add lagged differences of y
    exog_vars += [f'delta_y_lag{i}' for i in range(1, p_lags)]
    
    # Add lagged differences of decomposed x
    exog_vars += [f'delta_x_pos_lag{i}' for i in range(q_lags)]
    exog_vars += [f'delta_x_neg_lag{i}' for i in range(q_lags)]
    
    # Prepare data
    y = df['delta_y']
    X = df[exog_vars]
    X = sm.add_constant(X)
    
    # Estimate OLS
    model = OLS(y, X)
    results = model.fit()
    
    return results, exog_vars


# =============================================================================
# BOUNDS TEST (Pesaran, Shin, Smith 2001)
# =============================================================================

def bounds_test(results, exog_vars, alpha=0.05):
    """
    Bounds test for cointegration in ARDL/NARDL framework
    
    H0: No cointegration (ρ_y = θ⁺ = θ⁻ = 0)
    
    Test statistic: F-statistic from joint test
    Compare to Pesaran et al. (2001) critical values
    """
    print(f"\n{'='*80}")
    print("BOUNDS TEST FOR COINTEGRATION")
    print(f"{'='*80}")
    
    # Test H0: y_lag1 = x_pos_lag1 = x_neg_lag1 = 0
    restrictions = 'y_lag1 = 0, x_pos_lag1 = 0, x_neg_lag1 = 0'
    f_test = results.f_test(restrictions)
    
    f_stat = f_test.fvalue[0][0]
    p_value = f_test.pvalue
    
    print(f"\nF-statistic: {f_stat:.4f}")
    print(f"p-value: {p_value:.4f}")
    
    # Pesaran et al. (2001) critical values for k=2 regressors
    # Table CI(iii) Case III: unrestricted intercept, no trend
    critical_values = {
        0.10: {'I(0)': 3.17, 'I(1)': 4.14},
        0.05: {'I(0)': 3.79, 'I(1)': 4.85},
        0.01: {'I(0)': 5.15, 'I(1)': 6.36}
    }
    
    print(f"\nPesaran et al. (2001) Critical Values (k=2):")
    print(f"{'Significance':<15}{'I(0) Bound':<15}{'I(1) Bound':<15}")
    print("-" * 45)
    for sig, bounds in critical_values.items():
        print(f"{sig:<15}{bounds['I(0)']:<15.2f}{bounds['I(1)']:<15.2f}")
    
    print(f"\nInterpretation:")
    if f_stat > critical_values[alpha]['I(1)']:
        print(f"✓ F-stat > I(1) bound → Reject H0: Cointegration EXISTS")
        conclusion = "Cointegrated"
    elif f_stat < critical_values[alpha]['I(0)']:
        print(f"✗ F-stat < I(0) bound → Fail to reject H0: NO cointegration")
        conclusion = "Not cointegrated"
    else:
        print(f"? F-stat in inconclusive region → Ambiguous result")
        conclusion = "Inconclusive"
    
    return f_stat, p_value, conclusion


# =============================================================================
# ASYMMETRY TESTS (Wald Tests)
# =============================================================================

def test_long_run_asymmetry(results):
    """
    Test for long-run asymmetry
    
    H0: μ⁺ = μ⁻
    where μ⁺ = -θ⁺/ρ_y and μ⁻ = -θ⁻/ρ_y
    
    Equivalently: H0: θ⁺/θ⁻ = 1
    or: H0: θ⁺ - θ⁻ = 0
    """
    print(f"\n{'='*80}")
    print("LONG-RUN ASYMMETRY TEST")
    print(f"{'='*80}")
    
    # Extract coefficients
    theta_pos = results.params['x_pos_lag1']
    theta_neg = results.params['x_neg_lag1']
    rho_y = results.params['y_lag1']
    
    # Calculate long-run multipliers
    mu_pos = -theta_pos / rho_y
    mu_neg = -theta_neg / rho_y
    
    print(f"\nLong-run multipliers:")
    print(f"μ⁺ (positive shock): {mu_pos:.4f}")
    print(f"μ⁻ (negative shock): {mu_neg:.4f}")
    print(f"Ratio (μ⁺/μ⁻): {mu_pos/mu_neg:.4f}")
    
    # Wald test: H0: theta_pos - theta_neg = 0
    wald_test = results.wald_test('x_pos_lag1 - x_neg_lag1 = 0')
    
    print(f"\nWald Test: H0: θ⁺ = θ⁻")
    print(f"Test statistic: {wald_test.statistic:.4f}")
    print(f"p-value: {wald_test.pvalue:.4f}")
    
    if wald_test.pvalue < 0.05:
        print(f"\n✓ Reject H0 at 5%: LONG-RUN ASYMMETRY detected")
        conclusion = "Asymmetric"
    else:
        print(f"\n✗ Fail to reject H0: NO long-run asymmetry")
        conclusion = "Symmetric"
    
    return mu_pos, mu_neg, wald_test.statistic, wald_test.pvalue, conclusion


def test_short_run_asymmetry(results, q_lags):
    """
    Test for short-run asymmetry
    
    H0: Σ π_i⁺ = Σ π_i⁻  for all i
    """
    print(f"\n{'='*80}")
    print("SHORT-RUN ASYMMETRY TEST")
    print(f"{'='*80}")
    
    # Build restriction string
    pos_params = ' + '.join([f'delta_x_pos_lag{i}' for i in range(q_lags)])
    neg_params = ' + '.join([f'delta_x_neg_lag{i}' for i in range(q_lags)])
    restriction = f'({pos_params}) - ({neg_params}) = 0'
    
    # Wald test
    wald_test = results.wald_test(restriction)
    
    # Calculate sum of coefficients
    sum_pos = sum([results.params[f'delta_x_pos_lag{i}'] for i in range(q_lags)])
    sum_neg = sum([results.params[f'delta_x_neg_lag{i}'] for i in range(q_lags)])
    
    print(f"\nShort-run multipliers (sum of coefficients):")
    print(f"Σ π⁺: {sum_pos:.4f}")
    print(f"Σ π⁻: {sum_neg:.4f}")
    
    print(f"\nWald Test: H0: Σ π⁺ = Σ π⁻")
    print(f"Test statistic: {wald_test.statistic:.4f}")
    print(f"p-value: {wald_test.pvalue:.4f}")
    
    if wald_test.pvalue < 0.05:
        print(f"\n✓ Reject H0 at 5%: SHORT-RUN ASYMMETRY detected")
        conclusion = "Asymmetric"
    else:
        print(f"\n✗ Fail to reject H0: NO short-run asymmetry")
        conclusion = "Symmetric"
    
    return sum_pos, sum_neg, wald_test.statistic, wald_test.pvalue, conclusion


# =============================================================================
# DYNAMIC MULTIPLIERS (Cumulative Effects)
# =============================================================================

def compute_dynamic_multipliers(results, exog_vars, p_lags, q_lags, horizon=12):
    """
    Compute dynamic multipliers showing cumulative price response over time
    
    m_h⁺ = Σ(j=0 to h) ∂y_{t+j}/∂x⁺_t
    m_h⁻ = Σ(j=0 to h) ∂y_{t+j}/∂x⁻_t
    """
    print(f"\n{'='*80}")
    print("DYNAMIC MULTIPLIERS (Cumulative Effects)")
    print(f"{'='*80}")
    
    # Extract parameters
    rho_y = results.params['y_lag1']
    theta_pos = results.params['x_pos_lag1']
    theta_neg = results.params['x_neg_lag1']
    
    gamma = [results.params[f'delta_y_lag{i}'] for i in range(1, p_lags)]
    pi_pos = [results.params[f'delta_x_pos_lag{i}'] for i in range(q_lags)]
    pi_neg = [results.params[f'delta_x_neg_lag{i}'] for i in range(q_lags)]
    
    # Initialize multipliers
    mult_pos = np.zeros(horizon + 1)
    mult_neg = np.zeros(horizon + 1)
    
    # Simplified calculation (direct iteration)
    # For more accurate: use companion form VAR representation
    
    # Period 0 (contemporaneous)
    mult_pos[0] = pi_pos[0]
    mult_neg[0] = pi_neg[0]
    
    # Periods 1 to horizon
    for h in range(1, horizon + 1):
        # Autoregressive component
        ar_component = sum([gamma[i-1] * (mult_pos[h-i] if h-i >= 0 else 0) 
                          for i in range(1, min(h+1, p_lags))])
        
        # Distributed lag component (positive)
        dl_pos = sum([pi_pos[i] if h-i >= 0 and i < q_lags else 0 
                     for i in range(q_lags)])
        
        # Distributed lag component (negative)
        dl_neg = sum([pi_neg[i] if h-i >= 0 and i < q_lags else 0 
                     for i in range(q_lags)])
        
        mult_pos[h] = ar_component + dl_pos
        mult_neg[h] = ar_component + dl_neg
    
    # Cumulative sums
    cumul_pos = np.cumsum(mult_pos)
    cumul_neg = np.cumsum(mult_neg)
    
    # Long-run values
    lr_pos = -theta_pos / rho_y
    lr_neg = -theta_neg / rho_y
    
    print(f"\nCumulative multipliers (first 12 periods):")
    print(f"{'Period':<10}{'Positive':<15}{'Negative':<15}{'Difference':<15}")
    print("-" * 55)
    for h in range(min(13, horizon + 1)):
        print(f"{h:<10}{cumul_pos[h]:<15.4f}{cumul_neg[h]:<15.4f}"
              f"{cumul_pos[h] - cumul_neg[h]:<15.4f}")
    
    print(f"\nLong-run multipliers (theoretical):")
    print(f"μ⁺: {lr_pos:.4f}")
    print(f"μ⁻: {lr_neg:.4f}")
    
    return cumul_pos, cumul_neg


def plot_dynamic_multipliers(cumul_pos, cumul_neg, horizon, save_name='nardl_multipliers'):
    """
    Plot dynamic multipliers with confidence bands
    """
    fig, ax = plt.subplots(figsize=(12, 7))
    
    periods = np.arange(0, horizon + 1)
    
    ax.plot(periods, cumul_pos, linewidth=2.5, label='Positive Price Change', 
            color='#2E86AB', marker='o', markersize=4)
    ax.plot(periods, cumul_neg, linewidth=2.5, label='Negative Price Change', 
            color='#C73E1D', marker='s', markersize=4)
    
    ax.axhline(0, color='black', linestyle='--', linewidth=1, alpha=0.5)
    
    ax.set_title('Dynamic Multipliers: Cumulative Price Response', 
                fontsize=16, fontweight='bold')
    ax.set_xlabel('Months After Shock', fontsize=12)
    ax.set_ylabel('Cumulative Effect on Retail Price', fontsize=12)
    ax.legend(loc='best', fontsize=11)
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(BASE_PATH + f'plots/{save_name}.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"\nDynamic multiplier plot saved: {save_name}.png")


# =============================================================================
# DIAGNOSTIC TESTS
# =============================================================================

def nardl_diagnostics(results, df):
    """
    Run diagnostic tests on NARDL residuals
    """
    print(f"\n{'='*80}")
    print("NARDL RESIDUAL DIAGNOSTICS")
    print(f"{'='*80}")
    
    # 1. Normality test
    print(f"\n1. JARQUE-BERA NORMALITY TEST")
    jb_stat, jb_pval, skew, kurt = stats.jarque_bera(results.resid)
    print(f"Test statistic: {jb_stat:.4f}")
    print(f"p-value: {jb_pval:.4f}")
    if jb_pval < 0.05:
        print("→ Reject H0: Residuals NOT normally distributed")
    else:
        print("→ Fail to reject H0: Residuals appear normally distributed")
    
    # 2. Autocorrelation test
    print(f"\n2. LJUNG-BOX AUTOCORRELATION TEST")
    lb_test = acorr_ljungbox(results.resid, lags=10, return_df=True)
    print(lb_test)
    
    # 3. Heteroskedasticity test
    print(f"\n3. BREUSCH-PAGAN HETEROSKEDASTICITY TEST")
    bp_stat, bp_pval, _, _ = het_breuschpagan(results.resid, results.model.exog)
    print(f"Test statistic: {bp_stat:.4f}")
    print(f"p-value: {bp_pval:.4f}")
    if bp_pval < 0.05:
        print("→ Reject H0: Heteroskedasticity detected")
    else:
        print("→ Fail to reject H0: Homoskedastic residuals")
    
    # 4. Durbin-Watson test
    print(f"\n4. DURBIN-WATSON TEST")
    dw_stat = durbin_watson(results.resid)
    print(f"DW statistic: {dw_stat:.4f}")
    print("(Values near 2 indicate no autocorrelation)")
    
    # 5. Plot residuals
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # Time series plot
    axes[0, 0].plot(results.resid)
    axes[0, 0].axhline(0, color='black', linestyle='--', linewidth=1)
    axes[0, 0].set_title('Residuals Over Time', fontsize=12, fontweight='bold')
    axes[0, 0].set_xlabel('Observation')
    axes[0, 0].set_ylabel('Residual')
    axes[0, 0].grid(True, alpha=0.3)
    
    # Histogram
    axes[0, 1].hist(results.resid, bins=30, density=True, alpha=0.7, color='#2E86AB')
    mu, sigma = results.resid.mean(), results.resid.std()
    x = np.linspace(results.resid.min(), results.resid.max(), 100)
    axes[0, 1].plot(x, stats.norm.pdf(x, mu, sigma), 'r-', linewidth=2)
    axes[0, 1].set_title('Residual Distribution', fontsize=12, fontweight='bold')
    axes[0, 1].set_xlabel('Residual')
    axes[0, 1].set_ylabel('Density')
    axes[0, 1].grid(True, alpha=0.3)
    
    # Q-Q plot
    stats.probplot(results.resid, dist="norm", plot=axes[1, 0])
    axes[1, 0].set_title('Q-Q Plot', fontsize=12, fontweight='bold')
    axes[1, 0].grid(True, alpha=0.3)
    
    # ACF of residuals
    from statsmodels.graphics.tsaplots import plot_acf
    plot_acf(results.resid, lags=20, ax=axes[1, 1], alpha=0.05)
    axes[1, 1].set_title('ACF of Residuals', fontsize=12, fontweight='bold')
    axes[1, 1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig(BASE_PATH + 'plots/nardl_diagnostics.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"\nDiagnostic plots saved")


# =============================================================================
# MAIN NARDL ANALYSIS
# =============================================================================

import statsmodels.api as sm

def run_nardl_analysis():
    """
    Run full NARDL analysis pipeline
    """
    # Load processed data
    print("Loading processed datasets...")
    
    class3_monthly = pd.read_csv(BASE_PATH + 'processed/class3_monthly.csv')
    class3_monthly['Date'] = pd.to_datetime(class3_monthly['Date'])
    class3_monthly = class3_monthly.set_index('Date')
    
    novus_monthly = pd.read_csv(BASE_PATH + 'processed/novus_monthly.csv')
    novus_monthly['Date'] = pd.to_datetime(novus_monthly['Date'])
    novus_monthly = novus_monthly.set_index('Date')
    
    # Merge datasets
    merged = pd.merge(class3_monthly[['ln_Price']], 
                     novus_monthly[['ln_unit_price']], 
                     left_index=True, right_index=True, how='inner')
    
    merged.columns = ['ln_Class3', 'ln_Novus']
    
    print(f"\nMerged dataset shape: {merged.shape}")
    
    if len(merged) < 30:
        print("\n⚠ WARNING: Very short time series for NARDL.")
        return
    
    # =========================================================================
    # ESTIMATE NARDL MODEL
    # =========================================================================
    
    print(f"\n{'='*80}")
    print("NARDL MODEL: Class III → Novus Retail Price")
    print(f"{'='*80}")
    
    # Lag selection (use AIC/BIC in practice; here use p=q=4)
    p_lags = 4
    q_lags = 4
    
    # Create NARDL data
    nardl_data = create_nardl_data(merged['ln_Novus'], merged['ln_Class3'],
                                   p_lags=p_lags, q_lags=q_lags)
    
    print(f"\nNARDL({p_lags}, {q_lags}) specification")
    print(f"Effective sample size: {len(nardl_data)}")
    
    # Estimate model
    results, exog_vars = estimate_nardl(nardl_data, p_lags=p_lags, q_lags=q_lags)
    
    print(f"\n{results.summary()}")
    
    # =========================================================================
    # BOUNDS TEST
    # =========================================================================
    
    f_stat, p_val, coint_conclusion = bounds_test(results, exog_vars)
    
    # =========================================================================
    # ASYMMETRY TESTS
    # =========================================================================
    
    mu_pos, mu_neg, lr_wald_stat, lr_wald_pval, lr_conclusion = test_long_run_asymmetry(results)
    
    sr_sum_pos, sr_sum_neg, sr_wald_stat, sr_wald_pval, sr_conclusion = test_short_run_asymmetry(results, q_lags)
    
    # =========================================================================
    # DYNAMIC MULTIPLIERS
    # =========================================================================
    
    cumul_pos, cumul_neg = compute_dynamic_multipliers(results, exog_vars, 
                                                       p_lags, q_lags, horizon=12)
    
    plot_dynamic_multipliers(cumul_pos, cumul_neg, horizon=12)
    
    # =========================================================================
    # DIAGNOSTICS
    # =========================================================================
    
    nardl_diagnostics(results, nardl_data)
    
    # =========================================================================
    # SUMMARY TABLE
    # =========================================================================
    
    summary_results = {
        'Model': 'NARDL({}, {})'.format(p_lags, q_lags),
        'Sample_Size': len(nardl_data),
        'R_squared': results.rsquared,
        'Adj_R_squared': results.rsquared_adj,
        'F_statistic': results.fvalue,
        'Bounds_Test_F': f_stat,
        'Cointegration': coint_conclusion,
        'LR_Multiplier_Pos': mu_pos,
        'LR_Multiplier_Neg': mu_neg,
        'LR_Asymmetry': lr_conclusion,
        'SR_Sum_Pos': sr_sum_pos,
        'SR_Sum_Neg': sr_sum_neg,
        'SR_Asymmetry': sr_conclusion
    }
    
    summary_df = pd.DataFrame([summary_results]).T
    summary_df.columns = ['Value']
    
    print(f"\n{'='*80}")
    print("NARDL MODEL SUMMARY")
    print(f"{'='*80}")
    print(summary_df)
    
    summary_df.to_csv(BASE_PATH + 'results/nardl_summary.csv')
    
    # Save detailed results
    with open(BASE_PATH + 'results/nardl_detailed_output.txt', 'w') as f:
        f.write(str(results.summary()))
        f.write("\n\n" + "="*80 + "\n")
        f.write("BOUNDS TEST RESULTS\n")
        f.write("="*80 + "\n")
        f.write(f"F-statistic: {f_stat:.4f}\n")
        f.write(f"Conclusion: {coint_conclusion}\n")
    
    print(f"\n{'='*80}")
    print("NARDL ANALYSIS COMPLETE")
    print(f"{'='*80}")


if __name__ == "__main__":
    run_nardl_analysis()
