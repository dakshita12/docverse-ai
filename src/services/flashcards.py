from src.rag.llm import generate_response
from utils.prompts import FLASHCARD_PROMPT


def generate_flashcards(context: str, count: int) -> str:
    if not context or not context.strip():
        raise ValueError("Study material cannot be empty.")

    if count <= 0:
        raise ValueError("Flashcard count must be greater than zero.")

    prompt = FLASHCARD_PROMPT.invoke(
        {
            "context": context,
            "count": count,
        }
    )

    return generate_response(prompt)