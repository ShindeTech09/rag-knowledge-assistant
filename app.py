from fastapi import FastAPI
from contextlib import asynccontextmanager
from pydantic import BaseModel
from agent_graph import build_agent_graph
from ingest import load_documents, split_documents
from vector_store import build_vector_store
from agent_state import AgentState

app = FastAPI(title="RAG Knowledge Assistant")


vector_store = None
agent = None

class QuestionRequest(BaseModel):
    question:str


class AnswerResponse(BaseModel):
    answer:str


@asynccontextmanager
async def lifespan(app:FastAPI):
    # "Runs once the application starts up and once it shuts down."
    global vector_store
    global agent

    print("Initializing RAG system......")

    docs = load_documents("data/sample.pdf")

    chunks = split_documents(docs)

    vector_store = build_vector_store(chunks)

    agent = build_agent_graph(vector_store)

    print("RAG system is initialized and ready to use.")

    yield

    print("Shutting down RAG system...")

    vector_store = None


app = FastAPI(title="RAG Knowledge Assistant", lifespan=lifespan)

@app.post("/ask", response_model=AnswerResponse)
async def ask_question(request: QuestionRequest):
    result = await agent.ainvoke(AgentState(question=request.question)) 
    return {"answer": result["answer"]} 