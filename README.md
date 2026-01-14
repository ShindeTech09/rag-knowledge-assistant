# 📚 RAG Knowledge Assistant (AI Agent)

A **production-grade Retrieval-Augmented Generation (RAG) Knowledge Assistant** built using **Python, Ollama, FAISS, LangGraph, and FastAPI**.  
This system enables **accurate, document-grounded Q&A** over heterogeneous data sources such as **PDF, DOCX, TXT, and Excel files**, using a clean **AI agent orchestration architecture**.

---

## 🚀 Key Features

- 📄 **Multi-Document Support** — PDF, DOCX, TXT, XLS/XLSX  
- 🧠 **RAG Pipeline** — Prevents hallucinations by grounding answers in documents  
- 🔎 **Semantic Search** — FAISS vector database for meaning-based retrieval  
- 🤖 **AI Agent Architecture** — LangGraph-based deterministic agent workflow  
- ⚡ **Local LLMs** — Ollama (no API keys, private, cost-free)  
- 🌐 **FastAPI Backend** — Async, scalable REST API  
- 🧩 **Extensible Design** — Ready for multi-agent, tools, and observability  

---

## 🏗️ High-Level Architecture

```
Documents (PDF / DOCX / TXT / Excel)
        ↓
Document Ingestion & Chunking
        ↓
Embeddings (Ollama – nomic-embed-text)
        ↓
Vector Store (FAISS)
        ↓
Semantic Retrieval
        ↓
LLM Generation (Ollama – llama3)
        ↓
LangGraph Agent Orchestration
        ↓
FastAPI REST Endpoint
```

---

## 🧠 Why RAG?

Traditional LLMs answer questions based only on training data, which can cause:
- ❌ Hallucinations  
- ❌ Outdated or incorrect answers  
- ❌ No control over knowledge sources  

This project uses **Retrieval-Augmented Generation (RAG)** to ensure:
- ✅ Answers are grounded in your documents  
- ✅ Higher accuracy and reliability  
- ✅ Enterprise-ready AI behavior  

---

## 🧑‍🚀 Agent Design (LangGraph)

The system is modeled as an **AI Agent** using **LangGraph**, represented as a state machine:

```
START
  ↓
Retrieve Relevant Context (FAISS)
  ↓
Generate Answer (LLM)
  ↓
END
```

### Agent State (Pydantic)

```python
class AgentState(BaseModel):
    question: str
    context: str = ""
    answer: str = ""
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|-----|-----------|
| Language | Python |
| API Framework | FastAPI |
| Agent Orchestration | LangGraph |
| LLM Runtime | Ollama |
| Embeddings Model | nomic-embed-text |
| Chat Model | llama3 |
| Vector Database | FAISS |
| Document Processing | LangChain |
| Server | Uvicorn |

---

## 📂 Project Structure

```
rag-knowledge-assistant/
│
├── app.py               # FastAPI entry point
├── ingest.py            # Multi-format document ingestion
├── embeddings.py        # Ollama embeddings
├── vector_store.py      # FAISS vector database
├── llm.py               # Ollama LLM wrapper
├── qa.py                # RAG Q&A logic
├── agent_state.py       # Agent state (Pydantic)
├── agent_nodes.py       # LangGraph nodes
├── agent_graph.py       # LangGraph workflow
│
├── data/                # Input documents
└── README.md
```

---

## ⚙️ Setup Instructions

### Install Ollama
https://ollama.com

```bash
ollama pull nomic-embed-text
ollama pull llama3
```

### Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install fastapi uvicorn langchain langchain-community faiss-cpu docx2txt unstructured openpyxl pandas langgraph
```

### Run API

```bash
uvicorn app:app --reload
```

Open:
http://127.0.0.1:8000/docs

---

## 🎯 Use Cases

- Internal knowledge assistant  
- SOP and policy Q&A  
- Onboarding automation  
- Enterprise document search  

---

## 👤 Author

Built by **Pawan Ashok Shinde**  
AI Agent Engineer | Python | LangGraph | RAG
