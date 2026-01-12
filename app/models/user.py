from sqlalchemy import Column, Integer, String,Boolean
from uuid import uuid4
from app.core.database import Base

class User(Base):
    
    __tablename__='users'
    
    user_id = Column(String, primary_key=True,default=lambda:str(uuid4()))
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, nullable=False)
    role= Column(String, nullable=False)
    
    
    
    
    
    