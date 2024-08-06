# src/vectorize.py
from sklearn.metrics.pairwise import cosine_similarity


def calculate_similarity(vectors):
    similarity_matrix = cosine_similarity(vectors)
    return similarity_matrix
