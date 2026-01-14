from fastapi import APIRouter, Depends
from app.schemas.appointment import AppointmentCreate
from app.services.appointment_service import (
    create_appointment_service,
    get_doctor_appointments_service
)
from app.core.dependencies import require_roles, get_current_user

router = APIRouter(
    prefix="/appointments",
    tags=["Appointments"]
)


@router.post("/", dependencies=[Depends(require_roles("RECEPTIONIST"))])
async def create_appointment(
    payload: AppointmentCreate,
    current_user=Depends(get_current_user)
):
    appointment_id = await create_appointment_service(
        hospital_id=current_user["hospital_id"],
        receptionist_id=current_user["user_id"],
        data=payload.dict()
    )
    return {"appointment_id": appointment_id}


@router.get("/doctor/{doctor_id}", dependencies=[Depends(require_roles("DOCTOR"))])
async def get_doctor_appointments(
    doctor_id: str,
    appointment_date: str,
    current_user=Depends(get_current_user)
):
    return await get_doctor_appointments_service(
        hospital_id=current_user["hospital_id"],
        doctor_id=doctor_id,
        appointment_date=appointment_date
    )
