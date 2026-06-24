import streamlit as st
import numpy as np
import joblib

st.set_page_config(
    page_title="Insurance Premium Predictor",
    page_icon="💰",
    layout="wide"
)

model = joblib.load(
    "insurance_model.pkl"
)

scaler = joblib.load(
    "scaler.pkl"
)

st.title("💰 Insurance Premium Predictor")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:

    age = st.number_input(
        "Age",
        18,
        100,
        25
    )

    sex = st.selectbox(
        "Gender",
        ["Male","Female"]
    )

    bmi = st.number_input(
        "BMI",
        10.0,
        50.0,
        25.0
    )

with col2:

    children = st.number_input(
        "Children",
        0,
        10,
        0
    )

    smoker = st.selectbox(
        "Smoker",
        ["No","Yes"]
    )

    region = st.selectbox(
        "Region",
        [
            "northwest",
            "southeast",
            "southwest"
        ]
    )

if st.button("Predict"):

    sex = 1 if sex=="Female" else 0

    smoker = 1 if smoker=="Yes" else 0

    region_northwest = (
    1 if region=="northwest"
    else 0
    )

    region_southeast = (
        1 if region=="southeast"
        else 0
    )

    region_southwest = (
        1 if region=="southwest"
        else 0
    )

    bmi_category_obese = (
        1 if bmi >= 30
        else 0
    )

    scaled = scaler.transform(
        [[age,bmi,children]]
    )

    age_scaled = scaled[0][0]
    bmi_scaled = scaled[0][1]
    children_scaled = scaled[0][2]

    features = np.array([
        [
            age_scaled,
            sex,
            bmi_scaled,
            children_scaled,
            smoker,
            region_northwest,
            region_southeast,
            region_southwest,
            bmi_category_obese
        ]
    ])

    prediction = model.predict(
        features
    )[0]

    st.success(
        f"Predicted Insurance Cost: ${prediction:,.2f}"
    )