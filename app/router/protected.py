from sqlalchemy.orm import Session
from app.service.userService import UserService
from app.core.database import get_db
from app.core.security.authHandler import AuthHandler
from typing import Annotated, Union
from fastapi import Header, status, HTTPException, Depends
from app.db.schema.schemas import UserOutput

AUTH_PREFIX = 'Bearer '

def get_current_user(
        session: Session = Depends(get_db),
        authorization: Annotated[Union[str, None], Header()] = None
) -> UserOutput:
    
    auth_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid token"
    )

    if not authorization:
        raise auth_exception
    
    if not authorization.startswith(AUTH_PREFIX):
        raise auth_exception
    
    payload = AuthHandler.decode_jwt(authorization[len(AUTH_PREFIX):])

    if payload and payload["user_id"]:
        user = UserService(session=session).get_user(user_id=payload["user_id"])
        return UserOutput(
            id=user.id,
            username=user.username
        )
    raise auth_exception