from langchain_core.prompts import ChatPromptTemplate


RAG_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are DocVerse AI, an intelligent study assistant. "
            "Answer questions using the provided study material. "
            "If the answer cannot be found in the provided context, "
            "clearly say that the information is not available in the "
            "provided documents."
        ),
        (
            "human",
            "Context:\n{context}\n\n"
            "Question:\n{question}"
        ),
    ]
)