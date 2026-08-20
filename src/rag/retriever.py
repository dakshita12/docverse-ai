from src.rag.embeddings import EmbeddingService
from src.rag.vector_store import VectorStore


class Retriever:
    """Retrieve relevant document chunks using semantic similarity."""

    def __init__(
        self,
        embedding_service: EmbeddingService | None = None,
        vector_store: VectorStore | None = None,
    ):
        self.embedding_service = embedding_service or EmbeddingService()
        self.vector_store = vector_store or VectorStore()

    def search(
        self,
        query: str,
        top_k: int = 5,
        document_id: str | None = None,
    ):
        """
        Retrieve the top-k most relevant document chunks.

        Args:
            query: User's search query.
            top_k: Maximum number of results to retrieve.
            document_id: Optional document ID to restrict the search.

        Returns:
            A list of dictionaries containing:
            - text
            - metadata
            - distance
        """

        # Validate query
        if not query or not query.strip():
            raise ValueError("Query cannot be empty.")

        # Validate top_k
        if top_k <= 0:
            raise ValueError("top_k must be greater than zero.")

        # Validate document ID
        if document_id is not None and not document_id.strip():
            raise ValueError("Document ID cannot be empty.")

        # Generate embedding for the query
        query_embedding = self.embedding_service.embed_text(query)

        # Build metadata filter
        where_filter = None

        if document_id:
            where_filter = {
                "document_id": document_id
            }

        # Query ChromaDB
        results = self.vector_store.collection.query(
            query_embeddings=[query_embedding.tolist()],
            n_results=top_k,
            where=where_filter,
        )

        # Extract results
        documents = results.get("documents", [[]])[0]
        metadatas = results.get("metadatas", [[]])[0]
        distances = results.get("distances", [[]])[0]

        # Format results
        retrieved_results = []

        for document, metadata, distance in zip(
            documents,
            metadatas,
            distances,
        ):
            retrieved_results.append(
                {
                    "text": document,
                    "metadata": metadata,
                    "distance": distance,
                }
            )

        return retrieved_results