from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.core.database import Base

class Task(Base):
    
    __tablename__='tasks'
    
    task_id= Column(Integer, primary_key=True, autoincrement=True, index=True)
    project_id = Column(Integer, ForeignKey('projects.project_id'), nullable=False)
    user_id = Column(String, ForeignKey('users.user_id'), nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    status = Column(String, default='pending')
    date = Column(DateTime, default=DateTime.now)    