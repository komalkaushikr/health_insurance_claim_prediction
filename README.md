# Health Insurance Claim Prediction

A machine learning project that predicts health insurance claim amounts using patient data. Built to demonstrate end-to-end data science skills — from raw data to a trained model with business insights.



## Business Problem

Insurance companies need to accurately predict claim costs to set fair premiums. Overestimating loses customers. Underestimating loses money. This model predicts claim amounts with 96% accuracy (R² = 0.96).



## Dataset

- 15,000 patients
- 13 features: age, BMI, smoker status, hereditary diseases, diabetes, and more
- Target variable: claim amount (ranges from $0 to $65,000)



## Key Findings from EDA

- Smokers claim **3x more** than non-smokers
- Heart Disease patients have the highest average claims
- Claim amounts increase with age
- Diabetic patients claim significantly more than non-diabetic



## Model Performance

| Metric | Score |
|--------|-------|
| R² Score | 0.960 |
| Mean Absolute Error | $1,053 |

Model used: **XGBoost Regressor**


## Top Features Driving Claims

1. Smoker status (by far the most important)
2. Hereditary diseases
3. BMI
4. Diabetes
5. Age

---

## Project Structure

    ├── data/
    │   └── raw/               # Original dataset
    ├── notebooks/
    │   ├── 01_EDA.ipynb       # Exploratory data analysis
    │   └── 02_model.ipynb     # Model training and evaluation
    ├── src/                   # Source code 
    └── README.md



## Tools Used

- Python, Pandas, NumPy
- Scikit-learn, XGBoost
- Matplotlib, Seaborn
- Git, GitHub



## How to Run

```bash
git clone https://github.com/komalkaushikr/health_insurance_claim_prediction.git
cd health_insurance_claim_prediction
pip install -r requirements.txt
jupyter notebook
```