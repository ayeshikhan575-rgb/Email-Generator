from dotenv import load_dotenv
import streamlit as st
from email_generator import generate_cold_email

load_dotenv()

st.set_page_config(page_title="AI Cold Email Generator")
st.title("📧 AI-Powered Cold Email Generator")

name = st.text_input("Your Full Name")
company = st.text_input("Company Name")
job_title = st.text_input("Job Title (e.g. Software Engineer)")
skills = st.text_area("Your Skills (comma separated)")
job_description = st.text_area("Paste Job Description")
portfolio_info = st.text_input("Portfolio / LinkedIn (optional)")

if st.button("Generate Email"):
    if name and company and job_title and skills and job_description:
        with st.spinner("Generating email..."):
            email = generate_cold_email(
                name,
                company,
                job_title,
                skills,
                job_description,
                portfolio_info
            )
        st.success("Email Generated Successfully 🎉")
        st.text_area("Your Cold Email", email, height=320)
    else:
        st.warning("⚠️ Please fill all required fields")
