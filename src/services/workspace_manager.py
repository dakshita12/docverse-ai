from pathlib import Path

from src.processing.document_loader import load_document
from src.processing.chunking import create_chunk_documents
from src.rag.embeddings import EmbeddingService
from src.rag.vector_store import VectorStore


UPLOAD_FOLDER = Path("data/uploads")


def save_uploaded_file(uploaded_file):
    """
    Saves and indexes an uploaded document.
    """

    UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)

    file_path = UPLOAD_FOLDER / uploaded_file.name

    # Save file
    with open(file_path, "wb") as file:
        file.write(uploaded_file.getbuffer())

    # Load document text
    text = load_document(file_path)

    # Split text into chunks
    chunks = create_chunk_documents(
        text,
        uploaded_file.name
    )

    # Add document ID to metadata
    for chunk in chunks:
        chunk.metadata["document_id"] = uploaded_file.name

    # Generate embeddings
    embedding_service = EmbeddingService()

    embeddings = embedding_service.embed_documents(
        [chunk.page_content for chunk in chunks]
    )

    # Store in ChromaDB
    vector_store = VectorStore()

    vector_store.add_documents(
        documents=[chunk.page_content for chunk in chunks],
        embeddings=embeddings,
        metadatas=[chunk.metadata for chunk in chunks],
        ids=[
            f"{uploaded_file.name}_{i}"
            for i in range(len(chunks))
        ],
    )

    return True


def get_uploaded_documents():
    """
    Returns a list of uploaded documents.
    """

    documents = []

    if not UPLOAD_FOLDER.exists():
        return documents

    for file in UPLOAD_FOLDER.iterdir():
        if file.is_file() and file.name != ".gitkeep":
            documents.append(file.name)

    return documents


def delete_document(filename):
    """
    Deletes a document from the uploads folder.
    """

    file_path = UPLOAD_FOLDER / filename

    if file_path.exists():
        file_path.unlink()
        return True

    return False