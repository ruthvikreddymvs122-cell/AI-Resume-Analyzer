import streamlit as st
import pdfplumber

st.title("🧠 AI Resume Analyzer")

skills = [
"python","java","machine learning","data science",
"sql","html","css","javascript","artificial intelligence"
]

uploaded_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])

if uploaded_file is not None:

    text = ""

    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                text += page.extract_text()

    text = text.lower()

    st.subheader("Detected Skills")

    found_skills = []

    for skill in skills:
        if skill in text:
            found_skills.append(skill)

    st.write(found_skills)

    st.subheader("Suggested Skills")

    missing_skills = [skill for skill in skills if skill not in found_skills]

    st.write(missing_skills)
