
from langchain_community.document_loaders import PyPDFLoader, TextLoader, Docx2txtLoader, UnstructuredExcelLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from vector_store import build_vector_store
from embeddings import embed_documents
from qa import answer_question
from typing import List
import os

SUPPORTED_EXTENSIONS = {".pdf", ".txt", ".docx", ".xlsx",".xls"}

# def load_documents(file_path:str):
#     loader = PyPDFLoader(file_path)
#     documents = loader.load()
#     return documents

def load_single_doc(file_path:str) -> List[Document]:
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".pdf":
        return PyPDFLoader(file_path).load()
    
    if ext == ".txt":
        return TextLoader(file_path).load()
    
    if ext == ".docx":
        return Docx2txtLoader(file_path).load()
    
    if ext in {".xlsx", ".xls"}:
        return UnstructuredExcelLoader(file_path).load()
    
    raise ValueError(f"Unsupported file extension: {ext}")

def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )
    chunks = splitter.split_documents(documents)
    return chunks



if __name__ == "__main__":
    docs = load_documents("data/sample.pdf")
    print(f"Loaded {len(docs)} pages")

    chunks = split_documents(docs)
    print(f"Created {len(chunks)} chunks")

    embeddings = embed_documents(chunks)
    print('*'*20)
    print(f"Generated {len(embeddings)} embeddings")
    print(f"Embedding Vector Length: {len(embeddings[0])}")
    print('*'*20)

    vector_store = build_vector_store(chunks)

    # query = "What is the document about?"
    # results = search_vector_store(vector_store, query)

    while True: 
        question = input("\nAsk a question (or type exit to quit):")
        if question.lower() =="exit":
            break

        answer = answer_question(vector_store, question)

        print(f"\nAnswer: {answer}")
    

    # print("\nTop Retrieved Chunks:\n")
    # for i,doc in enumerate(results, 1):
    #     print(f"------- Result {i} -------")
    #     print(doc.page_content[:500])

