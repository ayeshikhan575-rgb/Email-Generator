import os
from langchain_groq import ChatGroq

# Read API key from Streamlit Secrets / Environment
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found in environment variables")

# Initialize Groq LLM
llm = ChatGroq(
    model_name="llama-3.1-8b-instant",
    temperature=0.3
)

def generate_cold_email(name, company, job_title, skills, job_description, portfolio):
    prompt = f"""
Write a short, professional cold email.

Name: {name}
Company: {company}
Job Title: {job_title}
Skills: {skills}
Job Description: {job_description}
Portfolio: {portfolio}
"""
    response = llm.invoke(prompt)
    return response.content

