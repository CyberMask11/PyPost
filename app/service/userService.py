from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.core.security.authHandler import AuthHandler
from app.core.security.encrypt import hashing, verify
from app.db.schema.schemas import UserCreate, UserLogin, UserOutput, UserToken
from app.db.repository.userRepo import UserRepo

class UserService:
    def __init__(self, session: Session):
        self.__userRepository = UserRepo(session=session)

    def signup(self, user_details: UserCreate) -> UserOutput:
        if self.__userRepository.user_exist_by_email(email=user_details.email):
            raise HTTPException(status_code=400, detail="This user already exists")
        
        hashed_pwd = hashing(user_details.password)
        user_details.password = hashed_pwd
        return self.__userRepository.create_user(userDetails=user_details)
    
    def login(self, user_details: UserLogin) -> UserToken:
        if not self.__userRepository.user_exist_by_email(email=user_details.email):
            raise HTTPException(status_code=404, detail="This user does not exist")
        
        user = self.__userRepository.get_user_by_email(email=user_details.email)
        verify_user = verify(user_details.password, user.password)

        if verify_user:
            token = AuthHandler.sign_jwt(user_id=user.id)
            if token:
                return UserToken(token=token)
            raise HTTPException(status_code=500, detail="Unable to generate token")
        raise HTTPException(status_code=400, detail="password is incorrect")
    
    def get_user(self, user_id: int):
        return self.__userRepository.get_user_by_id(user_id=user_id)
