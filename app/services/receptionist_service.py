from app.repositories.receptionist_repo import create_receptionist, get_receptionists_by_hospital
from app.repositories.user_repo import create_user
from app.utils.password import hash_password


async def create_receptionist_service(hospital_id: str, data: dict):
    user_data = {
        "email": data["email"],
        "password": hash_password(data["password"]),
        "role": "RECEPTIONIST",
        "hospital_id": hospital_id,
        "is_active": True
    }

    user_id = await create_user(user_data)

    receptionist_data = {
        "user_id": user_id,
        "hospital_id": hospital_id,
        "full_name": data["full_name"],
        "shift_start": data.get("shift_start"),
        "shift_end": data.get("shift_end"),
        "is_active": True
    }

    return await create_receptionist(receptionist_data)


async def get_receptionists_service(hospital_id: str):
    return await get_receptionists_by_hospital(hospital_id)
