from guard import is_in_scope
from retrieve import search
from answer import write_answer
from verify import is_grounded

REFUSAL = "I can only answer questions about this loan product's terms and conditions."

def ask(question: str) -> str:
    # STEP 1 - INPUT GUARD (security): is the question in scope?
    if not is_in_scope(question):
        return REFUSAL

    # STEP 2 - retrieve the real clauses from the PDF
    chunks = search(question)

    # STEP 3 - answer using ONLY those clauses
    draft = write_answer(question, chunks)

    # STEP 4 - OUTPUT GUARD (security): is the answer backed by the PDF?
    if not is_grounded(draft, chunks):
        return "I can't confirm this from the document."

    return draft

if __name__ == "__main__":
    tests = [
        "What is the late payment penalty?",   # in scope  -> answer + page
        "Write me a poem about the moon.",     # off topic -> refused
        "What is the interest rate on a car?", # maybe not in this PDF -> Not stated
    ]
    for q in tests:
        print(">", q)
        print(ask(q), "\n")
