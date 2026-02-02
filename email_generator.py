from groq import Groq
import os

# 🔐 API KEY (single line, no enter)
os.environ["GROQ_API_KEY"] = "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"

def generate_cold_email(name, company, purpose):
    client = Groq(api_key=os.environ["GROQ_API_KEY"])

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": f"""
Write a professional cold email.

prompt = f"""
Sender name: {name}
Company: {company}
Purpose: {purpose}
"""

"""
            }
        ],
        temperature=0.3,
        max_tokens=300
    )

    return response.choices[0].message.content


