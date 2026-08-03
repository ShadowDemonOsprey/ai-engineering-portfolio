from sentence_transformers import SentenceTransformer
import json

from vector_store.vector_store import create_index

from pdf_loader import load_pdf
from document_loader import load_document



model = SentenceTransformer(
    r"C:\models\all-MiniLM-L6-v2"
)



def create_embeddings(file_path):


    if file_path.endswith(".pdf"):

        text = load_pdf(
            file_path
        )

    else:

        text = load_document(
            file_path
        )


    chunk_size = 1000


    chunks = [
        text[i:i+chunk_size]
        for i in range(
            0,
            len(text),
            chunk_size
        )
    ]



    data = []


    for chunk in chunks:


        if chunk.strip():


            vector = model.encode(
                chunk
            ).tolist()



            data.append(
                {
                    "text": chunk,
                    "embedding": vector
                }
            )



    with open(
        "embeddings/embeddings.json",
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f
        )


    create_index()


    return len(data)