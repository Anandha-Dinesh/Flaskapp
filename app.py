import streamlit as st
# import openai
import os

# SET YOUR OPENAI API KEY
# openai.api_key = os.getenv("OPENAI_API_KEY")  # or replace with a string if testing locally

st.set_page_config(page_title="Feelink AI Friend", page_icon="💬")
st.title("🧸 Feelink – Your Friendly Chat Companion")

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat input
user_input = st.chat_input("Say something...")

# Display chat history
for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# On new message
if user_input:
    # Show user message
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Call AI
    with st.chat_message("assistant"):
        with st.spinner("Typing..."):
            # response = openai.ChatCompletion.create(
            #     model="gpt-3.5-turbo",  # or "gpt-4" if you have access
            #     messages=[
            #         {"role": "system", "content": "You're a kind, understanding friend who helps kids express their feelings in a safe and supportive way."},
            #         *st.session_state.chat_history
            #     ],
            #     temperature=0.7
            # )
            # ai_reply = response.choices[0].message["content"]
            st.markdown("thankyou")

    # Save AI response
    st.session_state.chat_history.append({"role": "assistant", "content": "thankyou"})
