import streamlit as st
from model import classify_text

st.set_page_config(page_title="AI Content Analyzer", layout="centered")

# --- Custom CSS (Apple / ChatGPT style) ---
st.markdown("""
<style>
body {
    background-color: #f7f7f8;
}

.main {
    display: flex;
    justify-content: center;
}

.block-container {
    max-width: 700px;
    padding-top: 3rem;
}

.card {
    background-color: white;
    padding: 25px;
    border-radius: 16px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.05);
}

.title {
    font-size: 28px;
    font-weight: 600;
    text-align: center;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #6b7280;
    font-size: 14px;
    margin-bottom: 20px;
}

textarea {
    border-radius: 12px !important;
    border: 1px solid #e5e7eb !important;
    padding: 12px !important;
}

button {
    width: 100%;
    border-radius: 12px !important;
    background-color: black !important;
    color: white !important;
    font-weight: 500;
    padding: 10px;
}

.result {
    margin-top: 20px;
    padding: 15px;
    border-radius: 12px;
    text-align: center;
    font-size: 16px;
}

.safe {
    background-color: #ecfdf5;
    color: #065f46;
}

.hate {
    background-color: #fef2f2;
    color: #7f1d1d;
}

.uncertain {
    background-color: #fff7ed;
    color: #92400e;
}
</style>
""", unsafe_allow_html=True)

# --- UI Layout ---
st.markdown("<div class='title'>AI Content Analyzer</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Analyze text for harmful or hateful content</div>", unsafe_allow_html=True)

st.markdown("<div class='card'>", unsafe_allow_html=True)

user_input = st.text_area("", placeholder="Type something...")

analyze = st.button("Analyze")

if analyze:
    if user_input.strip():
        with st.spinner("Analyzing..."):
            result = classify_text(user_input)

        if "Hate Speech" in result:
            st.markdown(f"<div class='result hate'>{result}</div>", unsafe_allow_html=True)

        elif "Not Hate" in result:
            st.markdown(f"<div class='result safe'>{result}</div>", unsafe_allow_html=True)

        else:
            st.markdown(f"<div class='result uncertain'>{result}</div>", unsafe_allow_html=True)

    else:
        st.markdown("<div class='result uncertain'>Please enter some text.</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
