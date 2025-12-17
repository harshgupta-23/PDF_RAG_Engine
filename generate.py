import os
from typing import List
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Initialize the client and validate key
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment variables.")

client = OpenAI(api_key=api_key)

def generate_response(retrieved_texts: List[str], query: str, max_tokens: int = 150) -> str:
    """
    Generates an AI response using the modern OpenAI client.
    """
    context = "\n\n---\n\n".join(retrieved_texts)
    prompt = f"Use the following context to answer the question.\n\nContext: {context}\n\nQuestion: {query}"
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant. Use the context provided to answer accurately."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens,
            temperature=0.5,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error generating response: {e}"
