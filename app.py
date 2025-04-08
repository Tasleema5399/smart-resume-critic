from resume_parser import load_resume
from llm_helper import get_feedback

resume = load_resume("sample_resume.txt")
job_description = input("Paste job description:\n")

feedback = get_feedback(resume, job_description)
print("\n=== Resume Feedback ===\n")
print(feedback)
