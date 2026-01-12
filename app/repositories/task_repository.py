from typing import List
from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.task import TaskResponse

class TaskRespository():
    
    def create_task(self, db:Session, task_data: Task) -> TaskResponse:
        db.add(task_data)
        db.commit()
        db.refresh(task_data)
        
        return task_data
    
    def get_my_task(self, db:Session, user_id:str) -> List[TaskResponse]:
        return db.query(Task).filter(Task.user_id==user_id).all()
    
    def get_all_task(self, db:Session) -> List[TaskResponse]:
        return db.query(Task).all()
    
    def delete_task_by_id(self, db:Session, task_data:Task):
        db.delete(task_data)
        db.commit()
    
    def update_task(self, db:Session, task_Updated: Task) -> TaskResponse:
        db.commit()
        db.refresh(task_Updated)
        
        return task_Updated 
        
    def get_task_by_id(self, db:Session, task_id:int) -> TaskResponse:
        return db.query(Task).filter(Task.task_id==task_id).first()
        
        