from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from app.db.schema.schemas import UserCreate, UserLogin, UserOutput, UserToken
from app.service.userService import UserService
from app.core.database import get_db

route = APIRouter()

@route.post('/signup', status_code=201, response_model=UserOutput)
def signup(signupDetails: UserCreate, session: Session = Depends(get_db)) -> UserOutput:
    return UserService(session=session).signup(user_details=signupDetails)

@route.post('/login', status_code=200, response_model=UserToken)
def login(loginDetails: UserLogin, session: Session = Depends(get_db)) -> UserToken:
    return UserService(session=session).login(user_details=loginDetails)