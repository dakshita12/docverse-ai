import streamlit as st

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

st.divider()

st.header("📁 Uploaded Documents")
st.info("No documents uploaded yet.")
