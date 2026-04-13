Document Question Answering System (Advanced NLP)

This project is a **Document Question Answering System** built using Python and basic NLP techniques.  
It allows users to ask questions from multiple PDF documents and returns the most relevant sentence as the answer.

--
What This Project Does

- Reads multiple PDF files  
- Extracts and processes text  
- Converts text into meaningful data using NLP  
- Accepts a user question  
- Finds and returns the most relevant answer  

---
Technologies Used

- Python  
- NLTK (Natural Language Toolkit)  
- NumPy  
- Scikit-learn  
- PyPDF2  

---

How It Works

1. Load PDF documents  
2. Extract text from each file  
3. Split text into sentences  
4. Preprocess text:
   - Tokenization  
   - Stopword removal  
   - Stemming  
5. Convert sentences into vectors using **TF-IDF**  
6. Compare user query with sentences using **Cosine Similarity**  
7. Return the best matching sentence  

---
How to Run

1. Clone the repository:
```bash
git clone https://github.com/Prem507/Advanced-NLP.git
cd Advanced-NLP
Install required libraries:
Bash
pip install nltk numpy scikit-learn PyPDF2
Run the program:
Bash
python main.py
Enter your question in the terminal.


Example
Input:

Ask Question: What is leave policy?
Output:

Best Matching Sentence:
Employees are entitled to leave as per company policy.

Future Improvements
Improve accuracy using advanced models (BERT, Sentence Transformers)
Add semantic search instead of keyword matching
Build a web app using Streamlit
Deploy on cloud

Author
Premchandh 
B.Tech CSE (Final Year)
Note
This project demonstrates how basic NLP techniques can be used to build a simple AI-based question answering system.
