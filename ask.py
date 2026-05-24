from sentence_transformers import SentenceTransformer
from modules.vector_store import load
from modules.retriever import retrieve
from modules.generator import generate_answer

query = input("Ask something: ")

model = SentenceTransformer("all-MiniLM-L6-v2")

index, chunks = load()

context = retrieve(query, model, index, chunks, k=5)

answer = generate_answer(query, context)

print("\nAI Answer:\n")
print(answer)