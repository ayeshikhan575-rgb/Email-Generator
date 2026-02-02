from email_generator import generate_cold_email
import streamlit as st

st.set_page_config(page_title="Cold Email Generator")

st.title("📧 AI Cold Email Generator")

name = st.text_input("Your Name")
company = st.text_input("Company Name")
purpose = st.text_area("Purpose of Email")

if st.button("Generate Email"):
    if name and company and purpose:
        email = generate_cold_email(name, company, purpose)
        st.success("Email Generated!")
        st.text_area("Your Email", email, height=250)
    else:
        st.warning("Please fill all fields")

