import streamlit as st
import joblib
import numpy as np

# إعداد شكل الصفحة
st.set_page_config(page_title="CKD Prediction App", page_icon="🩺", layout="centered")

# تحميل الموديل
model = joblib.load('kidney_model.pkl')

# عنوان البرنامج
st.title("🩺 Chronic Kidney Disease (CKD) Predictor")
st.write("Please enter the patient's test results below:")

# إنشاء خانات الإدخال (للـ 5 تحاليل اللي اخترناهم)
col1, col2 = st.columns(2)

with col1:
    sg = st.number_input("Specific Gravity (sg) - e.g., 1.010", min_value=1.000, max_value=1.030, format="%.3f")
    al = st.number_input("Albumin (al) - e.g., 0, 1, 2, 3, 4", min_value=0.0, max_value=5.0, step=1.0)
    sc = st.number_input("Serum Creatinine (sc) - e.g., 1.2", min_value=0.0, max_value=50.0, format="%.1f")

with col2:
    hemo = st.number_input("Hemoglobin (hemo) - e.g., 15.0", min_value=0.0, max_value=20.0, format="%.1f")
    bp = st.number_input("Blood Pressure (bp) - e.g., 80", min_value=0.0, max_value=200.0, step=1.0)

# زر التوقع
if st.button("Predict 💡"):
    # تجميع المدخلات في مصفوفة
    input_data = np.array([[sg, al, sc, hemo, bp]])
    
    # التوقع
    prediction = model.predict(input_data)
    
    # عرض النتيجة
    st.divider()
    if prediction[0] == 1:
        st.error("⚠️ **High Risk of Chronic Kidney Disease (CKD).** Please consult a nephrologist immediately.")
    else:
        st.success("✅ **Low Risk of CKD.** The patient's kidney functions appear normal.")