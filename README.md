# AI Engineering Portfolio

Welcome to my AI Engineering Portfolio.

I am a Mathematics graduate transitioning into Applied AI Engineering. I combine mathematical problem-solving skills with practical experience building machine learning models, APIs, and AI applications using Python.

## About Me

- 🎓 Master's Degree in Mathematics
- 🤖 Focus: Applied AI Engineering / Machine Learning Engineering
- 🐍 Programming: Python
- 🚀 Interested in building and deploying real-world AI systems

## Technical Skills

- Python
- Machine Learning
- Deep Learning
- Natural Language Processing
- Large Language Models (LLMs)
- Retrieval-Augmented Generation (RAG)
- Scikit-learn
- Pandas
- NumPy
- FastAPI
- REST APIs
- FAISS
- Docker
- Git
- Linux

---

## Repository Structure

```text
FIRST_AI_PROJECT
│
├── project_1_text_classifier
│   ├── Model training
│   ├── Text preprocessing
│   └── Classification prediction
│
├── project_2_sentiment_analysis
│   ├── FastAPI application
│   ├── Sentiment prediction endpoint
│   └── REST API service
│
├── project_3_ml_pipeline
│   ├── Data processing
│   ├── Feature engineering
│   ├── Model training
│   └── Evaluation
│
├── project_4_ai_chatbot
│   ├── FastAPI chatbot API
│   ├── User message processing
│   └── AI response generation
│
├── project_5_rag_ai_assistant
│   ├── Document processing
│   ├── Embedding generation
│   ├── FAISS vector search
│   ├── RAG pipeline
│   └── Local LLM integration
│
├── .github
│   └── workflows
│       └── python-check.yml
│
├── README.md
├── PROFILE.md
├── PORTFOLIO.md
├── CONTRIBUTING.md
├── CHANGELOG.md
├── LICENSE
└── .gitignore
```

---

# Projects Overview

| Project | Description | Technologies |
|---|---|---|
| AI Text Classification | Classifies text into categories using machine learning | Python, Pandas, Scikit-learn |
| Sentiment Analysis API | REST API for sentiment prediction | Python, FastAPI, Uvicorn |
| Machine Learning Pipeline | Complete ML workflow from data preparation to evaluation | Pandas, NumPy, Scikit-learn |
| AI Chatbot Assistant | Chatbot API for processing user messages | Python, FastAPI, NLP |
| RAG AI Assistant | Document-based AI assistant using retrieval and generation | Python, FastAPI, FAISS, Sentence Transformers, Ollama |

---

# Project 1: AI Text Classification

## Goal

Build a machine learning model that classifies text into categories.

![Text Classification](screenshots/text_classifier.png)

## Tools

- Python
- Scikit-learn
- Pandas
- NumPy

## Status

Completed first working version.

## How to Run

1. Create and activate the conda environment:

```bash
conda activate ai-project
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the model:

```bash
python text_classifier.py
```

---

# Project 2: Sentiment Analysis API

## Overview

A simple REST API that analyzes text sentiment.

![Sentiment API](screenshots/sentiment_api.png)

## Features

- FastAPI web service
- Text prediction endpoint
- JSON response format
- Ready for future machine learning model integration

## Technologies

- Python
- FastAPI
- Uvicorn
- Machine Learning

## API Example

### Endpoint

```text
GET /predict?text=I%20love%20this%20product
```

### Example Response

```json
{
  "text": "I love this product",
  "sentiment": "positive"
}
```

---

# Project 3: Machine Learning Pipeline

## Goal

Build a complete machine learning workflow from data preparation to model evaluation.

![ML Pipeline](screenshots/ml_pipeline.png)

## Pipeline Steps

1. Data loading
2. Data cleaning
3. Feature engineering
4. Model training
5. Model evaluation
6. Prediction

## Technologies

- Python
- Pandas
- NumPy
- Scikit-learn

## Status

Completed working pipeline.

---

# Project 4: AI Chatbot Assistant

## Goal

Build a simple AI chatbot API that processes user messages and generates responses.

![AI Chatbot](screenshots/ai_chatbot.png)

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

# Project 5: RAG AI Assistant

## Goal

Build a complete Retrieval-Augmented Generation system that allows users to upload documents and ask questions using a local AI model.

## Overview

A local document-based AI assistant built with:

- FastAPI
- Sentence Transformers
- FAISS vector database
- Ollama Qwen LLM

The system retrieves relevant document information before generating answers.

---

## Features

- PDF document upload
- TXT document upload
- Document text extraction
- Automatic text chunking
- Embedding generation
- FAISS semantic search
- Context retrieval
- Local LLM answer generation

---

## Architecture

```text
User Question
       |
       v
