import fitz
from docx import Document
from pptx import Presentation
from src.processing.text_processing import clean_text

def read_pdf(file_path):
    """
    Reads a PDF file and returns its text.
    """
    document = fitz.open(file_path)

    text = ""

    for page in document:
        text += page.get_text()

    document.close()
    text = clean_text(text)
    return text


def read_docx(file_path):
    """
    Reads a DOCX file and returns its text.
    """
    document = Document(file_path)

    text = "" 

    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"

    text = clean_text(text)
    return text


def read_pptx(file_path):
    """
    Reads a PPTX file and returns its text.
    """
    presentation = Presentation(file_path)

    text = ""

    for slide in presentation.slides:
        for shape in slide.shapes:
            if hasattr(shape, "text"):
                text += shape.text + "\n"

    text = clean_text(text)
    return text


def load_document(file_path):
    """
    Loads a document based on its file extension.
    """

    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    try:
        extension = file_path.suffix.lower()

        if extension == ".pdf":
            return read_pdf(file_path)

        elif extension == ".docx":
            return read_docx(file_path)

        elif extension == ".pptx":
            return read_pptx(file_path)

        raise ValueError(f"Unsupported file type: {extension}")

    except (FileNotFoundError, ValueError):
        raise 
    
    except Exception as e:
        raise RuntimeError(f"Error loading document: {e}")