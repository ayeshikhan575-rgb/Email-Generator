from groq import Groq
import os

# 🔐 API KEY (single line, no enter)
os.environ["GROQ_API_KEY"] = "PASTE_YOUR_NEW_GROQ_API_KEY_HERE"

def generate_cold_email(name, company, purpose):
    client = Groq(api_key=os.environ["GROQ_API_KEY"])

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": f"""
Write a professional cold email.

Sender name: {name}
Company: {company}
Purpose: {purpose}
"""
            }
        ],
        temperature=0.3,
        max_tokens=300
    )

    return response.choices[0].message.content
