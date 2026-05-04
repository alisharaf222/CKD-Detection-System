# 🩺 NephroPredict AI - Chronic Kidney Disease (CKD) Detection

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Random%20Forest-green.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red.svg)
![Data Analysis](https://img.shields.io/badge/Data%20Analysis-Pandas%20%7C%20Seaborn-yellow.svg)

## 📌 Project Overview
**NephroPredict AI** is a Medical Decision Support System designed to predict the likelihood of Chronic Kidney Disease (CKD) in patients. By leveraging Machine Learning algorithms and Exploratory Data Analysis (EDA), this project analyzes key medical indicators to provide accurate, real-time predictions, aiding in early diagnosis and proactive healthcare.

## 🚀 Key Features
- **Data-Driven Insights:** Comprehensive EDA performed to uncover hidden patterns and strong correlations between clinical features (e.g., Hemoglobin levels, Hypertension) and CKD.
- **High-Accuracy Model:** Powered by a tuned `RandomForestClassifier` to prevent overfitting while maintaining high predictive accuracy.
- **Feature Optimization:** Reduced 24 medical features down to the **5 most impactful indicators** for faster and more efficient screening.
- **Interactive Web Interface:** A user-friendly web application built with Streamlit, bridging the gap between complex ML models and end-users (medical professionals).

## 🧬 Medical Indicators Used (Features)
The model requires only 5 key laboratory results to make a prediction:
1. **Specific Gravity (sg)**
2. **Albumin (al)**
3. **Serum Creatinine (sc)**
4. **Hemoglobin (hemo)**
5. **Blood Pressure (bp)**

## 🛠️ Tech Stack
- **Data Processing & Analysis:** `pandas`, `numpy`
- **Data Visualization:** `matplotlib`, `seaborn`
- **Machine Learning:** `scikit-learn`, `joblib`
- **Web App / Deployment:** `streamlit`

## 💻 How to Run the App Locally

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/alisharaf222/NephroPredict-AI.git](https://github.com/alisharaf222/NephroPredict-AI.git)
   cd NephroPredict-AI
