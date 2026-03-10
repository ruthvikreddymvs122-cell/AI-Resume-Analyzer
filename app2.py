import streamlit as st
import pdfplumber

# Page settings
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="centered"
)

# Header
st.title("🧠 AI Resume Analyzer")
st.markdown("### Analyze your resume and discover your technical skills")

st.markdown("---")

# Skills database
skills = [
    "python","java","machine learning","data science",
    "sql","html","css","javascript","artificial intelligence"
]

# Upload section
st.subheader("📤 Upload Your Resume")

uploaded_file = st.file_uploader(
    "Upload your Resume in PDF format",
    type=["pdf"]
)

if uploaded_file is not None:

    st.success("✅ Resume uploaded successfully!")

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

    st.markdown("---")

    # Detected skills
    st.subheader("🎯 Detected Skills")

    if found:
        st.write(found)
    else:
        st.warning("No skills detected")

    # Missing skills
    st.subheader("💡 Recommended Skills")

    missing = [skill for skill in skills if skill not in found]

    st.write(missing)

    st.markdown("---")

# Footer
st.markdown(
"""
---
👨‍💻 Developed by **Ruthvik Reddy**  
📊 AI & Machine Learning Student Project
"""
)
