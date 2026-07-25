import streamlit as st
from ollama import chat

st.title("Shanmugam's Ollama Chat")
st.text("Social Eagle - This is a simple chat interface using the Ollama API")

prompt = st.chat_input("Ask something...")

if prompt:
    st.chat_message("user").write(prompt)

    response = chat(
        model="qwen2.5:0.5b",
        messages=[{"role": "user", "content": prompt}]
    )

    st.chat_message("assistant").write(response["message"]["content"])