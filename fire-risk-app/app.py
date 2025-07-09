import streamlit as st
import joblib
import json
from streamlit_lottie import st_lottie

# Load the trained model
model = joblib.load("fire_risk_model.pkl")

# Load Lottie animation from local file
def load_lottie_file(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

fire_animation = load_lottie_file("fire.json")

# Streamlit page configuration
st.set_page_config(page_title="Forest Fire Risk Predictor", page_icon="🔥", layout="centered")

# Custom dark background with nice styles
st.markdown("""
<style>
/* Global background */
.stApp {
    background-color: #000000;
    color: #FFFFFF;
}

/* Headings and text */
h1, h2, h3, h4, h5, h6, p, label {
    color: #FFFFFF !important;
    font-family: 'Segoe UI', sans-serif;
}

/* Inputs */
input, .stNumberInput input, .stSelectbox div div {
    background-color: #1a1a1a !important;
    color: #FFFFFF !important;
    border-radius: 8px !important;
    border: 1px solid #444444 !important;
}

/* Sliders */
.stSlider > div > div {
    background-color: #1a1a1a !important;
}

/* Buttons */
.stButton > button {
    background-color: #FF4500 !important;
    color: white !important;
    border-radius: 10px !important;
    font-weight: bold;
    padding: 10px 20px;
    border: none;
}
.stButton > button:hover {
    background-color: #FF6347 !important;
    transform: scale(1.02);
    transition: 0.3s ease;
}

/* Divider */
hr {
    border-color: #333333;
}
</style>
""", unsafe_allow_html=True)

# 🔥 Title and animation
if fire_animation:
    st_lottie(fire_animation, height=180, key="fire")
st.markdown("<h1 style='text-align: center;'>🔥 Forest Fire Risk Predictor</h1>", unsafe_allow_html=True)

st.markdown("""
Welcome to the <b>Forest Fire Risk Predictor</b> powered by <b>AI & MODIS satellite data</b>!  
Enter geolocation and brightness to predict the fire risk level in your region.
""", unsafe_allow_html=True)

st.divider()

# 📍 Input Section
st.header("📍 Input Parameters")

col1, col2 = st.columns(2)
with col1:
    lat = st.number_input("🌐 Latitude (India: 8.0°N to 37.5°N)", min_value=0.0, max_value=50.0, step=0.01, format="%.4f")
    brightness = st.slider("🔥 Brightness Temperature (Kelvin)", 290.0, 450.0, 320.0, step=1.0)

with col2:
    lon = st.number_input("🧭 Longitude (India: 68.0°E to 98.0°E)", min_value=60.0, max_value=110.0, step=0.01, format="%.4f")
    month = st.selectbox("📅 Observation Month", options=[1,2,3,4,5,6,7,8,9,10,11,12], index=4)
    st.write("Your selected month:", month)



# Warning for values out of range
if lat < 8.0 or lat > 37.5 or lon < 68.0 or lon > 98.0:
    st.warning("⚠️ Coordinates are outside India’s extent. Predictions may be inaccurate.")

st.divider()

# 🔍 Prediction
st.header("🔍 Predict Fire Risk")

if st.button("🚨 Predict Now"):
    input_data = [[lat, lon, brightness, month]]
    prediction = model.predict(input_data)[0]

    risk_labels = {0: "Low", 1: "Medium", 2: "High"}
    risk = risk_labels.get(prediction, "Unknown")

    st.markdown("### 📢 Prediction Result")

    if risk == "High":
        st.error("🔥 Very High Risk! Take fire prevention measures immediately.")
    elif risk == "Medium":
        st.warning("🌤 Moderate fire risk. Stay alert and informed.")
    else:
        st.success("✅ Low fire risk. No immediate danger.")

    st.markdown(f"### 🧭 Predicted Risk Level: **:orange[{risk}]**")

# Footer
st.divider()
st.markdown("<center>Made with ❤️ by Team FireWatchers</center>", unsafe_allow_html=True)





