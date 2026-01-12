from langchain_ollama import OllamaEmbeddings
from dotenv import load_dotenv

load_dotenv()

def create_embedding_model():
    return OllamaEmbeddings(model="nomic-embed-text")


def embed_documents(chunks):
    embedding_model = create_embedding_model()
    texts = [chunk.page_content for chunk in chunks]
    embeddings = embedding_model.embed_documents(texts)
    return embeddings


if __name__ == "__main__":
    print("Embedding model ready.")