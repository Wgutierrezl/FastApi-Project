from jose import jwt
from app.models.user import User
from datetime import datetime, timedelta

class TokenService():
    
    SECRET_KEY = "HH24qJLS/mRBsykjM9LG6e4qEOLoVOBkwbaQzRdZcM3XX3lK62mTYqGseMmrr16/24wUdOHEg+SxxNahr/RNaQ=="
    ALGORITHM = "HS256"
    EXPIRE_MINUTES = 60
    
    def create_token(self,user:User):
        payload={
            "user_id":user.user_id,
            "name":user.name,
            "email":user.email,
            "is_active":user.is_active,
            "exp": datetime.utcnow() + timedelta(minutes=self.EXPIRE_MINUTES)
        }
        
        return jwt.encode(
            payload,
            self.SECRET_KEY,
            algorithm=self.ALGORITHM
        )
        
        


