from typing import List
from app.repositories.user_repository import UserRepository
from app.security.hash_service import HashService
from app.security.token_service import TokenService
from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserResponse, UserCreated, LoginDTO, SessionDTO

class UserService():
    
    
    def __init__(self, repo:UserRepository, token:TokenService, hass:HashService):
        self._repo=repo
        self._token=token
        self._hash=hass
        
    def create_user(self, db:Session, data:UserCreated) -> UserResponse:
        hass_password=self._hash.hash_password(data.password)
        
        user=User(
            name=data.name,
            email=data.email,
            role=data.role,
            password=hass_password,
            is_active=True
        )
        
        created_user=self._repo.create_user(db, user)
        if created_user is None:
            return None
        
        return created_user
    
    def login_user(self, db:Session, data:LoginDTO) -> SessionDTO:
        user=self._repo.get_user_by_email(db,data.email)
        
        if user is None:
            return None
        
        if not self._hash.verify_password(data.password, user.password):
            return None
        
        return SessionDTO(
            user_id=user.user_id,
            name=user.name,
            email=user.email,
            token=self._token.create_token(user)
        )
    
    def get_user_by_id(self, db:Session, user_id:str) -> UserResponse:
        user=self._repo.get_profile(db, user_id)
        
        if not user:
            return None
        
        return user
    
    def get_all_users(self, db:Session) -> List[UserResponse]:
        users=self._repo.get_all_users(db)
        
        if not users:
            return None
        
        return users
    
    def get_user_by_id(self, db:Session, user_id:str) -> UserResponse:
        user=self._repo.get_user_by_id(db, user_id)
        
        if not user:
            return None
        
        return user
        
         