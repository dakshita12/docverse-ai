import streamlit as st

st.set_page_config(
    page_title="DocVerse AI",
    page_icon="📚",
    layout="wide"
)

st.title("📚 DocVerse AI")
st.subheader("Intelligent Study Workspace")

st.write(
    "An AI-powered workspace for organizing study materials "
    "and preparing for exams."
)

st.divider()

st.markdown("### 🚀 What you can do")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("#### 📄 Manage Documents")
    st.write(
        "Upload and process PDF, DOCX, and PPTX study materials "
        "with OCR support."
    )

with col2:
    st.markdown("#### 🤖 Ask AI")
    st.write(
        "Chat with your study materials using "
        "retrieval-augmented generation."
    )

with col3:
    st.markdown("#### 📚 Study Smarter")
    st.write(
        "Generate summaries, flashcards, MCQs, important questions, "
        "and smart notes."
    )

st.divider()

st.info(
    "👈 Use the sidebar to navigate through DocVerse AI."
)