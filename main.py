from fastapi import FastAPI, Depends, Path
from contextlib import asynccontextmanager
from app.util.init_db import create_tables
from app.router.auth import route
from app.router.protected import get_current_user
from app.db.schema.schemas import UserOutput, PostOutput, PostCreate, PostUpdate
from fastapi.middleware.cors import CORSMiddleware
from app.service.postService import PostService
from app.core.database import get_db
from sqlalchemy.orm import Session
from uuid import UUID

asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield

app = FastAPI(lifespan=lifespan)
origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5500"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(route, tags=["Authentication"], prefix='/auth')


@app.post('/Createpost', status_code=201, response_model=PostOutput)
def CreatePost(
    postDetails: PostCreate,
    user: UserOutput = Depends(get_current_user),
    session: Session = Depends(get_db),
):
    return PostService(session=session).createPost(post_details=postDetails, user_id=user.id)

@app.delete('/Deletepost/{post_id}', status_code=204)
def DeletePost(
    post_id: UUID = Path(...),
    user: UserOutput = Depends(get_current_user),
    session: Session = Depends(get_db)
):
    return PostService(session=session).deletePost(PostId=post_id, userId=user.id)

@app.get('/posts', status_code=200, response_model=list[PostOutput])
def ReadPosts(
    user: UserOutput = Depends(get_current_user),
    session: Session = Depends(get_db)
):
    return PostService(session=session).readallPosts(UserId=user.id)

@app.get('/post/{title}', status_code=200, response_model=PostOutput)
def ReadPost(
    title: str,
    user: UserOutput = Depends(get_current_user),
    session: Session = Depends(get_db)
):
    return PostService(session=session).readPost(postTitle=title)

@app.get('/Posts', status_code=200, response_model=list[PostOutput])
def ReadEveryPost(
    user: UserOutput = Depends(get_current_user),
    session: Session = Depends(get_db)
):
    return PostService(session=session).readeveryPost()

@app.put('/UpdatePost/{post_id}', status_code=201, response_model=PostOutput)
def UpdatePost(
    details: PostUpdate,
    post_id: UUID = Path(...),
    user: UserOutput = Depends(get_current_user),
    session: Session = Depends(get_db)
):
    return PostService(session=session).updatePost(
        post_details=details,
        user_id=user.id,
        PostId=post_id
    )

