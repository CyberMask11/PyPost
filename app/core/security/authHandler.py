import jwt
from decouple import config
import time

SECRET = config("JWT_SECRET")
ALGORITHM = config("JWT_ALGORITHM")

class AuthHandler:
    @staticmethod
    def sign_jwt(user_id: int):
        payload = {
            "user_id": user_id,
            "expires": time.time() + 900
        }

        token = jwt.encode(payload, SECRET, algorithm=ALGORITHM)
        return token
    
    @staticmethod
    def decode_jwt(token: str):
        try:
            decoded_token = jwt.decode(token, SECRET, algorithms=[ALGORITHM])
            return decoded_token if decoded_token["expires"] >= time.time() else None
        except:
            return None
        