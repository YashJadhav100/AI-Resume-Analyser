import streamlit as st
import fitz  # PyMuPDF
import string
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
nltk.download('stopwords')

st.set_page_config(page_title="AI Resume Analyzer", layout="centered")
st.title("📄 AI-Powered Resume Analyzer")

# Upload resume
uploaded_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])

# Paste Job Description
job_description = st.text_area("Paste the Job Description here")

def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))  # remove punctuation
    words = text.split()
    words = [word for word in words if word not in stopwords.words('english')]
    return ' '.join(words)

def extract_keywords(text, top_n=15):
    vectorizer = TfidfVectorizer(stop_words='english', max_features=top_n)
    tfidf_matrix = vectorizer.fit_transform([text])
    return set(vectorizer.get_feature_names_out())

if uploaded_file and job_description:
    with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
        resume_text = ""
        for page in doc:
            resume_text += page.get_text()

    st.subheader("✅ Extracted Resume Text:")
    st.write(resume_text[:1000])  # show preview

    clean_resume = clean_text(resume_text)
    clean_jd = clean_text(job_description)

    # TF-IDF and cosine similarity
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([clean_resume, clean_jd])
    similarity_score = cosine_similarity(vectors[0], vectors[1])[0][0]
    relevance_percent = round(similarity_score * 100, 2)

    # Show score
    st.subheader("📊 Resume Relevance Score")
    st.write(f"**Your resume is {relevance_percent}% relevant to this job description.**")
    st.progress(int(relevance_percent))

    # Show keywords
    resume_keywords = extract_keywords(clean_resume, top_n=15)
    jd_keywords = extract_keywords(clean_jd, top_n=15)
    matched_keywords = resume_keywords & jd_keywords
    missing_keywords = jd_keywords - resume_keywords

    st.subheader("✅ Matched Keywords")
    st.write(', '.join(matched_keywords) if matched_keywords else "None matched.")

    st.subheader("❌ Missing Keywords from JD")
    st.write(', '.join(missing_keywords) if missing_keywords else "No critical keywords missing!")

    st.info("💡 Consider adding the missing keywords above to your resume to increase relevance.")
