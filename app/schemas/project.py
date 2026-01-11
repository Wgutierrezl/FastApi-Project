from pydantic import BaseModel

class projectCreated(BaseModel):
    
    name:str
    description:str
    
class ProjectResponse(BaseModel):
    project_id: int
    user_id:str
    name:str   
    description:str