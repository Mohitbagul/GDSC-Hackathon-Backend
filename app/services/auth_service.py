from app.repositories.user_repo import get_user_by_email
from app.utils.password import verify_password
from app.utils.token import create_access_token


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
