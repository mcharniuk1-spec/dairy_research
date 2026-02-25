# =============================================================================
# MASTER THESIS DAIRY PRICE TRANSMISSION ANALYSIS
# Part 3: Stationarity Tests (ADF, KPSS, Zivot-Andrews)
# =============================================================================

import pandas as pd
import numpy as np
from statsmodels.tsa.stattools import adfuller, kpss
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

BASE_PATH = '/Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/'

# =============================================================================
# STATIONARITY TEST FUNCTIONS
# =============================================================================

def adf_test(series, name, regression='ct'):
    """
    Augmented Dickey-Fuller test for unit root
    
    H0: Series has a unit root (non-stationary)
    H1: Series is stationary
    
    regression options:
    - 'c': constant only
    - 'ct': constant and trend
    - 'ctt': constant, linear and quadratic trend
    - 'n': no constant, no trend
    """
    print(f"\n{'='*80}")
    print(f"ADF TEST: {name}")
    print(f"{'='*80}")
    
    result = adfuller(series.dropna(), regression=regression, autolag='AIC')
    
    print(f"ADF Statistic: {result[0]:.6f}")
    print(f"p-value: {result[1]:.6f}")
    print(f"Lags used: {result[2]}")
    print(f"Number of observations: {result[3]}")
    print(f"\nCritical Values:")
    for key, value in result[4].items():
        print(f"  {key}: {value:.3f}")
    
    if result[1] < 0.05:
        print(f"\n→ Reject H0 at 5% level: Series is STATIONARY")
        conclusion = "Stationary"
    else:
        print(f"\n→ Fail to reject H0: Series has UNIT ROOT (non-stationary)")
        conclusion = "Non-stationary"
    
    return {
        'Test': 'ADF',
        'Statistic': result[0],
        'p-value': result[1],
        'Lags': result[2],
        'Critical_1%': result[4]['1%'],
        'Critical_5%': result[4]['5%'],
        'Critical_10%': result[4]['10%'],
        'Conclusion': conclusion
    }


def kpss_test(series, name, regression='ct'):
    """
    Kwiatkowski-Phillips-Schmidt-Shin test
    
    H0: Series is stationary
    H1: Series has a unit root
    
    regression options:
    - 'c': constant only (level stationary)
    - 'ct': constant and trend (trend stationary)
    """
    print(f"\n{'='*80}")
    print(f"KPSS TEST: {name}")
    print(f"{'='*80}")
    
    result = kpss(series.dropna(), regression=regression, nlags='auto')
    
    print(f"KPSS Statistic: {result[0]:.6f}")
    print(f"p-value: {result[1]:.6f}")
    print(f"Lags used: {result[2]}")
    print(f"\nCritical Values:")
    for key, value in result[3].items():
        print(f"  {key}: {value:.3f}")
    
    if result[1] < 0.05:
        print(f"\n→ Reject H0 at 5% level: Series has UNIT ROOT")
        conclusion = "Non-stationary"
    else:
        print(f"\n→ Fail to reject H0: Series is STATIONARY")
        conclusion = "Stationary"
    
    return {
        'Test': 'KPSS',
        'Statistic': result[0],
        'p-value': result[1],
        'Lags': result[2],
        'Critical_1%': result[3]['1%'],
        'Critical_5%': result[3]['5%'],
        'Critical_10%': result[3]['10%'],
        'Conclusion': conclusion
    }


def test_integration_order(series, name, max_diff=2):
    """
    Determine order of integration I(d) by testing levels and differences
    """
    print(f"\n{'='*80}")
    print(f"INTEGRATION ORDER TEST: {name}")
    print(f"{'='*80}")
    
    results = []
    current_series = series.dropna().copy()
    
    for d in range(max_diff + 1):
        if d == 0:
            level_name = f"{name} (Levels)"
        else:
            level_name = f"{name} (Δ^{d})"
        
        print(f"\n{'-'*80}")
        print(f"Testing: {level_name}")
        print(f"{'-'*80}")
        
        # ADF test
        adf_result = adf_test(current_series, level_name, regression='ct')
        
        # KPSS test
        kpss_result = kpss_test(current_series, level_name, regression='ct')
        
        # Store results
        results.append({
            'Differencing': d,
            'ADF_Stat': adf_result['Statistic'],
            'ADF_pval': adf_result['p-value'],
            'ADF_Conclusion': adf_result['Conclusion'],
            'KPSS_Stat': kpss_result['Statistic'],
            'KPSS_pval': kpss_result['p-value'],
            'KPSS_Conclusion': kpss_result['Conclusion']
        })
        
        # If stationary, stop
        if adf_result['Conclusion'] == 'Stationary' and kpss_result['Conclusion'] == 'Stationary':
            print(f"\n✓ Series is I({d}) - stationary at difference order {d}")
            break
        
        # Take first difference for next iteration
        current_series = current_series.diff().dropna()
    
    results_df = pd.DataFrame(results)
    print(f"\n{'='*80}")
    print("INTEGRATION ORDER SUMMARY")
    print(f"{'='*80}")
    print(results_df.to_string(index=False))
    
    return results_df


