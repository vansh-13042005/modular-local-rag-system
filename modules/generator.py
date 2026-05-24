import ollama


def generate_answer(query: str, context: list[str]) -> str:
    context_text = "\n\n".join(context)

    prompt = f"""
You are a helpful AI assistant.

Use ONLY the provided context to answer the question.

If the answer is not present in the context, say:
"I could not find that information in the document."

Context:
{context_text}

Question:
{query}

Answer:
"""

    response = ollama.chat(
        model="tinyllama",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]