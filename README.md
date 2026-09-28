# 📚 DocVerse AI — Intelligent AI Study Workspace

**AI-Powered Study Platform for Document Management, RAG-Based Document Chat, Smart Revision, & Exam Preparation**

---

## 📌 Project Overview

**DocVerse AI** is an AI-powered study workspace designed to help students organize their study materials and use AI-driven tools for learning, revision, and exam preparation.

The platform supports **PDF, DOCX, and PPTX documents**, including OCR-based processing for scanned PDF documents. Uploaded materials are processed, cleaned, divided into smaller chunks, converted into semantic embeddings, and stored in **ChromaDB** for retrieval.

DocVerse AI uses a **Retrieval-Augmented Generation (RAG)** pipeline to retrieve relevant content from uploaded study materials and provide it as context to **Google Gemini** for generating context-aware responses.

In addition to document-based AI chat, DocVerse AI provides dedicated study tools for generating **summaries, smart notes, flashcards, MCQs, and important questions**.

---

## 🔄 System Workflow

```text
                  ┌──────────────────────┐
                  │   Study Materials    │
                  │  PDF / DOCX / PPTX   │
                  └──────────┬───────────┘
                             │
                             ▼
                  ┌───────────────────────┐
                  │ Document Processing   │
                  │ Text Extraction / OCR │
                  │ Cleaning & Chunking   │
                  └──────────┬────────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │ Semantic Embeddings  │
                  │ Sentence Transformers│
                  └──────────┬───────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │      ChromaDB        │
                  │    Vector Storage    │
                  └──────────┬───────────┘
                             │
                             ▼
                  ┌──────────────────────┐
                  │ Relevant Context     │
                  │      Retrieval       │
                  └──────────┬───────────┘
                             │
                 ┌───────────┴───────────┐
                 ▼                       ▼
        ┌──────────────────┐    ┌──────────────────┐
        │     AI Chat      │    │   Study Tools    │
        │      + RAG       │    │                  │
        └────────┬─────────┘    │ Summary          │
                 │              │ Smart Notes      │
                 │              │ Flashcards       │
                 │              │ MCQs             │
                 │              │ Important Qs     │
                 │              └────────┬─────────┘
                 └──────────────┬────────┘
                                ▼
                     ┌────────────────────┐
                     │    Google Gemini   │
                     │   AI Generation    │
                     └────────────────────┘
```

---

## ✨ Key Features

- 📄 **Multi-Format Document Support:** Upload and process PDF, DOCX, and PPTX study materials.
- 🔍 **OCR for Scanned Documents:** Automatically use OCR when a PDF page contains insufficient extractable text.
- 🧹 **Document Processing Pipeline:** Extract, clean, and split document content into manageable chunks for retrieval.
- 🧠 **Semantic Embeddings:** Generate document embeddings using the all-MiniLM-L6-v2 Sentence Transformer model.
- 🗄️ **Vector Storage with ChromaDB:** Store document embeddings and metadata in a persistent local vector database.
- 🤖 **RAG-Based AI Chat:** Ask questions about uploaded study materials and receive responses based on retrieved document context.
- 📚 **Document-Specific Chat:** Select a particular document when working with multiple uploaded study materials.
- 📑 **AI Summary Generation:** Generate concise, exam-oriented summaries containing important concepts and key points.
- 🗒️ **Smart Notes:** Convert study material into structured revision notes with headings and bullet points.
- 🃏 **Flashcard Generation:** Generate question-and-answer flashcards based on the uploaded study material.
- 📝 **MCQ Generation:** Generate multiple-choice questions with options, correct answers, and explanations.
- ❓ **Important Question Generation:** Generate exam-oriented questions focused on important concepts, definitions, processes, comparisons, and technical topics.
- 📖 **Multiple Document Support:** Upload and work with multiple study materials within the same workspace.

---

## 💻 Technology Stack

