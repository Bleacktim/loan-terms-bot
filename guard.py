from gem import chat
import config

GUARD_PROMPT = """You are a strict topic gate for a bank Loan-Terms assistant.
The assistant may ONLY answer questions about: {scope}.

Categorize the user's input. Reply with exactly one word: ALLOW, REFUSE, or GREETING.

Rules:
- Basic conversational greetings ("hello", "hi", "salom", "qalesan", "qalaysiz", "привет") -> GREETING.
- Advice or opinions ("should I take this loan?") -> REFUSE.
- General knowledge, jokes, coding, other companies -> REFUSE.
- Factual questions about THIS product's terms -> ALLOW.

User input: {q}
Category (ALLOW, REFUSE, or GREETING):"""

def classify_input(question: str) -> str:
    out = chat(GUARD_PROMPT.format(scope=config.SCOPE, q=question)).strip().upper()
    if out.startswith("GREETING"):
        return "GREETING"
    if out.startswith("ALLOW"):
        return "ALLOW"
    return "REFUSE"
