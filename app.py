"""
Flask Web GUI Application for the LLM Q&A System
Displays:
    - User question
    - Processed version
    - LLM response
"""

from flask import Flask, render_template, request
from groq import Groq
import os
import re
from dotenv import load_dotenv

# loading environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
MODEL = os.getenv("MODEL", "llama-3.1-8b-instant")

def preprocess_text(text):
    """Lowercase, remove punctuation, tokenize."""
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    tokens = text.split()
    return " ".join(tokens)

def ask_llm(question):
    """Send processed question to Groq LLM API."""
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful Q&A assistant."},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content

@app.route("/", methods=["GET", "POST"])
def index():
    answer = ""
    processed_question = ""

    if request.method == "POST":
        question = request.form["question"]
        processed_question = preprocess_text(question)
        answer = ask_llm(processed_question)
    return render_template("index.html", answer=answer, processed_question=processed_question)

if __name__ == "__main__":
    app.run(debug=True)