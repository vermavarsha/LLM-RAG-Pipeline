# 📄 LLM-Powered RAG Pipeline

This project allows users to upload documents and ask questions about their content using a Retrieval-Augmented Generation (RAG) pipeline.

## 🚀 Features
- PDF upload & text chunking
- Vector DB (Chroma) for similarity search
- OpenAI LLM API for answers
- REST API using FastAPI
- Dockerized for easy deployment

## 🛠️ Setup Instructions

1. Clone the repo:
    git clone https://github.com/vermavarsha/LLM-RAG-Pipeline.git
    cd LLM-RAG-Pipeline
 
3. Add your OpenAI key:

   Set environment variable OPENAI_API_KEY.

4. Build and run:
   docker-compose up --build

📌 API Usage
Upload Document
   POST /upload
   Form-data: file=<PDF file>
Query Document
   POST /query
   Form-data: user_query=your question
Get Metadata
   GET /metadata

✅ Testing
Install dependencies locally or use Docker:
  pip install -r requirements.txt
  pytest
