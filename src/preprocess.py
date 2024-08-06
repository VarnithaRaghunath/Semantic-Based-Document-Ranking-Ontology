# src/preprocess.py
import os

from sklearn.feature_extraction.text import TfidfVectorizer


def load_documents(doc_dir):
    documents = []
    for filename in os.listdir(doc_dir):
        if filename.endswith(".txt"):
            with open(os.path.join(doc_dir, filename), 'r', encoding='utf-8') as file:
                documents.append(file.read())
    return documents

def preprocess_documents(documents):
    vectorizer = TfidfVectorizer(stop_words='english')
    X = vectorizer.fit_transform(documents)
    return X, vectorizer
