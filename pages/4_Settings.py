import streamlit as st

st.title("⚙️ Settings")

st.subheader("AI Configuration")

st.write("**Model:** Gemini")
st.write("**Retrieval Context:** Top 30 chunks")

st.divider()

st.subheader("Document Processing")

st.write("**Chunk Size:** 1000")
st.write("**Chunk Overlap:** 200")

st.divider()

st.subheader("About DocVerse AI")

st.write(
    "DocVerse AI is an AI-powered study workspace that helps students work with their study materials and use AI-driven tools for learning, revision, and exam preparation."
)