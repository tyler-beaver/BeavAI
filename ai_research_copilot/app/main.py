from fastapi import FastAPI
from .services.openai_service import ask_gpt
from dotenv import load_dotenv

load_dotenv(); 

app = FastAPI()

# Simple test route
@app.get("/ask")
def ask(prompt: str):
    answer = ask_gpt(prompt)
    return {"answer": answer}
