import streamlit as st
import pandas as pd
import pickle
import os

# Correct path to model from deployment folder
model_path = os.path.join(os.path.dirname(__file__), "../models/space_mission_model.pkl")

@st.cache_resource
def load_model():
    if os.path.exists(model_path):
        with open(model_path, "rb") as f:
            model = pickle.load(f)
        return model
    else:
        st.error("❌ Model file not found! Run model.py first to train and save the model.")
        return None

model = load_model()

st.title("🚀 Space Mission Success Predictor")
st.markdown("Predict the likelihood of a space mission being successful.")

# Input fields
company_name = st.text_input("Company Name", "SpaceX")
location = st.text_input("Launch Location", "Cape Canaveral")
rocket_status = st.selectbox("Rocket Status", ["Active", "Retired"])
rocket_type = st.text_input("Rocket Type", "Falcon 9")

# Collect input into dataframe
input_df = pd.DataFrame({
    "company_name": [company_name],
    "location": [location],
    "status_rocket": [rocket_status],
    "rocket": [rocket_type]
})

# Preprocess input
def preprocess_input(df):
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].astype(str)
    return df

input_df = preprocess_input(input_df)

# Predict button
if st.button("Predict Mission Success"):
    if model:
        try:
            prediction = model.predict(input_df)
            if prediction[0] == 1:
                st.success("✅ Prediction: Mission likely to be SUCCESSFUL 🚀")
            else:
                st.warning("❌ Prediction: Mission may FAIL 🛰️")
        except Exception as e:
            st.error(f"Error during prediction: {e}")
