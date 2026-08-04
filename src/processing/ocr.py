from pathlib import Path
import logging

import pytesseract 
from PIL import Image

from config import TESSERACT_PATH


logger = logging.getLogger(__name__)


class OCRProcessor:
    """
    Handles Optical Character Recognition (OCR) using the Tesseract OCR engine.
    """

    def __init__(self):
        """
        Configure the Tesseract executable path.
        """
        pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH


    def extract_text(self, image_path: str | Path) -> str:
        """
        Extract text from an image.

        Args:
            image_path: Path to the image file.

        Returns:
            Extracted text from the image.
        """

        image_path = Path(image_path)

        if not image_path.exists():
            raise FileNotFoundError(f"Image not found: {image_path}")

        logger.info(f"Extracting text from: {image_path}")

        try:
            with Image.open(image_path) as image:
                text = pytesseract.image_to_string(image)
            logger.info("Text extraction completed successfully.")
            return text.strip()

        except Exception as e:
            logger.exception(f"OCR failed for image: {image_path}")
            raise RuntimeError(
                f"Failed to extract text from {image_path}"
            ) from e
