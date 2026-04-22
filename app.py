import streamlit as st
from pdfminer.high_level import extract_text

# Page Configuration
st.set_page_config(page_title="AI Resume Analyser", layout="wide")

st.title("🚀 AI Resume Analyser")
st.subheader("Automated Skills Extraction & Matcher")

# File Uploader
uploaded_file = st.file_uploader("Upload your Resume (PDF format)", type="pdf")

if uploaded_file is not None:
    # 1. Extract Text from PDF
    with st.spinner('Scanning resume content...'):
        text = extract_text(uploaded_file)
        text_lower = text.lower() 

    st.success("Resume Successfully Uploaded!")

    # 2. Skill Keywords to Match
    keywords = ["Python", "Java", "Docker", "AWS", "SQL", "Machine Learning", "DevOps", "React", "Kubernetes", "Git"]
    found_skills = []

    for skill in keywords:
        if skill.lower() in text_lower:
            found_skills.append(skill)

    # 3. Layout: Two Columns for Analysis
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("Extracted Skills")
        if found_skills:
            for s in found_skills:
                st.write(f"✔️ {s}")
        else:
            st.warning("No matching technical skills identified.")

    with col2:
        st.header("Analysis Report")
        # Simple Scoring Logic: 10% per skill, max 100%
        score = len(found_skills) * 10 
        st.metric(label="ATS Compatibility Score", value=f"{min(score, 100)}%")
        
        if "Python" in found_skills or "DevOps" in found_skills:
            st.balloons()
            st.info("Key Skills Detected: Your profile matches the target role requirements.")

    # 4. Preview Section
    with st.expander("View Extracted Raw Text"):
        st.text(text)
