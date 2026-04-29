import streamlit as st
from openai import OpenAI

# OpenRouter client (same pattern as your reference code)
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=st.secrets["OPENROUTER_API_KEY"],
)

MODEL = "openai/gpt-oss-120b:free"

def classify_text(text: str) -> str:
    """
    Returns one of:
    - "Hate Speech"
    - "Not Hate Speech"
    - "Uncertain"
    (with a short confidence note)
    """
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": (
                    "Classify the following text as Hate Speech, Not Hate Speech, or Uncertain.\n"
                    "Reply in exactly this format:\n"
                    "LABEL: <Hate Speech|Not Hate Speech|Uncertain>\n"
                    "CONFIDENCE: <0.00-1.00>\n\n"
                    f"TEXT: {text}"
                ),
            }
        ],
    )

    content = (response.choices[0].message.content or "").strip()

    # Simple parse (fallback-safe)
    label = "Uncertain"
    confidence = None
    for line in content.splitlines():
        if line.upper().startswith("LABEL:"):
            label = line.split(":", 1)[1].strip()
        if line.upper().startswith("CONFIDENCE:"):
            try:
                confidence = float(line.split(":", 1)[1].strip())
            except:
                confidence = None

    if confidence is None:
        return f"{label} (confidence: n/a)"
    return f"{label} (confidence: {confidence:.2f})"
