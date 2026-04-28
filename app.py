import streamlit as st
from model import classify_text

st.set_page_config(page_title="Hate Speech Detector", layout="centered")

st.title("🛡️ Hate Speech Detection Agent")

st.write("Enter text below to analyze whether it contains hate speech.")

user_input = st.text_area("Enter text:")

if st.button("Analyze"):
    if user_input:
        result = classify_text(user_input)
        
        if "Hate Speech" in result:
            st.error(result)   # red box
        elif "Not Hate" in result:
            st.success(result)  # green box
        else:
            st.warning(result)  # yellow box
            
    else:
        st.info("Please enter some text.")
