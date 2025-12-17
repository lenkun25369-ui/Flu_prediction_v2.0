import streamlit as st
from predict_core import predict_flu_probability

st.title("Flu Prediction Model by XGBoost Algorithm")

# -------- Numeric inputs --------
temp = st.number_input("Temperature (°C)", 30.0, 42.0, 37.3, step=1.0)
height = st.number_input("Height (CM)", 1.0, 400.0, 160.0, step=0.5)
weight = st.number_input("Weight (KG)", 1.0, 400.0, 60.0, step=0.5)
DOI = st.number_input("Days of illness", 1, 14, 1)
WOS = st.number_input("Week of year", 1, 53, 1)
season = st.number_input("Season (1–4)", 1, 4, 1)
rr = st.number_input("Respiratory rate", 10, 30, 12)
sbp = st.number_input("Systolic BP", 50, 250, 90)
o2s = st.number_input("Oxygen saturation (%)", 1, 100, 100)
pulse = st.number_input("Pulse", 50, 180, 100)

# -------- Binary inputs --------
def yn(label):
    return st.selectbox(label, ["No", "Yes"])

fluvaccine = yn("Influenza vaccine this year?")
cough = yn("New or increased cough?")
coughsputum = yn("Cough with sputum?")
sorethroat = yn("Sore throat?")
rhinorrhea = yn("Rhinorrhea / nasal congestion?")
sinuspain = yn("Sinus pain?")
exposehuman = yn("Exposure to confirmed influenza?")
travel = yn("Recent travel?")
medhistav = yn("Influenza antivirals in past 30 days?")
pastmedchronlundis = yn("Chronic lung disease?")

# -------- Prediction --------
if st.button("Predict"):
    prob = predict_flu_probability(
        temp, height, weight, DOI, WOS, season,
        rr, sbp, o2s, pulse,
        fluvaccine, cough, coughsputum, sorethroat,
        rhinorrhea, sinuspain, exposehuman, travel,
        medhistav, pastmedchronlundis
    )

    st.metric("Predicted probability (%)", f"{prob:.2f}")
