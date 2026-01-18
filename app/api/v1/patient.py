from fastapi import APIRouter, Depends
from app.schemas.patient import PatientCreate
from app.services.patient_service import (
    create_patient_service,
    get_patients_service
)
from app.core.dependencies import require_roles, get_current_user

router = APIRouter(
    prefix="/patients",
    tags=["Patients"]
)


@router.post("/", dependencies=[Depends(require_roles("RECEPTIONIST"))])
async def create_patient(
    payload: PatientCreate,
    current_user=Depends(get_current_user)
):
    patient_id = await create_patient_service(
        hospital_id=current_user["hospital_id"],
        data=payload.dict()
    )
    return {"patient_id": patient_id}


@router.get("/", dependencies=[Depends(require_roles("RECEPTIONIST", "DOCTOR","HOSPITAL_ADMIN"))])
async def list_patients(current_user=Depends(get_current_user)):
    return await get_patients_service(current_user["hospital_id"])
