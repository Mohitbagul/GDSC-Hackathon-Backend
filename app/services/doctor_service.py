from app.repositories.doctor_repo import create_doctor, get_doctors_by_hospital
from app.repositories.user_repo import create_user
from app.utils.password import hash_password


async def create_doctor_service(hospital_id: str, data: dict):
    user_data = {
        "email": data["email"],
        "password": hash_password(data["password"]),
        "role": "DOCTOR",
        "hospital_id": hospital_id,
        "is_active": True
    }

    user_id = await create_user(user_data)

    doctor_data = {
        "user_id": user_id,
        "hospital_id": hospital_id,
        "full_name": data["full_name"],
        "specialization": data.get("specialization"),
        "qualification": data.get("qualification"),
        "experience_years": data.get("experience_years"),
        "consultation_fee": data.get("consultation_fee"),
        "is_active": True
    }

    return await create_doctor(doctor_data)


async def get_doctors_service(hospital_id: str):
    return await get_doctors_by_hospital(hospital_id)
