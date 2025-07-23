# app.py
import streamlit as st
import pandas as pd
import joblib
import json

# ---------------- Custom CSS ----------------
st.markdown("""
    <style>
    body {
        background-color: #f7f9fc;
        font-family: 'Segoe UI', sans-serif;
    }

    .main .block-container {
        padding: 2rem 3rem;
        background-color: #ffffff;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0,0,0,0.05);
    }

    h1 {
        color: #2b2d42;
        text-align: center;
        font-size: 42px;
        font-weight: bold;
    }

    .stButton > button {
        background-color: #4CAF50;
        color: white;
        font-size: 18px;
        border-radius: 8px;
        padding: 10px 24px;
        border: none;
        transition: background-color 0.3s ease;
    }

    .stButton > button:hover {
        background-color: #45a049;
        cursor: pointer;
    }

    .predict-box {
        background: linear-gradient(to right, #74ebd5, #acb6e5);
        border-radius: 10px;
        padding: 20px 30px;
        margin-top: 20px;
        color: #003049;
        font-size: 20px;
        font-weight: bold;
        border: 1px solid #ddd;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------- Title ----------------
st.title("💼 AI-Based Salary Category Predictor")
st.markdown("### Fill in the details below to estimate your salary category")

# ---------------- Load Model ----------------
@st.cache_resource
def load_model_and_columns():
    model_data = joblib.load("salary_predictor.pkl")
    with open("model_columns.json", "r") as f:
        columns = json.load(f)
    return model_data['model'], model_data['label_encoders'], columns

try:
    model, encoders, expected_cols = load_model_and_columns()
except FileNotFoundError as e:
    st.error(f"❌ Model files not found: {e}")
    st.stop()


# ---------------- Form ----------------
with st.form("predict_form"):
    st.subheader("🔍 Candidate Information:")

    col1, col2 = st.columns(2)

    with col1:
        education = st.selectbox("📘 Education", ["Bachelor", "Master", "PhD"])
        job_title = st.selectbox("🧾 Job Title", ["Data Scientist", "Software Engineer", "Manager", "Analyst"])
        gender = st.selectbox("🧑 Gender", ["Male", "Female", "Other"])

    with col2:
        experience = st.slider("💼 Experience (Years)", 0, 40, 3)
        age = st.slider("🎂 Age", 18, 65, 25)

    submitted = st.form_submit_button("👉 Predict Salary Category")

# ---------------- Process & Predict ----------------
if submitted:
    input_data = pd.DataFrame([{
        "Education": education,
        "Experience": experience,
        "Job_Title": job_title,
        "Age": age,
        "Gender": gender
    }])

    for col in ["Education", "Gender", "Job_Title"]:
        le = encoders[col]
        try:
            input_data[col] = le.transform([input_data[col][0]])
        except ValueError:
            st.error(f"❌ '{input_data[col][0]}' not in model's trained data for column '{col}'")
            st.stop()

    input_data = input_data[expected_cols]

    # Prediction
    prediction = model.predict(input_data)[0]

    # Fancy result box
    st.markdown(f"""
        <div class='predict-box'>
            💡 Based on the input, the predicted <b>Salary Category</b> is:<br><br>
            <center><h2 style='color:#064420'>💰 {prediction}</h2></center>
        </div>
    """, unsafe_allow_html=True)
