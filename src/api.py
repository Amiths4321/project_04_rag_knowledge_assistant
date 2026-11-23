
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from src.rag_pipeline import answer_question
from src.vector_store import collection

app = FastAPI(
    title="RAG Knowledge Assistant API",
    description="Ask questions about indexed PDF documents.",
    version="1.0.0"
)


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "RAG Knowledge Assistant API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "indexed_chunks": collection.count()
    }


@app.post("/ask")
def ask_question(request: QuestionRequest):
    if not request.question.strip():
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty."
        )

    if collection.count() == 0:
        raise HTTPException(
            status_code=400,
            detail="No documents indexed. Index PDFs first."
        )

    try:
        result = answer_question(request.question)
        return result

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Question processing failed: {str(error)}"
        )
