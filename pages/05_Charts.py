import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Charts", page_icon="📈")

st.title("📈 Chart Functions")
st.write("Streamlit has built-in chart functions that need no extra setup.")

chart_data = pd.DataFrame(
    np.random.randn(20, 3), columns=["A", "B", "C"]
)

st.divider()
st.header("1. st.line_chart()")
st.write("Draws a line chart from a table of numbers.")
st.code("st.line_chart(chart_data)")
st.line_chart(chart_data)

st.divider()
st.header("2. st.bar_chart()")
st.write("Draws a bar chart from a table of numbers.")
st.code("st.bar_chart(chart_data)")
st.bar_chart(chart_data)

st.divider()
st.header("3. st.area_chart()")
st.write("Draws a filled area chart from a table of numbers.")
st.code("st.area_chart(chart_data)")
st.area_chart(chart_data)

st.divider()
st.header("4. st.scatter_chart()")
st.write("Draws a scatter plot from a table of numbers.")
st.code("st.scatter_chart(chart_data)")
st.scatter_chart(chart_data)

st.divider()
st.header("5. st.map()")
st.write("Plots points on a map, given latitude and longitude columns.")
st.code(
    '''map_data = pd.DataFrame({
    "lat": [16.7050, 18.5204],
    "lon": [74.2433, 73.8567],
})
st.map(map_data)'''
)
map_data = pd.DataFrame({
    "lat": [16.7050, 18.5204],
    "lon": [74.2433, 73.8567],
})
st.map(map_data)
