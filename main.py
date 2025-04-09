import pandas as pd
from openai import OpenAI
import time
import streamlit as st

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=st.secrets["openai_api_key"],
)

def analyze_feedback_C(feedback_text):
    completion = client.chat.completions.create(
        model="deepseek/deepseek-r1:free",
        messages=[
            {"role": "system", "content":"""Classify the following feedback as 'Positive', 'Negative', or 'Neutral'. Only return one word: 'Positive', 'Negative', or 'Neutral'. These comments are in response to the question: "Please provide supplementary comments for the course" — therefore, prioritize feedback related to the course content and structure over delivery or teaching style. If the feedback contains mixed sentiments, classify it according to the dominant sentiment about the course itself."""},
            {"role": "user", "content": feedback_text},
        ]
    )
    return completion.choices[0].message.content.strip()

def analyze_feedback_I(feedback_text):
    completion = client.chat.completions.create(
        model="deepseek/deepseek-r1:free",
        messages=[
            {"role": "system", "content": """Classify the following feedback as 'Positive', 'Negative', or 'Neutral'. Only return one word: 'Positive', 'Negative', or 'Neutral'. For context, These comments are in response to the question: "Please provide supplementary comments for the instructor on the overall quality of the instruction in this course". Respond with only one word. If the feedback contains mixed sentiments, classify it according to the dominant sentiment."""},
            {"role": "user", "content": feedback_text},
        ]
    )
    return completion.choices[0].message.content.strip()

st.subheader("Input text to Test Model (Course) :robot_face:")
feedback_C = st.text_area("",placeholder="Enter text here...",key="C")

st.markdown(f"Sentiment: **{analyze_feedback_C(feedback_C)}**")

st.subheader("Input text to Test Model (Instructor) :robot_face:")
feedback_I = st.text_area("",placeholder="Enter text here...",key="I")

st.markdown(f"Sentiment: **{analyze_feedback_I(feedback_I)}**")





