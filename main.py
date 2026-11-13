from fastapi import FastAPI

app=FastAPI(
    title="Enterprise RAG Chatbot",
    description="Production-Ready Enterprise Document Intelligence Platform",
    version="0.1.0"
)

@app.get("/")
def root():
    return {
        "message": "Enterprise RAG Chatbot API is running",
        "status": "success"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "application": "Enterprise RAG Chatbot"
    }