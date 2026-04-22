#  Health Insurance Claim Prediction

> Predicting insurance claim costs using machine learning — helping insurers set accurate premiums and reduce financial risk.

##  Live Demo
###  [Try the Live Dashboard](https://healthinsuranceclaimprediction.streamlit.app)
*Enter any patient profile and get an instant claim prediction with full explanation*

---

##  Business Problem

Insurance companies lose millions every year from mispriced premiums:
- **Underpricing** → company pays more than it collects → financial loss
- **Overpricing** → customers leave for competitors → revenue loss

This model predicts claim amounts for new customers **before** they file a claim — allowing insurers to price premiums accurately from day one.

**Who benefits:**
- Underwriters setting premium prices
- Risk assessment teams
- Actuarial departments

---

##  Results

| Metric | Score |
|--------|-------|
| R² Score | 0.960 |
| Mean Absolute Error | $1,053 |
| Training Data | 15,000 patients |

> The model explains **96% of claim variation** with an average error of only $1,053 on claims up to $65,000.

---

##  Key Insights

-  **Smokers claim 3x more** than non-smokers — the single biggest cost driver
-  **Heart Disease** patients have the highest average claims of all conditions
-  **Age** and **BMI** consistently increase claim amounts
-  **Diabetic patients** cost significantly more than non-diabetic on average

These insights can directly inform premium pricing tiers by risk segment.

---

##  Technical Stack

| Layer | Tools |
|-------|-------|
| Data Analysis | Python, Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn, XGBoost |
| Explainability | SHAP |
| Dashboard | Streamlit |
| Version Control | Git, GitHub |

---

##  Project Structure

    ├── data/
    │   └── raw/               # Original dataset (15,000 patients)
    ├── notebooks/
    │   ├── 01_EDA.ipynb       # Exploratory analysis & business insights
    │   └── 02_model.ipynb     # Model training, evaluation & SHAP
    ├── src/
    │   ├── app.py             # Streamlit dashboard
    │   └── model.pkl          # Trained XGBoost model
    └── README.md

---

##  Methodology

1. **EDA** — Identified key cost drivers across 13 patient features
2. **Feature Engineering** — Encoded categorical variables, handled missing values
3. **Modeling** — Trained XGBoost Regressor with 80/20 train-test split
4. **Explainability** — SHAP values show exactly why each prediction was made
5. **Deployment** — Live Streamlit dashboard for real-time predictions

---

## ▶ Run Locally

```bash
git clone https://github.com/komalkaushikr/health_insurance_claim_prediction.git
cd health_insurance_claim_prediction
pip install -r requirements.txt
streamlit run src/app.py
```

---

##  About

Built by **Komal Kaushik** as a demonstration of end-to-end data science skills —
from raw data to a deployed, explainable ML product.

[![GitHub](https://img.shields.io/badge/GitHub-komalkaushikr-181717?style=flat&logo=github)](https://github.com/komalkaushikr)