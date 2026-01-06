from .base import BaseRepo
from app.db.model.models import User
from app.db.schema.schemas import UserCreate, UserOutput

class UserRepo(BaseRepo):
    #Adds signup data into database
    def create_user(self, userDetails: UserCreate) -> UserOutput:
        user = User(**userDetails.model_dump(exclude_none=True))

        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)

        return user
    
    def get_user_by_email(self, email: str) -> User:
        return self.session.query(User).filter_by(email=email).first() 
    
    def get_user_by_id(self, user_id: int) -> User:
        return self.session.query(User).filter_by(id=user_id).first()
    
    def user_exist_by_email(self, email: str) -> bool:
        user = self.session.query(User).filter_by(email=email).first()
        return bool(user)
