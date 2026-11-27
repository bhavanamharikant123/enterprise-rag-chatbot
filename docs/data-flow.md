
# Data Flow Design

## 1. Document Ingestion

1. User uploads PDF through Streamlit.
2. FastAPI validates the uploaded document.
3. Original PDF is stored in data/raw.
4. PyMuPDF extracts page-level text.
5. Text is cleaned.
6. Text is divided into overlapping chunks.
7. OpenAI generates embeddings.
8. Chunks, embeddings and metadata are stored in ChromaDB.

## 2. Question Answering

1. User submits a question.
2. Conversation history is considered.
3. The question is converted into an embedding.
4. Vector search and BM25 retrieve relevant chunks.
5. RRF combines retrieval rankings.
6. Cross-encoder reranks retrieved chunks.
7. Relevant context is constructed.
8. OpenAI generates a grounded answer.
9. Source citations are attached.
10. The response is returned to Streamlit.

## 3. Error Handling

The application should handle:

- Invalid PDF files.
- Empty documents.
- Extraction failures.
- Embedding API errors.
- Vector database errors.
- Retrieval failures.
- LLM API errors.
- Questions without relevant document context.

## 4. Design Decisions

- Single-user initial implementation.
- PDF-only ingestion.
- Persistent ChromaDB storage.
- Hybrid retrieval.
- Source and page-level citations.
- Modular backend architecture.
