# Import file upload tools from FastAPI
from fastapi import UploadFile, File

# Import document loader
from document_loader import load_document

# Import FastAPI framework
from fastapi import FastAPI

# Import document retrieval function
from vector_store.search import search

# Import LLM generation function
from rag_generator import generate_answer

# Import automatic embedding generator
from embedding_generator import create_embeddings

# Create FastAPI application
app = FastAPI()


# Home endpoint
@app.get("/")
def home():

    # Return API status
    return {
        "message": "RAG AI Assistant running"
    }


# Create RAG query endpoint
@app.get("/query")
def query(text: str):

    # Retrieve top 3 relevant document chunks
    results = search(
        text,
        top_k=3
    )


    # Combine retrieved chunks into one context
    context = "\n\n".join(
        [
            item["text"]
            for item in results
        ]
    )


    # Generate answer using Qwen2.5
    answer = generate_answer(
        text,
        context
    )


    # Return complete RAG response
    return {
        "query": text,
        "context": context,
        "answer": answer,
        "sources": results
    }

# Create document upload endpoint
@app.post("/upload")
async def upload_document(
    file: UploadFile = File(...)
):

    # Save uploaded file path
    file_path = f"data/{file.filename}"


    # Open destination file
    with open(
        file_path,
        "wb"
    ) as buffer:

        # Write uploaded file content
        buffer.write(
            await file.read()
        )


    # Load document text
    text = load_document(
        file_path
    )

    # Create embeddings and rebuild FAISS index
    create_embeddings(
        file_path
    )


    # Return upload result
    return {
        "filename": file.filename,
        "characters": len(text),
        "message": "Document uploaded successfully"
    }