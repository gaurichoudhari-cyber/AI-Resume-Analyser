import streamlit as st
from pdfminer.high_level import extract_text

st.set_page_config(page_title="AI Resume Analyser", layout="wide")

st.title("🚀 AI Resume Analyser")
st.subheader("Automated Skills Extraction & Matcher")

uploaded_file = st.file_uploader("Apna Resume (PDF) yahan upload karein", type="pdf")

if uploaded_file is not None:
    # 1. Text Extract karein
    with st.spinner('Resume scan ho raha hai...'):
        text = extract_text(uploaded_file)
        text_lower = text.lower() # Sab kuch small letters mein taaki match ho sake

    st.success("✅ Resume Successfully Uploaded!")

    # 2. Skills ki list jo humein check karni hai
    keywords = ["Python", "Java", "Docker", "AWS", "SQL", "Machine Learning", "DevOps", "React"]
    found_skills = []

    for skill in keywords:
        if skill.lower() in text_lower:
            found_skills.append(skill)

    
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("Extracted Skills")
        if found_skills:
            for s in found_skills:
                st.write(f"- {s}")
        else:
            st.warning("Koi specific technical skills nahi mili.")

    with col2:
        st.header("Analysis Result")
        score = len(found_skills) * 12.5 
        st.metric(label="Resume Match Score", value=f"{min(score, 100)}%")
        
        if "Python" in found_skills:
            st.balloons() 
            st.success("Target Skill Found: Aapne Python seekhi hai, Great!")

    # Full text preview (niche)
    with st.expander("Resume ka poora text dekhne ke liye click karein"):
        st.text(text)
