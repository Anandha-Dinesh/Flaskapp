import streamlit as st
# import openai
import os
from emotionalAnalysis import generate
from agent import Ai_Pipeline

# SET YOUR OPENAI API KEY
# openai.api_key = os.getenv("OPENAI_API_KEY")  # or replace with a string if testing locally

st.set_page_config(page_title="Feelink AI Friend", page_icon="💬")
st.title("🧸 Feelink – Your Friendly Chat Companion")
gender=''
age=0
name=''
# Initialize session state for user info and chat history
if "user_info" not in st.session_state:
    st.session_state.user_info = {"name": "", "age": None, "gender": ""}
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Collect user info
if not st.session_state.user_info["name"] or not st.session_state.user_info["age"] or not st.session_state.user_info["gender"]:
    st.subheader("Tell us about yourself")
    col1, col2, col3 = st.columns(3)
    with col1:
        name = st.text_input("Name", value=st.session_state.user_info["name"])
    with col2:
        age = st.number_input("Age", min_value=1, max_value=120, value=st.session_state.user_info["age"] or 10)
    with col3:
        gender = st.selectbox("Gender", ["", "Male", "Female", "Other"], index=0 if not st.session_state.user_info["gender"] else ["", "Male", "Female", "Other"].index(st.session_state.user_info["gender"]))

    if name and age and gender:
        st.session_state.user_info = {"name": name, "age": age, "gender": gender}
        st.success("Thank you! You can now start chatting.")
    else:
        st.info("Please fill in all fields to start chatting.")
        st.stop()
else:
    st.write(f"**Name:** {st.session_state.user_info['name']} | **Age:** {st.session_state.user_info['age']} | **Gender:** {st.session_state.user_info['gender']}")

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
    user_info = st.session_state.user_info
    st.session_state.chat_history.append({"role": "assistant", "content": Ai_Pipeline(name=user_info["name"] ,gender=user_info["gender"], age=user_info["age"], input=user_input)})
