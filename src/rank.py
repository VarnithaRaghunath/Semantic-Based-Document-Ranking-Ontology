# src/rank.py
import numpy as np


def rank_documents(similarity_matrix, query_idx):
    rankings = np.argsort(-similarity_matrix[query_idx])
    return rankings
