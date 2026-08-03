# Import JSON to read saved embeddings
import json

# Import NumPy for vector processing
import numpy as np

# Import FAISS for similarity search
import faiss


# Create function to build FAISS index
def create_index():

    # Open embeddings file
    with open(
        "embeddings/embeddings.json",
        "r",
        encoding="utf-8"
    ) as f:

        # Load embeddings data
        data = json.load(f)


    # Convert embeddings into NumPy array
    vectors = np.array(
        [
            item["embedding"]
            for item in data
        ],
        dtype="float32"
    )


    # Get embedding size
    dimension = vectors.shape[1]


    # Create FAISS L2 index
    index = faiss.IndexFlatL2(
        dimension
    )


    # Add vectors into FAISS
    index.add(
        vectors
    )


    # Save FAISS index
    faiss.write_index(
        index,
        "vector_store/faiss.index"
    )


    # Print status
    print(
        "FAISS index updated:",
        index.ntotal,
        "vectors"
    )


# Run only when executing this file directly
if __name__ == "__main__":

    create_index()