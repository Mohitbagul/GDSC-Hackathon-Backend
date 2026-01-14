from fastapi import APIRouter, Depends
from app.schemas.hospital import HospitalCreate
from app.services.hospital_service import create_hospital_service
from app.core.dependencies import require_roles

router = APIRouter(
    prefix="/hospitals",
    tags=["Hospitals"]
)


@router.post("/", dependencies=[Depends(require_roles("SYSTEM_ADMIN"))])
async def create_hospital(payload: HospitalCreate):
    hospital_id = await create_hospital_service(payload.dict())
    return {"hospital_id": hospital_id}
