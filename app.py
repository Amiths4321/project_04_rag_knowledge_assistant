
import streamlit as st

from src.rag_pipeline import answer_question
from src.index_documents import index_documents
from src.vector_store import collection


st.set_page_config(
    page_title="RAG Knowledge Assistant",
    page_icon="📚",
    layout="wide"
)

st.title("📚 RAG Knowledge Assistant")
st.write("Ask questions about your indexed PDF documents.")

# Sidebar
with st.sidebar:
    st.header("Document Management")

    st.write(f"Indexed chunks: {collection.count()}")

    if st.button("Index PDF Documents"):
        with st.spinner("Processing documents and generating embeddings..."):
            try:
                index_documents()
                st.success("Documents indexed successfully!")
                st.rerun()
            except Exception as error:
                st.error(f"Indexing failed: {error}")

# Question input
question = st.text_area(
    "Enter your question",
    placeholder="What are the termination conditions in the agreement?"
)

if st.button("Ask Question", type="primary"):
    if not question.strip():
        st.warning("Please enter a question.")
    elif collection.count() == 0:
        st.warning("Please index your PDF documents first.")
    else:
        with st.spinner("Searching documents and generating answer..."):
            try:
                result = answer_question(question)

                st.subheader("Answer")
                st.write(result["answer"])

                st.subheader("Sources")

                for source in result["sources"]:
                    st.write(
                        f"- {source['source']} | Page {source['page']}"
                    )

            except Exception as error:
                st.error(f"Unable to answer question: {error}")

st.divider()
st.caption("Powered by ChromaDB, Sentence Transformers and Ollama")
