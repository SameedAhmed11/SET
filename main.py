import pandas as pd
from openai import OpenAI
import time
import streamlit as st

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=st.secrets["openai_api_key"],
)

def analyze_feedback(feedback_text):
    completion = client.chat.completions.create(
        model="deepseek/deepseek-r1:free",
        messages=[
            {"role": "system", "content": "Classify the following feedback as 'Positive', 'Negative', or 'Neutral'. Only return one word: 'Positive', 'Negative', or 'Neutral'.  Respond with only one word per feedback in the same order. If the feedback contains mixed sentiments, classify it according to the dominant sentiment."},
            {"role": "user", "content": feedback_text},
        ]
    )
    return completion.choices[0].message.content.strip()


st.markdown("# Input text to Test Model :robot_face:")
feedback = st.text_input("",placeholder="Enter text here...")

st.write("Sentiment: ",analyze_feedback(feedback))


