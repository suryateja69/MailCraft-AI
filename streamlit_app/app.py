import os
from datetime import datetime

import ollama
import streamlit as st


st.set_page_config(
    page_title="MailCraft AI",
    page_icon="📧",
    layout="wide"
)


def get_generated_emails_folder():
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    folder_path = os.path.join(base_path, "generated_emails")
    os.makedirs(folder_path, exist_ok=True)
    return folder_path


def generate_email(prompt):
    response = ollama.chat(
        model="qwen3:4b",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are MailCraft AI, a professional email writing assistant. "
                    "Write clear, polite, useful, well-structured emails with a subject line."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]


def save_email(email_text, email_type):
    folder_path = get_generated_emails_folder()
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{email_type}_{timestamp}.txt"
    file_path = os.path.join(folder_path, filename)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(email_text)

    return file_path


def view_saved_emails():
    folder_path = get_generated_emails_folder()
    files = sorted(os.listdir(folder_path), reverse=True)
    return files


def build_prompt(email_type, tone, data):
    if email_type == "Leave Request":
        email_key = "leave_request"
        prompt = f"""
Write a {tone.lower()} leave request email.

Reason: {data["reason"]}
Number of Days: {data["days"]}

Include:
- Subject
- Greeting
- Body
- Closing
"""

    elif email_type == "Job Application":
        email_key = "job_application"
        prompt = f"""
Write a {tone.lower()} job application email.

Job Role: {data["job_role"]}
Company: {data["company"]}
Skills: {data["skills"]}

Include:
- Subject
- Greeting
- Body
- Closing
"""

    elif email_type == "Complaint Email":
        email_key = "complaint_email"
        prompt = f"""
Write a {tone.lower()} complaint email.

Complaint Issue: {data["issue"]}
Company/Service Name: {data["company"]}

Include:
- Subject
- Greeting
- Body
- Closing
"""

    elif email_type == "Meeting Request":
        email_key = "meeting_request"
        prompt = f"""
Write a {tone.lower()} meeting request email.

Meeting Purpose: {data["purpose"]}
Preferred Date and Time: {data["date_time"]}

Include:
- Subject
- Greeting
- Body
- Closing
"""

    else:
        email_key = "custom_email"
        prompt = f"""
Write a {tone.lower()} professional email based on this request:

{data["custom_request"]}

Include:
- Subject
- Greeting
- Body
- Closing
"""

    return prompt, email_key


st.title("📧 MailCraft AI")
st.markdown("### Generate professional emails using a local LLM with Ollama")

st.sidebar.title("MailCraft AI")
st.sidebar.write("Local AI Email Generator")
st.sidebar.markdown("---")

email_type = st.selectbox(
    "Select Email Type",
    [
        "Leave Request",
        "Job Application",
        "Complaint Email",
        "Meeting Request",
        "Custom Email"
    ]
)

tone = st.selectbox(
    "Select Email Tone",
    [
        "Professional",
        "Formal",
        "Friendly",
        "Apology",
        "Persuasive"
    ]
)

st.markdown("---")

data = {}

if email_type == "Leave Request":
    data["reason"] = st.text_input("Reason for Leave", placeholder="Example: Fever")
    data["days"] = st.number_input("Number of Days", min_value=1, step=1)

elif email_type == "Job Application":
    data["job_role"] = st.text_input("Job Role", placeholder="Example: Data Analyst Intern")
    data["company"] = st.text_input("Company Name", placeholder="Example: Google")
    data["skills"] = st.text_area(
        "Skills",
        placeholder="Example: Python, SQL, Pandas, Power BI, Machine Learning"
    )

elif email_type == "Complaint Email":
    data["issue"] = st.text_input("Complaint Issue", placeholder="Example: Product not delivered")
    data["company"] = st.text_input("Company/Service Name", placeholder="Example: Amazon")

elif email_type == "Meeting Request":
    data["purpose"] = st.text_input("Meeting Purpose", placeholder="Example: Project discussion")
    data["date_time"] = st.text_input("Preferred Date and Time", placeholder="Example: Monday at 4 PM")

else:
    data["custom_request"] = st.text_area(
        "Describe the email you want",
        placeholder="Example: Write an email requesting internship opportunity"
    )

st.markdown("---")

if "generated_email" not in st.session_state:
    st.session_state.generated_email = ""

if "email_key" not in st.session_state:
    st.session_state.email_key = ""

col1, col2 = st.columns(2)

with col1:
    generate_button = st.button("🚀 Generate Email", use_container_width=True)

with col2:
    clear_button = st.button("🧹 Clear Output", use_container_width=True)

if clear_button:
    st.session_state.generated_email = ""
    st.session_state.email_key = ""

if generate_button:
    prompt, email_key = build_prompt(email_type, tone, data)

    with st.spinner("Generating email with Qwen3:4B..."):
        email = generate_email(prompt)

    st.session_state.generated_email = email
    st.session_state.email_key = email_key

if st.session_state.generated_email:
    st.success("Email generated successfully!")

    st.markdown("## 📄 Generated Email")

    st.text_area(
        "Output",
        st.session_state.generated_email,
        height=350
    )

    st.download_button(
        label="📥 Download Email",
        data=st.session_state.generated_email,
        file_name=f"{st.session_state.email_key}.txt",
        mime="text/plain",
        use_container_width=True
    )

    if st.button("💾 Save Email to History", use_container_width=True):
        saved_path = save_email(
            st.session_state.generated_email,
            st.session_state.email_key
        )
        st.success(f"Email saved successfully: {saved_path}")

st.markdown("---")

with st.expander("📂 View Saved Email History"):
    saved_files = view_saved_emails()

    if not saved_files:
        st.info("No saved emails found yet.")
    else:
        for file_name in saved_files:
            st.write(file_name)