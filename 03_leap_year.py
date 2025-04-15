import streamlit as st

# Title of the app
st.title("Leap Year Checker")

# Input for the year
year = st.number_input("Enter a year:", min_value=1)

# Function to check if a year is a leap year
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

# Button to check the leap year
if st.button("Check Leap Year"):
    if is_leap_year(year):
        st.write(f"{year} is a leap year.")
    else:
        st.write(f"{year} is not a leap year.")
