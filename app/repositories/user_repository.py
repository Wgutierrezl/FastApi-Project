from sqlalchemy.orm import Session
from app.models.user import User

class UserRepository():
    
    def create_user(self, db:Session, user:User) -> User:
        db.add(user)
        db.commit()
        db.refresh(user)
        
        return user
    
    def get_profile(self, db:Session, user_id:str) -> User:
        return db.query(User).filter(User.user_id==user_id).first()
    
    def get_user_by_email(self, db:Session, email:str) -> User:
        return db.query(User).filter(User.email==email).first()
    
           
        