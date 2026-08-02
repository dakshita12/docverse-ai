import streamlit as st
from src.services.workspace_manager import (
    save_uploaded_file,
    get_uploaded_documents,
    delete_document,
)

st.title("📂 Workspace")

st.write("Manage your study materials.")

st.divider()

st.header("⬆ Upload Document")
st.write("Upload your PDF, DOCX or PPTX files.")

# Upload Section
uploaded_file = st.file_uploader(
    label = "Choose a document",
    type=["pdf", "docx", "pptx"]
)

# Display selected files
if uploaded_file is not None:
    st.success("Document selected successfully !")
    st.subheader("📄 Selected File")
    st.write(f"**File Name:** {uploaded_file.name}")
    st.write(f"**File Type:** {uploaded_file.type}")
    file_size_mb = uploaded_file.size / (1024 * 1024)
    st.write(f"**File Size:** {file_size_mb: .2f} MB")

upload_button = st.button("📤 Upload Document")
if upload_button:
    if uploaded_file is not None:
        save_uploaded_file(uploaded_file)
        st.success("Document uploaded successfully")
        st.rerun()
    else:
        st.warning("Please select a document first")

st.divider()

st.header("📁 Uploaded Documents")
documents = get_uploaded_documents()

if documents:
    for document in documents:
        col1, col2 = st.columns([5,1])
        with col1:
            st.write(f"📄 {document}")
        with col2:
            if st.button("🗑️ Delete", key=document):
                if delete_document(document):
                    st.success(f"{document} deleted successfully!")
                    st.rerun()
else:
    st.info("No documents uploaded yet.")

