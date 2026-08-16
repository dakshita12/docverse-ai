from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=CHUNK_SIZE,
    chunk_overlap=CHUNK_OVERLAP,
    separators=["\n\n", "\n", " ", ""],
)


def split_text(text: str) -> list[str]:
    """
    Split cleaned document text into overlapping chunks.

    Args:
        text: Cleaned document text.

    Returns:
        A list of text chunks.
    """

    if not text or not text.strip():
        return []

    return text_splitter.split_text(text)


def create_chunk_documents(
    text: str,
    source: str
) -> list[Document]:
    """
    Convert text chunks into LangChain Document objects with metadata.

    Args:
        text: Cleaned document text.
        source: Source document name.

    Returns:
        A list of LangChain Document objects.
    """

    chunks = split_text(text)

    documents = []

    for chunk_id, chunk in enumerate(chunks):
        document = Document(
            page_content=chunk,
            metadata={
                "source": source,
                "chunk_id": chunk_id,
            },
        )

        documents.append(document)

    return documents