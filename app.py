import numpy as np
import pickle
import pandas as pd
import streamlit as st
from PIL import Image
import base64

# Load the pickled model
pickle_in = open("Health.pkl", "rb")
Health = pickle.load(pickle_in)

def predict_health_condition(age, billing_amount, gender, blood_type, medication, insurance_provider, medical_condition, admission_type):
    """
    Function to predict the health condition.
    """
    # Process input data
    input_data = pd.DataFrame({
        'Age': [age],
        'Billing Amount': [billing_amount],
        'Gender': [gender],
        'Blood Type': [blood_type],
        'Medication': [medication],
        'Insurance Provider': [insurance_provider],
        'Medical Condition': [medical_condition],
        'Admission Type': [admission_type]
    })
    
    # Make prediction
    prediction = Health.predict(input_data)[0]
    
    return prediction

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

def main():
    # Get base64 image
    img_base64 = get_base64_image('bg.jpg')
    
    # Add CSS to style the background image
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{img_base64}");
            background-size: cover;
        }}
        .main .block-container {{
            backdrop-filter: blur(10px);
            background: rgba(255, 255, 255, 0.7);
            border-radius: 10px;
            padding: 20px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.markdown(
        """
        <div style="background-color: tomato; padding: 15px">
        <h2 style="color: white; text-align: center;">Health Prediction App</h2>
        </div>
        <br>
        <h5>Fill out the form below to predict patient health condition</h5>
        """,
        unsafe_allow_html=True
    )
    
    # Input fields
    age = st.slider("Age", 1, 100, 50)
    billing_amount = st.slider("Billing Amount", 1, 100000, 50000)
    gender = st.selectbox("Gender", ["Female", "Male"])
    blood_type = st.selectbox("Blood Type", ["A+", "A-", "AB+", "AB-", "B+", "B-", "O+", "O-"])
    medication = st.selectbox("Medication", ["Ibuprofen", "Lipitor", "Aspirin", "Paracetamol", "Penicillin"])
    insurance_provider = st.selectbox("Insurance Provider", ["Aetna", "Blue Cross", "Cigna", "Medicare", "UnitedHealthcare"])
    medical_condition = st.selectbox("Medical Condition", ["Arthritis", "Asthma", "Cancer", "Diabetes", "Hypertension", "Obesity"])
    admission_type = st.selectbox("Admission Type", ["Elective", "Emergency", "Urgent"])
    
    # Make prediction
    if st.button("Make Prediction"):
        prediction = predict_health_condition(age, billing_amount, gender, blood_type, medication, insurance_provider, medical_condition, admission_type)
        st.success(f"Predicted Health Condition: {prediction}")

if __name__ == "__main__":
    main()
