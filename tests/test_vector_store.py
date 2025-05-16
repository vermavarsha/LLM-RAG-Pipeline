from app.services.vector_store import store_documents, retrieve_similar_chunks

def test_store_and_retrieve():
    chunks = ["LangChain is amazing.", "FastAPI is great for APIs."]
    store_documents(chunks)
    results = retrieve_similar_chunks("What is LangChain?")
    assert any("LangChain" in doc.page_content for doc in results)
