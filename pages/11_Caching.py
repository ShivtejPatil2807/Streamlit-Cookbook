import streamlit as st
import time

st.set_page_config(page_title="Caching", page_icon="⚡")

st.title("⚡ Caching")
st.write(
    "Streamlit reruns your whole script on every interaction. Caching stops it "
    "from redoing slow work (like loading a big file) when nothing changed."
)

st.divider()
st.header("1. st.cache_data()")
st.write("Caches the return value of a function that returns data (numbers, dataframes, etc).")
st.code(
    '''@st.cache_data
def slow_calculation(n):
    time.sleep(2)
    return n * n

result = slow_calculation(5)'''
)


@st.cache_data
def slow_calculation(n):
    time.sleep(2)
    return n * n


if st.button("Run slow calculation"):
    start = time.time()
    result = slow_calculation(5)
    st.write("Result:", result)
    st.write(f"Took {time.time() - start:.2f} seconds — try clicking again!")

st.divider()
st.header("2. st.cache_resource()")
st.write("Caches objects that shouldn't be recreated each time, like a database connection or ML model.")
st.code(
    '''@st.cache_resource
def load_model():
    # e.g. load a large ML model once
    return "pretend_model_object"

model = load_model()'''
)
st.caption("Use this instead of st.cache_data for things like models, connections, or clients.")
