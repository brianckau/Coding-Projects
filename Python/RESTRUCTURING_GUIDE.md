# GitHub Repository Restructuring Guide

## Progress Summary

I've successfully started reorganizing your GitHub repository to transform it from a "student-like" structure into a production-grade, professional portfolio that will impress S&T and Hedge Fund recruiters.

### ✅ Completed Actions:

1. **Created `research/notebooks/` folder** - Professional home for all .ipynb files
2. **Created `src/quantlib/` package** - With proper `__init__.py` for reusable quant finance modules

### 📋 Current File Inventory:

**Finance Folder:**
- Monte_Carlo_Sim.py
- Portfolio_Sharpe.py
- Technical Indicators.py

**Data Mining/Coursework:**
- ConvNeuralNet_Digit.ipynb
- CustomerChurn.ipynb
- KNN_MovieRecommend.ipynb

**Data Mining/Kaggle:**
- 1.ipynb

**WebScraping:**
- SentimentAnalysisFromNews.ipynb

**Quantitative Research:**
- UnderDevelopment.py (DELETE - never show WIP files)

---

## Complete Restructuring Plan

### Target Structure:
```
Python/
├── research/
│   └── notebooks/
│       ├── 01_portfolio_optimization.ipynb    (from Portfolio_Sharpe.py)
│       ├── 02_monte_carlo_risk.ipynb          (from Monte_Carlo_Sim.py)
│       ├── 03_cnn_digit_recognition.ipynb     (from ConvNeuralNet_Digit.ipynb)
│       ├── 04_customer_churn_analysis.ipynb   (from CustomerChurn.ipynb)
│       ├── 05_knn_movie_recommend.ipynb       (from KNN_MovieRecommend.ipynb)
│       ├── 06_news_sentiment_analysis.ipynb   (from SentimentAnalysisFromNews.ipynb)
│       └── 07_kaggle_competition.ipynb        (from 1.ipynb - rename meaningfully)
│
├── src/
│   ├── quantlib/
│   │   ├── __init__.py                        (✅ Already created)
│   │   ├── portfolio.py                       (from Portfolio_Sharpe.py)
│   │   ├── risk.py                            (from Monte_Carlo_Sim.py)
│   │   └── technicals.py                      (from Technical Indicators.py)
│   │
│   └── scrapers/
│       ├── __init__.py
│       └── news_scraper.py                    (extracted from SentimentAnalysisFromNews.ipynb)
│
├── tests/
│   ├── test_portfolio.py
│   └── test_risk.py
│
├── data/                                      (Add to .gitignore)
│   ├── raw/
│   └── processed/
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Git Commands to Complete Restructuring

### Option 1: Using Git Locally (RECOMMENDED - Fastest)

```bash
# Clone the repository
cd ~/Desktop  # or wherever you want to work
git clone https://github.com/brianckau/Programming-Projects.git
cd Programming-Projects/Python

# Create remaining folder structure
mkdir -p src/scrapers tests data/raw data/processed

# Create __init__.py files
echo '"""' > src/__init__.py
echo 'Scrapers and data collection modules' >> src/__init__.py
echo '"""' >> src/__init__.py

echo '# Placeholder for tests' > tests/__init__.py

# Move and rename .ipynb files to research/notebooks/
git mv "Data Mining/Coursework/ConvNeuralNet_Digit.ipynb" "research/notebooks/03_cnn_digit_recognition.ipynb"
git mv "Data Mining/Coursework/CustomerChurn.ipynb" "research/notebooks/04_customer_churn_analysis.ipynb"
git mv "Data Mining/Coursework/KNN_MovieRecommend.ipynb" "research/notebooks/05_knn_movie_recommend.ipynb"
git mv "Data Mining/Kaggle/1.ipynb" "research/notebooks/07_kaggle_competition.ipynb"  # Rename this meaningfully!
git mv "WebScraping/SentimentAnalysisFromNews.ipynb" "research/notebooks/06_news_sentiment_analysis.ipynb"

# Move .py files to src/quantlib/
git mv Finance/Portfolio_Sharpe.py src/quantlib/portfolio.py
git mv Finance/Monte_Carlo_Sim.py src/quantlib/risk.py
git mv "Finance/Technical Indicators.py" src/quantlib/technicals.py

# Delete old folders and unwanted files
git rm "Quantitative Research/UnderDevelopment.py"
git rm -r "Data Mining" Finance "Quantitative Research" WebScraping

# Commit all changes
git commit -m "Restructure: Transform into professional production-grade portfolio

- Moved all notebooks to research/notebooks/ with numbered prefixes
- Created src/quantlib package for reusable finance modules
- Deleted student-like folder names (Data Mining, etc.)
- Removed WIP file (UnderDevelopment.py)
- Prepared structure for tests/ and data/ directories"

# Push to GitHub
git push origin main
```

### Option 2: Create Essential Files

Create `.gitignore`:
```
# Data
data/
*.csv
*.xlsx
*.json

# Python
__pycache__/
*.py[cod]
*$py.class
.ipynb_checkpoints/
*.so
.Python
env/
venv/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db
```

Create `requirements.txt`:
```
# Core Data Science
numpy>=1.24.0
pandas>=2.0.0
matplotlib>=3.7.0
seaborn>=0.12.0

# Financial Data
yfinance>=0.2.18
pandas-datareader>=0.10.0

# Machine Learning
scikit-learn>=1.2.0
tensorflow>=2.12.0

# Web Scraping
beautifulsoup4>=4.12.0
requests>=2.31.0
selenium>=4.9.0

# Visualization
plotly>=5.14.0

# Development
jupyter>=1.0.0
ipykernel>=6.23.0
pytest>=7.3.0
```

---

## Key Improvements This Achieves:

### 1. **Separation of Concerns**
- `research/notebooks/` = Exploration & analysis
- `src/` = Production-ready, reusable code
- `tests/` = Professional testing practice

### 2. **Module Naming**
- `portfolio.py` instead of `Portfolio_Sharpe.py` → Suggests extensibility (can add Sortino, Treynor, etc.)
- `risk.py` instead of `Monte_Carlo_Sim.py` → Broader scope for VaR, CVaR, stress testing

### 3. **Notebook Numbering**
- `01_`, `02_`, `03_` prefixes show systematic approach
- Easy to understand your analytical workflow

### 4. **Professional Signal**
- Tests directory (even if empty) = Top 1% of students
- Proper Python packages with `__init__.py`
- `.gitignore` and `requirements.txt` = Production mindset

---

## After Restructuring:

1. **Delete this guide file** (once done)
2. **Update README.md** with:
   - Project overview
   - Installation instructions
   - Module descriptions
   - Your contact info

3. **Add at least ONE test** to `tests/` folder:
```python
# tests/test_portfolio.py
import sys
sys.path.append('../src')
from quantlib import portfolio

def test_sharpe_ratio_calculation():
    # Simple test example
    assert True  # Replace with actual test
```

---

## Questions?

This structure mirrors actual quant desk organization. You've separated:
- **Research** (experimentation in notebooks)
- **Production** (reusable modules in src/)
- **Quality Assurance** (tests/)

This will immediately differentiate your GitHub from other candidates.
