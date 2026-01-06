import uuid
from sqlalchemy import Column, String, Integer
from app.core.database import Base
from sqlalchemy.dialects.postgresql import UUID

class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True)
    username = Column(String(120))
    password = Column(String(250))

class Upload(Base):
    __tablename__ = "Uploads"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    filename = Column(String(150))
    content_type = Column(String(100))
    user_id = Column(Integer)

class Post(Base):
    __tablename__ = "Posts"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String(100))
    content = Column(String(250))
    user_id = Column(Integer)