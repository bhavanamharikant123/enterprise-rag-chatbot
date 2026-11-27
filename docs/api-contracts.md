
# API Contract Design

Base URL: /api/v1

## Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| POST | /documents/upload | Upload PDFs |
| GET | /documents | List documents |
| DELETE | /documents/{document_id} | Delete document |
| POST | /chat | Ask questions |

## Chat Request

{
  "question": "How can employees apply for leave?",
  "session_id": "session_001"
}

## Chat Response

{
  "answer": "Submit requests through the HR portal.",
  "session_id": "session_001",
  "sources": [
    {
      "filename": "HR_Policy.pdf",
      "page": 1,
      "chunk_id": "hr_001"
    }
  ]
}

## Error Response

{
  "error": {
    "code": "INVALID_FILE_TYPE",
    "message": "Only PDF files are supported."
  }
}
