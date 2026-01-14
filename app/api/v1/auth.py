from fastapi import APIRouter, HTTPException, status
from app.schemas.user import UserLogin
from app.services.auth_service import login_user

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/login")
async def login(payload: UserLogin):
    token = await login_user(payload.email, payload.password)
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )
    return {
        "access_token": token,
        "token_type": "bearer"
    }
