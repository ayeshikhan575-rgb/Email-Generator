import streamlit as st
from email_generator import generate_cold_email

st.set_page_config(page_title="AI Cold Email Generator")

st.title("📧 AI-Powered Cold Email Generator")

name = st.text_input("Your Full Name")
company_name = st.text_input("Company Name")
job_title = st.text_input("Job Title")
skills = st.text_input("Your Skills (comma separated)")
job_description = st.text_area("Paste the Job Description")
portfolio_info = st.text_input("Portfolio / LinkedIn (optional)")

if st.button("Generate Email"):
    if name and company_name and job_title and skills and job_description:
        email = generate_cold_email(
            name=name,
            company_name=company_name,
            job_title=job_title,
            skills=skills,
            job_description=job_description,
            portfolio_info=portfolio_info
        )
        st.subheader("Generated Email")
        st.write(email)
    else:
        st.error("Please fill all required fields.")
