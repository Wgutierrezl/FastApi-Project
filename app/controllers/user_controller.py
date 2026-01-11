from fastapi import APIRouter, HTTPException, Depends, status
from app.schemas.user import UserCreated, UserResponse, LoginDTO, SessionDTO
from sqlalchemy.orm import Session
from app.dependencies import get_db_session
from app.security.jwt_dependency import current_user
from app.services.user_service import UserService
from app.repositories.user_repository import UserRepository
from app.security.hash_service import HashService
from app.security.token_service import TokenService

router=APIRouter(prefix='/users',
                 tags=['Users'])


service=UserService(repo=UserRepository(),
                    token=TokenService(), 
                    hass=HashService())


@router.post('/registerUser')
def register_user(data: UserCreated,
                  db:Session= Depends(get_db_session)) -> UserResponse: 
    try:
        user_created=service.create_user(db, data)
        if user_created is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='we didnt created the user'
            )
        
        return user_created
    
    except HTTPException as e:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=f"error {e}"
        )
    
    
@router.post('loginUser')
def login_user(data:LoginDTO,
               db:Session=Depends(get_db_session)) -> SessionDTO:
    try:
        user_log=service.login_user(db, data)
        
        if user_log is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='email or password incorrect'
            )
        return user_log
    
    except HTTPException as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"there was happened an error {e}"
        )