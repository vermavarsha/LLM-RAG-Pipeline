from fastapi import APIRouter, UploadFile, File, Form
from app.services.pdf_utils import extract_text_from_pdf, chunk_text
from app.services.vector_store import store_documents, retrieve_similar_chunks
from app.services.llm_client import ask_llm

# Import for metadata storage
from sqlalchemy.orm import sessionmaker
from app.models import engine, Document

router = APIRouter()

Session = sessionmaker(bind=engine)

@router.get("/")
async def root():
    return {"message": "RAG app API is running"}

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        text = extract_text_from_pdf(contents)
        chunks = chunk_text(text)
        store_documents(chunks)

        # Save metadata
        session = Session()
        session.add(Document(filename=file.filename, chunk_count=len(chunks)))
        session.commit()

        return {"message": f"Stored {len(chunks)} chunks"}
    except Exception as e:
        return {"error": str(e)}


@router.post("/query")
async def query_doc(user_query: str = Form(...)):
    chunks = retrieve_similar_chunks(user_query)
    context = "\n".join([doc.page_content for doc in chunks])
    prompt = f"Answer the question based on context:\n{context}\n\nQuestion: {user_query}"
    response = ask_llm(prompt)
    return {"answer": response}

@router.get("/metadata")
async def get_metadata():
    session = Session()
    docs = session.query(Document).all()
    return [
        {
            "filename": d.filename,
            "chunks": d.chunk_count,
            "uploaded": d.uploaded_at.isoformat()
        }
        for d in docs
    ]
    
