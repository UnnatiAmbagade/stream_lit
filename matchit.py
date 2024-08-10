import streamlit as st
import random

# Sample data for classmates
classmates = [
    {'name': 'Alice', 'gender': 'female', 'hobby': 'reading'},
    {'name': 'Bob', 'gender': 'male', 'hobby': 'sports'},
    {'name': 'Charlie', 'gender': 'male', 'hobby': 'gaming'},
    {'name': 'Diana', 'gender': 'female', 'hobby': 'music'},
    # Add more classmates as needed
]

# App title
st.title("Class Cupid")
st.subheader("Where fate meets funny business!")

# App introduction
st.write("Ready to see who your class soulmate is? Don't take it too seriously—just have a laugh!")

# Form to get user input
with st.form(key='user_form'):
    name = st.text_input("Your Name:", "")
    gender = st.selectbox("Gender:", ["male", "female", "other"])
    hobby = st.text_input("Favorite Hobby:")
    
    submit_button = st.form_submit_button(label='Find My Match!')

# Matching logic
if submit_button:
    # Filter potential matches by hobby and opposite gender
    potential_matches = [person for person in classmates if person['hobby'] == hobby and person['gender'] != gender]
    
    # Randomly select a match
    if potential_matches:
        match = random.choice(potential_matches)
    else:
        match = random.choice(classmates)
    
    # Display the match result
    st.subheader("Your Match!")
    st.write(f"You and {match['name']} both love {match['hobby']}! You're destined to be study buddies.")

# Option to restart the app
if st.button("Match Again"):
    st.experimental_rerun()
