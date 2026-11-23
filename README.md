# Project 4 — RAG-Based Contract Knowledge Assistant

## Overview

An AI-powered document question-answering system built using Retrieval-Augmented Generation (RAG). It extracts information from PDF contracts, retrieves relevant passages using semantic search, and generates context-grounded answers using a locally hosted embedding model and remote Ollama inference.

## Features

- PDF document ingestion using PyMuPDF
- Text extraction and chunking
- Local semantic embeddings using Sentence Transformers
- Persistent vector storage using ChromaDB
- Semantic retrieval of relevant document passages
- AI-powered answers using Qwen 2.5 VL through Ollama
- Source document and page references
- Streamlit user interface
- FastAPI REST API
- Application logging
- Environment-variable configuration

## Technology Stack

- Python
- PyMuPDF
- Sentence Transformers
- ChromaDB
- Ollama
- Qwen 2.5 VL
- Streamlit
- FastAPI
- SQLite (reserved for future extension)

## Architecture

1. Load PDF documents.
2. Extract page-level text and metadata.
3. Split text into overlapping chunks.
4. Generate local embeddings.
5. Store chunks and vectors in ChromaDB.
6. Convert user questions into embeddings.
7. Retrieve relevant document passages.
8. Send retrieved context to the Ollama model.
9. Return the generated answer with source references.

## Project Structure

```text
project_04_rag_knowledge_assistant/
├── data/
│   ├── processed/
│   └── vector_db/
├── documents/
│   └── contracts/
├── reports/
│   └── logs/
├── src/
│   ├── app_logger.py
│   ├── api.py
│   ├── document_loader.py
│   ├── embedding_model.py
│   ├── evaluate_rag.py
│   ├── index_documents.py
│   ├── ollama_client.py
│   ├── rag_pipeline.py
│   ├── retriever.py
│   ├── text_chunker.py
│   └── vector_store.py
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Setup

Create and activate a virtual environment:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

Configure environment variables in `.env`:

```text
OLLAMA_URL=http://YOUR_OLLAMA_SERVER:11434
OLLAMA_MODEL=qwen2.5vl:latest
```

Place permitted PDF documents in `documents/contracts/`.

## Index Documents

```powershell
python -m src.index_documents
```

## Run the RAG Pipeline

```powershell
python -m src.rag_pipeline
```

## Run Streamlit

```powershell
streamlit run app.py
```

## Run FastAPI

```powershell
uvicorn src.api:app --reload --port 8001
```

API documentation:

`http://127.0.0.1:8001/docs`

## Evaluation

A basic keyword-based evaluation script is included:

```powershell
python -m src.evaluate_rag
```

This is an initial functional check, not a comprehensive benchmark of retrieval or answer accuracy.

## Security

- Server configuration is stored in `.env`.
- `.env` is excluded from Git.
- `.env.example` provides placeholder configuration.
- Local vector database and logs are excluded from Git.

## Current Limitations

- Retrieval quality depends on document chunking and embedding similarity.
- The evaluation script uses simple keyword matching.
- Scanned PDFs may require OCR support.
- Answers depend on the quality and completeness of retrieved passages.
- The prototype has not been validated for production or legal decision-making.

## Future Enhancements

- Hybrid search using keyword and semantic retrieval
- Reranking retrieved passages
- Improved chunking strategies
- OCR for scanned PDFs
- Conversation history
- User authentication
- Advanced RAG evaluation

## Learning Objectives

This project demonstrates practical AI Engineering concepts including document ingestion, embeddings, vector databases, semantic retrieval, LLM integration, API development, and RAG application deployment.