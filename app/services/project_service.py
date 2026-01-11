from typing import List
from app.repositories.project_repository import ProjectRepository
from app.models.project import Project
from app.schemas.project import projectCreated, ProjectResponse
from sqlalchemy.orm import Session

class ProjectService():
    
    def __init__(self, projectRepository:ProjectRepository):
        self._repo=projectRepository
        
    
    def create_project(self, db:Session, data:projectCreated, user_id:str) -> ProjectResponse:
        project=Project(
            name=data.name,
            description=data.description,
            user_id=user_id
        )
        
        project_created=self._repo.create_project(db, project)
        
        if project_created is None:
            return None
        
        return project_created
    
    def get_projects_by_user_id(self, db:Session, user_id:str) -> List[ProjectResponse]:
        projects=self._repo.get_my_projects(db, user_id)
        
        if not projects:
            return None
        
        return projects
    
    def delete_project(self, db:Session, project_id:int) -> bool:
        project=self._repo.get_projects_by_id(db, project_id)
        
        if project is None:
            return False
        
        self._repo.delete_project(db, project)
        
        return True
    
    def get_all_projects(self, db:Session) -> List[ProjectResponse]:
        projects=self._repo.get_all_project(db)
        
        if not projects:
            return None
        
        return projects
            