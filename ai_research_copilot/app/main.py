from dotenv import load_dotenv
import os

dotenv_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '.env'))
load_dotenv(dotenv_path)

from fastapi import FastAPI
from .services.openai_service import ask_gpt

app = FastAPI()

@app.get("/ping")
def ping():
    return {"status": "ok"}

@app.get("/ask")
def ask(prompt: str):
    answer = ask_gpt(prompt)
    return {"answer": answer}