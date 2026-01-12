from pydantic import BaseModel
from datetime import datetime

class TaskCreated(BaseModel):
    project_id:int
    title:str
    description:str

class TaskUpdated(BaseModel):
    title:str
    description:str
    
class TaskResponse(BaseModel):
    task_id:int
    user_id:str
    project_id:int  
    title:str
    description:str
    status:str
    date:datetime
    

    

    
    