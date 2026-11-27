# Architecture Review – Enterprise RAG Chatbot

## 1. Purpose

This document consolidates the final architecture and technical decisions for the Enterprise RAG Chatbot.

## 2. Architecture Layers

1. Presentation Layer – Streamlit
2. API Layer – FastAPI
3. RAG Processing Layer – ingestion, embeddings, retrieval, reranking, generation, and memory
4. Storage Layer – ChromaDB, SQLite, and local filesystem
5. Monitoring and Evaluation – Python logging, LangSmith, RAGAS, and Pytest

## 3. Document Ingestion

PDF Upload → Validation → Document Registration → PDF Storage → Text Extraction → Cleaning → Chunking → Embeddings → ChromaDB → BM25 Index Update → Document Status Update

## 4. Question Answering

Question → API Validation → Conversation Context → Query Preparation → Hybrid Retrieval → Reciprocal Rank Fusion → Cross-Encoder Reranking → Context Construction → LLM Generation → Grounding Validation → Answer and Sources → Memory Update

## 5. Technology Stack

- Python
- FastAPI
- Streamlit
- LangChain
- OpenAI GPT-4o-mini
- OpenAI text-embedding-3-small
- PyMuPDF
- ChromaDB
- BM25
- Reciprocal Rank Fusion
- Sentence Transformers
- SQLite
- RAGAS
- LangSmith
- Pytest
- Docker
- Git and GitHub

## 6. Key Design Decisions

- Initial single-user implementation
- PDF-only ingestion
- Persistent ChromaDB collection
- SQLite document registry
- In-memory BM25 index
- In-memory conversation history
- Hybrid retrieval
- RRF-based ranking fusion
- Cross-encoder reranking
- Source-aware responses
- Modular application structure

## 7. Error Handling and Security

- Validate uploaded PDFs.
- Protect API credentials using environment variables.
- Use consistent error responses.
- Record ingestion failures.
- Apply bounded retries for temporary API errors.
- Track partial document deletion failures.
- Exclude confidential data from Git.

## 8. Future Enhancements

- Multi-user authentication and authorization
- Additional document formats
- Persistent conversation history
- LangGraph workflows
- Cloud deployment
- Distributed document processing
- Advanced monitoring and evaluation

## 9. Architecture Status

Phase 2 architecture and design decisions are finalized. Implementation will proceed in separate development phases.