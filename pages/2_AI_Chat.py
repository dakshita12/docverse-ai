import streamlit as st

from src.rag.retriever import Retriever
from src.rag.rag_pipeline import generate_rag_response


st.title("AI Chat")

st.write("Chat with your study documents")


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


# Chat input
user_input = st.chat_input("Ask something about your documents...")


if user_input:

    # Add user message to history
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Display user message
    with st.chat_message("user"):
        st.write(user_input)

    # Retrieve relevant document chunks
    retriever = Retriever()

    results = retriever.search(
        user_input,
        top_k=5
    )

    # Combine retrieved chunks into context
    context = "\n\n".join(
        result["text"]
        for result in results
    )

    # Generate AI response
    assistant_response = generate_rag_response(
        context=context,
        question=user_input
    )

    # Add AI response to history
    st.session_state.messages.append({
        "role": "assistant",
        "content": assistant_response
    })

    # Display AI response
    with st.chat_message("assistant"):
        st.write(assistant_response)