import streamlit as st
import pdfplumber

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="centered"
)

st.title("🧠 AI Resume Analyzer")
st.markdown("### Upload your resume and analyze your skills")

st.markdown("---")

skills = {
    "python":"https://www.w3schools.com/python/",
    "java":"https://www.w3schools.com/java/",
    "machine learning":"https://www.coursera.org/learn/machine-learning",
    "data science":"https://www.coursera.org/specializations/data-science",
    "sql":"https://www.w3schools.com/sql/",
    "html":"https://www.w3schools.com/html/",
    "css":"https://www.w3schools.com/css/",
    "javascript":"https://www.w3schools.com/js/",
    "artificial intelligence":"https://www.coursera.org/learn/ai-for-everyone"
}

uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

if uploaded_file is not None:

    st.success("✅ Resume uploaded successfully!")

    text = ""

    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text

    text_lower = text.lower()

    # Detect Name (first line of resume)
    lines = text.split("\n")
    name = lines[0]

    st.subheader("👤 Candidate Name")
    st.write(name)

    st.markdown("---")

    # Detect Skills
    found = []

    for skill in skills:
        if skill in text_lower:
            found.append(skill)

    st.subheader("🎯 Detected Skills")

    if found:
        for skill in found:
            st.success(skill)
    else:
        st.warning("No skills detected")

    st.markdown("---")

    # Missing Skills
    st.subheader("📚 Skills You Can Learn")

    missing = [skill for skill in skills if skill not in found]

    for skill in missing:
        st.write(f"🔹 {skill}")

    st.markdown("---")

    # Learning Links
    st.subheader("🔗 Learning Resources")

    for skill in missing:
        st.write(f"Learn {skill}: {skills[skill]}")

st.markdown("---")
st.markdown("👨‍💻 Developed by **Ruthvik Reddy**")