| **Layer**                | **Technologies Used**                             |
| ------------------------ | ------------------------------------------------- |
| **Frontend & UI**        | Streamlit                                         |
| **Programming Language** | Python                                            |
| **Document Processing**  | PyMuPDF, python-docx, python-pptx                 |
| **OCR**                  | Tesseract OCR, Pytesseract, Pillow                |
| **Text Processing**      | LangChain Text Splitters                          |
| **Embeddings**           | Sentence Transformers (`all-MiniLM-L6-v2`)        |
| **Vector Database**      | ChromaDB                                          |
| **LLM**                  | Google Gemini 3.6 Flash                           |
| **AI Integration**       | LangChain, LangChain Core, LangChain Google GenAI |
| **Configuration**        | Python-dotenv                                     |
| **Development**          | VS Code, Git, GitHub                              |

---

## 📂 Project Structure

```text

DocVerseAI/
├── DocVerse_AI.py              # Main Streamlit application
├── config.py                   # Environment and API configuration
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore rules
├── README.md                   # Project documentation
│
├── pages/
│   ├── 1_Workspace.py          # Document upload and workspace
│   ├── 2_AI_Chat.py            # RAG-based document chat
│   ├── 3_Study_Tools.py        # AI-powered study tools
│   └── 4_Settings.py           # Application settings
│
├── src/
│   ├── processing/
│   │   ├── chunking.py         # Document chunking
│   │   ├── document_loader.py  # PDF/DOCX/PPTX loading
│   │   ├── ocr.py              # OCR processing
│   │   └── text_processing.py  # Text cleaning
│   │
│   ├── rag/
│   │   ├── embeddings.py       # Embedding generation
│   │   ├── llm.py              # Gemini integration
│   │   ├── rag_pipeline.py     # RAG response generation
│   │   ├── retriever.py        # Relevant context retrieval
│   │   └── vector_store.py     # ChromaDB integration
│   │
│   └── services/
│       ├── workspace_manager.py
│       ├── summarizer.py
│       ├── flashcards.py
│       ├── mcq_generator.py
│       ├── important_questions.py
│       └── notes_generator.py
│
├── utils/
│   ├── __init__.py
│   └── prompts.py              # AI prompts
│
├── data/
│   ├── uploads/                # Uploaded study documents
│   └── chroma_db/              # Local ChromaDB storage
│
└── logs/                       # Application logs

```

---

## 🚀 Quickstart Installation Guide

### 1. Clone the Repository
```bash
git clone <repository-url>
cd DocVerseAI
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
```
Activate the environment on Windows:
```bash
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure the Gemini API
Create a `.env` file in the project root:
```env
GEMINI_API_KEY=your_api_key_here
```

> **Note:** Never commit your `.env` file or expose your Gemini API key publicly.

### 5. Run DocVerse AI
```bash
streamlit run DocVerse_AI.py
```

The application will open in your browser.

---

## 🧪 Application Workflow

**1. Upload Study Materials**
Upload PDF, DOCX, or PPTX files through the Workspace.

**2. Process Documents**
DocVerse AI extracts the document content, applies OCR when required, cleans the extracted text, and divides it into chunks.

**3. Generate Embeddings**
Each document chunk is converted into a semantic vector using Sentence Transformers.

**4. Store Embeddings**
The generated embeddings and document metadata are stored in the local ChromaDB vector store.

**5. Chat with Documents**
Select a specific document or use all available documents in AI Chat.
The system retrieves relevant document chunks and provides them as context to Google Gemini.

**6. Generate Study Material**
Use Study Tools to generate:

- AI Summaries
- Smart Notes
- Flashcards
- MCQs
- Important Questions

---

## 🛠️ Future Improvements

- User authentication
- Subject-based study workspaces
- Cloud-based document storage
- Improved RAG evaluation
- Enhanced document organization
- Additional AI-powered learning features

---

## 🏷️ Recommended GitHub Meta

**Short Description:**
AI-powered study workspace with RAG-based document chat, semantic retrieval, and AI-driven exam preparation tools.

**Topics:**
`python`
`streamlit`
`langchain`
`generative-ai`
`rag`
`nlp`
`chromadb`
`sentence-transformers`
`gemini`
`ai`
`study-assistant`
`document-chat` 
`exam-preparation`

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---