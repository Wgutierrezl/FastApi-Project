from sqlalchemy.orm import Session
from app.models.project import Project


class ProjectRepository():
    
    def create_project(self, db:Session, project_data:Project):
        db.add(project_data)
        db.commit()
        db.refresh()
        
        return project_data

    def get_my_projects(self, db:Session, user_id:str):
        return db.query(Project).filter(Project.user_id==user_id).all()
    
    def delete_project(self, db:Session, project:Project):
        db.delete(project)
        db.commit()
    
    def get_all_project(self, db:Session):
        return db.query(Project).all()
        
    