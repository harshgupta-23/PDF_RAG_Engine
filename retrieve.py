import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer


def create_vectorizer(processed_texts):
    """
    Creates a TF-IDF vectorizer and transforms the texts.

    Args:
    processed_texts (list): List of preprocessed and tokenized texts.

    Returns:
    tuple: TF-IDF vectorizer and transformed text matrix.
    """
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform([' '.join(text) for text in processed_texts])
    return vectorizer, X

def retrieve(query, X, vectorizer, top_k=5):
    """
    Retrieves the top-k most relevant texts for a given query.

    Args:
    query (str): Query string.
    X (matrix): TF-IDF transformed text matrix.
    vectorizer (TfidfVectorizer): TF-IDF vectorizer.
    top_k (int): Number of top results to retrieve.

    Returns:
    list: Indices of the top-k most relevant texts.
    """
    query_vec = vectorizer.transform([query])
    scores = np.dot(X, query_vec.T).toarray()
    top_indices = np.argsort(scores, axis=0)[-top_k:][::-1]
    return top_indices.flatten()
