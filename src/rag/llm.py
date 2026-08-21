from langchain_google_genai import ChatGoogleGenerativeAI

from config import GEMINI_API_KEY


llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    google_api_key=GEMINI_API_KEY
)


def generate_response(prompt) -> str:
    """Generate a response from Gemini using the provided prompt."""

    try:
        response = llm.invoke(prompt)

        if isinstance(response.content, str):
            return response.content

        if isinstance(response.content, list):
            text_parts = []

            for block in response.content:
                if isinstance(block, dict) and block.get("type") == "text":
                    text_parts.append(block.get("text", ""))

            return "".join(text_parts)

        return str(response.content)

    except Exception as e:
        print(f"Gemini API error: {e}")
        return "Sorry, I was unable to generate a response. Please try again."