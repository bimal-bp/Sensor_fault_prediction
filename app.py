import streamlit as st
import pandas as pd
import joblib

# Load the saved models
fault_model = joblib.load('trained_model.pkl')  # Load the fault prediction model
anomaly_pipeline = joblib.load('isolation_forest_pipeline.pkl')  # Load the anomaly detection pipeline

# Streamlit app title
st.title("Equipment Monitoring App")

# Input fields for user
st.header("Enter Equipment Details")
temperature = st.number_input("Temperature", value=58.18)
pressure = st.number_input("Pressure", value=25.03)
vibration = st.number_input("Vibration", value=0.61)
humidity = st.number_input("Humidity", value=45.69)
equipment = st.selectbox("Equipment", ["Turbine", "Compressor", "Pump"])
location = st.selectbox("Location", ["Atlanta", "Chicago", "San Francisco", "New York", "Houston"])

# Create a DataFrame from the input data
input_data = pd.DataFrame({
    'temperature': [temperature],
    'pressure': [pressure],
    'vibration': [vibration],
    'humidity': [humidity],
    'equipment': [equipment],
    'location': [location]
})

# Buttons for prediction and anomaly detection
col1, col2 = st.columns(2)

with col1:
    if st.button("Predict Fault"):
        # Make fault prediction
        fault_prediction = fault_model.predict(input_data)
        
        # Display fault prediction result
        st.subheader("Fault Prediction Result")
        if fault_prediction[0] == 0:
            st.success("The equipment is predicted to be **NON-FAULTY**.")
        else:
            st.error("The equipment is predicted to be **FAULTY**.")

with col2:
    if st.button("Detect Anomaly"):
        # Make anomaly detection
        anomaly_prediction = anomaly_pipeline.predict(input_data)
        
        # Display anomaly detection result
        st.subheader("Anomaly Detection Result")
        if anomaly_prediction[0] == 1:
            st.success("The equipment is predicted to be **NORMAL**.")
        else:
            st.error("The equipment is predicted to be **ANOMALOUS**.")
