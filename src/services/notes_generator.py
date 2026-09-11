from src.rag.llm import generate_response
from utils.prompts import SMART_NOTES_PROMPT


def generate_smart_notes(context: str) -> str:
    if not context or not context.strip():
        raise ValueError("Study material cannot be empty.")

    prompt = SMART_NOTES_PROMPT.invoke(
        {
            "context": context
        }
    )

    return generate_response(prompt)