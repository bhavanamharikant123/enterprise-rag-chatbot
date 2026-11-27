
# System Architecture

## Overview

The Enterprise RAG Chatbot follows a modular,
layered architecture.

## Architecture Layers

1. Presentation Layer - Streamlit
2. API Layer - FastAPI
3. RAG Processing Layer - Python and LangChain
4. Storage Layer - ChromaDB and Filesystem
5. Monitoring Layer - LangSmith and RAGAS

## Main Components

### Frontend
Responsible for document uploads and chat interaction.

### Backend
Exposes REST APIs and coordinates application services.

### Ingestion
Extracts PDF text and divides it into chunks.

### Embeddings
Converts document chunks into vector representations.

### Retrieval
Finds relevant information using vector and keyword search.

### Reranking
Improves the relevance ordering of retrieved chunks.

### Generation
Generates answers using retrieved document context.

### Storage
Persists document embeddings and original files.

### Monitoring
Tracks application execution and evaluates RAG quality.

## Design Principles

- Separation of concerns
- Modular architecture
- Reusable components
- Configurable application
- Testable services
- Single-user initial deployment
