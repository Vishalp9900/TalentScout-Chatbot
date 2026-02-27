import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv
import json
from datetime import datetime

# -------------------------
# Load Environment Variables
# -------------------------
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("❌ OPENAI_API_KEY not found. Please check your .env file.")
    st.stop()

client = OpenAI(api_key=api_key)

# -------------------------
# Page Config
# -------------------------
st.set_page_config(page_title="TalentScout Hiring Assistant", page_icon="🤖")
st.title("🤖 TalentScout - AI Hiring Assistant")

# -------------------------
# Session State Initialization
# -------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "candidate_data" not in st.session_state:
    st.session_state.candidate_data = {}

if "step" not in st.session_state:
    st.session_state.step = 0

if "completed" not in st.session_state:
    st.session_state.completed = False

# -------------------------
# Questions & Fields
# -------------------------
questions = [
    "Please enter your Full Name:",
    "Please enter your Email Address:",
    "Please enter your Phone Number:",
    "How many years of experience do you have?",
    "What position(s) are you applying for?",
    "What is your current location?",
    "Please list your Tech Stack (comma separated):"
]

fields = [
    "Full Name",
    "Email",
    "Phone",
    "Experience",
    "Desired Position",
    "Location",
    "Tech Stack"
]

# -------------------------
# Initial Greeting
# -------------------------
if len(st.session_state.messages) == 0:
    greeting = (
        "Hello 👋 Welcome to TalentScout Hiring Assistant.\n\n"
        "I will collect your details and generate technical interview questions.\n\n"
        + questions[0]
    )
    st.session_state.messages.append(
        {"role": "assistant", "content": greeting}
    )

# -------------------------
# Display Chat Messages
# -------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -------------------------
# MAIN LOGIC
# -------------------------

if not st.session_state.completed:

    user_input = st.chat_input("Type your response here...")

    if user_input:

        # Store user response
        st.session_state.messages.append(
            {"role": "user", "content": user_input}
        )

        current_step = st.session_state.step

        # -------------------------
        # Collect Data Step-by-Step
        # -------------------------
        if current_step < len(fields):

            field_name = fields[current_step]
            st.session_state.candidate_data[field_name] = user_input
            st.session_state.step += 1

            # Ask Next Question
            if st.session_state.step < len(questions):
                next_question = questions[st.session_state.step]
                st.session_state.messages.append(
                    {"role": "assistant", "content": next_question}
                )

            # -------------------------
            # Generate Technical Questions
            # -------------------------
            else:
                tech_stack = st.session_state.candidate_data["Tech Stack"]

                prompt = f"""
Generate 3-5 medium-level interview questions for each of the following technologies:

{tech_stack}

Return only numbered questions.
"""

                try:
                    response = client.chat.completions.create(
                        model="gpt-4.1-mini",
                        messages=[{"role": "user", "content": prompt}]
                    )

                    tech_questions = response.choices[0].message.content

                except Exception:
                    # Fallback if API fails
                    tech_questions = f"""
1. Explain the core concepts of {tech_stack}.
2. What are real-world applications of {tech_stack}?
3. What challenges did you face while using {tech_stack}?
4. Describe a project where you used {tech_stack}.
5. What best practices should be followed in {tech_stack}?
"""

                final_message = f"""
## 🎉 Application Submitted Successfully!

### 📌 Technical Interview Questions:

{tech_questions}

---

Our HR team will review your profile and contact you soon.
"""

                st.session_state.messages.append(
                    {"role": "assistant", "content": final_message}
                )

                # -------------------------
                # Save Candidate Data
                # -------------------------
                os.makedirs("data", exist_ok=True)
                filename = "data/candidates.json"

                record = {
                    "timestamp": str(datetime.now()),
                    "candidate_data": st.session_state.candidate_data
                }

                if os.path.exists(filename):
                    try:
                        with open(filename, "r") as f:
                            existing = json.load(f)
                    except:
                        existing = []
                else:
                    existing = []

                existing.append(record)

                with open(filename, "w") as f:
                    json.dump(existing, f, indent=4)

                st.session_state.completed = True

        st.rerun()

# -------------------------
# AFTER COMPLETION SECTION
# -------------------------

else:
    st.success("✅ Your application has been submitted successfully!")

    st.markdown("If you would like to apply again, click below.")

    if st.button("🔄 Start New Application"):
        st.session_state.messages = []
        st.session_state.candidate_data = {}
        st.session_state.step = 0
        st.session_state.completed = False
        st.rerun()