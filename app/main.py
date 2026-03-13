from fastapi import FastAPI
from app.model import generate_answer

app = FastAPI()

@app.get("/")
def root():
    return {"message": "DevOps AI Assistant running"}

@app.post("/chat")
def chat(prompt: str):

    answer = generate_answer(prompt)

    return {"response": answer}