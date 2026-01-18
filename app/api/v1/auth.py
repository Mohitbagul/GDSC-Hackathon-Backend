from fastapi import APIRouter, HTTPException, status, Depends
from app.schemas.user import UserLogin, HospitalAdminCreate
from app.services.auth_service import login_user, register_hospital_admin
from app.core.dependencies import get_current_user

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


@router.post("/register-hospital-admin")
async def register_hospital_admin_route(payload: HospitalAdminCreate):
    result = await register_hospital_admin(
        payload.email,
        payload.password,
        payload.hospital_id
    )
    
    if result is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already exists or hospital not found"
        )
    
    return {
        "message": "Hospital admin registered successfully",
        "user_id": result["user_id"],
        "email": result["email"],
        "role": result["role"]
    }


@router.get("/me")
async def get_profile(current_user: dict = Depends(get_current_user)):
    return {
        "user_id": current_user.get("user_id"),
        "role": current_user.get("role"),
        "hospital_id": current_user.get("hospital_id")
    }
