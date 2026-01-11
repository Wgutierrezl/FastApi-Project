from pydantic import BaseModel

class Task(BaseModel):
    
    user_id:str
    project_id:str
    title:str
    description:str
    
    