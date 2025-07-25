import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.title("Ball Mill Parameter Prediction")
st.write("Enter material input values to predict mill parameters")

# Load trained model
model = joblib.load("ball_mill_model.pkl")

# Input fields
st.subheader("Input Variables")

rh = st.number_input("RH", value=0.0)
oxide = st.number_input("Oxide ", value=0.0)
crushed_odisha = st.number_input("Crushed Odisha", value=0.0)
nmdc = st.number_input("NMDC", value=0.0)
odisha = st.number_input("Odisha", value=0.0)
vale_brbf = st.number_input("VALE BRBF", value=0.0)
vale_iocj = st.number_input("Vale IOCJ", value=0.0)
mel = st.number_input("MEL", value=0.0)

# Create DataFrame for model input
input_data = pd.DataFrame([[
    rh, oxide , crushed_odisha, nmdc, odisha, vale_brbf, vale_iocj, mel
]], columns=[
    "RH", "Oxide ", "Crushed odisha", "NMDC", "Odisha",
    "VALE BRBF", "Vale IOCJ", "MEL"
])

# Predict
if st.button("Predict Ball Mill Parameters"):
    prediction = model.predict(input_data)[0]
    st.success("Prediction Complete!")
    st.write(f"**Feed (TPH)**: {prediction[0]:.2f}")
    st.write(f"**Feed Water**: {prediction[1]:.2f}")
    st.write(f"**Cyclone Pressure**: {prediction[2]:.2f}")
