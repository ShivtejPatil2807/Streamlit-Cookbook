import streamlit as st
import time

st.set_page_config(page_title="Status & Messages", page_icon="💬")

st.title("💬 Status & Message Functions")
st.write("These functions give the user feedback about what's happening.")

st.divider()
st.header("1. st.success()")
st.write("Shows a green success message.")
st.code('st.success("Task completed successfully!")')
st.success("Task completed successfully!")

st.divider()
st.header("2. st.error()")
st.write("Shows a red error message.")
st.code('st.error("Something went wrong.")')
st.error("Something went wrong.")

st.divider()
st.header("3. st.warning()")
st.write("Shows a yellow warning message.")
st.code('st.warning("This action cannot be undone.")')
st.warning("This action cannot be undone.")

st.divider()
st.header("4. st.info()")
st.write("Shows a blue informational message.")
st.code('st.info("Streamlit auto-reruns on every interaction.")')
st.info("Streamlit auto-reruns on every interaction.")

st.divider()
st.header("5. st.progress()")
st.write("Shows a progress bar for a value between 0 and 100.")
st.code('st.progress(70)')
st.progress(70)

st.divider()
st.header("6. st.spinner()")
st.write("Shows a spinner while a block of code is running.")
st.code(
    '''with st.spinner("Loading..."):
    time.sleep(1)
st.write("Done!")'''
)
if st.button("Run spinner demo"):
    with st.spinner("Loading..."):
        time.sleep(1)
    st.write("Done!")

st.divider()
st.header("7. st.toast()")
st.write("Shows a small temporary notification in the corner of the screen.")
st.code('st.toast("Saved!")')
if st.button("Show toast"):
    st.toast("Saved!")

st.divider()
st.header("8. st.balloons()")
st.write("Celebrates with floating balloons across the screen.")
st.code('st.balloons()')
if st.button("Launch balloons"):
    st.balloons()
