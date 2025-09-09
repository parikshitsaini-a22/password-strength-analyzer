import streamlit as st
from .analyzer import analyze_password
from .wordlist import generate_wordlist

st.set_page_config(page_title="Password Analyzer", page_icon="🔑", layout="centered")

st.markdown("<h1 style='color:red;'>Password Strength Analyzer</h1>", unsafe_allow_html=True)

password = st.text_input("Enter Password", type="password")
if password:
    score, feedback = analyze_password(password)
    st.write(f"**Score:** {score}/4")
    st.write(f"**Feedback:** {feedback}")

st.markdown("### Custom Wordlist Generator")
name = st.text_input("Name")
pet = st.text_input("Pet Name")
years = st.text_input("Year Range (e.g., 1990-2000)")

if st.button("Generate Wordlist"):
    wordlist = generate_wordlist(name, pet, years)
    st.download_button("Download Wordlist", "\n".join(wordlist), "wordlist.txt")
