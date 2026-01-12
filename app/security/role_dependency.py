from app.models.user import User
from app.security.jwt_dependency import current_user
from fastapi import HTTPException, Depends, status


def require_roles(*roles:str):
    def role_checker(data:dict=Depends(current_user)):
        if data.get("role") not in roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You don't have permission to perform this action"
            )
        return data
    return role_checker
    
        