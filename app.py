import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker" ,page_icon="🔐")

st.title("🔐 Password Strength Checker ")

st.markdown( ''' ## Welcome to the Password Strength chacker 🛠
use this simple tool for chack your passwrod strength  '''  )

password = st.text_input("Enter Your Password", type="password")

feedback = []

score = 0

if password:
    if len(password) >= 8:
        score +=1
    else :
        feedback.append("❌ Password should be at 8 characters long.")

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌Passwrod should contain both upper and lower case characters.")

    if re.search(r'\d',password):
        score += 1
    else :
        feedback.append("❌Password should contain at lesst one digit.")

    if re.search(r'[@#$%*&]',password ):
        score += 1
    else :
        feedback.append("❌Password should be contain at lesst one spacial character ( @#$%*& ) .")

    if score == 4:
        feedback.append("✅ Your Password is Strong! 💪")
    
    elif score == 3:
        feedback.append("🌓 Your Password is medium strength, it could be stronger!.")
    else:
        feedback.append("❎  Your Password is weak please make it stronger!")

    if feedback:
        st.markdown("## Suggestions")
        for tip in feedback:
            st.write(tip)
else:
    st.info("Please enter your password to get started")