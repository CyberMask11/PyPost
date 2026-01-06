from sqlalchemy.orm import Session
from app.db.repository.postRepo import PostRepo
from app.db.schema.schemas import PostCreate, PostOutput, PostUpdate
from fastapi import HTTPException
from sqlalchemy.dialects.postgresql import UUID

class PostService:
    def __init__(self, session: Session):
        self.__postRepository = PostRepo(session=session)
    
    def createPost(self, post_details: PostCreate, user_id: int) -> PostOutput:        
        post_details.user_id = user_id
        return self.__postRepository.create_post(postDetails=post_details)
    
    def updatePost(self, post_details: PostUpdate, user_id: int, PostId: UUID) -> PostOutput:
        post_details.user_id = user_id
        return self.__postRepository.update_post(
            postDetails=post_details,
            PostId=PostId,
            user_id=user_id
        )

    def deletePost(self, PostId: UUID, userId: int): #Gets PostId from frontend
        post = self.__postRepository.get_post_by_id(post_id=PostId)

        if post.user_id == userId:
            return self.__postRepository.delete_post(post_id=PostId)
        raise HTTPException(status_code=401, detail="Your not allowed to delete this post")
    
    def readPost(self, postTitle: str) -> PostOutput:
        post = self.__postRepository.read_post(title=postTitle)
        if not post:
            raise HTTPException(status_code=404, detail="Post not found")
        return post
    
    def readeveryPost(self) -> list[PostOutput]:
        return self.__postRepository.read_every_post()
    
    def readallPosts(self, UserId: int) -> list[PostOutput]:
        return self.__postRepository.read_all_posts(userId=UserId)