def plot_acf_pacf(series, name, lags=40):
    """
    Plot ACF and PACF to identify autocorrelation structure
    """
    fig, axes = plt.subplots(2, 1, figsize=(12, 8))
    
    # ACF
    plot_acf(series.dropna(), lags=lags, ax=axes[0], alpha=0.05)
    axes[0].set_title(f'ACF: {name}', fontsize=14, fontweight='bold')
    axes[0].set_xlabel('Lag', fontsize=11)
    axes[0].set_ylabel('Autocorrelation', fontsize=11)
    axes[0].grid(True, alpha=0.3)
    
    # PACF
    plot_pacf(series.dropna(), lags=lags, ax=axes[1], alpha=0.05, method='ywm')
    axes[1].set_title(f'PACF: {name}', fontsize=14, fontweight='bold')
    axes[1].set_xlabel('Lag', fontsize=11)
    axes[1].set_ylabel('Partial Autocorrelation', fontsize=11)
    axes[1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    safe_name = name.replace(' ', '_').replace('(', '').replace(')', '').lower()
    plt.savefig(BASE_PATH + f'plots/acf_pacf_{safe_name}.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"ACF/PACF plot saved: acf_pacf_{safe_name}.png")


# =============================================================================
# ZIVOT-ANDREWS TEST (Structural Break)
# =============================================================================

def zivot_andrews_test(series, name, model='c', trim=0.15):
    """
    Zivot-Andrews test for unit root with structural break
    
    H0: Unit root with drift (no break)
    H1: Trend stationary with structural break
    
    model options:
    - 'c': break in intercept
    - 't': break in trend
    - 'ct': break in both intercept and trend
    
    NOTE: This requires manual implementation or arch package
    For simplicity, we'll use a rolling window ADF approach
    """
    print(f"\n{'='*80}")
    print(f"STRUCTURAL BREAK DETECTION: {name}")
    print(f"{'='*80}")
    
    # Simple approach: Rolling window ADF statistics
    # More sophisticated: Use arch.unitroot.ZivotAndrews
    
    try:
        from arch.unitroot import ZivotAndrews
        
        za = ZivotAndrews(series.dropna(), trend=model, lags=None)
        
        print(f"\nZivot-Andrews Test Statistic: {za.stat:.6f}")
        print(f"p-value: {za.pvalue:.6f}")
        print(f"Lags used: {za.lags}")
        print(f"Break point: {za.break_point}")
        
        print(f"\nCritical Values:")
        for key, value in za.critical_values.items():
            print(f"  {key}: {value:.3f}")
        
        if za.pvalue < 0.05:
            print(f"\n→ Reject H0 at 5%: Trend stationary with structural break")
            conclusion = "Break-stationary"
        else:
            print(f"\n→ Fail to reject H0: Unit root process")
            conclusion = "Unit root"
        
        return {
            'Test': 'Zivot-Andrews',
            'Statistic': za.stat,
            'p-value': za.pvalue,
            'Break_Point': za.break_point,
            'Conclusion': conclusion
        }
        
    except ImportError:
        print("\n⚠ arch package not installed. Using rolling ADF as alternative.")
        print("Install with: pip install arch")
        
        # Alternative: Rolling ADF
        window = int(len(series) * 0.3)
        adf_stats = []
        dates = []
        
        for i in range(window, len(series) - window):
            subset = series.iloc[i-window:i+window]
            result = adfuller(subset.dropna(), regression=regression, autolag='AIC')
            adf_stats.append(result[0])
            dates.append(series.index[i])
        
        # Find minimum ADF statistic (most evidence against unit root)
        min_idx = np.argmin(adf_stats)
        break_point = dates[min_idx]
        
        print(f"\nRolling ADF minimum at: {break_point}")
        print(f"ADF statistic at break: {adf_stats[min_idx]:.6f}")
        
        return {
            'Test': 'Rolling ADF',
            'Break_Point': break_point,
            'Min_ADF_Stat': adf_stats[min_idx]
        }


# =============================================================================
# MAIN STATIONARITY TESTING
# =============================================================================

def run_stationarity_tests():
    """
    Run comprehensive stationarity tests on all price series
    """
    
    # Load processed data
    print("Loading processed datasets...")
    
    class3_monthly = pd.read_csv(BASE_PATH + 'processed/class3_monthly.csv')
    class3_monthly['Date'] = pd.to_datetime(class3_monthly['Date'])
    class3_monthly = class3_monthly.set_index('Date')
    
    novus_monthly = pd.read_csv(BASE_PATH + 'processed/novus_monthly.csv')
    novus_monthly['Date'] = pd.to_datetime(novus_monthly['Date'])
    novus_monthly = novus_monthly.set_index('Date')
    
    try:
        silpo_monthly = pd.read_csv(BASE_PATH + 'processed/silpo_monthly.csv')
        silpo_monthly['Date'] = pd.to_datetime(silpo_monthly['Date'])
        silpo_monthly = silpo_monthly.set_index('Date')
        has_silpo = True
    except:
        has_silpo = False
    
    # =========================================================================
    # TEST 1: CLASS III MILK FUTURES
    # =========================================================================
    
    print("\n" + "="*80)
    print("TESTING CME CLASS III MILK FUTURES")
    print("="*80)
    
    # Log transformation
    class3_monthly['ln_Price'] = np.log(class3_monthly['Price'])
    
    # Test integration order
    class3_integration = test_integration_order(class3_monthly['ln_Price'], 
                                               'ln(Class III Price)')
    
    # Plot ACF/PACF
    plot_acf_pacf(class3_monthly['ln_Price'], 'ln(Class III Price) - Levels')
    plot_acf_pacf(class3_monthly['ln_Price'].diff().dropna(), 
                 'ln(Class III Price) - First Difference')
    
    # Test for structural break (e.g., COVID, war)
    # za_class3 = zivot_andrews_test(class3_monthly['ln_Price'], 
    #                                'ln(Class III Price)', model='ct')
    
    # =========================================================================
    # TEST 2: NOVUS RETAIL PRICES
    # =========================================================================
    
    print("\n" + "="*80)
    print("TESTING NOVUS RETAIL PRICES")
    print("="*80)
    
    # Test integration order
    novus_integration = test_integration_order(novus_monthly['ln_unit_price'],
                                              'ln(Novus Unit Price)')
    
    # Plot ACF/PACF
    plot_acf_pacf(novus_monthly['ln_unit_price'], 'ln(Novus Price) - Levels')
    plot_acf_pacf(novus_monthly['ln_unit_price'].diff().dropna(),
                 'ln(Novus Price) - First Difference')
    
    # =========================================================================
    # TEST 3: SILPO RETAIL PRICES (if available)
    # =========================================================================
    
    if has_silpo:
        print("\n" + "="*80)
        print("TESTING SILPO RETAIL PRICES")
        print("="*80)
        
        silpo_integration = test_integration_order(silpo_monthly['ln_unit_price'],
                                                  'ln(Silpo Unit Price)')
        
        plot_acf_pacf(silpo_monthly['ln_unit_price'], 'ln(Silpo Price) - Levels')
        plot_acf_pacf(silpo_monthly['ln_unit_price'].diff().dropna(),
                     'ln(Silpo Price) - First Difference')
    
    # =========================================================================
    # SUMMARY TABLE
    # =========================================================================
    
    print("\n" + "="*80)
    print("STATIONARITY TESTS SUMMARY")
    print("="*80)
    
    summary_data = []
    
    # Class III
    summary_data.append({
        'Series': 'ln(Class III Price)',
        'Level': class3_integration.loc[0, 'ADF_Conclusion'],
        'First_Diff': class3_integration.loc[1, 'ADF_Conclusion'] if len(class3_integration) > 1 else 'N/A',
        'Integration_Order': 'I(1)' if class3_integration.loc[0, 'ADF_Conclusion'] == 'Non-stationary' else 'I(0)'
    })
    
    # Novus
    summary_data.append({
        'Series': 'ln(Novus Unit Price)',
        'Level': novus_integration.loc[0, 'ADF_Conclusion'],
        'First_Diff': novus_integration.loc[1, 'ADF_Conclusion'] if len(novus_integration) > 1 else 'N/A',
        'Integration_Order': 'I(1)' if novus_integration.loc[0, 'ADF_Conclusion'] == 'Non-stationary' else 'I(0)'
    })
    
    # Silpo
    if has_silpo:
        summary_data.append({
            'Series': 'ln(Silpo Unit Price)',
            'Level': silpo_integration.loc[0, 'ADF_Conclusion'],
            'First_Diff': silpo_integration.loc[1, 'ADF_Conclusion'] if len(silpo_integration) > 1 else 'N/A',
            'Integration_Order': 'I(1)' if silpo_integration.loc[0, 'ADF_Conclusion'] == 'Non-stationary' else 'I(0)'
        })
    
    summary_df = pd.DataFrame(summary_data)
    print("\n" + summary_df.to_string(index=False))
    
    summary_df.to_csv(BASE_PATH + 'results/stationarity_summary.csv', index=False)
    
    print("\n" + "="*80)
    print("STATIONARITY TESTING COMPLETE")
    print("="*80)


if __name__ == "__main__":
    run_stationarity_tests()
