import string

import nltk

nltk.download('punkt')
from nltk.tokenize import word_tokenize


def preprocess_text(texts):
    """
    Preprocesses a list of texts by converting to lowercase, removing punctuation, and tokenizing.

    Args:
    texts (list): List of text strings to preprocess.

    Returns:
    list: List of preprocessed and tokenized texts.
    """
    processed_texts = []
    for text in texts:
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        tokens = word_tokenize(text)
        processed_texts.append(tokens)
    return processed_texts
