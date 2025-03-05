import re
import streamlit as st

#page styling
st.set_page_config(page_title="Password Strength Checker", page_icon="✅", layout="centered")

#custom css
st.markdown("""
<style>
     .main {text-align: center;}
     .sttextinput {width: 60% !important; margin: auto; }
     .stButton button {width: 50%; background-color #4CAF50; color:black; font-size: 18px}                     
    .stButton button:hover { background-color: #45a49}
</style>
 """, unsafe_allow_html=True)

#PAGE Title and description
st.title("🔐 Password Strength Generator")
st.write("🔑 Generates Strong, Unique & Secure Password!")

#function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1 #increase score by 1
    else:
        feedback.append("⚠️ Password must be atleast 8 Characters long!")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1 
    else:
        feedback.append("⚠️ Password must contain both Upper & Lower Case!")

    if re.search(r"\d", password):
        score += 1 
    else:
        feedback.append("⚠️ Password must contain atleast one number!")

        #for special characters
    if re.search(r"[!@#$%^&*]", password):
        score += 1 
    else:
        feedback.append("⚠️ Password must contain special characters!")

    #string ko display krengy
    if score == 4:
        st.success(" **Strong Password** Your password is secured✅")
    elif score == 3:
        st.info("❗**Medium Strength Password** !")
    else:
        st.error("❌ **Week Password**- Try again.") 

    #feedback
    if feedback:
        with st.expander(" **Improve Your Password** "):
            for item in feedback:
                st.write(item)

password = st.text_input("Enter your password:", type="password", help="Ensure your password is strong 🔐")


#Button working
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Enter Password First!")

       
        



