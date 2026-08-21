from src.rag.llm import generate_response
from utils.prompts import RAG_PROMPT


def generate_rag_response(context: str, question: str) -> str:
    """Generate an AI response using the provided context and question."""

    prompt = RAG_PROMPT.invoke(
        {
            "context": context,
            "question": question
        }
    )

    return generate_response(prompt)