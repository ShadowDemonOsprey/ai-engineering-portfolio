from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Sentiment Analysis API is running"
    }

@app.get("/predict")
def predict(text: str):
    if "good" in text.lower() or "love" in text.lower():
        sentiment = "positive"
    else:
        sentiment = "negative"

    return {
        "text": text,
        "sentiment": sentiment
    }