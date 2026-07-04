import jwt
import os
import dotenv


dotenv.load_dotenv("environment/.env")

class Utilities():
    def __init__(self):
        pass
    def validate_token(self, token):
        try:
            return jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=["HSA256"])
        except Exception as e:
            return {"error": e}
    
    def create_token(**kwargs):
        try:
            return jwt.encode(kwargs, os.getenv("SECRET_KEY"), algorithm="HSA256")
        except Exception as e:
            return {"error": e}