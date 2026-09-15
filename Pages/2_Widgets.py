import streamlit as st

st.set_page_config(
    page_title="Widgets",
    page_icon="🎛️"
)

st.title("🎛️ Streamlit Widgets")

# --------------------------------------------------
# 1. st.button()
# --------------------------------------------------

st.header("1. st.button()")
st.write("Creates a button that users can click to perform an action.")

st.code('st.button("Click Me")', language = "python")
if st.button("Click Me"):
    st.success("Button clicked! 🎉")

# --------------------------------------------------
# 2. st.checkbox()
# --------------------------------------------------

st.divider()

st.header("2. st.checkbox()")
st.write("Creates a box that users can tick or untick.")

st.code('st.checkbox("IF YOU AGREE")', language = "python")
st.checkbox("IF YOU AGREE")

# --------------------------------------------------
# 3. st.radio()
# --------------------------------------------------

st.divider()

st.header("3. st.radio()")
st.write("Lets the user choose one option from several options.")

st.code('st.radio("Which language is best for programming ?",["HTML","JAVA","PYTHON","C++"])', language = "python")
lan = st.radio("Which language is best for programming ?",["HTML","JAVA","PYTHON","C++"])
st.write(f"You Selected : {lan}")

# --------------------------------------------------
# 4. st.selectbox()
# --------------------------------------------------

st.divider()

st.header("4. st.selectbox()")
st.write("Creates a dropdown menu where the user chooses one option.")

st.code('st.selectbox("how would you like to be contacted ?",["Email","Home Phone","Mobile Phone","Twitter"])', language = "python")
sel = st.selectbox("how would you like to be contacted ?",["Email","Home Phone","Mobile Phone","Twitter"])
st.write(f"You Selected : {sel}")

# --------------------------------------------------
# 5. st.multiselect()
# --------------------------------------------------

st.divider()

st.header("5. st.multiselect()")
st.write("Lets the user choose multiple options from a list.")

st.code('st.multiselect("Who is the creator of Python ?",["Guido Van Rossum","Dennis Ritchie","Bjarne Stroustrup","James Gosling"])', language = "python")
st.multiselect("Who is the creator of Python ?",["Guido Van Rossum","Dennis Ritchie","Bjarne Stroustrup","James Gosling"])

# --------------------------------------------------
# 6. st.select_slider()
# --------------------------------------------------

st.divider()

st.header("6. st.select_slider()")
st.write("Lets the user select one option by sliding through choices.")

st.code('st.select_slider("Increase Volume 50%",[10, 20, 30, 40, 50, 60, 70, 80, 90, 100])',language = "python")
st.select_slider("Increase Volume 50%",[10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# --------------------------------------------------
# 7. st.text_input()
# --------------------------------------------------

st.divider()

st.header("7. st.text_input()")
st.write("Creates a box where the user can type a short piece of text.")

st.code('st.text_input("Enter Your Name :")', language = "python")
st.text_input("Enter Your Name :")

# --------------------------------------------------
# 8. st.text_area()
# --------------------------------------------------

st.divider()

st.header("8. st.text_area()")
st.write("Creates a larger box where the user can type longer text.")

st.code('st.text_area(label ="Enter your text below:", placeholder ="Type something amazing...")', language = "python")
st.text_area(label ="Enter your text below:", placeholder ="Type something amazing...")

# --------------------------------------------------
# 9. st.number_input()
# --------------------------------------------------

st.divider()

st.header("9. st.number_input()")
st.write("Creates an input box where the user can enter a number.")

st.code('st.number_input("Enter any number")', language = "python")
st.number_input(" Enter any number")

# --------------------------------------------------
# 10. st.slider()
# --------------------------------------------------

st.divider()

st.header("10. st.slider()")
st.write("Lets the user choose a number by moving a slider.")

st.code('st.slider(label="Select your age", min_value=0, max_value=100, value=25, step=1)', language = "python")
age = st.slider(
    label="Select your age",
    min_value=0,
    max_value=100,
    value=25, 
    step=1    
)
st.write(f"You are {age} years old.")

# --------------------------------------------------
# 11. st.date_input()
# --------------------------------------------------

st.divider()

st.header("11. st.date_input()")
st.write("Lets the user select a date from a calendar.")

st.code('st.date_input("Calendar")', language = "python")
st.date_input("Calendar")

# --------------------------------------------------
# 12 .st.time_input()
# --------------------------------------------------

st.divider()

st.header("12 .st.time_input()")
st.write("Lets the user select a time.")

st.code('st.time_input("Clock:")', language = "python")
st.time_input("Clock:")

# --------------------------------------------------
# 13. st.file_uploader()
# --------------------------------------------------

st.divider()

st.header("13. st.file_uploader()")
st.write("Lets the user upload a file to the Streamlit app.")

st.code('st.file_uploader("Upload your document file:")', language = "python")
st.file_uploader("Upload your document file:")

# --------------------------------------------------
# 14. st.camera_input()
# --------------------------------------------------

st.divider()

st.header("14. st.camera_input()")
st.write("Lets the user take/upload a photo using their camera.")

st.code('st.camera_input("Camera:")', language = "python")
st.camera_input("Camera:")

# --------------------------------------------------
# 15. st.color_picker()
# --------------------------------------------------

st.divider()

st.header("15. st.color_picker()")
st.write("Lets the user choose a color.")

st.code('st.color_picker("Pick any color")', language = "python")
st.color_picker("Pick any color")

# --------------------------------------------------
# 16. st.download_button()
# --------------------------------------------------

st.divider()

st.header("16. st.download_button()")
st.write("Creates a button that lets the user download something.")

data = """
Hello Everyone✋!

This is a file created using Streamlit.
You can download this file to your computer.
"""

st.code('st.download_button(label = "Download file", data = data, file_name = "filename.txt", mime = "text/plain")', language = "python")
st.download_button(
    label="Download file",
     data= data,
    file_name="filename.txt",
    mime="text/plain"
)

# --------------------------------------------------
# 17. st.link_button()
# --------------------------------------------------

st.divider()

st.header("17. st.link_button()")
st.write("Creates a button that takes the user to another webpage/link.")


st.code('st.link_button("Go to Streamlit", "https://streamlit.io")', language = "python")
st.link_button("Go to Streamlit", "https://streamlit.io")
