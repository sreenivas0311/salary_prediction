💼 Glassdoor Salary Prediction

An end-to-end machine learning regression project that predicts the average salary for data-related job roles using Glassdoor job listings.
The project covers data cleaning, feature engineering, modeling, evaluation, and deployment with a Streamlit web app.

📌 Project Overview

Salary prediction is challenging due to:

high variance across roles

location and company differences

incomplete information in job postings

This project builds a realistic, leakage-free salary prediction model and deploys it as an educational demo application.

⚠️ Predictions are approximate and intended for learning and portfolio demonstration.

🗂️ Project Structure
glassdoor-salary-prediction/
│
├── notebooks/
│   └── salary_model_training.ipynb   # Data cleaning, EDA, modeling
│
├── deployment/
│   ├── app.py                        # Streamlit web app
│   └── salary_prediction_model.joblib
│
├── requirements.txt
├── README.md

📊 Dataset

Source: Glassdoor job postings dataset

Target Variable: avg_salary

Key Features:

Job role

Sector

State

Company size

Company rating

Skills extracted from job description

Seniority inferred from text

❌ Leakage Prevention

The following columns were intentionally removed:

min_salary

max_salary

These are directly related to the target and would cause target leakage.

🧹 Data Cleaning & Feature Engineering
✔ Cleaning

Removed invalid values (-1)

Dropped hourly salary entries

Standardized salary format

Extracted State from location

✔ Feature Engineering

Company Size → ordinal encoding (1–7)

Skills extraction (binary flags):

Python, SQL, AWS, Spark, Tableau, ML, etc.

Seniority indicators:

Junior

Senior

Manager

Categorical encoding:

One-Hot Encoding via ColumnTransformer

🧠 Modeling Approach
Models Evaluated

Linear Regression

Ridge Regression

Random Forest

Gradient Boosting

Evaluation Strategy

Train/Test split (80/20)

5-fold Cross-Validation on training data

Metrics:

MAE (Mean Absolute Error)

R² Score

Best Performing Model

Ridge Regression

Chosen for:

stability

generalization

interpretability

minimal overfitting

📈 Final Results
Metric	Value
Test MAE	~22–25
R² Score	~0.25

The model captures a reasonable amount of salary signal given the available features.
Additional improvements would require richer data (experience, skill depth, company pay bands).

🚀 Deployment

The model is deployed as a Streamlit web application.

Features

Dropdown-based inputs (no free text errors)

Skill selection via checkboxes

Seniority selection

Clear disclaimers on prediction uncertainty

Run Locally
pip install -r requirements.txt
streamlit run app.py

🧰 Tech Stack

Python

pandas, numpy

scikit-learn (1.6.1)

joblib

Streamlit

🎯 Key Learnings

Feature engineering does not always guarantee better performance

Preventing target leakage is critical

Model evaluation must respect proper train/test separation

Deployment requires environment version consistency

Honest communication of model limitations is essential

📌 Disclaimer

This project is for educational and portfolio purposes only.
Predictions should not be used for real-world compensation decisions.

🙌 Author

Sreenivas Sree
Data Science & Machine Learning Enthusiast

⭐ Future Improvements

Experience extraction (years)

TF-IDF features from job descriptions

City-level cost-of-living adjustment

Model explainability (SHAP)
