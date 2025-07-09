# 🔥 Forest Fire Risk Prediction App

Welcome to the Forest Fire Risk Predictor — a machine learning-based web app built to help assess forest fire danger using geolocation, satellite temperature data, and seasonal context.
Designed as a submission for the Bharatiya Antariksh Hackathon 2025 organized by ISRO 🚀.

---

## 🌟 Why We Built This

Forest fires have devastating impacts on biodiversity, human settlements, and climate. Unfortunately, fire alerts often come too late — after the fire has already begun.

This app aims to:

* 🧠 Predict fire risk proactively (Low, Medium, High)
* 📍 Accept user inputs like location & time of year
* 🛰️ Leverage real satellite fire data (MODIS)
* 🌐 Provide a user-friendly web interface for public and institutional use

By simulating forest fire risk zones, this tool can aid early awareness, community preparedness, and smarter disaster response.

---

## 🧪 How It Works

1. 🔍 A classification model is trained on MODIS Active Fire Dataset.
2. 📊 Key features:

   * Latitude
   * Longitude
   * Brightness Temperature (Kelvin)
   * Observation Month
3. 🤖 The model learns patterns and predicts the fire risk level (0: Low, 1: Medium, 2: High).
4. 💾 Model saved using joblib and deployed via a lightweight Streamlit app.
5. 🎨 Lottie animations and dark-themed UI added for enhanced experience.

---

## 🛠️ Tech Stack

| Area              | Tools / Libraries Used                   |
| ----------------- | ---------------------------------------- |
| Language          | Python 🐍                                |
| ML Model          | scikit-learn (RandomForestClassifier) 🌲 |
| Data Handling     | pandas 🧺                                |
| Model Persistence | joblib 💾                                |
| Web App           | Streamlit 🌐                             |
| UI Enhancements   | streamlit-lottie 🎞 + custom CSS 🎨      |
| Dataset Source    | MODIS Fire Archive 🔥 (NASA FIRMS)       |

---

## 🖼️ Demo Screenshot

![App Screenshot](./assets/screenshot.png)
*(replace with your own screenshot if available)*

---

## 🎯 What Makes This Unique?

* ✅ Trained on real NASA MODIS data
* 🌍 Accepts any coordinates within India’s lat/long range
* 🌤 Considers seasonal variation (month-wise trends)
* 🚦 Easy to use: no login, no maps, just pure AI prediction
* 💻 Fully local deployment possible — no internet required for prediction
* 🎥 Clean UI with animation and responsive input sections

---

## 🧑‍💻 How to Run It Locally

1. Clone the repo:

```bash
git clone https://github.com/your-username/fire-risk-app.git
cd fire-risk-app
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Launch the app:

```bash
streamlit run app.py
```

---

## 📁 Folder Structure

```
fire-risk-app/
├── app.py                  ← Main Streamlit application
├── fire_risk_model.pkl     ← Trained ML model
├── requirements.txt        ← Python dependencies
├── README.md               ← Project documentation
├── assets/                 ← (Optional) Images, icons, or animations
```

---

## 🧠 Future Improvements

* 🔄 Integrate automatic temperature lookup via open weather APIs
* 🗺️ Add satellite map-based interface for location selection
* ⏰ Enable time-series visualization for trend analysis
* 📱 Make it mobile-responsive

---

## 🧑‍🚀 Built for:

Bharatiya Antariksh Hackathon 2025 (Challenge 1: Forest Fire Spread Simulation) 🚀
Organized by: Indian Space Research Organisation (ISRO)


