# app/main.py

from fastapi import FastAPI

# THIS IS THE FASTAPI INSTANCE
app = FastAPI()

# Simple test route
@app.get("/ping")
def ping():
    return {"message": "pong"}
