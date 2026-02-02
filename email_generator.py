from groq import Groq
import os

# 🔐 API KEY DIRECT (Secrets ki zarurat nahi)
os.environ["GROQ_API_KEY"] = "PASTE_YOUR_GROQ_API_KEY_HERE"

client = Groq()

def generate_cold_email(name, company, purpose):
    prompt = f"""
    Write a professional cold email.

    Name: {name}
    Company: {company}
    Purpose: {purpose}
    """

    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return completion.choices[0].message.content
