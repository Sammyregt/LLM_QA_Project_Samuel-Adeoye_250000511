"""
Docstring for LLM_QA_CLI
a Python CLI application that accepts a natural-language question from the user, processes it, sends it to an LLM API (e.g., OpenAI, Cohere, HuggingFace, Groq, Gemini), and displays the final answer.

General CLI Requirements:
- Accept natural-language questions from the user.
- Apply basic preprocessing (lowercasing, tokenization, punctuation removal).
- Construct a prompt and send it to the chosen LLM API.
- Display the final answer to the user.
"""

import os
import re
import sys
from groq import Groq
from dotenv import load_dotenv

# loading environment variables from .env file
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
MODEL = os.getenv("MODEL", "llama-3.1-8b-instant")

def preprocess_text(text):
    """Lowercase, remove punctuation, tokenize."""
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    tokens = text.split()
    return " ".join(tokens)

def ask_model(question):
    """Send processed question to Groq LLM API."""
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful Q&A assistant."},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content

def main():
    print("\n=== LLM Q&A CLI SYSTEM ===")
    question = input("Enter your question: ")

    processed = preprocess_text(question)
    print(f"\nProcessed Question: {processed}\n")

    answer = ask_model(processed)
    print("Answer:", answer)

if __name__ == "__main__":
    main()