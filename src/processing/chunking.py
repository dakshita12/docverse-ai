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
    Split cleaned text into overlapping chunks.

    Args:
        text: Cleaned document text.

    Returns:
        A list of text chunks.
    """

    if not text or not text.strip():
        return []

    return text_splitter.split_text(text)