from modules.loader import load_pdf
from modules.chunker import chunk_text
from modules.embedder import embed_chunks
from modules.vector_store import build_and_save


CHUNK_SIZE = 1000
CHUNK_OVERLAP = 150


def load_and_chunk(pdf_path: str) -> list[str]:
    """
    Load PDF and split into chunks.
    """
    text = load_pdf(pdf_path)

    chunks = chunk_text(
        text,
        chunk_size=CHUNK_SIZE,
        overlap=CHUNK_OVERLAP
    )

    return chunks


def build_index(chunks: list[str]) -> None:
    """
    Generate embeddings and build FAISS index.
    """
    embeddings = embed_chunks(chunks)

    build_and_save(embeddings, chunks)


def run_ingestion(pdf_path: str) -> int:
    """
    Full ingestion pipeline.
    Returns number of chunks created.
    """
    chunks = load_and_chunk(pdf_path)

    build_index(chunks)

    return len(chunks)