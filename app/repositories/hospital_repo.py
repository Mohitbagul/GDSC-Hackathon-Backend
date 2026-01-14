from bson import ObjectId
from app.core.database import hospital_collection


async def create_hospital(data: dict) -> str:
    result = await hospital_collection.insert_one(data)
    return str(result.inserted_id)


async def get_hospital_by_id(hospital_id: str):
    hospital = await hospital_collection.find_one(
        {"_id": ObjectId(hospital_id)}
    )
    if hospital:
        hospital["id"] = str(hospital["_id"])
        del hospital["_id"]
    return hospital
