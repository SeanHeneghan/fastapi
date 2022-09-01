from pydantic import BaseModel

class ToDo(BaseModel):
    id: int
    task: str
    
    class Config:
        orm_mode = True
    
class ToDoCreate(BaseModel):
    task: str