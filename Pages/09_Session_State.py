import streamlit as st

st.set_page_config(page_title="Session State", page_icon="🧠")

st.title("🧠 Session State")
st.write(
    "Normally, Streamlit forgets everything and reruns your script top to bottom "
    "on every interaction. st.session_state is a dictionary that survives "
    "between reruns, so your app can remember things."
)

st.divider()
st.header("1. Creating and reading session state")
st.write("Store a value the first time, then reuse it on every rerun.")
st.code(
    '''if "count" not in st.session_state:
    st.session_state.count = 0

st.write("Count is:", st.session_state.count)'''
)
if "count" not in st.session_state:
    st.session_state.count = 0
st.write("Count is:", st.session_state.count)

st.divider()
st.header("2. Updating session state")
st.write("A button click can update the stored value, and it stays updated after the rerun.")
st.code(
    '''if st.button("Increment"):
    st.session_state.count += 1'''
)
if st.button("Increment"):
    st.session_state.count += 1
st.write("Current count:", st.session_state.count)

st.divider()
st.header("3. Widget keys as session state")
st.write("Every widget with a key= automatically stores its value in st.session_state.")
st.code(
    '''st.text_input("Your name", key="username")
st.write(st.session_state.username)'''
)
st.text_input("Your name", key="username")
st.write("Stored value:", st.session_state.get("username", ""))
