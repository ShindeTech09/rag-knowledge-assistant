from pydantic import BaseModel

class AgentState(BaseModel):
    question:str
    context:str = ""
    answer:str = ""