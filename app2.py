import streamlit as st
import pdfplumber

st.title("AI Resume Analyzer")

skills = ["python","java","machine learning","data science","sql","html","css","javascript"]

uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")

if uploaded_file is not None:
    st.write("File uploaded successfully!")

    text = ""

    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text

    text = text.lower()

    found = []

    for skill in skills:
        if skill in text:
            found.append(skill)

    st.subheader("Detected Skills")
    st.write(found)

    st.subheader("Suggested Skills")
    missing = [skill for skill in skills if skill not in found]
    st.write(missing)
