from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials
from jose import jwt, JWTError
from app.security.token_service import TokenService


security=HTTPBearer()

def current_user(
    credentials:HTTPAuthorizationCredentials = Depends(security)
):
    token=credentials.credentials
    
    try:
        payload=jwt.decode(
            token,
            TokenService.SECRET_KEY,
            algorithms=[TokenService.ALGORITHM]
            
        )
        
        user_id=payload.get('user_id')
        
        if user_id is None:
            return HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail='token invalido'
            )
        
        return payload
    
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='token invalido o expirado'
        )        
    