import streamlit as st
import pandas as pd

st.set_page_config(page_title="Data Display", page_icon="📊")

st.title("📊 Data Display Functions")
st.write("These functions show data — tables, numbers, and raw structures.")

df = pd.DataFrame({
    "Name": ["Shivtej", "Tejas", "Amit"],
    "Score": [70, 85, 78],
})

st.divider()
st.header("1. st.dataframe()")
st.write("Displays an interactive table — sortable and scrollable.")
st.code('st.dataframe(df)')
st.dataframe(df)

st.divider()
st.header("2. st.table()")
st.write("Displays a static (non-interactive) table.")
st.code('st.table(df)')
st.table(df)

st.divider()
st.header("3. st.metric()")
st.write("Shows a single number, with an optional change indicator.")
st.code('st.metric("Average Score", "84.3", "+2.1")')
st.metric("Average Score", "84.3", "+2.1")

st.divider()
st.header("4. st.json()")
st.write("Displays a dictionary or JSON-like data in a readable, collapsible format.")
st.code('st.json({"name": "Shivtej", "skills": ["Python", "Streamlit"]})')
st.json({"name": "Shivtej", "skills": ["Python", "Streamlit"]})
