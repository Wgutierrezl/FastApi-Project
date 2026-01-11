from pydantic import BaseModel

class project(BaseModel):
    
    user_id:str
    name:str
    description:str