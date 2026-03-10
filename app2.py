import streamlit as st
import pdfplumber

skills = [
"python","java","machine learning","data science",
"sql","html","css","javascript","artificial intelligence"
]

st.title("AI Resume Analyzer")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")

if uploaded_file:
    text=""

    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            if page.extract_text():
                text+=page.extract_text()

    text=text.lower()

    st.subheader("Detected Skills")

    found=[]
    for skill in skills:
        if skill in text:
            found.append(skill)

    st.write(found)

    st.subheader("Suggested Skills")

    missing=[skill for skill in skills if skill not in found]
    st.write(missing)