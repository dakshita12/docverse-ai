from src.rag.llm import generate_response
from utils.prompts import IMPORTANT_QUESTIONS_PROMPT


def generate_important_questions(context: str, count: int) -> str:
    if not context or not context.strip():
        raise ValueError("Study material cannot be empty.")

    if count <= 0:
        raise ValueError("Question count must be greater than zero.")

    prompt = IMPORTANT_QUESTIONS_PROMPT.invoke(
        {
            "context": context,
            "count": count,
        }
    )

    return generate_response(prompt)