# Storage Design – Enterprise RAG Chatbot

## 1. Overview

The application uses multiple storage mechanisms to manage original documents, document metadata, vector embeddings, and conversational history.

## 2. Storage Technologies

| Technology | Responsibility |
|---|---|
| Local File System | Store original PDF documents |
| ChromaDB | Store document chunks, embeddings, and chunk metadata |
| SQLite | Maintain document registry and processing status |
| In-Memory Storage | Maintain BM25 index and conversation history |

## 3. Document Storage

Original PDF files are stored in `data/raw/`.

Each uploaded document receives a unique document ID. The ID is included in the stored filename to prevent filename collisions.

## 4. Vector Database

ChromaDB uses a persistent collection named `enterprise_documents`.

Each chunk contains:
- Unique chunk ID
- Document text
- Embedding vector
- Document ID
- Original filename
- Page number
- Chunk index

A single collection is used for all uploaded documents. Document-level filtering is performed using metadata.

## 5. Document Metadata Database

SQLite stores document-level information.

The `documents` table contains:
- document_id
- filename
- stored_path
- content_hash
- status
- chunk_count
- created_at
- updated_at
- error_message

SQLite is used for document listing, duplicate detection, processing status, and document management.

## 6. BM25 Index

The BM25 index is initially maintained in memory and rebuilt from stored document chunks when the application starts.

## 7. Conversation Memory

Conversation history is maintained in memory for the initial single-user implementation.

Conversation history is not persistent and is cleared when the application restarts.

## 8. Document Lifecycle

Documents follow these statuses:

- uploaded
- processing
- processed
- failed
- deleting

## 9. Duplicate Detection

SHA-256 content hashing is used to identify identical uploaded files and prevent duplicate ingestion.

## 10. Data Deletion

Document deletion removes associated ChromaDB chunks, the original PDF, and the SQLite registry entry. The BM25 index is then refreshed.

## 11. Security and Backup

- API keys and environment variables are excluded from Git.
- Original enterprise documents are not committed to GitHub.
- Vector database files and local metadata databases are excluded from Git.
- Backups should preserve consistency between source documents, metadata, and vector storage.

## 12. Future Improvements

- Persistent conversation history
- Managed database for larger deployments
- Cloud object storage
- Automated backup and recovery
- Multi-user document isolation and access control