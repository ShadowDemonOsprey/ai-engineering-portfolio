from fastapi import FastAPI

from pydantic import BaseModel


app = FastAPI()


class ChatRequest(BaseModel):
    message: str


@app.get("/")
def home():
    return {
        "message": "AI Chatbot API is running"
    }


@app.post("/chat")
def chat(request: ChatRequest):

    user_message = request.message.lower()

    if "hello" in user_message:
        response = "Hello! How can I help you today?"

    elif "ai" in user_message:
        response = "AI is the field of building systems that can learn and make decisions."

    else:
        response = "I am still learning. Please ask me another question."

    return {
        "user": request.message,
        "assistant": response
    }