import string
from typing import List
import nltk
from nltk.tokenize import word_tokenize

# Ensure NLTK resources are available without redundant downloads
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

def preprocess_text(texts: List[str]) -> List[List[str]]:
    """
    Cleans and tokenizes a list of strings.
    """
    # Create a translation table for removing punctuation efficiently
    table = str.maketrans('', '', string.punctuation)
    
    return [
        word_tokenize(text.lower().translate(table)) 
        for text in texts
    ]
