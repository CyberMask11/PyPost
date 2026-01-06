from .base import BaseRepo
from sqlalchemy.dialects.postgresql import UUID
from app.db.schema.schemas import PostCreate, PostUpdate
from app.db.model.models import Post

class PostRepo(BaseRepo):
    def create_post(self, postDetails: PostCreate):
        post = Post(**postDetails.model_dump())

        self.session.add(post)
        self.session.commit()
        self.session.refresh(post)

        return post
    
    def update_post(self, postDetails: PostUpdate, user_id: int, PostId: UUID) -> Post | None:
        post = self.session.query(Post).filter_by(id=PostId).first()
        if not post:
            return None
        
        if post.user_id != user_id:
            return None
        
        new_post = postDetails.model_dump(exclude_unset=True)

        for field, value in new_post.items():
            setattr(post, field, value)

        self.session.commit()
        self.session.refresh(post)

        return post
            
    
    def delete_post(self, post_id: UUID):
        post = self.session.query(Post).filter_by(id=post_id).first()
        if not post:
            return False

        self.session.delete(post)
        self.session.commit()

    def read_all_posts(self, userId: int) -> list[Post]:
        return self.session.query(Post).filter(Post.user_id==userId).all()
    
    def read_every_post(self) -> list[Post]:
        return self.session.query(Post).all()
    
    def read_post(self, title: str) -> Post | None:
        return self.session.query(Post).filter(Post.title==title).first()

    def get_post_by_id(self, post_id: UUID) -> Post:
        post = self.session.query(Post).filter_by(id=post_id).first()
        return post