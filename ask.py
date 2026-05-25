from sentence_transformers import SentenceTransformer

from modules.vector_store import load
from modules.retriever import retrieve
from modules.generator import generate_answer


MODEL_NAME = "all-MiniLM-L6-v2"
DEFAULT_K = 5


def load_model() -> SentenceTransformer:
    """
    Load embedding model.
    """
    return SentenceTransformer(MODEL_NAME)


def load_index():
    """
    Load FAISS index and stored chunks.
    """
    return load()


def answer_query(
    query: str,
    model,
    index,
    chunks,
    k: int = DEFAULT_K
) -> str:
    """
    Run retrieval + generation pipeline.
    """
    context = retrieve(
        query=query,
        model=model,
        index=index,
        chunks=chunks,
        k=k
    )

    answer = generate_answer(query, context)

    return answer