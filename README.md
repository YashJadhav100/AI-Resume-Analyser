# 🧠 AI Resume Analyzer

A simple AI-powered web app that analyzes how well your resume matches a given job description using NLP techniques. Built with **Python** and **Streamlit**, the app provides a relevance score (in %) and highlights matched and missing keywords to help tailor your resume for better job targeting.

---

## 🚀 Features

- 📄 Upload your **resume (PDF format)**
- 📋 Paste the **job description**
- 🧠 Text preprocessing using **NLTK** (stopwords removal, cleaning)
- 📊 **TF-IDF + Cosine Similarity** for resume–JD matching
- ✅ Shows a **relevance match score (%)**
- 📈 **Green progress bar** visualization
- 🔍 Displays **matched keywords**
- ❗ Highlights **missing keywords** from the job description
- 💡 Resume improvement suggestions

---

## 🛠️ Tech Stack

- Python
- Streamlit
- scikit-learn (TF-IDF, Cosine Similarity)
- NLTK (stopwords)
- PyMuPDF (resume PDF parsing)

## 📂 Project Structure

ai_resume_analyzer/

├── app.py

├── requirements.txt

├── README.md

└── .gitignore

## 🧪 How to Run Locally

1. Clone the repository  
   ```bash
   git clone https://github.com/YashJadhav100/AI-Resume-Analyser.git
   cd AI-Resume-Analyser
   
2. Create and activate a virtual environment 
   ```bash
   python -m venv venv
   venv\Scripts\activate

4. Install dependencies
   ```bash
   pip install -r requirements.txt

6. Download NLTK stopwords
   ```bash
   import nltk
   nltk.download('stopwords')

8. Run the app
   ```bash
   streamlit run app.py

🌐 Deployment
You can deploy this project for free using Streamlit Cloud. Just connect your GitHub repo and click "Deploy".

✍️ Author
Made with 💻 by Yash Jadhav
Master's in Computer Science | Syracuse University
