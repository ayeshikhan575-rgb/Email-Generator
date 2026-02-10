import os
from langchain_groq import ChatGroq

# 🔐 Sirf Streamlit Secrets / Environment se key lo
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# ❗ Cloud app crash na ho, sirf error message aaye
if not GROQ_API_KEY:
    raise RuntimeError("GROQ_API_KEY Streamlit Secrets me set nahi hai")

# 🤖 Groq LLM initialize
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
