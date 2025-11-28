import pandas as pd
import numpy as np
import streamlit as st
import pickle

# Load model and scaler
model = pickle.load(open('model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))
print("XGBoost Model Loaded Successfully")

st.set_page_config(
    page_title="Phishing Website Detection App",
    page_icon="🕵️‍♂️",
    layout="centered"
)

# App Title
st.title("🕵️‍♂️ Phishing Website Detection App")

st.write("""
Welcome!  
Enter the feature values below and the model will predict whether the website is  
**Phishing (0)** or **Legitimate (1)**.
""")

# ---- User Input Function ----
def user_input_features():

    features = [
        'having_IP_Address', 'URL_Length', 'Shortining_Service',
        'having_At_Symbol', 'double_slash_redirecting', 'Prefix_Suffix',
        'having_Sub_Domain', 'SSLfinal_State', 'Domain_registeration_length',
        'Favicon', 'port', 'HTTPS_token', 'Request_URL', 'URL_of_Anchor',
        'Links_in_tags', 'SFH', 'Submitting_to_email', 'Abnormal_URL',
        'Redirect', 'on_mouseover', 'RightClick', 'popUpWidnow',
        'Iframe', 'age_of_domain', 'DNSRecord', 'web_traffic',
        'Page_Rank', 'Google_Index', 'Links_pointing_to_page',
        'Statistical_report'
    ]

    user_data = {}

    st.subheader("🔧 Enter Website Feature Values:")

    for feature in features:
        user_data[feature] = st.selectbox(f"{feature}", options= [0, 1])

    return pd.DataFrame([user_data])

# Get user input
input_df = user_input_features()

# Scale input
input_scaled = scaler.transform(input_df)

# ---- Prediction Button ----
if st.button("🔍 Predict"):
    prediction = model.predict(input_scaled)[0]

    if prediction == 1:
        st.success("✔️ This website is **Legitimate**")
    else:
        st.error("🛑 This website is **Phishing**")

# Footer
st.write("---")
st.write("— Phishing Detection ML Model")

#to run this python -m streamlit run app.py in Terminal.
