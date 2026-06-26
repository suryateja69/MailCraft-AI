import ollama
import os
from datetime import datetime


# ------------------ Generate Email ------------------ #
def generate_email(prompt):
    print("\nGenerating email. Please wait...\n")

    response = ollama.chat(
        model="qwen3:4b",
        messages=[
            {
                "role": "system",
                "content": "You are MailCraft AI, a professional email writing assistant. Write clear, polite, well-structured emails with a subject line."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]


# ------------------ Save Email ------------------ #
def save_email(email_text, email_type):
    base_path = os.path.dirname(os.path.abspath(__file__))
    folder_path = os.path.join(base_path, "generated_emails")

    os.makedirs(folder_path, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    filename = f"{email_type}_{timestamp}.txt"

    file_path = os.path.join(folder_path, filename)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(email_text)

    print("\nEmail saved successfully!")
    print(f"Location: {file_path}")


# ------------------ View Saved Emails ------------------ #
def view_saved_emails():
    base_path = os.path.dirname(os.path.abspath(__file__))
    folder_path = os.path.join(base_path, "generated_emails")

    if not os.path.exists(folder_path):
        print("\nNo saved emails found.")
        return

    files = sorted(os.listdir(folder_path))

    if len(files) == 0:
        print("\nNo saved emails found.")
        return

    print("\n========== SAVED EMAILS ==========\n")

    for i, file in enumerate(files, start=1):
        print(f"{i}. {file}")

    print()


# ------------------ Main Program ------------------ #

while True:

    print("\n==============================")
    print("      MAILCRAFT AI")
    print("==============================")
    print("1. Leave Request")
    print("2. Job Application")
    print("3. Complaint Email")
    print("4. Meeting Request")
    print("5. Custom Email")
    print("6. View Saved Emails")
    print("7. Exit")

    choice = input("\nChoose an option (1-7): ")

    # ---------------- Leave ---------------- #

    if choice == "1":

        email_type = "leave_request"

        reason = input("Reason: ")
        days = input("Number of Days: ")

        prompt = f"""
Write a professional leave request email.

Reason: {reason}
Days: {days}

Include:
- Subject
- Greeting
- Body
- Closing
"""

    # ---------------- Job ---------------- #

    elif choice == "2":

        email_type = "job_application"

        job = input("Job Role: ")
        company = input("Company: ")
        skills = input("Skills: ")

        prompt = f"""
Write a professional job application email.

Job Role: {job}
Company: {company}
Skills: {skills}

Include:
- Subject
- Greeting
- Body
- Closing
"""

    # ---------------- Complaint ---------------- #

    elif choice == "3":

        email_type = "complaint_email"

        issue = input("Complaint Issue: ")
        company = input("Company Name: ")

        prompt = f"""
Write a professional complaint email.

Issue: {issue}
Company: {company}

Include:
- Subject
- Greeting
- Body
- Closing
"""

    # ---------------- Meeting ---------------- #

    elif choice == "4":

        email_type = "meeting_request"

        purpose = input("Meeting Purpose: ")
        date = input("Preferred Date & Time: ")

        prompt = f"""
Write a professional meeting request email.

Purpose: {purpose}
Preferred Date: {date}

Include:
- Subject
- Greeting
- Body
- Closing
"""

    # ---------------- Custom ---------------- #

    elif choice == "5":

        email_type = "custom_email"

        request = input("Describe your email: ")

        prompt = f"""
Write a professional email.

Request:

{request}

Include:
- Subject
- Greeting
- Body
- Closing
"""

    # ---------------- View Saved Emails ---------------- #

    elif choice == "6":

        view_saved_emails()

        input("\nPress Enter to return to menu...")

        continue

    # ---------------- Exit ---------------- #

    elif choice == "7":

        print("\nThank you for using MailCraft AI.")

        break

    else:

        print("\nInvalid Choice!")

        continue

    # ---------------- Generate ---------------- #

    email = generate_email(prompt)

    print("\n========== GENERATED EMAIL ==========\n")

    print(email)

    save = input("\nSave this email? (Y/N): ")

    if save.lower() == "y":

        save_email(email, email_type)

    again = input("\nGenerate another email? (Y/N): ")

    if again.lower() != "y":

        print("\nThank you for using MailCraft AI.")

        break