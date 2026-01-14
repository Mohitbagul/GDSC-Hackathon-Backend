from bson import ObjectId
from app.core.database import doctor_collection


async def create_doctor(data: dict) -> str:
    result = await doctor_collection.insert_one(data)
    return str(result.inserted_id)


async def get_doctors_by_hospital(hospital_id: str):
    doctors = []
    cursor = doctor_collection.find({"hospital_id": hospital_id, "is_active": True})
    async for doc in cursor:
        doc["id"] = str(doc["_id"])
        del doc["_id"]
        doctors.append(doc)
    return doctors


async def get_doctor_by_id(doctor_id: str):
    doctor = await doctor_collection.find_one({"_id": ObjectId(doctor_id)})
    if doctor:
        doctor["id"] = str(doctor["_id"])
        del doctor["_id"]
    return doctor
