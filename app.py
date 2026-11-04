import streamlit as st
from model import train_model

st.set_page_config(
    page_title="SWYNEX Profile Detector",
    page_icon="🔍"
)

model, features = train_model()

st.title("🔍 AI-Based LinkedIn Profile Detection")

st.write(
    "An educational AI application that identifies "
    "potentially suspicious profile patterns."
)

st.subheader("Enter Profile Information")

age = st.number_input(
    "Account Age (Months)", 0, 300, 12
)

connections = st.number_input(
    "Number of Connections", 0, 10000, 100
)

completeness = st.slider(
    "Profile Completeness (%)", 0, 100, 50
)

skills = st.number_input(
    "Number of Skills", 0, 100, 5
)

experience = st.number_input(
    "Work Experience (Years)", 0, 50, 1
)

about_words = st.number_input(
    "About Section Word Count", 0, 1000, 50
)

if st.button("Analyze Profile"):

    profile = [[
        age,
        connections,
        completeness,
        skills,
        experience,
        about_words
    ]]

    prediction = model.predict(profile)[0]

    st.subheader("Analysis Result")

    if prediction == "Genuine":
        st.success("Prediction: Genuine-looking profile")
    else:
        st.warning("Prediction: Suspicious-looking profile")

    st.write("### Risk Indicators")

    if age < 6:
        st.write("- Very new account")

    if connections < 50:
        st.write("- Low connection count")

    if completeness < 40:
        st.write("- Low profile completeness")

    if skills < 3:
        st.write("- Very few listed skills")

    if experience == 0:
        st.write("- No listed work experience")

    st.info(
        "This is an educational prototype using synthetic "
        "training data. Predictions are not proof of fraud."
    )