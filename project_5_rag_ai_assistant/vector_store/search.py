# Import FAISS library for loading and searching the vector index
import faiss

# Import NumPy for converting vectors into the correct format
import numpy as np

# Import JSON for reading stored documents and embeddings
import json

# Import SentenceTransformer to convert queries into embeddings
from sentence_transformers import SentenceTransformer


# Load the local embedding model
model = SentenceTransformer(
    r"C:\models\all-MiniLM-L6-v2"
)


# Load the FAISS vector database
index = faiss.read_index(
    "vector_store/faiss.index"
)


# Load documents with their embeddings
with open("embeddings/embeddings.json", "r", encoding="utf-8") as f:
    documents = json.load(f)


# Create search function with top_k option
def search(query, top_k=3):

    # Convert user query into embedding vector
    query_vector = model.encode(query)

    # Convert vector into FAISS format
    query_vector = np.array(
        [query_vector],
        dtype="float32"
    )

    # Search for multiple similar documents
    distance, result = index.search(
        query_vector,
        k=top_k
    )

    # Store retrieved documents
    results = []


    # Loop through every matched document
    for i in range(top_k):

        # Get document index
        document_index = result[0][i]

        # Add document text and score
        results.append(
            {
                "text": documents[document_index]["text"],
                "score": float(distance[0][i])
            }
        )


    # Return multiple documents
    return results