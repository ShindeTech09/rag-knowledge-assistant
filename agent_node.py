from typing import cast
from agent_state import AgentState
from vector_store import search_vector_store
from llm import generate_answer


def retrieval_node(state: AgentState, vector_store) -> AgentState:

    docs = search_vector_store(vector_store,state.question, k=3)

    context = "\n\n".join(doc.page_content for doc in docs)

    return AgentState(question=state.question, context=context, answer=state.answer)


def generation_node(state: AgentState) -> AgentState:

    answer = generate_answer(context=state.context, question=state.question)

    return AgentState(question=state.question, context=state.context, answer=answer)