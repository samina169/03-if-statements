import streamlit as st

# Title of the app
st.title("Height Requirement Checker for Roller Coaster")

# Input for height in centimeters
height = st.number_input("Enter your height (in cm):", min_value=0)

# Minimum height requirement for the ride
min_height = 120  # Example minimum height in cm

# Button to check if tall enough
if st.button("Check Height"):
    if height >= min_height:
        st.write("You are tall enough to ride!")
    else:
        st.write("Sorry, you are not tall enough to ride.")
