
from pathlib import Path
import fitz  # PyMuPDF


DOCUMENTS_DIR = Path("documents/contracts")


def load_pdf(file_path):
    """Extract text and metadata from a PDF."""
    file_path = Path(file_path)
    documents = []

    pdf = fitz.open(file_path)

    for page_number, page in enumerate(pdf, start=1):
        text = page.get_text("text").strip()

        if text:
            documents.append({
                "text": text,
                "source": file_path.name,
                "page": page_number
            })

    pdf.close()
    return documents


def load_all_pdfs():
    """Load all PDFs from the documents directory."""
    all_documents = []

    for pdf_path in DOCUMENTS_DIR.glob("*.pdf"):
        all_documents.extend(load_pdf(pdf_path))

    return all_documents


if __name__ == "__main__":
    documents = load_all_pdfs()

    print(f"Total extracted pages: {len(documents)}")

    for document in documents[:3]:
        print("\nSource:", document["source"])
        print("Page:", document["page"])
        print("Text preview:", document["text"][:300])
