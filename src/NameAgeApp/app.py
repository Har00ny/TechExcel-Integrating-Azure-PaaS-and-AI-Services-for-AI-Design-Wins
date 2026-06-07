import streamlit as st

st.title("Name and Age Form")

name = st.text_input("What is your name?")
age = st.number_input("What is your age?", min_value=0, max_value=150, step=1)

if st.button("Submit"):
    if not name:
        st.warning("Please enter your name.")
    elif age <= 0:
        st.warning("Please enter a valid age.")
    else:
        st.success(f"Hello, {name}! You are {int(age)} years old.")
