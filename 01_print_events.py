import streamlit as st

# Title of the app
st.title("Event Logger")

# Input for event
event = st.text_input("Enter an event:")

# Button to log the event
if st.button("Log Event"):
    if event:
        st.write(f"Event logged: {event}")
    else:
        st.write("Please enter an event.")
