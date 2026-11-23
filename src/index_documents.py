
from src.document_loader import load_all_pdfs
from src.text_chunker import chunk_documents
from src.embedding_model import generate_embeddings
from src.vector_store import store_chunks


def index_documents():
    print("Loading PDFs...")
    documents = load_all_pdfs()

    if not documents:
        print("No PDF documents found in documents/.")
        return

    print("Creating text chunks...")
    chunks = chunk_documents(documents)

    if not chunks:
        print("No text chunks were generated.")
        return

    print("Generating embeddings...")
    texts = [chunk["text"] for chunk in chunks]
    embeddings = generate_embeddings(texts)

    print("Saving to ChromaDB...")
    stored = store_chunks(chunks, embeddings)

    print(f"Successfully indexed {stored} chunks.")


if __name__ == "__main__":
    index_documents()
