# Project 5: RAG AI Assistant

A Retrieval-Augmented Generation (RAG) AI Assistant built with Python, FastAPI, and Sentence Transformers.

This project demonstrates how to build a document-based AI assistant using embeddings, semantic search, and a RAG pipeline architecture.

---

# Project Structure

    project_5_rag_ai_assistant/
    │
    ├── app.py
    ├── requirements.txt
    ├── README.md
    │
    ├── documents/
    │   └── sample.txt
    │
    ├── embeddings/
    │   └── embeddings.json
    │
    └── models/
        └── all-MiniLM-L6-v2

---

# Features

- Document loading
- Text preprocessing
- Text chunking
- Sentence Transformer embedding generation
- Local Hugging Face model support
- Semantic similarity search foundation
- FastAPI backend
- RAG architecture foundation

---

# Environment Setup

## Create Conda Environment

```bash
conda create -n ai-project python=3.11
```

Activate environment:

```bash
conda activate ai-project
```

---

# Install Dependencies

Install required packages:

```bash
pip install -r requirements.txt
```

Main dependencies:

```text
fastapi
uvicorn
sentence-transformers
torch
numpy
scikit-learn
```

---

# Embedding Model

This project uses:

```text
sentence-transformers/all-MiniLM-L6-v2
```

## Model Purpose

The Sentence Transformer model converts text into numerical vectors called embeddings.

Example:

Input:

```text
"Artificial intelligence is changing the world."
```

Output:

```text
A vector representation of the text meaning.
```

These embeddings allow the system to compare the meaning of different texts.

---

# Download Embedding Model

Download the model locally from Hugging Face:

```bash
hf download sentence-transformers/all-MiniLM-L6-v2 --local-dir C:\models\all-MiniLM-L6-v2 --force-download
```

Model location:

```text
C:\models\all-MiniLM-L6-v2
```

---

# Test Embedding Model

Start Python:

```bash
python
```

Run:

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    r"C:\models\all-MiniLM-L6-v2"
)

print(model.encode("hello world")[:5])
```

Expected output:

```text
[-0.03447726  0.03102325  0.00673501  0.02610896 -0.03936204]
```

Successful output means the embedding model is working correctly.

---

# Running the Application

Start FastAPI server:

```bash
uvicorn app:app --reload
```

Server address:

```text
http://127.0.0.1:8000
```

---

# API Endpoints

## Health Check

Endpoint:

```text
GET /
```

Example:

```text
http://127.0.0.1:8000/
```

Response:

```json
{
    "message": "RAG AI Assistant running"
}
```

---

## Create Embeddings

Endpoint:

```text
GET /embeddings
```

Example:

```text
http://127.0.0.1:8000/embeddings
```

The endpoint performs:

```text
Document
    |
    v
Text Loading
    |
    v
Text Chunking
    |
    v
Embedding Generation
    |
    v
Vector Storage
```

---

# RAG Pipeline

Retrieval-Augmented Generation workflow:

```text
User Question
       |
       v
Convert Question Into Embedding
       |
       v
Search Similar Document Embeddings
       |
       v
Retrieve Relevant Context
       |
       v
Generate Final Answer
```

---

# How Embeddings Work

Example:

Document 1:

```text
Machine learning is a branch of artificial intelligence.
```

Document 2:

```text
AI systems can learn patterns from data.
```

Although the words are different, their meanings are similar.

The embedding model converts both texts into vectors and measures their similarity.

---

# Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| FastAPI | API development |
| Uvicorn | ASGI server |
| Sentence Transformers | Text embedding generation |
| Hugging Face | Model repository |
| PyTorch | Deep learning framework |
| NumPy | Numerical computation |
| Scikit-learn | Similarity calculations |

---

# Development Progress

## Completed

- [x] Project initialization
- [x] Conda environment setup
- [x] FastAPI application created
- [x] Document loading implemented
- [x] Document loading tested
- [x] Sentence Transformer integration
- [x] Hugging Face model downloaded
- [x] Local embedding model configured
- [x] Embedding generation tested
- [x] API server running successfully

---

# Future Improvements

## 1. Add Vector Database

Current:

```text
Documents
    |
    v
Embeddings
    |
    v
Storage
```

Future:

```text
Documents
    |
    v
Embeddings
    |
    v
Vector Database
    |
    v
Fast Similarity Search
```

Possible technologies:

```text
FAISS
ChromaDB
Pinecone
```

---

## 2. Add Document Upload

Future features:

- Upload PDF files
- Upload text files
- Extract document content
- Automatically create embeddings

---

## 3. Add Large Language Model

Integrate:

```text
Llama
Mistral
DeepSeek
OpenAI API
```

Pipeline:

```text
Question
    |
    v
Retrieve Documents
    |
    v
Send Context To LLM
    |
    v
Generate Answer
```

---

## 4. Build Complete RAG Chatbot

Final goal:

```text
User
 |
 v
Chat Interface
 |
 v
RAG System
 |
 +--> Document Retrieval
 |
 +--> Vector Search
 |
 +--> LLM Response
```

Features:

- Document upload
- Question answering
- Context retrieval
- AI-generated responses
- Conversation memory

---

# Author

AI Engineering Portfolio Project

Built as part of an Applied AI Engineer roadmap.