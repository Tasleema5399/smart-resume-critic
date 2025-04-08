from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()  # Load from .env file
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))



def get_feedback(resume_text, job_description):
    prompt = f"""
    Resume:\n{resume_text}\n\n
    Job Description:\n{job_description}\n\n
    Provide professional feedback on the resume with:
    - What’s missing for this job
    - Suggested improvements
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()
