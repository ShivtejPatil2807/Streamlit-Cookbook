import streamlit as st

st.set_page_config(page_title="Navigation", page_icon="🔄")

st.title("🔄 Navigation")
st.write("These functions move users between pages in a multipage app.")

st.divider()
st.header("1. st.page_link()")
st.write("Displays a clickable link to another page in your app.")
st.code('st.page_link("Home.py", label="Go to Home", icon="🏠")')
st.page_link("Home.py", label="Go to Home", icon="🏠")

st.divider()
st.header("2. st.switch_page()")
st.write("Jumps the user straight to another page in code (e.g. after a button click).")
st.code(
    '''if st.button("Jump to Home"):
    st.switch_page("Home.py")'''
)
if st.button("Jump to Home"):
    st.switch_page("Home.py")

st.divider()
st.header("3. How multipage apps work")
st.write(
    "Any .py file placed in a folder named pages/, next to your main script, "
    "automatically shows up as its own page in the sidebar — no extra setup needed. "
    "Streamlit orders them by filename, so this repo uses numbered prefixes like "
    "1_Text_and_Markdown.py, 2_Input_Widgets.py, and so on."
)
st.code("your-app/\n├── Home.py\n└── pages/\n    ├── 1_Text_and_Markdown.py\n    └── 2_Input_Widgets.py")
