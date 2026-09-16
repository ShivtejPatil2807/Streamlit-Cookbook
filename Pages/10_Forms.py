import streamlit as st

st.set_page_config(page_title="Forms", page_icon="📝")

st.title("📝 Forms")
st.write(
    "A form groups several widgets together so the app only reruns once, "
    "when the Submit button is pressed — not after every single input."
)

st.divider()
st.header("1. st.form() and st.form_submit_button()")
st.write("Wrap widgets in a form, then use a submit button to process them all at once.")
st.code(
    '''with st.form("my_form"):
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0)
    submitted = st.form_submit_button("Submit")

if submitted:
    st.write(f"Hi {name}, you are {age} years old.")'''
)
with st.form("my_form"):
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0)
    submitted = st.form_submit_button("Submit")

if submitted:
    st.write(f"Hi {name}, you are {age} years old.")
