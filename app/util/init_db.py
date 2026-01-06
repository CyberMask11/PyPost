from app.core.database import Base, engine
from app.db.model.models import User, Post

def create_tables():
    Base.metadata.create_all(engine)