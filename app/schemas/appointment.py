from pydantic import BaseModel
from typing import Optional


class AppointmentCreate(BaseModel):
    doctor_id: str
    patient_id: str
    appointment_date: str   # YYYY-MM-DD


class AppointmentResponse(BaseModel):
    id: str
    doctor_id: str
    patient_id: str
    appointment_date: str
    token_number: int
    status: str
