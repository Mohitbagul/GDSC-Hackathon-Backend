from app.repositories.user_repo import get_user_by_email, create_user
from app.repositories.hospital_repo import get_hospital_by_id
from app.utils.password import verify_password, hash_password
from app.utils.token import create_access_token
from app.utils.constants import HOSPITAL_ADMIN


async def login_user(email: str, password: str) -> str | None:
    user = await get_user_by_email(email)
    if not user:
        return None

    if not verify_password(password, user["password"]):
        return None

    token_payload = {
        "user_id": str(user["_id"]),
        "role": user["role"],
        "hospital_id": user["hospital_id"]
    }

    return create_access_token(token_payload)


async def register_hospital_admin(email: str, password: str, hospital_id: str) -> dict | None:
    # Check if user already exists
    existing_user = await get_user_by_email(email)
    if existing_user:
        return None
    
    # Check if hospital exists
    hospital = await get_hospital_by_id(hospital_id)
    if not hospital:
        return None
    
    # Create hospital admin user
    user_data = {
        "email": email,
        "password": hash_password(password),
        "role": HOSPITAL_ADMIN,
        "hospital_id": hospital_id,
        "is_active": True
    }
    
    user_id = await create_user(user_data)
    return {"user_id": user_id, "email": email, "role": HOSPITAL_ADMIN}
