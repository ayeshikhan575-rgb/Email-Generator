import os
from langchain_groq import ChatGroq

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name="llama-3.1-8b-instant",   # ✅ WORKING MODEL
    temperature=0.3
)

def generate_cold_email(
    name,
    company,
    job_title,
    skills,
    job_description,
    portfolio_info=""
):
    prompt = f"""
Write a professional cold job application email.

Candidate Name: {name}
Company Name: {company}
Job Title: {job_title}
Skills: {skills}
Job Description: {job_description}
Portfolio/LinkedIn: {portfolio_info}

Tone: polite, confident, professional.
End with a strong call to action.
"""

    response = llm.invoke(prompt)
    return response.content

