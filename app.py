import streamlit as st
from model import classify_text

# Page config
st.set_page_config(page_title="Hate Speech Detector", layout="centered")

# Custom styling (clean + minimal)
st.markdown("""
    <style>
    .main {
        text-align: center;
    }
    textarea {
        border-radius: 10px !important;
        padding: 10px !important;
    }
    button {
        border-radius: 8px !important;
        padding: 10px 20px !important;
        font-weight: 500;
    }
    </style>
""", unsafe_allow_html=True)

# Title (clean, centered)
st.markdown("<h1 style='text-align: center;'>Hate Speech Detector</h1>", unsafe_allow_html=True)

# Subtitle
st.markdown("<p style='text-align: center; color: grey;'>Analyze text for harmful or hateful content</p>", unsafe_allow_html=True)

# Spacer
st.write("")
st.write("")

# Input box
user_input = st.text_area("", placeholder="Type or paste text here...")

# Spacer
st.write("")

# Button centered
col1, col2, col3 = st.columns([1,2,1])
with col2:
    analyze = st.button("Analyze")

# Output
if analyze:
    if user_input.strip():
        result = classify_text(user_input)

        st.write("")  # spacing

        if "Hate Speech" in result:
            st.markdown(f"<div style='text-align:center; color:red; font-size:18px;'>{result}</div>", unsafe_allow_html=True)

        elif "Not Hate" in result:
            st.markdown(f"<div style='text-align:center; color:green; font-size:18px;'>{result}</div>", unsafe_allow_html=True)

        else:
            st.markdown(f"<div style='text-align:center; color:orange; font-size:18px;'>{result}</div>", unsafe_allow_html=True)

    else:
        st.markdown("<p style='text-align:center; color:grey;'>Please enter some text.</p>", unsafe_allow_html=True)
