from typing import List
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserResponse

class UserRepository():
    
    def create_user(self, db:Session, user:User) -> User:
        db.add(user)
        db.commit()
        db.refresh(user)
        
        return user
    
    def get_profile(self, db:Session, user_id:str) -> UserResponse:
        return db.query(User).filter(User.user_id==user_id).first()
    
    def get_user_by_email(self, db:Session, email:str) -> UserResponse:
        return db.query(User).filter(User.email==email).first()
    
    def get_all_users(self, db:Session) -> List[UserResponse]:
        return db.query(User).all()
    
    def get_user_by_id(self, db:Session, user_id:str) -> UserResponse:
        return db.query(User).filter(User.user_id==user_id).first()
    
           
        