import faiss
import pickle
import numpy as np
import os

INDEX_PATH = "data/index.faiss"
CHUNKS_PATH = "data/chunks.pkl"


def build_and_save(embeddings, chunks: list[str]):
    os.makedirs("data", exist_ok=True)

    vectors = np.array(embeddings).astype("float32")

    if len(vectors.shape) != 2:
        raise ValueError("Embeddings must be 2D")

    index = faiss.IndexFlatL2(vectors.shape[1])
    index.add(vectors)

    faiss.write_index(index, INDEX_PATH)

    with open(CHUNKS_PATH, "wb") as f:
        pickle.dump(chunks, f)


def load():
    index = faiss.read_index(INDEX_PATH)

    with open(CHUNKS_PATH, "rb") as f:
        chunks = pickle.load(f)

    return index, chunks