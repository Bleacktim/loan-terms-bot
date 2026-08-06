from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from pypdf import PdfReader
from gem import embed
import config

def load_chunks(pdf_path, size=900, overlap=150):
    """Read the PDF and cut each page into small overlapping pieces."""
    reader = PdfReader(pdf_path)
    chunks = []
    for page_no, page in enumerate(reader.pages, start=1):
        text = (page.extract_text() or "").strip()
        if not text:
            continue
        start = 0
        while start < len(text):
            piece = text[start:start + size]
            chunks.append({"text": piece, "page": page_no})
            start += size - overlap
    return chunks

def load_chunks_from_stream(file_stream, size=900, overlap=150):
    reader = PdfReader(file_stream)
    chunks = []
    for page_no, page in enumerate(reader.pages, start=1):
        text = (page.extract_text() or "").strip()
        if not text:
            continue
        start = 0
        while start < len(text):
            piece = text[start:start + size]
            chunks.append({"text": piece, "page": page_no})
            start += size - overlap
    return chunks

def ingest_pdf_stream(file_stream):
    chunks = load_chunks_from_stream(file_stream)
    dim = len(embed("dimension probe"))
    client = QdrantClient(path=config.QDRANT_PATH)
    client.recreate_collection(
        collection_name=config.COLLECTION,
        vectors_config=VectorParams(size=dim, distance=Distance.COSINE),
    )
    points = []
    for i, c in enumerate(chunks):
        points.append(PointStruct(
            id=i, vector=embed(c["text"]),
            payload={"text": c["text"], "page": c["page"]},
        ))
    client.upsert(collection_name=config.COLLECTION, points=points)

def main():
    chunks = load_chunks(config.PDF_PATH)
    print(f"Loaded {len(chunks)} chunks from {config.PDF_PATH}")

    # Ask the model its own vector size, so we never hard-code the wrong number.
    dim = len(embed("dimension probe"))
    print(f"Embedding size = {dim}")

    client = QdrantClient(path=config.QDRANT_PATH)
    client.recreate_collection(
        collection_name=config.COLLECTION,
        vectors_config=VectorParams(size=dim, distance=Distance.COSINE),
    )

    points = []
    for i, c in enumerate(chunks):
        points.append(PointStruct(
            id=i, vector=embed(c["text"]),
            payload={"text": c["text"], "page": c["page"]},
        ))
    client.upsert(collection_name=config.COLLECTION, points=points)
    print(f"Stored {len(points)} clauses in Qdrant. The document is ready.")

if __name__ == "__main__":
    main()
