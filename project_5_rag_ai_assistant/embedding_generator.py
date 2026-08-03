# Import SentenceTransformer to create embeddings
from sentence_transformers import SentenceTransformer

# Import JSON to save embeddings
import json

# Import FAISS index builder
from vector_store.vector_store import create_index


# Load embedding model
model = SentenceTransformer(
    r"C:\models\all-MiniLM-L6-v2"
)


# Create function to generate embeddings
def create_embeddings(file_path):

    # Read uploaded document
    with open(
        file_path,
        "r",
        encoding="utf-8"
    ) as file:

        # Store document text
        text = file.read()


    # Split document into chunks
    chunks = text.split("\n\n")


    # Store embedding results
    data = []


    # Process every chunk
    for chunk in chunks:

        # Ignore empty chunks
        if chunk.strip():

            # Convert chunk into vector
            embedding = model.encode(
                chunk
            ).tolist()


            # Save text and vector
            data.append(
                {
                    "text": chunk,
                    "embedding": embedding
                }
            )


    # Save embeddings
    with open(
        "embeddings/embeddings.json",
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f
        )


    # Rebuild FAISS index
    create_index()