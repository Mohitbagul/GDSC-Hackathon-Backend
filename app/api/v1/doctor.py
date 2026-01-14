from fastapi import APIRouter, Depends
from app.schemas.doctor import DoctorCreate
from app.services.doctor_service import (
    create_doctor_service,
    get_doctors_service
)
from app.core.dependencies import require_roles, get_current_user

router = APIRouter(
    prefix="/doctors",
    tags=["Doctors"]
)


@router.post("/", dependencies=[Depends(require_roles("HOSPITAL_ADMIN"))])
async def create_doctor(
    payload: DoctorCreate,
    current_user=Depends(get_current_user)
):
    doctor_id = await create_doctor_service(
        hospital_id=current_user["hospital_id"],
        data=payload.dict()
    )
    return {"doctor_id": doctor_id}


@router.get("/", dependencies=[Depends(require_roles("HOSPITAL_ADMIN", "RECEPTIONIST"))])
async def list_doctors(current_user=Depends(get_current_user)):
    return await get_doctors_service(current_user["hospital_id"])
