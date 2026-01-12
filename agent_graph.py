from langgraph.graph import StateGraph, END 
from functools import partial
from agent_state import AgentState
from agent_node import retrieval_node, generation_node


def build_agent_graph(vector_store):

    graph = StateGraph(AgentState)

    retrieve_node = partial(retrieval_node, vector_store=vector_store)

    graph.add_node("retrieve", retrieve_node)
    graph.add_node("generate", generation_node)

    graph.set_entry_point("retrieve")
    graph.add_edge("retrieve", "generate")
    graph.add_edge("generate", END)

    return graph.compile()