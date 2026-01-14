import os
from dotenv import load_dotenv

load_dotenv()

# MongoDB
MONGO_URI: str = os.getenv("MONGO_URI")

# JWT
JWT_SECRET: str = os.getenv("JWT_SECRET", "change-this-secret")
JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM", "HS256")
JWT_EXPIRE_MINUTES: int = int(os.getenv("JWT_EXPIRE_MINUTES", 60))

if not MONGO_URI:
    raise RuntimeError("MONGO_URI is not set in environment variables")
