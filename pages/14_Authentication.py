import streamlit as st

st.set_page_config(page_title="Authentication", page_icon="🔐")

st.title("🔐 Authentication")
st.write(
    "Streamlit doesn't force any particular login system on you. The two most "
    "common approaches are shown below."
)

st.divider()
st.header("1. A simple session-state login (DIY)")
st.write(
    "For basic apps, you can store a logged_in flag in session state and "
    "check it before showing protected content. This is NOT secure for real "
    "passwords — it's just a pattern for learning."
)
st.code(
    '''if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    with st.form("login"):
        user = st.text_input("Username")
        pw = st.text_input("Password", type="password")
        if st.form_submit_button("Log in"):
            if user == "admin" and pw == "1234":
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Wrong username or password")
else:
    st.success("You are logged in!")'''
)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    with st.form("login"):
        user = st.text_input("Username")
        pw = st.text_input("Password", type="password")
        if st.form_submit_button("Log in"):
            if user == "admin" and pw == "1234":
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("Wrong username or password")
    st.caption("Try username 'admin' and password '1234' for this demo.")
else:
    st.success("You are logged in!")
    if st.button("Log out"):
        st.session_state.logged_in = False
        st.rerun()

st.divider()
st.header("2. st.login() / st.experimental_user (real authentication)")
st.write(
    "Newer Streamlit versions support st.login() to authenticate real users "
    "through an identity provider (like Google), configured in a secrets file."
)
st.code(
    '''if st.button("Log in with provider"):
    st.login()

st.write(st.user)  # access the logged-in user's info'''
)
st.caption("This needs an [auth] section in .streamlit/secrets.toml to actually run — see the Streamlit docs for setup.")

