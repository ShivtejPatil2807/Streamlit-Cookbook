import streamlit as st

st.set_page_config(page_title="Text & Markdown", page_icon="✍️")

st.title("✍️ Text & Markdown Functions")
st.write("This page shows the basic functions Streamlit gives you to display text.")

st.divider()
st.header("1. st.title()")
st.write("Shows the biggest heading — usually used once, at the top of the app.")
st.code('st.title("My Streamlit App")')

st.divider()
st.header("2. st.header()")
st.write("Shows a large section heading.")
st.code('st.header("Student Information")')

st.divider()
st.header("3. st.subheader()")
st.write("Shows a heading smaller than st.header() — good for sub-sections.")
st.code('st.subheader("Personal Details")')

st.divider()
st.header("4. st.write()")
st.write("The all-purpose function. Can display text, numbers, lists, and more.")
st.code('st.write("Hello, Streamlit!")')

st.divider()
st.header("5. st.markdown()")
st.write("Displays text with Markdown formatting, like **bold** or *italic*.")
st.code('st.markdown("**Hello, Streamlit!**")')
st.markdown("**Hello, Streamlit!**")

st.divider()
st.header("6. st.caption()")
st.write("Shows small, gray text — good for notes or extra info.")
st.code('st.caption("This is additional information.")')
st.caption("This is additional information.")

st.divider()
st.header("7. st.code()")
st.write("Displays a block of code with syntax highlighting.")
st.code('print("Hello, World!")')

st.divider()
st.header("8. st.divider()")
st.write("Draws a horizontal line to separate sections (used all over this page!).")
st.code("st.divider()")

st.divider()
st.header("9. st.table()")
st.write("Displays data in a simple table.")
st.code(
    '''data = {"Name": ["Shivtej", "Tejas"], "Marks": [70, 90]}
st.table(data)'''
)
data = {"Name": ["Shivtej", "Tejas"], "Marks": [70,90]}
st.table(data)

st.divider()
st.header("10. st.expander()")
st.write("Creates a section that can be opened or closed by the user.")
st.code(
    '''with st.expander("View Explanation"):
    st.write("This content can be expanded.")'''
)
with st.expander("View Explanation"):
    st.write("This content can be expanded.")
