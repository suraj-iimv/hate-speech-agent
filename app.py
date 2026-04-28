import streamlit as st
from model import classify_text

st.title("Hate Speech Detection Agent")

user_input = st.text_area("Enter text:")

if st.button("Analyze"):
    if user_input:
        result = classify_text(user_input)
        st.write(result)
    else:
        st.write("Please enter some text.")