
def chunk_documents(documents, chunk_size=500, overlap=100):
    """
    Split extracted document text into overlapping chunks.
    Preserve source and page metadata.
    """
    chunks = []

    for document in documents:
        text = document["text"]

        start = 0

        while start < len(text):
            end = start + chunk_size
            chunk_text = text[start:end].strip()

            if chunk_text:
                chunks.append({
                    "text": chunk_text,
                    "source": document["source"],
                    "page": document["page"]
                })

            start += chunk_size - overlap

    return chunks


if __name__ == "__main__":
    from src.document_loader import load_all_pdfs

    documents = load_all_pdfs()
    chunks = chunk_documents(documents)

    print("Total document pages:", len(documents))
    print("Total text chunks:", len(chunks))

    for index, chunk in enumerate(chunks[:3], start=1):
        print(f"\nChunk {index}")
        print("Source:", chunk["source"])
        print("Page:", chunk["page"])
        print("Text:", chunk["text"][:250])
