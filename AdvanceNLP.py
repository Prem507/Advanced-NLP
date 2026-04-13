import PyPDF2
import nltk
import numpy as np

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')
nltk.download('stopwords')

files = [
    r"D:\Desktop\CSV\AnnualHealthCheck.pdf",
    r"D:\Desktop\CSV\LeavePolicy.pdf",
    r"D:\Desktop\CSV\NoticePeriod.pdf",
    r"D:\Desktop\CSV\OfficeTime.pdf",
    r"D:\Desktop\CSV\Separation.pdf",
    r"D:\Desktop\CSV\Travel.pdf",
    r"D:\Desktop\CSV\USA_Employee_Handbook-Freely_Available.pdf"
]

documents = []

for file in files:
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    documents.append(text)
print("Documents Loaded:", len(documents))

sentences = []

for doc in documents:
    sents = sent_tokenize(doc)
    for s in sents:
        sentences.append(s)

print("Total Sentences:", len(sentences))



stop_words = set(stopwords.words("english"))


stemmer = PorterStemmer()

def preprocess(text):
    tokens = word_tokenize(text.lower())
    clean_tokens = []
    for word in tokens:
        if word.isalpha() and word not in stop_words:
            stem = stemmer.stem(word)
            clean_tokens.append(stem)
    return " ".join(clean_tokens)

processed_sentences = []

for s in sentences:
    processed_sentences.append(preprocess(s))



vectorizer = TfidfVectorizer()


tfidf_matrix = vectorizer.fit_transform(processed_sentences)

query = input("Ask Question: ")

processed_query = preprocess(query)

query_vector = vectorizer.transform([processed_query])

similarities = cosine_similarity(query_vector, tfidf_matrix)   #[[0.92, 0.45, 0.60]]

best_match_index = np.argmax(similarities)   #0.92

print("\nBest Matching Sentence:\n")

print(sentences[best_match_index])
