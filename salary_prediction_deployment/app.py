import streamlit as st
import joblib
import pandas as pd

# -----------------------------
# Load trained model
# -----------------------------
model = joblib.load('salary_prediction_model.joblib')

st.set_page_config(
    page_title="Salary Predictor",
    layout="centered",
    page_icon="💼"
)

# -----------------------------
# Title & Intro
# -----------------------------
st.title("💼 Salary Prediction App")
st.markdown(
    """
    This is an **educational demo** of a machine learning salary prediction model.  
    Predictions are **approximate** and depend on available features.
    """
)

st.divider()

# -----------------------------
# Job Details
# -----------------------------
st.subheader("🧾 Job Details")

job_role = st.selectbox(
    "Job Role",
    [
        "Data Scientist",
        "Data Analyst",
        "Data Engineer",
        "Machine Learning Engineer",
        "Business Analyst",
        "Other"
    ]
)

sector = st.selectbox(
    "Sector",
    [
        "Information Technology",
        "Finance",
        "Health Care",
        "Business Services",
        "Education",
        "Retail",
        "Manufacturing",
        "Other"
    ]
)

state = st.selectbox(
    "State",
    ["CA", "NY", "TX", "FL", "WA", "IL", "MA", "Other"]
)

ownership = st.selectbox(
    "Type of Ownership",
    ["Private", "Public", "Government", "Nonprofit", "Other"]
)

rating = st.slider(
    "Company Rating",
    min_value=1.0,
    max_value=5.0,
    value=3.5,
    step=0.1
)

size = st.selectbox(
    "Company Size",
    {
        1: "1–50 employees",
        2: "51–200 employees",
        3: "201–500 employees",
        4: "501–1000 employees",
        5: "1001–5000 employees",
        6: "5001–10000 employees",
        7: "10000+ employees"
    }.keys(),
    format_func=lambda x: {
        1: "1–50 employees",
        2: "51–200 employees",
        3: "201–500 employees",
        4: "501–1000 employees",
        5: "1001–5000 employees",
        6: "5001–10000 employees",
        7: "10000+ employees"
    }[x]
)

st.divider()

# -----------------------------
# Skills
# -----------------------------
st.subheader("🛠 Skills")

col1, col2, col3 = st.columns(3)

with col1:
    python = st.checkbox("Python")
    sql = st.checkbox("SQL")
    excel = st.checkbox("Excel")
    r = st.checkbox("R")

with col2:
    spark = st.checkbox("Spark")
    hadoop = st.checkbox("Hadoop")
    aws = st.checkbox("AWS")
    azure = st.checkbox("Azure")
    gcp = st.checkbox("GCP")

with col3:
    tableau = st.checkbox("Tableau")
    power_bi = st.checkbox("Power BI")
    tensorflow = st.checkbox("TensorFlow")
    pytorch = st.checkbox("PyTorch")
    nlp = st.checkbox("NLP")

machine_learning = st.checkbox("Machine Learning")
deep_learning = st.checkbox("Deep Learning")
statistics = st.checkbox("Statistics")

st.divider()

# -----------------------------
# Seniority
# -----------------------------
st.subheader("📈 Seniority Level")

seniority = st.radio(
    "Select seniority",
    ["Junior", "Senior", "Manager"],
    horizontal=True
)

seniority_junior = int(seniority == "Junior")
seniority_senior = int(seniority == "Senior")
seniority_manager = int(seniority == "Manager")

# -----------------------------
# Prediction
# -----------------------------
st.divider()

if st.button("🔮 Predict Salary", use_container_width=True):
    input_data = {
        'Rating': rating,
        'Size': size,
        'job_role': job_role,
        'Sector': sector,
        'State': state,
        'Type of ownership': ownership,
        'python': int(python),
        'sql': int(sql),
        'excel': int(excel),
        'r': int(r),
        'spark': int(spark),
        'hadoop': int(hadoop),
        'aws': int(aws),
        'azure': int(azure),
        'gcp': int(gcp),
        'tableau': int(tableau),
        'power_bi': int(power_bi),
        'tensorflow': int(tensorflow),
        'pytorch': int(pytorch),
        'machine_learning': int(machine_learning),
        'deep_learning': int(deep_learning),
        'statistics': int(statistics),
        'nlp': int(nlp),
        'seniority_junior': seniority_junior,
        'seniority_senior': seniority_senior,
        'seniority_manager': seniority_manager
    }

    df_input = pd.DataFrame([input_data])

    prediction = model.predict(df_input)[0]

    st.success(f"💰 Estimated Average Salary: **${prediction:,.2f}k**")
    st.caption("Typical prediction error: ±20–25k")

st.divider()
