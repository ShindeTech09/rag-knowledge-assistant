from langchain_ollama import OllamaLLM

def get_llm():
    return OllamaLLM(model="llama3")


def generate_answer(context:str, question:str) -> str:

    llm = get_llm()

    prompt = f"""
You are a helpful AI assistant.
Answer the question using ONLY the context below.
If the answer is not present, say "I don't know".

Context:
{context}

Question:
{question}

Answer:
"""
    return llm.invoke(prompt)
