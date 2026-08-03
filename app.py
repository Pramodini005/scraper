import streamlit as st
st.title("my first streamlit app")
name=st.text_input("Enter name:")
if st.button("Submit")
    st.write(f"Hello,{name}")
