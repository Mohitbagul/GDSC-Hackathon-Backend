from fastapi import APIRouter, Depends, Query, HTTPException, status
from app.schemas.appointment import AppointmentCreate, AppointmentUpdate
from app.services.appointment_service import (
    create_appointment_service,
    get_doctor_appointments_service,
    get_all_appointments_service,
    get_appointments_by_patient_service,
    get_appointments_by_doctor_service,
    get_appointments_by_date_range_service,
    update_appointment_service
)
from app.core.dependencies import require_roles, get_current_user

router = APIRouter(
    prefix="/appointments",
    tags=["Appointments"]
)


@router.post("/")
async def create_appointment(
    payload: AppointmentCreate,
    current_user=Depends(require_roles("RECEPTIONIST"))
):
    appointment_id = await create_appointment_service(
        hospital_id=current_user["hospital_id"],
        receptionist_id=current_user["user_id"],
        data=payload.dict()
    )
    return {"appointment_id": appointment_id}


@router.get("/doctor/{doctor_id}")
async def get_doctor_appointments(
    doctor_id: str,
    appointment_date: str = Query(None),
    current_user=Depends(get_current_user)
):
    # Allow doctor to view their own appointments or allow hospital_admin to view any doctor's appointments
    if current_user.get("role") == "DOCTOR" and doctor_id != current_user.get("user_id"):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can only view your own appointments"
        )
    
    # Check if user has required role
    if current_user.get("role") not in ["DOCTOR", "HOSPITAL_ADMIN"]:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have permission to view appointments"
        )
    
    if appointment_date:
        return await get_doctor_appointments_service(
            hospital_id=current_user["hospital_id"],
            doctor_id=doctor_id,
            appointment_date=appointment_date
        )
    else:
        return await get_appointments_by_doctor_service(
            hospital_id=current_user["hospital_id"],
            doctor_id=doctor_id
        )


@router.get("/patient/{patient_id}", dependencies=[Depends(require_roles("PATIENT", "DOCTOR", "HOSPITAL_ADMIN"))])
async def get_appointments_by_patient(
    patient_id: str,
    current_user=Depends(get_current_user)
):
    """Get all appointments for a specific patient"""
    return await get_appointments_by_patient_service(
        patient_id=patient_id,
        hospital_id=current_user.get("hospital_id")
    )


@router.get("/")
async def get_all_appointments_route(
    start_date: str = Query(None),
    end_date: str = Query(None),
    current_user=Depends(get_current_user)
):
    """Get all appointments or filter by date range if start_date and end_date are provided"""
    if start_date and end_date:
        return await get_appointments_by_date_range_service(
            start_date=start_date,
            end_date=end_date,
            hospital_id=current_user.get("hospital_id")
        )
    return await get_all_appointments_service(
        hospital_id=current_user.get("hospital_id")
    )


@router.put("/{appointment_id}")
async def update_appointment(
    appointment_id: str,
    payload: AppointmentUpdate,
    current_user=Depends(require_roles("DOCTOR", "HOSPITAL_ADMIN","RECEPTIONIST"))
):
    """Update appointment with optional fields (status, prescription, note, etc.)"""
    updated_appointment = await update_appointment_service(
        appointment_id=appointment_id,
        data=payload.dict()
    )
    
    if not updated_appointment:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Appointment not found"
        )
    
    return updated_appointment
