import os
from dotenv import load_dotenv

load_dotenv()  # reads the .env file

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY or GEMINI_API_KEY == "your_api_key_here":
    raise RuntimeError("GEMINI_API_KEY is missing. Put the key from your mentor in .env.")

# --- the class proxy: ALL AI calls go through here ---
PROXY_BASE = "https://saidazam-litellm-proxy.hf.space/gemini"

# --- model names (the ONLY ones the proxy allows) ---
CHAT_MODEL  = "gemini-flash-lite"   # the thinking model (cheap workhorse)
EMBED_MODEL = "gemini-embedding"    # turns text into vectors

# --- storage (local, no signup, no server) ---
QDRANT_PATH = "qdrant_data"   # a folder on your laptop
COLLECTION  = "loan_terms"

# --- your document ---
PDF_PATH = "docs/loan_terms.pdf"
TOP_K    = 5                   # how many clauses to read per question

# --- THE ONE TOPIC this assistant is allowed to answer about ---
SCOPE = (
    "the terms and conditions of THIS specific bank loan / credit product: "
    "interest rate, fees, repayment schedule, penalties, eligibility, and "
    "what the contract does or does not include"
)
