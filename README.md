🤖 TalentScout – AI Hiring Assistant Chatbot
AI-powered Hiring Assistant built using Python + Streamlit + OpenAI LLM for automated candidate screening.

📌 Project Overview
TalentScout is an intelligent chatbot designed for a fictional recruitment agency specializing in technology placements.
The chatbot:
⦁	Collects essential candidate information
⦁	Understands declared tech stack
⦁	Generates tailored technical interview questions
⦁	Maintains structured, professional conversation flow
⦁	Ensures hiring-focused interaction
This project demonstrates practical use of Large Language Models (LLMs) for recruitment automation.

🎯 Features
✅ 1. Professional Greeting
⦁	Welcomes candidate
⦁	Explains hiring process
⦁	Initiates structured interaction
✅ 2. Structured Information Collection
⦁	Collects the following details one by one:
⦁	Full Name
⦁	Email Address
⦁	Phone Number
⦁	Years of Experience
⦁	Desired Position
⦁	Current Location
⦁	Tech Stack
✔ One question at a time
✔ No skipping fields
✔ Stored in session state

✅ 3. Tech Stack-Based Question Generation
⦁	After collecting tech stack:
⦁	Generates 3–5 medium-level questions
⦁	For each technology listed
⦁	Interview-style format
⦁	No explanations included
Example:
If tech stack =
Python, Django, MySQL
The chatbot generates grouped technical questions for each.
✅ 4. Context-Aware Conversation
⦁	Uses st.session_state
⦁	Maintains conversation history
⦁	Prevents repetition
⦁	Ensures smooth flow
✅ 5. Fallback Handling
⦁	If user asks unrelated questions:
⦁	"I am here to assist with the hiring process only."
⦁	This prevents topic deviation.
✅ 6. Graceful Exit
⦁	Keywords supported:
⦁	exit
⦁	quit
⦁	bye
Bot responds professionally and ends session.

🏗️ System Architecture
User (Streamlit UI)
        ↓
Session State (Memory)
        ↓
Prompt Template
        ↓
OpenAI LLM
        ↓
Response Displayed
🛠️ Tech Stack
⦁	Python 3.11
⦁	Streamlit
⦁	OpenAI API
⦁	python-dotenv
⦁	JSON (Simulated storage)

📂 Project Structure
TalentScout-Chatbot/
│
├── app.py
├── requirements.txt
├── .env
├── README.md
└── data/
    └── candidates.json

⚙️ Installation Guide
1️ Clone Repository
	git clone <your-repo-link>
	cd TalentScout-Chatbot
2️ Create Virtual Environment (Recommended)
py -3.11 -m venv .venv
.venv\Scripts\activate
3️ Install Dependencies
pip install -r requirements.txt
4️ Add OpenAI API Key
Create .env file:
	OPENAI_API_KEY=your_api_key_here
5️ Run Application
streamlit run app.py

🧠 Prompt Engineering Strategy
1️ Role-Based System Prompt
⦁	Defines:
⦁	Chatbot identity
⦁	Hiring assistant role
⦁	Professional tone
⦁	Restricted domain behavior
2️ Controlled Question Generation Prompt
⦁	Explicit instructions:
⦁	3–5 questions per technology
⦁	Medium difficulty
⦁	No explanations
⦁	Grouped output format
⦁	Ensures structured and relevant responses.
3️ Domain Restriction
⦁	Prevents:
⦁	Irrelevant discussions
⦁	Casual conversation
⦁	Topic deviation
