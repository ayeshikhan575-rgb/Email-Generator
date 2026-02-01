import os
from langchain_groq import ChatGroq

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
     model_name="llama-3.1-8b-instant",  # ✅ UPDATED MODEL
    temperature=0.3
)

def generate_cold_email(
    name,
    company_name,
    job_title,
    skills,
    job_description,
    portfolio_info=""
):
    prompt = f"""
Write a professional cold email for a job application.

Candidate Name: {name}
Company: {company_name}
Job Title: {job_title}
Skills: {skills}
Job Description: {job_description}
Portfolio: {portfolio_info}

The email should be polite, confident, and realistic.
"""

    response = llm.invoke(prompt)
    return response.content
