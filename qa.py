from vector_store import search_vector_store
from llm import generate_answer


def answer_question(vector_store, question:str, k:int=3) -> str:
    docs = search_vector_store(vector_store, question, k=k)

    context = "\n\n".join(f"- {doc.page_content}" for doc in docs)

    answer = generate_answer(context, question)

    return answer