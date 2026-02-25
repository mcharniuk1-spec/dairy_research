#!/bin/bash

# =============================================================================
# DAIRY PRICE TRANSMISSION ANALYSIS - COMPLETE SETUP SCRIPT
# For macOS (zsh shell)
# =============================================================================

echo "================================================================================"
echo "DAIRY PRICE TRANSMISSION ANALYSIS - SETUP"
echo "================================================================================"
echo ""

# -----------------------------------------------------------------------------
# 1. CHECK PYTHON INSTALLATION
# -----------------------------------------------------------------------------

echo "Step 1: Checking Python installation..."

if command -v python3 &>/dev/null; then
    PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
    echo "✓ Python3 found: $PYTHON_VERSION"
    PYTHON_CMD="python3"
elif command -v python &>/dev/null; then
    PYTHON_VERSION=$(python --version 2>&1 | awk '{print $2}')
    echo "✓ Python found: $PYTHON_VERSION"
    PYTHON_CMD="python"
else
    echo "✗ Python not found!"
    echo ""
    echo "Please install Python 3.9+ first:"
    echo "  Option 1 - Official installer:"
    echo "    Download from: https://www.python.org/downloads/"
    echo ""
    echo "  Option 2 - Homebrew (recommended):"
    echo "    /bin/bash -c \"\$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\""
    echo "    brew install python@3.11"
    echo ""
    exit 1
fi

# -----------------------------------------------------------------------------
# 2. CHECK PIP INSTALLATION
# -----------------------------------------------------------------------------

echo ""
echo "Step 2: Checking pip installation..."

if command -v pip3 &>/dev/null; then
    echo "✓ pip3 found"
    PIP_CMD="pip3"
elif command -v pip &>/dev/null; then
    echo "✓ pip found"
    PIP_CMD="pip"
else
    echo "✗ pip not found. Installing pip..."
    $PYTHON_CMD -m ensurepip --upgrade
    PIP_CMD="$PYTHON_CMD -m pip"
fi

# -----------------------------------------------------------------------------
# 3. UPGRADE PIP
# -----------------------------------------------------------------------------

echo ""
echo "Step 3: Upgrading pip..."
$PIP_CMD install --upgrade pip

# -----------------------------------------------------------------------------
# 4. INSTALL REQUIRED PACKAGES
# -----------------------------------------------------------------------------

echo ""
echo "Step 4: Installing required Python packages..."
echo "This may take a few minutes..."
echo ""

# Core data science packages
$PIP_CMD install numpy pandas scipy

# Statistical analysis
$PIP_CMD install statsmodels

# Data visualization
$PIP_CMD install matplotlib seaborn

# Excel file handling
$PIP_CMD install openpyxl xlrd

# Optional: Advanced econometrics
$PIP_CMD install arch

echo ""
echo "✓ All packages installed successfully"

# -----------------------------------------------------------------------------
# 5. VERIFY INSTALLATIONS
# -----------------------------------------------------------------------------

echo ""
echo "Step 5: Verifying installations..."

$PYTHON_CMD -c "
import sys
import importlib

packages = {
    'numpy': 'NumPy',
    'pandas': 'Pandas',
    'scipy': 'SciPy',
    'statsmodels': 'Statsmodels',
    'matplotlib': 'Matplotlib',
    'seaborn': 'Seaborn',
    'openpyxl': 'OpenPyXL',
}

all_good = True
for module, name in packages.items():
    try:
        lib = importlib.import_module(module)
        version = getattr(lib, '__version__', 'unknown')
        print(f'✓ {name:15s} {version}')
    except ImportError:
        print(f'✗ {name:15s} NOT FOUND')
        all_good = False

if not all_good:
    sys.exit(1)
"

if [ $? -ne 0 ]; then
    echo ""
    echo "✗ Some packages failed to install. Please check error messages above."
    exit 1
fi

# -----------------------------------------------------------------------------
# 6. CREATE DIRECTORY STRUCTURE
# -----------------------------------------------------------------------------

echo ""
echo "Step 6: Creating directory structure..."

BASE_DIR="/Users/getapple/Documents/KSE/Master Thesis/Main materials/Model"

# Create subdirectories
mkdir -p "$BASE_DIR/processed"
mkdir -p "$BASE_DIR/plots"
mkdir -p "$BASE_DIR/results"

echo "✓ Created directories:"
echo "  - $BASE_DIR/processed/"
echo "  - $BASE_DIR/plots/"
echo "  - $BASE_DIR/results/"

# -----------------------------------------------------------------------------
# 7. CHECK DATA FILES
# -----------------------------------------------------------------------------

echo ""
echo "Step 7: Checking data files..."

cd "$BASE_DIR" || exit

DATA_FILES=(
    "Class-III-Milk-Futures-Historical-Data-2.csv"
    "Novus_newest.xlsx"
    "Silpo.xlsx"
    "dairy_enriched_filtered.xlsx"
    "EJgxfgP_daily_interpolated.xlsx"
)

MISSING_COUNT=0

for file in "${DATA_FILES[@]}"; do
    if [ -f "$file" ]; then
        FILE_SIZE=$(du -h "$file" | cut -f1)
        echo "✓ $file ($FILE_SIZE)"
    else
        echo "✗ $file - NOT FOUND"
        ((MISSING_COUNT++))
    fi
done

if [ $MISSING_COUNT -gt 0 ]; then
    echo ""
    echo "⚠ Warning: $MISSING_COUNT data file(s) missing"
    echo "Please ensure all data files are in: $BASE_DIR"
fi

# -----------------------------------------------------------------------------
# 8. SUMMARY
# -----------------------------------------------------------------------------

echo ""
echo "================================================================================"
echo "SETUP COMPLETE!"
echo "================================================================================"
echo ""
echo "Python command: $PYTHON_CMD"
echo "Pip command: $PIP_CMD"
echo ""
echo "Next steps:"
echo "  1. Navigate to project directory:"
echo "     cd \"$BASE_DIR\""
echo ""
echo "  2. Run the master pipeline:"
echo "     $PYTHON_CMD 00_master_pipeline.py"
echo ""
echo "  Or run individual scripts:"
echo "     $PYTHON_CMD 01_data_loading_preprocessing.py"
echo "     $PYTHON_CMD 02_descriptive_statistics.py"
echo "     # ... etc."
echo ""
echo "================================================================================"
