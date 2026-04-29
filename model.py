from transformers import pipeline
from config import MODEL_NAME, THRESHOLD

import streamlit as st
from transformers import pipeline
from config import MODEL_NAME, THRESHOLD

@st.cache_resource
def load_model():
    return pipeline("text-classification", model=MODEL_NAME)

classifier = load_model()

def classify_text(text):
    result = classifier(text)[0]
    
    label = result['label']
    score = result['score']
    
    if score < THRESHOLD:
        return f"Uncertain (confidence: {score:.2f})"
    
    if label == "HATE":
        return f"Hate Speech (confidence: {score:.2f})"
    else:
        return f"Not Hate Speech (confidence: {score:.2f})"
