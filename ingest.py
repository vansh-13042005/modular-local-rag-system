from modules.loader import load_pdf
from modules.chunker import chunk_text
from modules.embedder import embed_chunks
from modules.vector_store import build_and_save

text = load_pdf("data/sample.pdf")
chunks = chunk_text(text, chunk_size=1000, overlap=150)
embeddings = embed_chunks(chunks)

build_and_save(embeddings, chunks)

print("Index built and saved")