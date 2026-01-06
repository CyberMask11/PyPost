from pydantic import BaseModel, EmailStr, Field
from uuid import UUID

class UserCreate(BaseModel):
    email: EmailStr
    username: str
    password: str

class PostCreate(BaseModel):
    title: str = Field(..., min_length=1)
    content: str = Field(..., min_length=1)
    user_id: int | None = None

class PostUpdate(BaseModel):
    title: str | None = Field(None, min_length=1)
    content: str | None = Field(None, min_length=1)
    user_id: int | None = None

class PostOutput(BaseModel):
    id: UUID
    title: str
    content: str

    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class UserOutput(BaseModel):
    id: int
    username: str

class UserToken(BaseModel):
    token: str

class Upload(BaseModel):
    filename: str
    content_type: str
    user_id: int

class ImgOutput(BaseModel):
    id: UUID
    filename: str

    class Config:
        from_attributes = True