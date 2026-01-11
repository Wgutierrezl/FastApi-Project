from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base


class Project(Base):
    
    __tablename__='projects'
    
    project_id = Column(Integer, autoincrement=True, index=True, nullable=False, primary_key=True)
    user_id = Column(String, ForeignKey('users.user_id'), nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)