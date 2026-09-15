import streamlit as st

st.set_page_config(page_title="UI & Styling", page_icon="🎨")

st.title("🎨 UI & Styling Functions")
st.write("These functions change how your app looks and feels.")

st.divider()
st.header("1. st.set_page_config()")
st.write("Sets the browser tab title, icon, and page layout. Must be the first Streamlit command in a page.")
st.code('st.set_page_config(page_title="My App", page_icon="🎨", layout="wide")')
st.caption("Already used at the top of this page — that's why the tab shows 🎨 UI & Styling.")

st.divider()
st.header("2. st.color_picker()")
st.write("Lets the user pick a color.")
st.code('st.color_picker("Pick a color", "#1D9E75")')
color = st.color_picker("Pick a color", "#1D9E75")
st.write("You picked:", color)

st.divider()
st.header("3. Custom CSS with st.markdown()")
st.write("You can inject raw CSS using unsafe_allow_html to restyle elements.")
st.code(
    '''st.markdown(
    "<p style='color:#1D9E75; font-weight:bold;'>Styled text</p>",
    unsafe_allow_html=True,
)'''
)
st.markdown(
    "<p style='color:#1D9E75; font-weight:bold;'>Styled text</p>",
    unsafe_allow_html=True,
)

st.divider()
st.header("4. st.image() as a logo/banner")
st.write("Images aren't just for content — they're often used as logos or banners.")
st.code('st.image("https://placehold.co/400x80", use_container_width=True)')
st.image("https://placehold.co/400x80", use_container_width=True)
