import streamlit as st

from src.services.workspace_manager import get_uploaded_documents
from src.rag.retriever import Retriever
from src.services.summarizer import generate_summary
from src.services.flashcards import generate_flashcards
from src.services.mcq_generator import generate_mcqs
from src.services.important_questions import generate_important_questions
from src.services.notes_generator import generate_smart_notes


st.title("📚 Study Tools")

tool = st.selectbox(
    "Choose a tool",
    [
        "AI Summary",
        "Flashcards",
        "MCQs",
        "Important Questions",
        "Smart Notes",
    ]
)

st.divider()

documents = get_uploaded_documents()


if not documents:
    st.info("Please upload a document from the Workspace first.")


else:
    selected_document = st.selectbox(
        "Select a document",
        documents
    )


    # AI Summary
    if tool == "AI Summary":

        st.header("📑 AI Summary")

        if st.button("✨ Generate Summary"):

            with st.spinner("Generating summary..."):

                retriever = Retriever()

                results = retriever.search(
                    "Summarize the important topics and concepts in this document.",
                    top_k=30,
                    document_id=selected_document
                )

                context = "\n\n".join(
                    result["text"]
                    for result in results
                )

                summary = generate_summary(context)

            st.subheader("📌 Summary")
            st.write(summary)


    # Flashcards
    elif tool == "Flashcards":

        st.header("🃏 Flashcards")

        count = st.selectbox(
            "Number of flashcards",
            [5, 10, 15, 20]
        )

        if st.button("✨ Generate Flashcards"):

            with st.spinner("Generating flashcards..."):

                retriever = Retriever()

                results = retriever.search(
                    "Important concepts, definitions, facts, and technical terms.",
                    top_k=30,
                    document_id=selected_document
                )

                context = "\n\n".join(
                    result["text"]
                    for result in results
                )

                flashcards = generate_flashcards(
                    context,
                    count
                )

            st.subheader("🃏 Generated Flashcards")
            st.write(flashcards)


    # MCQs
    elif tool == "MCQs":

        st.header("📝 MCQs")

        count = st.selectbox(
            "Number of MCQs",
            [5, 10, 15, 20]
        )

        if st.button("✨ Generate MCQs"):

            with st.spinner("Generating MCQs..."):

                retriever = Retriever()

                results = retriever.search(
                    "Important concepts, definitions, facts, and technical terms.",
                    top_k=30,
                    document_id=selected_document
                )

                context = "\n\n".join(
                    result["text"]
                    for result in results
                )

                mcqs = generate_mcqs(
                    context,
                    count
                )

            st.subheader("📝 Generated MCQs")
            st.write(mcqs)


    # Important Questions
    elif tool == "Important Questions":

        st.header("❓ Important Questions")

        count = st.selectbox(
            "Number of questions",
            [5, 10, 15, 20]
        )

        if st.button("✨ Generate Important Questions"):

            with st.spinner("Generating important questions..."):

                retriever = Retriever()

                results = retriever.search(
                    "Important concepts, definitions, processes, comparisons, and technical topics.",
                    top_k=30,
                    document_id=selected_document
                )

                context = "\n\n".join(
                    result["text"]
                    for result in results
                )

                questions = generate_important_questions(
                    context,
                    count
                )

            st.subheader("❓ Generated Important Questions")
            st.write(questions)


    # Smart Notes
    elif tool == "Smart Notes":

        st.header("🗒️ Smart Notes")

        if st.button("✨ Generate Smart Notes"):

            with st.spinner("Generating smart notes..."):

                retriever = Retriever()

                results = retriever.search(
                    "Important concepts, definitions, processes, comparisons, and technical terms.",
                    top_k=30,
                    document_id=selected_document
                )

                context = "\n\n".join(
                    result["text"]
                    for result in results
                )

                notes = generate_smart_notes(context)

            st.subheader("🗒️ Generated Smart Notes")
            st.write(notes)