# src/main.py
from preprocess import load_documents, preprocess_documents
from rank import rank_documents
from vectorize import calculate_similarity


def main():
    doc_dir = "../documents"
    documents = load_documents(doc_dir)
    vectors, vectorizer = preprocess_documents(documents)
    similarity_matrix = calculate_similarity(vectors)
    
    query_idx = 0  # assuming the first document is the query
    rankings = rank_documents(similarity_matrix, query_idx)
    
    print("Document rankings (from most to least similar):")
    for rank, idx in enumerate(rankings, start=1):
        print(f"Rank{rank}: Document {idx + 1}")

if __name__ == "__main__":
    main()
