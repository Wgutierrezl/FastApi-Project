from sqlalchemy.orm import Session
from app.models.task import Task

class TaskRespository():
    
    def create_task(self, db:Session, task_data: Task):
        db.add(Task)
        db.commit()
        db.refresh()
        
        return task_data
    
    def get_my_task(self, db:Session, user_id:str):
        return db.query(Task).filter(Task.user_id==user_id).all()
    
    def get_all_task(self, db:Session):
        return db.query(Task).all()
    
    def delete_task_by_id(self, db:Session, task_data:Task):
        db.delete(task_data)
        db.commit()
    
    def update_task(self, db:Session, task_Updated: Task):
        db.commit()
        db.refresh(task_Updated)
        
        return task_Updated 