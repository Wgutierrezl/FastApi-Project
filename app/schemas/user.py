from pydantic import BaseModel

class UserCreated(BaseModel):
    name:str
    email:str
    password:str
    
class UserResponse(BaseModel):
    user_id:str
    name:str
    email:str
    is_active:bool
    
class LoginDTO(BaseModel):
    email:str
    password:str

class SessionDTO(BaseModel):
    user_id:str
    name:str
    email:str   
    token:str
    
    