from gem import chat

VERIFY_PROMPT = """Check if the ANSWER is fully supported by the CONTEXT.
Reply with exactly one word: GROUNDED or NOT_GROUNDED.
An answer that says "Not stated in the terms." is always GROUNDED.

CONTEXT:
{context}

ANSWER:
{answer}

Verdict:"""

def is_grounded(answer, chunks) -> bool:
    context = "\n\n".join(c["text"] for c in chunks)
    out = chat(VERIFY_PROMPT.format(context=context, answer=answer)).upper()
    return "NOT_GROUNDED" not in out
