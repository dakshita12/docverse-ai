import re

def clean_text(text: str) -> str:
    """
    Clean extracted document text by normalizing whitespaces.

    Args:
        text: Raw extracted text.

    Returns:
        Cleaned text ready for chunking.
    """

    if not text:
        return ""

    text = text.replace("\r\n", "\n")
    text = text.strip()
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text
