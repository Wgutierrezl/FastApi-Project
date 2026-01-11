from sqlalchemy.orm import Session
from app.models.project import Project
from app.schemas.project import ProjectResponse


class ProjectRepository():
    
    def create_project(self, db:Session, project_data:Project) -> ProjectResponse:
        db.add(project_data)
        db.commit()
        db.refresh(project_data)
        
        return project_data

    def get_my_projects(self, db:Session, user_id:str):
        return db.query(Project).filter(Project.user_id==user_id).all()
    
    def get_projects_by_id(self, db:Session, project_id:int) -> Project:
        return db.query(Project).filter(Project.project_id==project_id).first()
        
    def delete_project(self, db:Session, project:Project):
        db.delete(project)
        db.commit()
    
    def get_all_project(self, db:Session):
        return db.query(Project).all()
        
    