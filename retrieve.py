from qdrant_client import QdrantClient
from gem import embed
import config

_client = QdrantClient(path=config.QDRANT_PATH)

def search(question: str, k: int = config.TOP_K):
    vec = embed(question)
    # Using query_points which is the modern method in qdrant-client 1.19+
    res = _client.query_points(collection_name=config.COLLECTION, query=vec, limit=k)
    return [{"text": h.payload["text"], "page": h.payload["page"]} for h in res.points]
