from src.rag.llm import generate_response
from utils.prompts import SUMMARY_PROMPT


def generate_summary(context: str) -> str:
    if not context or not context.strip():
        raise ValueError("Study material cannot be empty.")

    prompt = SUMMARY_PROMPT.invoke(
        {
            "context": context
        }
    )

    return generate_response(prompt)