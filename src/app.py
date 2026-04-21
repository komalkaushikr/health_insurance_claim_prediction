import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Health Insurance Claim Predictor",
    page_icon="🏥",
    layout="wide"
)

st.markdown("""
<style>
    .main { background-color: #0f1117; }
    .block-container { padding: 2rem 3rem; }
    .stSlider > div > div { background: #1e2130; }
    .metric-card {
        background: #1e2130;
        border-radius: 12px;
        padding: 1.5rem;
        border: 1px solid #2d3250;
        margin-bottom: 1rem;
    }
    .result-card {
        background: linear-gradient(135deg, #1a472a, #2d6a4f);
        border-radius: 16px;
        padding: 2rem;
        text-align: center;
        border: 1px solid #40916c;
    }
    .driver-card {
        background: #1e2130;
        border-left: 4px solid #e63946;
        border-radius: 8px;
        padding: 1rem 1.5rem;
        margin: 0.5rem 0;
    }
    .driver-card-info {
        background: #1e2130;
        border-left: 4px solid #457b9d;
        border-radius: 8px;
        padding: 1rem 1.5rem;
        margin: 0.5rem 0;
    }
    h1 { color: #ffffff; font-size: 2.2rem !important; }
    h3 { color: #a8dadc; }
    .stSelectbox label, .stSlider label { color: #a8dadc !important; font-weight: 500; }
    .stButton > button {
        background: linear-gradient(135deg, #457b9d, #1d3557);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.75rem 2rem;
        font-size: 1.1rem;
        font-weight: 600;
        width: 100%;
        margin-top: 1rem;
        cursor: pointer;
    }
    .stButton > button:hover { opacity: 0.9; }
</style>
""", unsafe_allow_html=True)

model = joblib.load("src/model.pkl")

st.markdown("# 🏥 Health Insurance Claim Predictor")
st.markdown("##### Predict estimated insurance claim costs based on patient health profile")
st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 👤 Personal Info")
    age = st.slider("Age", 18, 95, 35)
    sex = st.selectbox("Sex", ["Male", "Female"])
    weight = st.slider("Weight (kg)", 30, 150, 70)
    bmi = st.slider("BMI", 10.0, 60.0, 25.0)
    no_of_dependents = st.slider("Number of Dependents", 0, 5, 1)

with col2:
    st.markdown("### 🏥 Health Info")
    hereditary_diseases = st.selectbox("Hereditary Disease", [
        "NoDisease", "Epilepsy", "Alzheimer", "Arthritis",
        "Cancer", "Diabetes", "EyeDisease", "HeartDisease",
        "High BP", "Obesity"
    ])
    smoker = st.selectbox("Smoker", ["No", "Yes"])
    diabetes = st.selectbox("Diabetes", ["No", "Yes"])
    bloodpressure = st.slider("Blood Pressure", 60, 130, 80)
    regular_ex = st.selectbox("Regular Exercise", ["No", "Yes"])

with col3:
    st.markdown("### 💼 Lifestyle")
    city_options = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata"]
    city = st.selectbox("City", city_options)
    job_options = ["Engineer", "Doctor", "Teacher", "Actor", "Chef",
                   "Academician", "HomeMakers", "Other"]
    job_title = st.selectbox("Job Title", job_options)

    st.markdown("<br>", unsafe_allow_html=True)
    predict = st.button("🔍 Predict Claim Amount")

disease_map = {
    "NoDisease": 0, "Epilepsy": 1, "Alzheimer": 2, "Arthritis": 3,
    "Cancer": 4, "Diabetes": 5, "EyeDisease": 6, "HeartDisease": 7,
    "High BP": 8, "Obesity": 9
}
city_map = {"Mumbai": 0, "Delhi": 1, "Bangalore": 2, "Chennai": 3, "Kolkata": 4}
job_map = {"Engineer": 0, "Doctor": 1, "Teacher": 2, "Actor": 3,
           "Chef": 4, "Academician": 5, "HomeMakers": 6, "Other": 7}

input_data = pd.DataFrame([{
    "age": age,
    "sex": 1 if sex == "Male" else 0,
    "weight": weight,
    "bmi": bmi,
    "hereditary_diseases": disease_map[hereditary_diseases],
    "no_of_dependents": no_of_dependents,
    "smoker": 1 if smoker == "Yes" else 0,
    "city": city_map.get(city, 0),
    "bloodpressure": bloodpressure,
    "diabetes": 1 if diabetes == "Yes" else 0,
    "regular_ex": 1 if regular_ex == "Yes" else 0,
    "job_title": job_map.get(job_title, 0)
}])

st.markdown("---")

if predict:
    prediction = model.predict(input_data)[0]

    st.markdown(f"""
    <div class="result-card">
        <h2 style='color:white; font-size:1.2rem; margin-bottom:0.5rem'>Estimated Claim Amount</h2>
        <h1 style='color:#95d5b2; font-size:3rem; margin:0'>${prediction:,.0f}</h1>
        <p style='color:#b7e4c7; margin-top:0.5rem'>Based on the patient profile provided</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("### 🔎 What's driving this prediction?")

    drivers = []
    if smoker == "Yes":
        drivers.append(("🚬 Smoker", "Smoking is the single biggest driver of high claims. It adds an estimated +$6,937 on average.", "risk"))
    if hereditary_diseases != "NoDisease":
        drivers.append((f"🧬 {hereditary_diseases}", f"Hereditary conditions significantly increase expected claim costs.", "risk"))
    if age > 50:
        drivers.append(("📅 Age above 50", "Older patients tend to have higher and more frequent claims.", "risk"))
    if bmi > 30:
        drivers.append(("⚖️ High BMI", f"BMI of {bmi:.1f} is above healthy range, increasing claim risk.", "risk"))
    if diabetes == "Yes":
        drivers.append(("💉 Diabetes", "Diabetic patients have higher average claim amounts.", "risk"))
    if regular_ex == "Yes":
        drivers.append(("🏃 Regular Exercise", "Exercise reduces long-term health risks and claim amounts.", "good"))
    if smoker == "No":
        drivers.append(("✅ Non-smoker", "Not smoking significantly reduces expected claim costs.", "good"))

    if not drivers:
        drivers.append(("✅ Low risk profile", "This patient has a generally healthy profile with no major risk factors.", "good"))

    for label, explanation, kind in drivers:
        css_class = "driver-card" if kind == "risk" else "driver-card-info"
        st.markdown(f"""
        <div class="{css_class}">
            <strong style='color:white'>{label}</strong>
            <p style='color:#adb5bd; margin:0.3rem 0 0'>{explanation}</p>
        </div>
        """, unsafe_allow_html=True)
else:
    st.markdown("""
    <div style='text-align:center; padding: 3rem; color: #6c757d;'>
        <h3 style='color:#6c757d'>Fill in the patient details above and click Predict</h3>
        <p>The model will estimate the insurance claim amount and explain what's driving it.</p>
    </div>
    """, unsafe_allow_html=True)