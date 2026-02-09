import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

# .env aur Streamlit Secrets se variables load karta hai
load_dotenv()

# Groq ki API key environment se uthata hai
GROQ_API_KEY = os.getenv("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")

# Agar key na mile to error throw kare


# Groq ka LLM initialize kar rahe hain
llm = ChatGroq(
    api_key=GROQ_API_KEY,     # yahan Groq ki key pass hoti hai
    model_name="llama-3.1-8b-instant",
    temperature=0.3
)

# Cold email generate karne ka function
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



