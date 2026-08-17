from sentence_transformers import SentenceTransformer


class EmbeddingService:
    """Generate embeddings for documents and queries."""

    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def embed_text(self, text: str):
        """Generate an embedding for a single text."""
        if not text or not text.strip():
            raise ValueError("Text cannot be empty.")

        return self.model.encode(text)

    def embed_documents(self, texts: list[str]):
        """Generate embeddings for multiple text chunks."""
        if not texts:
            raise ValueError("Document list cannot be empty.")

        return self.model.encode(texts)