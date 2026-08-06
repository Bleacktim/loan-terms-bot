from gem import chat

ANSWER_PROMPT = """You answer questions about a bank loan's Terms & Conditions.
Use ONLY the context below. Do not use outside knowledge.

If the answer is NOT clearly in the context, reply exactly:
"Not stated in the terms."

When you do answer, quote the exact number / fee / rule and add the page, e.g. (p. 3).

Context:
{context}

Question: {q}
Answer:"""

def write_answer(question, chunks):
    context = "\n\n".join(f"[p. {c['page']}] {c['text']}" for c in chunks)
    return chat(ANSWER_PROMPT.format(context=context, q=question))
