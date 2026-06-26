# 📧 MailCraft AI

An AI-powered email generator built with **Python**, **Streamlit**, and **Ollama**. MailCraft AI helps users generate professional emails instantly using a locally running Large Language Model (LLM).

---

## 🚀 Features

* Generate professional emails using AI
* Multiple email categories:

  * Leave Request
  * Job Application
  * Complaint Email
  * Meeting Request
  * Custom Email
* Multiple writing tones:

  * Professional
  * Formal
  * Friendly
  * Apology
  * Persuasive
* Save generated emails
* Download emails as `.txt`
* View saved email history
* Streamlit-based user interface
* Runs completely offline using Ollama

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Ollama
* Qwen3:4B
* VS Code

---

## 📂 Project Structure

```text
MailCraft-AI/
│
├── streamlit_app/
│   └── app.py
│
├── terminal/
│   └── email_writer.py
│
├── generated_emails/
├── screenshots/
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone <repository-url>
```

Go into the project:

```bash
cd MailCraft-AI
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Ollama:

https://ollama.com

Download the model:

```bash
ollama pull qwen3:4b
```

Run the application:

```bash
streamlit run streamlit_app/app.py
```

---

## 📸 Screenshots

Add screenshots of the application inside the `screenshots` folder and update this section after uploading them.

---

## 🔮 Future Improvements

* Copy email to clipboard
* Email templates
* Export as PDF
* Cloud deployment
* Multiple LLM support

---

## 👨‍💻 Author

**Bandaru Venkata Surya Teja**

Learning and building AI & LLM applications using Python.
