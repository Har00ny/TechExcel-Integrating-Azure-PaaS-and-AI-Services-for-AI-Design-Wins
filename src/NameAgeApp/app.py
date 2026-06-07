import streamlit as st

st.title("Name and Age Form")

name = st.text_input("What is your name?")
age = st.number_input("What is your age?", min_value=1, max_value=150, step=1, value=None, placeholder="Enter your age")

if st.button("Submit"):
    if not name:
        st.warning("Please enter your name.")
    elif age is None:
        st.warning("Please enter a valid age.")
    else:
        st.success(f"Hello, {name}! You are {int(age)} years old.")
