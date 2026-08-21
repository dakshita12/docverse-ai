import os
from dotenv import load_dotenv

load_dotenv()

TESSERACT_PATH = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")