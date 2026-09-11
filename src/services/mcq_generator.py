from src.rag.llm import generate_response
from utils.prompts import MCQ_PROMPT


def generate_mcqs(context: str, count: int) -> str:
    if not context or not context.strip():
        raise ValueError("Study material cannot be empty.")

    if count <= 0:
        raise ValueError("MCQ count must be greater than zero.")

    prompt = MCQ_PROMPT.invoke(
        {
            "context": context,
            "count": count,
        }
    )

    return generate_response(prompt)