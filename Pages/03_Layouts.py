import streamlit as st

st.set_page_config(page_title="Layouts", page_icon="📐")

st.title("📐 Layout Functions")
st.write("Layout functions control where things appear on the page.")

st.divider()
st.header("1. st.columns()")
st.write("Splits the page into side-by-side sections.")
st.code(
    '''col1, col2 = st.columns(2)
col1.write("Left column")
col2.write("Right column")'''
)
col1, col2 = st.columns(2)
col1.write("Left column")
col2.write("Right column")

st.divider()
st.header("2. st.tabs()")
st.write("Creates clickable tabs to organize content.")
st.code(
    '''tab1, tab2 = st.tabs(["Tab A", "Tab B"])
with tab1:
    st.write("Content for Tab A")
with tab2:
    st.write("Content for Tab B")'''
)
tab1, tab2 = st.tabs(["Tab A", "Tab B"])
with tab1:
    st.write("Content for Tab A")
with tab2:
    st.write("Content for Tab B")

st.divider()
st.header("3. st.container()")
st.write("Groups elements together so you can add to them later in the code.")
st.code(
    '''box = st.container(border=True)
box.write("I'm inside a container")'''
)
box = st.container(border=True)
box.write("I'm inside a container")

st.divider()
st.header("4. st.sidebar")
st.write("Puts a widget or text in the sidebar instead of the main page.")
st.code('st.sidebar.write("This appears in the sidebar")')
st.sidebar.write("👋 This came from the Layouts page")

st.divider()
st.header("5. st.empty()")
st.write("Reserves a spot on the page that you can update or replace later.")
st.code(
    '''placeholder = st.empty()
placeholder.write("Original text")
placeholder.write("Replaced text")'''
)
placeholder = st.empty()
placeholder.write("Original text")
placeholder.write("Replaced text")
