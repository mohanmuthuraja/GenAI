import streamlit as st

st.title("My First Streamlit App")

name = st.text_input("Enter your name:")

btn = st.button("Submit")

if btn:
    if name:
        st.success(f"Hello {name}! Welcome to my Page")
        
    else:
        st.error("Please enter your name")

#run streamlit app: streamlit run streamlit_ckass.py
