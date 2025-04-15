import streamlit as st
import random

# Title of the app
st.title("Random Number Generator")

# Input for the range of random numbers
min_value = st.number_input("Enter the minimum value:", value=0)
max_value = st.number_input("Enter the maximum value:", value=100)

# Button to generate random number
if st.button("Generate Random Number"):
    if min_value < max_value:
        random_number = random.randint(min_value, max_value)
        st.write(f"Random number between {min_value} and {max_value}: {random_number}")
    else:
        st.write("Please ensure that the minimum value is less than the maximum value.")
