import streamlit as st

st.set_page_config(page_title="Profile", page_icon="📊")

if "name" not in st.session_state:
    st.session_state.name=""

if "project" not in st.session_state:
    st.session_state.project=""    


menu = st.sidebar.selectbox("Menu", ["Home Page", "About Me", "My Projects"])

if menu == "Home Page":
    st.title("Main Page")
    
    text = st.text_input("Enter your name",value = st.session_state.name)
    pro = st.text_input("Enter your Project name ",value= st.session_state.project)

    if st.button("Submit"):
        st.session_state.name = text
        st.session_state.project = pro
        if text.strip() != "":
            st.success(f"Succsessfully registered!")
        else:
            st.error("Something went wrong.")

elif menu == "About Me":
    st.title("My Details")
    st.write("My Name is ",st.session_state.name)

elif menu == "My Projects":
    st.title("Projects")
    st.write("My Project name is ",st.session_state.project)

