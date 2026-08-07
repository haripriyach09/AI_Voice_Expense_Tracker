import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def extract_expenses(transcript):

    prompt = f"""
Extract all expenses from the transcript.

Return ONLY valid JSON.

Format:

[
  {{
    "Date":"",
    "Category":"",
    "Description":"",
    "Amount":0
  }}
]

Categories:
Food
Groceries
Transport
Shopping
Clothing
Medical
Bills
Education
Entertainment
Electronics
Others

Transcript:
{transcript}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    text = response.choices[0].message.content

    text = text.replace("```json", "")
    text = text.replace("```", "").strip()

    return json.loads(text)