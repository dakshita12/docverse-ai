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


def remove_noise(text: str) -> str:
    """
    Remove common document extraction artifacts.
    """

    if not text:
        return ""

    text = re.sub(r"^[-=*_=]{3,}$", "", text, flags=re.MULTILINE)
    text = re.sub(r"\n{3,}", "\n\n", text)
    
    return text


def preprocess_text(text: str) -> str:
    """
    Run the complete text preprocessing pipeline.
    """

    text = clean_text(text)
    text = remove_noise(text)

    return text
