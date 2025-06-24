# 📧 Cold Mail Generator

Generate personalized cold emails for tech service companies using **Groq**, **LangChain**, and **Streamlit**. This tool extracts job listings from a company's careers page and uses your portfolio data to generate relevant, persuasive outreach emails.

---

## 💡 Use Case

Imagine you're a **business development executive** at a software agency. Instead of waiting for job posts to close, you proactively reach out to companies that are hiring — offering your agency’s skilled developers as a faster alternative to internal hiring.

This tool automates that cold email process:

* Extracts job descriptions from a public job URL
* Matches them to relevant portfolio projects (from a CSV file)
* Generates custom cold emails using LLMs

---

## 🚀 Features

* Upload your portfolio CSV (must include `TechStack` and `Links` columns)
* Auto-delete existing vector store on each upload to keep data fresh
* Input:

  * Your name
  * company name
  * Job post URL
* Outputs cold email(s) tailored to each job, matched with your relevant projects
* Built with:

  * [Groq API](https://console.groq.com/)
  * [LangChain](https://www.langchain.com/)
  * [Streamlit](https://streamlit.io/)

---


## 🔧 Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/code-crafter3/cold-mail-generator-ai-project.git
cd cold-mail-generator-ai-project
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set your API key

Get your **GROQ API Key** from [console.groq.com](https://console.groq.com/keys) and add it to your `.env` file:

```env
GROQ_API_KEY=your_key_here
```

### 4. Run the app

```bash
streamlit run app/main.py
```

---

## 📌 Requirements for CSV Upload

Your CSV file must include the following columns:

| Column      | Description                          |
| ----------- | ------------------------------------ |
| `TechStack` | The technologies used in the project |
| `Links`     | URL to the project or case study     |

---

## 🤖 Example Use Case

You upload a portfolio with several projects. The app scrapes a job posting for a Backend Engineer requiring Python and PostgreSQL. It finds your most relevant project with those skills and generates a cold email linking directly to it.

---

## 🛠 Tech Stack

* **Streamlit** for UI
* **LangChain** for prompt chaining
* **FAISS** for vector search on portfolio data
* **Groq API** for LLM-based job parsing and email generation

---

## 📬 Output Example

```markdown
Subject: Helping You Fill the Backend Engineer Role — Faster & Smarter

Hi [Hiring Manager at Target Company],

I came across your job post for a Backend Engineer and noticed you're looking for someone with strong Python and PostgreSQL experience.

I’d love to help. Here’s a recent project that demonstrates our experience with similar requirements:
🔗 [Link to relevant portfolio item]

Let me know if you'd like to discuss how we can support your team immediately.

Best regards,  
[Your Name]
```

---

