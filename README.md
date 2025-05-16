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
   ```bash
   git clone https://github.com/yourname/rag-pipeline.git
   cd rag-pipeline

Add your OpenAI key:

Set environment variable OPENAI_API_KEY.

Build and run:

bash
Copy
Edit
docker-compose up --build
📌 API Usage
Upload Document

bash
Copy
Edit
POST /upload
Form-data: file=<PDF file>
Query Document

bash
Copy
Edit
POST /query
Form-data: user_query=your question
Get Metadata

bash
Copy
Edit
GET /metadata
🔁 LLM Configuration
To switch between providers:

Replace ask_llm() in llm_client.py with other APIs like Gemini or HuggingFace.

Add required auth keys in docker-compose.yml.

✅ Testing
bash
Copy
Edit
pytest
