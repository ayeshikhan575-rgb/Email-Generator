import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# env load (local + streamlit cloud)
load_dotenv()

# 🔥 yahan key read hoti hai
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY environment me nahi mil rahi")

# Groq LLM initialize
llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model_name="llama-3.1-8b-instant",
    temperature=0.3
)

def generate_cold_email(name, company, job_title, skills, job_description, portfolio):
    prompt = f"""
Professional cold email likho.

Naam: {name}
Company: {company}
Job Title: {job_title}
Skills: {skills}
Job Description: {job_description}
Portfolio: {portfolio}

Email short aur professional honi chahiye.
"""
    response = llm.invoke(prompt)
    return response.content
