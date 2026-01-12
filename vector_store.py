from langchain_community.vectorstores import FAISS 
# from langchain_core.documents import Document
from embeddings import create_embedding_model

def build_vector_store(chunks):
    embedding_model = create_embedding_model()
    vector_store = FAISS.from_documents(chunks, embedding_model)
    return vector_store

def search_vector_store(vector_store, query, k=3):
    results = vector_store.similarity_search(query, k=k)
    return results


if __name__ == "__main__":
    print("Vector store module ready.")