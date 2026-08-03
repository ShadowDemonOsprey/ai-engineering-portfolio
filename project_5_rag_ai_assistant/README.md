# Project 5: RAG AI Assistant

A local **Retrieval-Augmented Generation (RAG) AI Assistant** built with Python, FastAPI, FAISS, Sentence Transformers, and Ollama.

This project demonstrates a complete document-based AI question-answering system:

- Upload documents
- Extract text
- Split documents into chunks
- Generate embeddings
- Store vectors using FAISS
- Retrieve relevant context
- Generate answers using a local LLM

---

# Project Architecture

```text
project_5_rag_ai_assistant/

│
├── app.py
├── pdf_loader.py
├── document_loader.py
├── embedding_generator.py
├── rag_generator.py
├── requirements.txt
├── README.md
│
├── data/
│   └── documents.txt
│
├── embeddings/
│   └── embeddings.json
│
└── vector_store/
    ├── vector_store.py
    ├── search.py
    └── index.faiss
```

---

# Features

- PDF document loading
- TXT document loading
- Automatic document chunking
- Sentence Transformer embedding generation
- Local embedding model support
- FAISS vector similarity search
- Document upload API
- Semantic retrieval
- Local LLM answer generation
- Complete RAG pipeline

---

# Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| FastAPI | Backend API framework |
| Uvicorn | ASGI server |
| Sentence Transformers | Text embeddings |
| FAISS | Vector database/search engine |
| Ollama | Local LLM runtime |
| Qwen 2.5 | Answer generation |
| PyTorch | Deep learning framework |
| NumPy | Vector processing |

---

# Environment Setup

## Create Conda Environment

```bash
conda create -n ai-project python=3.11
```

Activate:

```bash
conda activate ai-project
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

Main packages:

```text
fastapi
uvicorn
sentence-transformers
faiss-cpu
torch
numpy
pypdf
ollama
python-multipart
```

---

# Embedding Model

This project uses:

```text
sentence-transformers/all-MiniLM-L6-v2
```

The model converts text into numerical vectors called embeddings.

Example:

Input:

```text
Artificial intelligence is changing the world.
```

Output:

```text
[0.0234, -0.0312, ...]
```

These vectors represent the semantic meaning of text.

---

# Local Embedding Model Setup

Download:

```bash
hf download sentence-transformers/all-MiniLM-L6-v2 --local-dir C:\models\all-MiniLM-L6-v2
```

Model location:

```text
C:\models\all-MiniLM-L6-v2
```

---

# Ollama Setup

Download Qwen model:

```bash
ollama pull qwen2.5:0.5b
```

Run:

```bash
ollama run qwen2.5:0.5b
```

The model generates answers using retrieved document context.

---

# Running the Application

Start FastAPI:

```bash
uvicorn app:app --reload
```

Server:

```text
http://127.0.0.1:8000
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

---

# API Endpoints

## Health Check

```
GET /
```

Example response:

```json
{
    "message": "RAG AI Assistant running"
}
```

---

## Upload Document

Endpoint:

```
POST /upload
```

Supported files:

```
.txt
.pdf
```

Pipeline:

```text
Document Upload
        |
        v
Text Extraction
        |
        v
Text Chunking
        |
        v
Embedding Generation
        |
        v
FAISS Index Creation
```

---

## Ask Question

Endpoint:

```
GET /query
```

Example:

```
/query?text=What is this document about?
```

Response:

```json
{
    "question": "What is this document about?",
    "answer": "Generated answer from Qwen",
    "sources": [
        "Retrieved document chunks"
    ]
}
```

---

# RAG Pipeline

Complete workflow:

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
Retrieve Relevant Documents
        |
        v
Context + Question
        |
        v
Local Qwen LLM
        |
        v
Final Answer
```

---

# Development Progress

## Completed

- [x] FastAPI backend created
- [x] Document loader implemented
- [x] PDF extraction implemented
- [x] Text chunking implemented
- [x] Sentence Transformer embeddings
- [x] Local embedding model configured
- [x] FAISS vector database integrated
- [x] Document upload endpoint
- [x] Semantic search implemented
- [x] Ollama LLM integration
- [x] Complete RAG pipeline completed

---

# Future Improvements

## Improve Retrieval

Possible upgrades:

- Better chunking strategies
- Metadata filtering
- Hybrid search
- Re-ranking models

---

## Add Chat Interface

Future architecture:

```text
User
 |
 v
Web Chat UI
 |
 v
FastAPI Backend
 |
 v
RAG System
 |
 v
LLM Response
```

---

## Deploy Application

Possible deployment:

- Docker
- AWS
- Azure
- Hugging Face Spaces

---

# Final Goal

A complete AI knowledge assistant:

```text
User
 |
 v
Chat Interface
 |
 v
FastAPI API
 |
 v
RAG Pipeline

 +--> Document Processing
 |
 +--> FAISS Retrieval
 |
 +--> LLM Generation
 |
 v

AI Answer
```

---

# Author

AI Engineering Portfolio Project

Built as part of an Applied AI Engineer roadmap.