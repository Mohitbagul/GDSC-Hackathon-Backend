from app.repositories.patient_repo import create_patient, get_patients_by_hospital


async def create_patient_service(hospital_id: str, data: dict):
    patient_data = {
        "hospital_id": hospital_id,
        "full_name": data["full_name"],
        "phone": data["phone"],
        "email": data.get("email"),
        "address": data.get("address"),
        "gender": data.get("gender"),
        "date_of_birth": data.get("date_of_birth"),
        "blood_group": data.get("blood_group"),
    }

    return await create_patient(patient_data)


async def get_patients_service(hospital_id: str):
    return await get_patients_by_hospital(hospital_id)
