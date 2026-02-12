from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv(); 

app = FastAPI()

# Simple test route
@app.get("/ping")
def ping():
    return {"message": "pong"}
