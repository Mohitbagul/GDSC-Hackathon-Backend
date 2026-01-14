from bson import ObjectId
from app.core.database import receptionist_collection


async def create_receptionist(data: dict) -> str:
    result = await receptionist_collection.insert_one(data)
    return str(result.inserted_id)


async def get_receptionists_by_hospital(hospital_id: str):
    receptionists = []
    cursor = receptionist_collection.find(
        {"hospital_id": hospital_id, "is_active": True}
    )
    async for rec in cursor:
        rec["id"] = str(rec["_id"])
        del rec["_id"]
        receptionists.append(rec)
    return receptionists
