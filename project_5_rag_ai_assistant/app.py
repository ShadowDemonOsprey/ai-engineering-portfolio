from fastapi import FastAPI, UploadFile, File

from pdf_loader import load_pdf
from document_loader import load_document

from embedding_generator import create_embeddings

from vector_store.search import search

from rag_generator import generate_answer


import os



app = FastAPI()



@app.get("/")
def home():

    return {
        "message":
        "RAG AI Assistant running"
    }



@app.post("/upload")
async def upload_document(
    file: UploadFile = File(...)
):


    os.makedirs(
        "data",
        exist_ok=True
    )


    path = (
        "data/"
        +
        file.filename
    )



    with open(
        path,
        "wb"
    ) as f:

        f.write(
            await file.read()
        )



    if file.filename.endswith(".pdf"):

        text = load_pdf(
            path
        )

    else:

        text = load_document(
            path
        )



    chunks = create_embeddings(
        path
    )



    return {

        "filename":
        file.filename,


        "characters":
        len(text),


        "chunks":
        chunks,


        "message":
        "Document indexed successfully"

    }





@app.get("/query")
def query(text:str):


    results = search(
        text,
        top_k=3
    )


    context = "\n\n".join(
        results
    )


    answer = generate_answer(
        text,
        context
    )



    return {


        "question":
        text,


        "answer":
        answer,


        "sources":
        results

    }