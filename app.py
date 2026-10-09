
import json
import os

import time
from google.genai import errors
import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

st.set_page_config(
    page_title="TechStyle AI Support",
    page_icon="🛍️",
    layout="centered"
)

st.title("🛍️ TechStyle AI Support")
st.caption("Ask us about products, shipping, and returns.")

if not API_KEY:
    st.error("GEMINI_API_KEY not found in your .env file.")
    st.stop()

try:
    with open("store_data.json", "r", encoding="utf-8") as file:
        store_data = json.load(file)
except (OSError, json.JSONDecodeError):
    st.error("Could not load store_data.json. Check the file.")
    st.stop()

client = genai.Client(api_key=API_KEY)

instructions = f"""
You are the customer support assistant for
{store_data['store_name']}.

Use only this store information to answer questions:
{json.dumps(store_data, indent=2)}

Rules:
- Be friendly, professional, and concise.
- Never invent product prices or store policies.
- If information is missing, say you cannot confirm it.
- Do not claim to check orders or issue refunds.
- Never request passwords or payment card details.
"""

if "messages" not in st.session_state:
    st.session_state.messages = []

if st.button("Clear conversation"):
    st.session_state.messages = []
    st.rerun()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

question = st.chat_input("Ask a question about our store...")

if question:
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        try:
            with st.spinner("Thinking..."):
                history = st.session_state.messages[-20:]

                prompt = (
                    instructions
                    + "\n\nConversation history:\n"
                    + "\n".join(
                        f"{m['role']}: {m['content']}"
                        for m in history
                    )
                    + "\n\nassistant:"
                )

                response = None

                for attempt in range(3):
                    try:
                        response = client.models.generate_content(
                            model="gemini-3.7-flash",
                            contents=prompt
                        )
                        break

                    except errors.APIError as error:
                        if error.code == 503 and attempt < 2:
                            time.sleep(2 * (attempt + 1))
                        else:
                            raise

                if response is None or not response.text:
                    raise RuntimeError("The AI returned an empty response.")

                answer = response.text

                if not answer:
                    answer = "Sorry, I couldn't generate an answer."

                st.markdown(answer)

            st.session_state.messages.append({
                "role": "assistant",
                "content": answer
            })

        except Exception as error:
            st.error(f"Request failed: {error}")
            st.session_state.messages.pop()