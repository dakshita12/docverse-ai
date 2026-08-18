import chromadb


class VectorStore:
    """Manage document embeddings using ChromaDB."""


    def __init__(
        self,
        persist_directory: str = "data/chroma_db",
        collection_name: str = "docverse_documents",
    ):
        self.client = chromadb.PersistentClient(path=persist_directory)

        self.collection = self.client.get_or_create_collection(
            name=collection_name
        )


    def add_documents(
        self,
        documents: list[str],
        embeddings,
        metadatas: list[dict],
        ids: list[str],
    ):
        """Store documents, embeddings, metadata, and IDs in ChromaDB."""

        if not documents:
            raise ValueError("Documents cannot be empty.")

        if len(documents) != len(embeddings):
            raise ValueError(
                "Number of documents must match number of embeddings."
            )

        if len(documents) != len(metadatas):
            raise ValueError(
                "Number of documents must match number of metadata entries."
            )

        if len(documents) != len(ids):
            raise ValueError(
                "Number of documents must match number of IDs."
            )

        self.collection.add(
            documents=documents,
            embeddings=embeddings.tolist(),
            metadatas=metadatas,
            ids=ids,
        )


    def count(self) -> int:
        """Return the number of stored chunks."""
        return self.collection.count()
    

    def get_documents(self, limit: int = 10):
        """Return stored documents and metadata."""
        if limit <= 0:
            raise ValueError("Limit must be greater than zero.")

        return self.collection.get(limit=limit)
    

    def delete_by_document(self, document_id: str):
        """Delete all chunks belonging to a document."""

        if not document_id or not document_id.strip():
            raise ValueError("Document ID cannot be empty.")

        self.collection.delete(
            where={"document_id": document_id}
        )