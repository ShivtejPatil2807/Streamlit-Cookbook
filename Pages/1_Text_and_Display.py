import streamlit as st

st.set_page_config(
    page_title="Text & Display",
    page_icon="📝"
)

st.title("📝 Text & Display Functions")

# --------------------------------------------------
# 1. st.title()
# --------------------------------------------------

st.header("1. st.title()")
st.write("Displays the main title of your Streamlit application.")

st.code('st.title("My Streamlit App")', language="python")
st.title("My Streamlit App")


# --------------------------------------------------
# 2. st.header()
# --------------------------------------------------

st.divider()

st.header("2. st.header()")
st.write("Displays a large section heading.")

st.code('st.header("Student Information")', language="python")
st.header("Student Information")


# --------------------------------------------------
# 3. st.subheader()
# --------------------------------------------------

st.divider()

st.header("3. st.subheader()")
st.write("Displays a smaller section heading than st.header().")

st.code('st.subheader("Personal Details")', language="python")
st.subheader("Personal Details")


# --------------------------------------------------
# 4. st.write()
# --------------------------------------------------

st.divider()

st.header("4. st.write()")
st.write("Displays text, numbers, data, Python objects, and other content.")

st.code('st.write("Hello, Streamlit!")', language="python")
st.write("Hello, Streamlit!")


# --------------------------------------------------
# 5. st.markdown()
# --------------------------------------------------

st.divider()

st.header("5. st.markdown()")
st.write("Displays text using Markdown formatting.")

st.code('st.markdown("**Hello, Streamlit!**")', language="python")
st.markdown("**Hello, Streamlit!**")


# --------------------------------------------------
# 6. st.caption()
# --------------------------------------------------

st.divider()

st.header("6. st.caption()")
st.write("Displays small, secondary text.")

st.code('st.caption("This is additional information.")', language="python")
st.caption("This is additional information.")


# --------------------------------------------------
# 7. st.text()
# --------------------------------------------------

st.divider()

st.header("7. st.text()")
st.write("Displays plain text without Markdown formatting.")

st.code('st.text("Hello, Streamlit!")', language="python")
st.text("Hello, Streamlit!")


# --------------------------------------------------
# 8. st.code()
# --------------------------------------------------

st.divider()

st.header("8. st.code()")
st.write("Displays source code with code formatting and syntax highlighting.")

st.code(
    'print("Hello, World!")',
    language="python"
)


# --------------------------------------------------
# 9. st.latex()
# --------------------------------------------------

st.divider()

st.header("9. st.latex()")
st.write("Displays mathematical equations and formulas using LaTeX.")

st.code(r'st.latex("x^2 + y^2 = z^2")', language="python")
st.latex(r"x^2 + y^2 = z^2")


# --------------------------------------------------
# 10. st.divider()
# --------------------------------------------------

st.divider()

st.header("10. st.divider()")
st.write("Displays a horizontal line to visually separate sections.")

st.code("st.divider()", language="python")
st.divider()


# --------------------------------------------------
# 11. st.table()
# --------------------------------------------------

st.header("11. st.table()")
st.write("Displays data as a static table.")

st.code(
    '''data = {
    "Name": ["Shivtej", "Tejas"],
    "Marks": [90, 85]
}

st.table(data)''',
    language="python"
)

data = {
    "Name": ["Shivtej", "Tejas"],
    "Marks": [90, 85]
}

st.table(data)


# --------------------------------------------------
# 12. st.expander()
# --------------------------------------------------

st.divider()

st.header("12. st.expander()")
st.write("Creates a collapsible section that users can open or close.")

st.code(
    '''with st.expander("View Explanation"):
    st.write("This content can be expanded.")''',
    language="python"
)

with st.expander("View Explanation"):
    st.write("This content can be expanded.")


# --------------------------------------------------
# 13. st.help()
# --------------------------------------------------

st.divider()

st.header("13. st.help()")
st.write(
    "Displays help and documentation information "
    "about a Python object or Streamlit function."
)

st.code("st.help(st.title)", language="python")

with st.expander("Try st.help(st.title)"):
    st.help(st.title)