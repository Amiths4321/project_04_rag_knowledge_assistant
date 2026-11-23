
import chromadb
from pathlib import Path

DB_PATH = Path("data/vector_db")

client = chromadb.PersistentClient(path=str(DB_PATH))

collection = client.get_or_create_collection(
    name="contract_knowledge",
    metadata={"hnsw:space": "cosine"}
)


def store_chunks(chunks, embeddings):
    """Replace existing records with the latest document chunks."""

    if len(chunks) != len(embeddings):
        raise ValueError("Chunks and embeddings count must match.")

    # Remove previous records to prevent stale document results.
    if collection.count() > 0:
        existing = collection.get()
        if existing["ids"]:
            collection.delete(ids=existing["ids"])

    if not chunks:
        return 0

    collection.add(
        ids=[f"chunk_{i}" for i in range(len(chunks))],
        documents=[chunk["text"] for chunk in chunks],
        embeddings=embeddings.tolist(),
        metadatas=[
            {
                "source": chunk["source"],
                "page": chunk["page"]
            }
            for chunk in chunks
        ]
    )

    return len(chunks)


def search_chunks(query_embedding, top_k=3):
    """Retrieve the most relevant chunks for a query."""

    count = collection.count()

    if count == 0:
        return {
            "documents": [[]],
            "metadatas": [[]],
            "distances": [[]]
        }

    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=min(top_k, count)
    )

    return results
