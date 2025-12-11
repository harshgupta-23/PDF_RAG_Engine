import os

import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Retrieve the OpenAI API key from the environment variable
openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_response(retrieved_texts, query, max_tokens=150):
    """
    Generates a response based on the retrieved texts and query.

    Args:
    retrieved_texts (list): List of retrieved text strings.
    query (str): Query string.
    max_tokens (int): Maximum number of tokens for the response.

    Returns:
    str: Generated response.
    """
    context = "\n".join(retrieved_texts)
    prompt = f"Context: {context}\n\nQuestion: {query}\n\nAnswer:"
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].message['content']
