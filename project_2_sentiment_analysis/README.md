# Sentiment Analysis API

## Goal
Build a simple AI system that analyzes text sentiment.

## Technologies
- Python
- Machine Learning
- Scikit-learn
- Pandas

## Status
Planning stage.

---

## Run with Docker

### Build Docker Image

From this folder:

```bash
docker build -t sentiment-api .
```

### Run Container

```bash
docker run -p 8000:8000 sentiment-api
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## Test API

Endpoint:

```text
GET /predict
```

Example:

```text
/predict?text=I%20love%20this%20product
```

Response:

```json
{
  "text": "I love this product",
  "sentiment": "positive"
}
```