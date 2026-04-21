import streamlit as st
from pdfminer.high_level import extract_text

st.title("AI Resume Analyser")
st.write("Upload a PDF to see magic!")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    text = extract_text(uploaded_file)
    st.header("Extracted Text:")
    st.text(text[:500]) # Pehle 500 characters dikhayega
