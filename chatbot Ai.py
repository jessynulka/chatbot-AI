import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

st.title("🤖 AI Chatbot")

prompt = st.chat_input("Type your message...")

if prompt:
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    st.write(response.text)