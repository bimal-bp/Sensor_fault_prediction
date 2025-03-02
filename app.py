import streamlit as st
import pandas as pd
import joblib

# Load the saved model
model = joblib.load('trained_model.pkl')

# Streamlit app title
st.title("Equipment Fault Prediction App")

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

# Predict button
if st.button("Predict"):
    # Make prediction
    prediction = model.predict(input_data)
    
    # Display prediction result
    st.subheader("Prediction Result")
    if prediction[0] == 0:
        st.success("The equipment is predicted to be **NON-FAULTY**.")
    else:
        st.error("The equipment is predicted to be **FAULTY**.")
