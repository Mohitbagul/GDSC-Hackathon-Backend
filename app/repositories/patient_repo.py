from bson import ObjectId
from app.core.database import patient_collection


async def create_patient(data: dict) -> str:
    result = await patient_collection.insert_one(data)
    return str(result.inserted_id)


async def get_patients_by_hospital(hospital_id: str):
    patients = []
    cursor = patient_collection.find({"hospital_id": hospital_id})
    async for patient in cursor:
        patient["id"] = str(patient["_id"])
        del patient["_id"]
        patients.append(patient)
    return patients


async def get_patient_by_id(patient_id: str):
    patient = await patient_collection.find_one({"_id": ObjectId(patient_id)})
    if patient:
        patient["id"] = str(patient["_id"])
        del patient["_id"]
    return patient
