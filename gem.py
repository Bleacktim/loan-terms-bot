import requests
import config

# Use standard OpenAI endpoints supported by LiteLLM proxy
PROXY_CHAT = "https://saidazam-litellm-proxy.hf.space/chat/completions"
PROXY_EMBED = "https://saidazam-litellm-proxy.hf.space/embeddings"

def chat(prompt: str) -> str:
    headers = {"Authorization": f"Bearer {config.GEMINI_API_KEY}", "Content-Type": "application/json"}
    data = {"model": config.CHAT_MODEL, "messages": [{"role": "user", "content": prompt}]}
    r = requests.post(PROXY_CHAT, headers=headers, json=data)
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"].strip()

def embed(text: str):
    headers = {"Authorization": f"Bearer {config.GEMINI_API_KEY}", "Content-Type": "application/json"}
    data = {"model": "gemini-embedding", "input": text}
    r = requests.post(PROXY_EMBED, headers=headers, json=data)
    r.raise_for_status()
    return r.json()["data"][0]["embedding"]

