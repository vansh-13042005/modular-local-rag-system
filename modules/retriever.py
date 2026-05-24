def retrieve(query: str, model, index, chunks: list[str], k: int = 3) -> list[str]:
    query_vector = model.encode([query], convert_to_numpy=True).astype("float32")
    
    _, indices = index.search(query_vector, k)
    
    return [chunks[i] for i in indices[0] if i != -1]