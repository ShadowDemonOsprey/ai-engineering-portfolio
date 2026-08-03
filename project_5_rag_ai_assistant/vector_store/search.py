import faiss
import json
import numpy as np
from sentence_transformers import SentenceTransformer


model = SentenceTransformer(
    r"C:\models\all-MiniLM-L6-v2"
)


index = faiss.read_index(
    "vector_store/index.faiss"
)


with open(
    "embeddings/embeddings.json",
    "r",
    encoding="utf-8"
) as f:
    documents = json.load(f)



def search(query, top_k=3):

    embedding = model.encode(
        [query]
    )


    embedding = np.array(
        embedding,
        dtype="float32"
    )


    distances, indices = index.search(
        embedding,
        top_k
    )


    results = []


    for i in indices[0]:

        results.append(
            documents[i]["text"]
        )


    return results