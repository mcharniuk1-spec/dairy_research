# INSTALLATION GUIDE

## Quick Setup (macOS)

### Option 1: Automated Setup (Recommended)

Run the provided setup script:

```bash
cd "/Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/"
chmod +x setup_environment.sh
./setup_environment.sh
```

This will:
- ✓ Check Python installation
- ✓ Install all required packages
- ✓ Create necessary directories
- ✓ Verify data files

---

### Option 2: Manual Installation

#### Step 1: Install Python

**Check if Python is installed:**
```bash
python3 --version
```

**If not installed, install via Homebrew:**
```bash
# Install Homebrew (if needed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install Python
brew install python@3.11
```

**Or download from official website:**
- Visit: https://www.python.org/downloads/
- Download Python 3.11+ for macOS
- Run installer

#### Step 2: Install Required Packages

```bash
# Upgrade pip
python3 -m pip install --upgrade pip

# Install core packages
pip3 install numpy pandas scipy statsmodels matplotlib seaborn openpyxl xlrd

# Optional: Advanced econometrics
pip3 install arch
```

#### Step 3: Verify Installation

```bash
python3 -c "import pandas, numpy, statsmodels, matplotlib, seaborn, openpyxl; print('All packages installed successfully!')"
```

#### Step 4: Create Directory Structure

```bash
cd "/Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/"
mkdir -p processed plots results
```

---

## Running the Analysis

### Option A: Run Complete Pipeline

```bash
cd "/Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/"
python3 00_master_pipeline.py
```

### Option B: Run Individual Scripts

```bash
python3 01_data_loading_preprocessing.py
python3 02_descriptive_statistics.py
python3 03_stationarity_tests.py
python3 04_vecm_cointegration.py
python3 05_nardl_asymmetric_transmission.py
python3 06_silpo_discount_analysis.py
python3 07_eu_us_comparison.py
python3 08_prozzoro_analysis.py
```

---

## Troubleshooting

### Issue: "zsh: command not found: python"

**Solution:**
Your system uses `python3` instead of `python`. Use:
```bash
python3 00_master_pipeline.py
```

Or create an alias:
```bash
echo "alias python=python3" >> ~/.zshrc
source ~/.zshrc
```

### Issue: "ModuleNotFoundError: No module named 'pandas'"

**Solution:**
Install packages with correct Python version:
```bash
python3 -m pip install pandas numpy scipy statsmodels matplotlib seaborn openpyxl
```

### Issue: "Permission denied"

**Solution:**
Install packages in user directory:
```bash
pip3 install --user pandas numpy scipy statsmodels matplotlib seaborn openpyxl
```

### Issue: "SSL Certificate Error"

**Solution:**
Update certificates:
```bash
pip3 install --upgrade certifi
/Applications/Python\ 3.11/Install\ Certificates.command
```

### Issue: Script runs but no output

**Solution:**
Check that you're in the correct directory:
```bash
pwd
# Should show: /Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/
```

Verify data files exist:
```bash
ls -lh *.csv *.xlsx
```

---

## Package Versions (Tested)

- **Python:** 3.9+ (recommended: 3.11)
- **NumPy:** 1.24+
- **Pandas:** 2.0+
- **SciPy:** 1.10+
- **Statsmodels:** 0.14+
- **Matplotlib:** 3.7+
- **Seaborn:** 0.12+
- **OpenPyXL:** 3.1+

---

## System Requirements

- **OS:** macOS 10.15+ (Catalina or newer)
- **RAM:** 8GB minimum (16GB recommended for Silpo.xlsx processing)
- **Disk Space:** 2GB free space
- **Python:** 3.9 or higher

---

## Getting Help

If you encounter issues:

1. **Check Python version:**
   ```bash
   python3 --version
   ```

2. **Check installed packages:**
   ```bash
   pip3 list | grep -E "pandas|numpy|statsmodels|matplotlib|seaborn|openpyxl"
   ```

3. **Run diagnostics:**
   ```bash
   python3 -c "
   import sys
   print('Python:', sys.version)
   import pandas as pd
   print('Pandas:', pd.__version__)
   import numpy as np
   print('NumPy:', np.__version__)
   import statsmodels
   print('Statsmodels:', statsmodels.__version__)
   "
   ```

4. **Check error logs** in the terminal output

---

## Quick Commands Reference

```bash
# Navigate to project directory
cd "/Users/getapple/Documents/KSE/Master Thesis/Main materials/Model/"

# Run setup script
./setup_environment.sh

# Run full analysis
python3 00_master_pipeline.py

# Check outputs
ls -lh processed/
ls -lh plots/
ls -lh results/

# View a result file
cat results/descriptive_summary.csv
open plots/class3_timeseries.png
```

---

**Last Updated:** February 3, 2026
