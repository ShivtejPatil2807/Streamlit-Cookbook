import streamlit as st

st.set_page_config(page_title="Chat Elements", page_icon="💬")

st.title("💬 Chat Elements")
st.write("These functions are built specifically for chatbot-style interfaces.")

st.divider()
st.header("1. st.chat_message()")
st.write("Displays a chat bubble styled for a given role (user or assistant).")
st.code(
    '''with st.chat_message("user"):
    st.write("Hello!")

with st.chat_message("assistant"):
    st.write("Hi there, how can I help?")'''
)
with st.chat_message("user"):
    st.write("Hello!")
with st.chat_message("assistant"):
    st.write("Hi there, how can I help?")

st.divider()
st.header("2. st.chat_input()")
st.write("A text box fixed to the bottom of the page, made for sending chat messages.")
st.code(
    '''prompt = st.chat_input("Say something")
if prompt:
    st.write(f"You said: {prompt}")'''
)
prompt = st.chat_input("Say something")
if prompt:
    st.write(f"You said: {prompt}")
