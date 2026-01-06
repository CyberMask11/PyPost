from passlib.context import CryptContext

context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hashing(password: str) -> str:
    return context.hash(password)

def verify(password: str, hashed_pwd: str):
    return context.verify(password, hashed_pwd)