# Smart Resume Critic 🤖📄
Your AI-powered career coach! Drop in your resume and a job description, and get instant, actionable feedback tailored to your dream role.

## ✨ Features
- Analyze your resume against any job description
- Highlights missing skills, clarity improvements, and keyword optimizations
- Powered by OpenAI GPT (or adaptable to local LLMs)

## 🛠️ Setup Instructions

### ✅ 1. Clone the Repository
git clone https://github.com/YOUR-USERNAME/smart-resume-critic.git cd smart-resume-critic

shell
Copy
Edit

### ✅ 2. Install Python Packages
Make sure you have Python 3.8+ installed.
pip install -r requirements.txt

cpp
Copy
Edit

If you prefer using a virtual environment:
python -m venv venv venv\Scripts\activate # On Windows source venv/bin/activate # On Linux/macOS pip install -r requirements.txt

markdown
Copy
Edit

### ✅ 3. Add Your OpenAI API Key

#### Option A: Use a `.env` file (Recommended)
1. Create a new file named `.env` in the root directory of the project.
2. Paste your OpenAI key inside like this:
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

pgsql
Copy
Edit
Get your key here: https://platform.openai.com/account/api-keys

#### Option B: Temporary (PowerShell only)
$env:OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

css
Copy
Edit
⚠️ This only lasts for one session. You’ll have to run it again if you restart the terminal.

### ✅ 4. Provide a Resume File
Place your resume in a plain `.txt` file named:
sample_resume.txt

mathematica
Copy
Edit
You can use or modify the included sample.

### ✅ 5. Run the Application
In the project directory, run:
python app.py

css
Copy
Edit
You’ll be prompted to paste a job description like:
We are looking for a Full-Stack Developer with 3+ years of experience in React and Node.js. Familiarity with AWS or Azure is a plus.

vbnet
Copy
Edit
After pressing Enter, the program will:
- Load your resume
- Send it to GPT along with the job description
- Return feedback customized for that job

## 📁 Project Structure
smart-resume-critic/ ├── app.py # Main execution script ├── llm_helper.py # Handles LLM requests ├── resume_parser.py # Reads resume text ├── sample_resume.txt # Sample resume (editable) ├── requirements.txt # Python dependencies ├── .env # Store your OpenAI key here ├── .gitignore # Keeps secrets, cache files out of Git └── README.md # You're reading this!

shell
Copy
Edit

## 🧠 Troubleshooting

### 🔸 `ModuleNotFoundError: No module named 'dotenv'`
Install the missing package:
pip install python-dotenv

markdown
Copy
Edit

### 🔸 `openai.RateLimitError: Error code: 429`
- You've used up your free quota or token limit.
- Check usage: https://platform.openai.com/account/usage
- Fix: Wait for reset, switch accounts, or add billing info.

## ✅ Next Ideas
- Add PDF support using `PyMuPDF` or `pdfminer`
- Make a beautiful frontend using Streamlit or Flask
- Replace OpenAI with a local model using LLaMA, GPT4All, or Mistral

## 📜 License
MIT License — free to use, fork, and improve.