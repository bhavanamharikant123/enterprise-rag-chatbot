
# Component-Level Design

## API Layer
Handles HTTP requests and response validation.

## Core Layer
Manages configuration, logging and exceptions.

## Ingestion Layer
Loads PDFs, cleans text and creates chunks.

## Embeddings Layer
Generates vector representations.

## Retrieval Layer
Implements vector search, BM25, hybrid retrieval,
RRF and reranking.

## Generation Layer
Manages prompts and LLM answer generation.

## Memory Layer
Maintains conversation history.

## Evaluation Layer
Evaluates retrieval and generation quality.

## Services Layer
Coordinates document processing and chat workflows.

## Frontend
Provides document upload and conversational UI.

## Design Principles
- Separation of concerns
- Modularity
- Reusability
- Testability
- Maintainability
- Configuration-driven implementation
