from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.hospital import HospitalCreate
from app.services.hospital_service import create_hospital_service, get_hospital_service, get_all_hospitals_service
from app.core.dependencies import require_roles

router = APIRouter(
    prefix="/hospitals",
    tags=["Hospitals"]
)


@router.post("/", dependencies=[Depends(require_roles("SYSTEM_ADMIN"))])
async def create_hospital(payload: HospitalCreate):
    hospital_id = await create_hospital_service(payload.dict())
    return {"hospital_id": hospital_id}


@router.get("/")
async def get_hospitals():
    hospitals = await get_all_hospitals_service()
    return hospitals


@router.get("/{hospital_id}")
async def get_hospital(hospital_id: str):
    hospital = await get_hospital_service(hospital_id)
    if not hospital:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Hospital not found"
        )
    return hospital
