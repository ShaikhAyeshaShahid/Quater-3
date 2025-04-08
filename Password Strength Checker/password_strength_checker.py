import streamlit as st
import re
import random
import string
from streamlit.components.v1 import html

# Function to check password strength
def validate_password(password):
    score = 0
    # Checking the length of the password
    if len(password) >= 8:
        score += 1
    # Checking for uppercase letter
    if re.search(r'[A-Z]', password):
        score += 1
    # Checking for lowercase letter
    if re.search(r'[a-z]', password):
        score += 1
    # Checking for number
    if re.search(r'[0-9]', password):
        score += 1
    # Checking for special characters
    if re.search(r'[!@#$%^&*()_+={}\[\]:;,.<>?]', password):
        score += 1

    # Defining the strength level based on score
    if score == 5:
        return "Strong", score / 5
    elif score == 4:
        return "Moderate", score / 5
    else:
        return "Weak", score / 5

# Function to generate a random strong password
def generate_strong_password():
    password_length = 12
    characters = string.ascii_letters + string.digits + string.punctuation
    strong_password = ''.join(random.choice(characters) for i in range(password_length))
    return strong_password

# Streamlit app layout
st.set_page_config(page_title="Password Strength Checker", layout='centered')
st.title("Password Strength Checker")

# User input for password
password = st.text_input("Enter your password:")

# Check password strength
if password:
    password_strength, strength_score = validate_password(password)
    
    # Display password strength
    st.write(f"Password strength: **{password_strength}**")

    # Dynamic progress bar
    st.progress(strength_score)

    # Provide suggestions for improvement if the password is weak
    if password_strength == "Weak":
        st.write("Suggestions to make it stronger:")
        st.write("- Use at least one uppercase letter.")
        st.write("- Use at least one lowercase letter.")
        st.write("- Include at least one number.")
        st.write("- Add at least one special character (e.g., @, #, $, %, etc.).")
        st.write("- Make the password at least 8 characters long.")
    elif password_strength == "Moderate":
        st.write("Your password is moderate, but it can still be stronger!")
    else:
        st.write("Your password is strong! Keep it up.")

    # Generate a strong password when the button is clicked
    if st.button("Generate a Strong Password"):
        strong_password = generate_strong_password()
        st.write(f"Generated strong password: **{strong_password}**")

# Add more features for future iterations if required
st.success("Password strength check completed!")
