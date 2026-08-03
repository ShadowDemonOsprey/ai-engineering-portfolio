import json
import faiss
import numpy as np
import os


def create_index():

    with open(
        "embeddings/embeddings.json",
        "r",
        encoding="utf-8"
    ) as f:
        data = json.load(f)


    embeddings = np.array(
        [
            item["embedding"]
            for item in data
        ],
        dtype="float32"
    )


    dimension = embeddings.shape[1]


    index = faiss.IndexFlatL2(
        dimension
    )


    index.add(
        embeddings
    )


    os.makedirs(
        "vector_store",
        exist_ok=True
    )


    faiss.write_index(
        index,
        "vector_store/index.faiss"
    )


    print("FAISS index created")