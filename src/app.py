import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Health Insurance Claim Predictor",
    page_icon="🛡️",
    layout="wide"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    * { font-family: 'Inter', sans-serif; }
    
    .main { background-color: #f0f4ff; }
    .block-container { padding: 2rem 4rem; max-width: 1200px; margin: 0 auto; }
    
    .hero {
        text-align: center;
        padding: 2.5rem 0 2rem;
    }
    .hero-icon {
        background: linear-gradient(135deg, #6366f1, #8b5cf6);
        width: 72px; height: 72px;
        border-radius: 20px;
        display: flex; align-items: center; justify-content: center;
        margin: 0 auto 1.5rem;
        font-size: 2rem;
    }
    .hero h1 {
        font-size: 2.6rem !important;
        font-weight: 700;
        background: linear-gradient(135deg, #6366f1, #8b5cf6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    .hero p {
        color: #64748b;
        font-size: 1rem;
        margin-bottom: 0.5rem;
    }
    .hero-badge {
        display: inline-block;
        background: #ede9fe;
        color: #6366f1;
        padding: 0.3rem 1rem;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 500;
    }

    .card {
        background: white;
        border-radius: 20px;
        padding: 1.8rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.06);
        margin-bottom: 1rem;
        border: 1px solid #e2e8f0;
    }
    .card-header {
        display: flex;
        align-items: center;
        gap: 0.8rem;
        margin-bottom: 1.5rem;
    }
    .card-icon {
        width: 40px; height: 40px;
        border-radius: 10px;
        display: flex; align-items: center; justify-content: center;
        font-size: 1.2rem;
    }
    .icon-blue { background: #dbeafe; }
    .icon-green { background: #dcfce7; }
    .icon-purple { background: #ede9fe; }
    .card-title { font-weight: 600; font-size: 1.05rem; color: #1e293b; margin: 0; }
    .card-subtitle { color: #94a3b8; font-size: 0.8rem; margin: 0; }

    .result-box {
        background: linear-gradient(135deg, #6366f1, #8b5cf6);
        border-radius: 20px;
        padding: 2.5rem;
        text-align: center;
        color: white;
        margin: 1.5rem 0;
    }
    .result-box .label { font-size: 1rem; opacity: 0.85; margin-bottom: 0.5rem; }
    .result-box .amount { font-size: 3.5rem; font-weight: 700; margin: 0; }
    .result-box .sub { font-size: 0.85rem; opacity: 0.7; margin-top: 0.5rem; }

    .driver-risk {
        background: #fff5f5;
        border-left: 4px solid #f87171;
        border-radius: 10px;
        padding: 0.9rem 1.2rem;
        margin: 0.5rem 0;
    }
    .driver-good {
        background: #f0fdf4;
        border-left: 4px solid #4ade80;
        border-radius: 10px;
        padding: 0.9rem 1.2rem;
        margin: 0.5rem 0;
    }
    .driver-title { font-weight: 600; color: #1e293b; font-size: 0.95rem; }
    .driver-desc { color: #64748b; font-size: 0.85rem; margin-top: 0.2rem; }

    .empty-state {
        text-align: center;
        padding: 3rem 1rem;
        color: #94a3b8;
    }
    .empty-state .icon { font-size: 2.5rem; margin-bottom: 1rem; }
    .empty-state h3 { color: #64748b; font-weight: 600; }

    .footer {
        text-align: center;
        padding: 2rem 0 1rem;
        color: #94a3b8;
        font-size: 0.85rem;
        border-top: 1px solid #e2e8f0;
        margin-top: 2rem;
    }
    .footer a {
        color: #6366f1;
        text-decoration: none;
        font-weight: 500;
    }

    div[data-testid="stSlider"] label { color: #475569 !important; font-weight: 500; }
    div[data-testid="stSelectbox"] label { color: #475569 !important; font-weight: 500; }
    .stSlider > div > div > div { background: #6366f1 !important; }

    .stButton > button {
        background: linear-gradient(135deg, #6366f1, #8b5cf6) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.75rem 2rem !important;
        font-size: 1rem !important;
        font-weight: 600 !important;
        width: 100% !important;
        margin-top: 0.5rem !important;
    }
</style>
""", unsafe_allow_html=True)

model = joblib.load("src/model.pkl")

st.markdown("""
<div class="hero">
    <div class="hero-icon">🛡️</div>
    <h1>Health Insurance Claim Predictor</h1>
    <p>AI-powered estimation of insurance claim costs based on comprehensive patient health data</p>
    <span class="hero-badge">✨ Powered by Advanced Analytics</span>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <div class="card-header">
            <div class="card-icon icon-blue">👤</div>
            <div>
                <p class="card-title">Personal Info</p>
                <p class="card-subtitle">Demographics</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    age = st.slider("Age", 18, 95, 35)
    sex = st.selectbox("Sex", ["Male", "Female"])
    weight = st.slider("Weight (kg)", 30, 150, 70)
    bmi = st.slider("BMI", 10.0, 60.0, 25.0)
    no_of_dependents = st.slider("Number of Dependents", 0, 5, 1)

with col2:
    st.markdown("""
    <div class="card">
        <div class="card-header">
            <div class="card-icon icon-green">🏥</div>
            <div>
                <p class="card-title">Health Info</p>
                <p class="card-subtitle">Medical History</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
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
    st.markdown("""
    <div class="card">
        <div class="card-header">
            <div class="card-icon icon-purple">💼</div>
            <div>
                <p class="card-title">Lifestyle</p>
                <p class="card-subtitle">Environment</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    city = st.selectbox("City", ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata"])
    job_title = st.selectbox("Job Title", [
        "Engineer", "Doctor", "Teacher", "Actor",
        "Chef", "Academician", "HomeMakers", "Other"
    ])
    st.markdown("<br><br><br>", unsafe_allow_html=True)
    predict = st.button("📊 Predict Claim Amount")

disease_map = {
    "NoDisease": 0, "Epilepsy": 1, "Alzheimer": 2, "Arthritis": 3,
    "Cancer": 4, "Diabetes": 5, "EyeDisease": 6, "HeartDisease": 7,
    "High BP": 8, "Obesity": 9
}
city_map = {"Mumbai": 0, "Delhi": 1, "Bangalore": 2, "Chennai": 3, "Kolkata": 4}
job_map = {"Engineer": 0, "Doctor": 1, "Teacher": 2, "Actor": 3,
           "Chef": 4, "Academician": 5, "HomeMakers": 6, "Other": 7}

input_data = pd.DataFrame([{
    "age": age, "sex": 1 if sex == "Male" else 0,
    "weight": weight, "bmi": bmi,
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
    <div class="result-box">
        <p class="label">Estimated Claim Amount</p>
        <p class="amount">${prediction:,.0f}</p>
        <p class="sub">Based on the patient profile provided</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🔎 What's driving this prediction?")

    drivers = []
    if smoker == "Yes":
        drivers.append(("🚬 Smoker status", "Smoking is the biggest driver — adds ~$6,937 on average to claims.", "risk"))
    if hereditary_diseases != "NoDisease":
        drivers.append((f"🧬 {hereditary_diseases}", "Hereditary conditions significantly increase expected claim costs.", "risk"))
    if age > 50:
        drivers.append(("📅 Age above 50", "Older patients tend to have higher and more frequent claims.", "risk"))
    if bmi > 30:
        drivers.append((f"⚖️ High BMI ({bmi:.1f})", "BMI above 30 is associated with higher health risks and costs.", "risk"))
    if diabetes == "Yes":
        drivers.append(("💉 Diabetes", "Diabetic patients have higher average claim amounts.", "risk"))
    if regular_ex == "Yes":
        drivers.append(("🏃 Regular Exercise", "Exercise reduces long-term health risks and lowers claims.", "good"))
    if smoker == "No":
        drivers.append(("✅ Non-smoker", "Not smoking significantly reduces expected claim costs.", "good"))
    if bmi <= 25:
        drivers.append(("✅ Healthy BMI", "A healthy BMI is associated with lower claim amounts.", "good"))

    if not drivers:
        drivers.append(("✅ Low risk profile", "This patient has a healthy profile with no major risk factors.", "good"))

    for title, desc, kind in drivers:
        css = "driver-risk" if kind == "risk" else "driver-good"
        st.markdown(f"""
        <div class="{css}">
            <div class="driver-title">{title}</div>
            <div class="driver-desc">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

else:
    st.markdown("""
    <div class="empty-state">
        <div class="icon">✨</div>
        <h3>Fill in the patient details above and click Predict</h3>
        <p>Our model will estimate the insurance claim amount and explain what's driving it.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="footer">
    Created by <strong>Komal Kaushik</strong> &nbsp;|&nbsp;
    <a href="https://github.com/komalkaushikr" target="_blank">View on GitHub</a>
</div>
""", unsafe_allow_html=True)