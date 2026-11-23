
from sentence_transformers import SentenceTransformer

MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"

_model = None


def get_embedding_model():
    """Load the embedding model once and reuse it."""
    global _model

    if _model is None:
        print("Loading embedding model...")
        _model = SentenceTransformer(MODEL_NAME)

    return _model


def generate_embeddings(texts):
    """Convert a list of text passages into embedding vectors."""
    model = get_embedding_model()

    embeddings = model.encode(
        texts,
        convert_to_numpy=True,
        show_progress_bar=True
    )

    return embeddings


if __name__ == "__main__":
    sample_texts = [
        "What are the payment terms?",
        "How can the agreement be terminated?",
        "What are the confidentiality obligations?"
    ]

    vectors = generate_embeddings(sample_texts)

    print("\nNumber of embeddings:", len(vectors))
    print("Embedding dimensions:", vectors.shape[1])
