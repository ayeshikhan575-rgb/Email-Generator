import os
from langchain_groq import ChatGroq

# Read Groq API key from environment variables (Streamlit Secrets / .env)
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# If API key is missing, raise an error immediately
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found in environment variables")

# Initialize Groq LLM
# IMPORTANT: ChatGroq requires `groq_api_key`, not `api_key`
llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name="llama-3.1-8b-instant",
    temperature=0.3
)

def generate_cold_email(name, company, job_title, skills, job_description, portfolio):
    """
    Generates a professional cold email using Groq LLM
    """

    prompt = f"""
Write a professional cold email.

Name: {name}
Company: {company}
Job Title: {job_title}
Skills: {skills}
Job Description: {job_description}
Portfolio: {portfolio}

Keep the email short and professional.
"""

    response = llm.invoke(prompt)
    return response.content

