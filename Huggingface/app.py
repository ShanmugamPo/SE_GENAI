import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# ---------------------------------
# Page Configuration
# ---------------------------------
st.set_page_config(
    page_title="Shanmugam's Chatbot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Shanmugam's Chatbot")
st.write("Feel free to ask me anything! Type your question below and press Enter. To exit, type 'exit' or 'quit'.")

# ---------------------------------
# Model Path
# ---------------------------------
MODEL_PATH = "./models/Qwen2.5-0.5B"

# ---------------------------------
# Load Model (only once)
# ---------------------------------
@st.cache_resource
def load_model():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)

    model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH,
        torch_dtype="auto",
        device_map="cpu"   # Use CPU
    )

    return tokenizer, model


with st.spinner("Loading model..."):
    tokenizer, model = load_model()

st.success("✅ Model loaded successfully!")

# ---------------------------------
# Chat History
# ---------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---------------------------------
# User Input
# ---------------------------------
prompt = st.chat_input("Ask me anything...")

if prompt:

    # Show user message
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # Build prompt
    text = tokenizer.apply_chat_template(
        st.session_state.messages,
        tokenize=False,
        add_generation_prompt=True
    )

    inputs = tokenizer(
        text,
        return_tensors="pt"
    )

    # Generate response
    with st.spinner("Thinking..."):
        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens=200,
                temperature=0.7,
                do_sample=True
            )

    response = tokenizer.decode(
        outputs[0][inputs["input_ids"].shape[1]:],
        skip_special_tokens=True
    )

    # Save assistant response
    st.session_state.messages.append(
        {"role": "assistant", "content": response}
    )

    with st.chat_message("assistant"):
        st.markdown(response)

# ---------------------------------
# Sidebar
# ---------------------------------
with st.sidebar:
    st.header("Model Information")
    st.write("**Model:** Qwen2.5-0.5B")
    st.write("**Device:** CPU")

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()