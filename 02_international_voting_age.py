import streamlit as st

# Title of the app
st.title("International Voting Age")

# Dictionary of countries and their voting ages
voting_ages = {
    "United States": 18,
    "Canada": 18,
    "United Kingdom": 18,
    "Germany": 18,
    "Australia": 18,
    "India": 18,
    "Brazil": 16,
    "Japan": 18,
    "South Africa": 18,
    "France": 18,
}

# Display the voting ages
st.write("Voting ages by country:")
for country, age in voting_ages.items():
    st.write(f"{country}: {age} years old")
