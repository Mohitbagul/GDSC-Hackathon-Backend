from bson import ObjectId
from app.core.database import user_collection


async def get_user_by_email(email: str):
    return await user_collection.find_one({"email": email})


async def create_user(data: dict) -> str:
    result = await user_collection.insert_one(data)
    return str(result.inserted_id)


async def get_user_by_id(user_id: str):
    user = await user_collection.find_one({"_id": ObjectId(user_id)})
    if user:
        user["id"] = str(user["_id"])
        del user["_id"]
    return user
