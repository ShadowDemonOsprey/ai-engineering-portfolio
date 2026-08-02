# AI Chatbot Assistant

## Goal

Build a simple AI chatbot API that processes user messages and generates responses.

## Features

- REST API chatbot endpoint
- User message processing
- JSON response format
- FastAPI backend
- Ready for future LLM integration

## Technologies

- Python
- FastAPI
- Uvicorn
- Pydantic
- Natural Language Processing

## API Usage

### Endpoint

```text
POST /chat
```

### Request Example

```json
{
  "message": "hello"
}
```

### Response Example

```json
{
  "user": "hello",
  "assistant": "Hello! How can I help you today?"
}
```

## Future Improvements

- Connect with Large Language Models (LLMs)
- Add conversation memory
- Add a web interface
- Deploy as a cloud service

---

## Run with Docker

### Build Docker Image

From this folder:

```bash
docker build -t ai-chatbot .
```

### Run Container

```bash
docker run -p 8000:8000 ai-chatbot
```

The API will be available at:

```text
http://127.0.0.1:8000
```

### Test Chatbot API

Endpoint:

```text
POST /chat
```

Request:

```json
{
  "message": "hello"
}
```

Response:

```json
{
  "user": "hello",
  "assistant": "Hello! How can I help you today?"
}
```