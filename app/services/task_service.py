from typing import List
from app.repositories.task_repository import TaskRespository
from app.schemas.task import TaskResponse, TaskCreated, TaskUpdated
from app.models.task import Task
from sqlalchemy.orm import Session
from datetime import datetime


class TaskService():
    
    def __init__(self, repo:TaskRespository):
        self._repo=repo
        
    
    def create_task(self, db:Session, data:TaskCreated, user_id:str) -> TaskResponse:
        task=Task(
            user_id=user_id,
            project_id=data.project_id,
            title=data.title,
            description=data.description,
            status='active'
        )
        
        task_created=self._repo.create_task(db, task)
        
        if task_created is None:
            return None
        
        return task_created
    
    def get_all_my_task(self, db:Session, user_id:str) -> List[TaskResponse]:
        response=self._repo.get_my_task(db, user_id)
        
        if not response:
            return None
        
        return response
    
    def get_all_task(self, db:Session) -> List[TaskResponse]:
        response=self._repo.get_all_task(db)
        
        if not response:
            return None
        
        return response
    
    
    def delete_task(self, db:Session, task_id:int) -> bool:
        task=self._repo.get_task_by_id(db, task_id)
        
        if not task:
            return False
        
        self._repo.delete_task_by_id(db, task)
        
        return True
    
    def update_task(self, db:Session, task_data:TaskUpdated, task_id:int) -> TaskResponse:
        task=self._repo.get_task_by_id(db, task_id)
        
        
        if task is None:
            return None
        
        task.title=task_data.title
        task.description=task_data.description
        
        task_updated=self._repo.update_task(db, task)
        
        if task_updated is None:
            return None
        
        return task_updated
        