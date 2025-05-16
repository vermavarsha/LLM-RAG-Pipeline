from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OpenAIEmbeddings

persist_dir = "chroma_store"

def get_vector_store():
    return Chroma(
        persist_directory=persist_dir,
        embedding_function=OpenAIEmbeddings()
    )

def store_documents(text_chunks):
    vectordb = get_vector_store()
    vectordb.add_texts(text_chunks)
    vectordb.persist()

def retrieve_similar_chunks(query):
    vectordb = get_vector_store()
    return vectordb.similarity_search(query, k=3)
