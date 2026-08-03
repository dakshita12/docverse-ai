import fitz
from docx import Document
from pptx import Presentation

def read_pdf(file_path):
    """
    Reads a PDF file and returns its text.
    """
    document = fitz.open(file_path)

    text = ""

    for page in document:
        text += page.get_text()

    document.close()
    return text


def read_docx(file_path):
    """
    Reads a DOCX file and returns its text.
    """
    document = Document(file_path)

    text = "" 

    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"

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

    return text