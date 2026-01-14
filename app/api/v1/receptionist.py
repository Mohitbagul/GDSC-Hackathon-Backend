from fastapi import APIRouter, Depends
from app.schemas.receptionist import ReceptionistCreate
from app.services.receptionist_service import (
    create_receptionist_service,
    get_receptionists_service
)
from app.core.dependencies import require_roles, get_current_user

router = APIRouter(
    prefix="/receptionists",
    tags=["Receptionists"]
)


@router.post("/", dependencies=[Depends(require_roles("HOSPITAL_ADMIN"))])
async def create_receptionist(
    payload: ReceptionistCreate,
    current_user=Depends(get_current_user)
):
    receptionist_id = await create_receptionist_service(
        hospital_id=current_user["hospital_id"],
        data=payload.dict()
    )
    return {"receptionist_id": receptionist_id}


@router.get("/", dependencies=[Depends(require_roles("HOSPITAL_ADMIN"))])
async def list_receptionists(current_user=Depends(get_current_user)):
    return await get_receptionists_service(current_user["hospital_id"])
