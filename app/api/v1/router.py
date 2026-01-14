from fastapi import APIRouter

from app.api.v1 import auth
from app.api.v1 import hospital
from app.api.v1 import doctor
from app.api.v1 import receptionist
from app.api.v1 import patient
from app.api.v1 import appointment

router = APIRouter(prefix="/api/v1")

router.include_router(auth.router)
router.include_router(hospital.router)
router.include_router(doctor.router)
router.include_router(receptionist.router)
router.include_router(patient.router)
router.include_router(appointment.router)
