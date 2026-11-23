
from src.embedding_model import generate_embeddings
from src.vector_store import search_chunks, collection


def retrieve_relevant_chunks(query, top_k=3):
    """Find document passages most relevant to a question."""

    if collection.count() == 0:
        print("Vector database is empty. Run indexing first.")
        return []

    query_embedding = generate_embeddings([query])[0]

    results = search_chunks(
        query_embedding=query_embedding,
        top_k=top_k
    )

    retrieved_chunks = []

    if results["documents"]:
        for text, metadata, distance in zip(
            results["documents"][0],
            results["metadatas"][0],
            results["distances"][0]
        ):
            retrieved_chunks.append({
                "text": text,
                "source": metadata["source"],
                "page": metadata["page"],
                "distance": distance
            })

    return retrieved_chunks


if __name__ == "__main__":
    question = input("Ask a question about your documents: ")

    chunks = retrieve_relevant_chunks(question)

    for index, chunk in enumerate(chunks, start=1):
        print(f"\nResult {index}")
        print("Source:", chunk["source"])
        print("Page:", chunk["page"])
        print("Distance:", round(chunk["distance"], 4))
        print("Text:", chunk["text"])