Question Embedding
       |
       v
FAISS Similarity Search
       |
       v
Retrieve Relevant Context
       |
       v
Context + Question
       |
       v
Ollama Qwen LLM
       |
       v
Generated Answer
```

---

## Technologies

- Python
- FastAPI
- Sentence Transformers
- FAISS
- Ollama
- Qwen 2.5
- PyTorch
- NumPy
- pypdf

---

## Project Structure

```text
project_5_rag_ai_assistant/

│
├── app.py
├── pdf_loader.py
├── document_loader.py
├── embedding_generator.py
├── rag_generator.py
│
├── data/
│
├── embeddings/
│
└── vector_store/
    ├── vector_store.py
    ├── search.py
    └── index.faiss
```

---

## API Endpoints

### Upload Document

```text
POST /upload
```

Supported:

```text
.pdf
.txt
```

Pipeline:

```text
Document
    |
    v
Text Extraction
    |
    v
Chunking
    |
    v
Embedding Generation
    |
    v
FAISS Index
```

---

### Query Document

```text
GET /query
```

Example:

```text
/query?text=What is this document about?
```

Response:

```json
{
  "question": "What is this document about?",
  "answer": "Generated answer",
  "sources": [
    "Retrieved document chunks"
  ]
}
```

---

## How to Run

Go to the project folder:

```bash
cd project_5_rag_ai_assistant
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start Ollama:

```bash
ollama run qwen2.5:0.5b
```

Start FastAPI:

```bash
uvicorn app:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

---
# Skills Demonstrated

- Python Programming
- Machine Learning
- Deep Learning
- Natural Language Processing
- Large Language Models (LLMs)
- Retrieval-Augmented Generation (RAG)
- Vector Database Development
- FAISS Similarity Search
- Embedding Engineering
- Data Processing
- Model Training and Evaluation
- REST API Development
- FastAPI Backend Development
- Docker and Containerization
- Git and GitHub Workflow

---

# Future Improvements

## 1. Improve RAG Retrieval

Possible improvements:

- Better document chunking strategies
- Metadata filtering
- Hybrid keyword + vector search
- Re-ranking models
- Multi-document knowledge bases

---

## 2. Add Chat Interface

Future architecture:

```text
User
 |
 v
Web Chat Interface
 |
 v
FastAPI Backend
 |
 v
RAG Pipeline
 |
 v
LLM Response
```

Future features:

- Conversation history
- Multiple user sessions
- Streaming responses
- Web-based interface

---

## 3. Add Cloud Deployment

Possible deployment platforms:

- AWS
- Azure
- Google Cloud
- Hugging Face Spaces
- Docker containers

---

# How to Run Projects

## Create Environment

Create the conda environment:

```bash
conda create -n ai-project python=3.13
```

Activate:

```bash
conda activate ai-project
```

---

# Project 1: AI Text Classification

Go to project folder:

```bash
cd project_1_text_classifier
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python text_classifier.py
```

---

# Project 2: Sentiment Analysis API

Go to project folder:

```bash
cd project_2_sentiment_analysis
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start API:

```bash
uvicorn app:app --reload
```

Test:

```text
GET /predict?text=I%20love%20this%20product
```

---

# Project 3: Machine Learning Pipeline

Go to project folder:

```bash
cd project_3_ml_pipeline
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run:

```bash
python pipeline.py
```

---

# Project 4: AI Chatbot Assistant

Go to project folder:

```bash
cd project_4_ai_chatbot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start chatbot:

```bash
uvicorn app:app --reload
```

Endpoint:

```text
POST /chat
```

---

# Project 5: RAG AI Assistant

Go to project folder:

```bash
cd project_5_rag_ai_assistant
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start Ollama:

```bash
ollama run qwen2.5:0.5b
```

Start FastAPI:

```bash
uvicorn app:app --reload
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

---

# Docker Support

This repository includes Docker support for running AI projects in isolated containers.

## Supported Projects

- Project 1: AI Text Classification
- Project 2: Sentiment Analysis API
- Project 5: RAG AI Assistant

---

# Docker Environment

- Python base images
- Containerized AI applications
- FastAPI API deployment
- REST API services
- Reproducible environments
- Docker Compose support

---

# Final Goal

Build production-ready AI systems combining:

```text
Machine Learning
        +
Deep Learning
        +
LLM Applications
        +
RAG Systems
        +
API Development
        +
Cloud Deployment
```

The goal is to develop practical AI engineering solutions for real-world applications.

---

# Resume

You can view my resume here:

[AI Engineer Resume](resume/Noah_Lin_Cruz_AI_Engineer_Resume.pdf)

---

# Author

AI Engineering Portfolio Project

Built as part of an Applied AI Engineer roadmap.
