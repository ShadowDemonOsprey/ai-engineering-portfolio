# Import SentenceTransformer to create text embeddings
from sentence_transformers import SentenceTransformer

# Import JSON to save embeddings
import json

# Import os to create folders
import os


# Load embedding model
model = SentenceTransformer(
    r"C:\models\all-MiniLM-L6-v2"
)


# Read the document file
with open(
    "data/documents.txt",
    "r",
    encoding="utf-8"
) as f:
    text = f.read()


# Split document into smaller chunks
chunks = text.split("\n\n")


# Create embedding list
data = []


# Process each chunk
for chunk in chunks:

    # Ignore empty chunks
    if chunk.strip():

        # Convert chunk text into vector
        embedding = model.encode(chunk).tolist()

        # Store text and embedding
        data.append(
            {
                "text": chunk,
                "embedding": embedding
            }
        )


# Create embeddings folder if missing
os.makedirs(
    "embeddings",
    exist_ok=True
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


# Show result
print("Created chunks:", len(data))