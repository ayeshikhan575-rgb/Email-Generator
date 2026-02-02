from groq import Groq

client = Groq()

def generate_cold_email(name, company, purpose):
    prompt = f"""
Write a professional cold email.

Sender name: {name}
Company: {company}
Purpose: {purpose}
"""

    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content
