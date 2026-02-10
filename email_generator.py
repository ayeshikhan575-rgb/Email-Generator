import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# env load (local + cloud)
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if GROQ_API_KEY is None:
    raise ValueError("GROQ_API_KEY missing")

llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model_name="llama-3.1-8b-instant",
    temperature=0.3
)

def generate_cold_email(name, company, job_title, skills, job_description, portfolio):
    prompt = f"""
Write a professional cold email.

Name: {name}
Company: {company}
Job Title: {job_title}
Skills: {skills}
Job Description: {job_description}
Portfolio: {portfolio}

Keep it short and professional.
"""
    response = llm.invoke(prompt)
    return response.content
