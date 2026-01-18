from pydantic import BaseModel, field_validator
from typing import Optional, List, Union, Dict, Any
from enum import Enum


class StatusEnum(str, Enum):
    BOOKED = "BOOKED"
    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"


class PrescriptionItem(BaseModel):
    name: str
    dosage: str
    time: str


class AppointmentCreate(BaseModel):
    doctor_id: str
    patient_id: str
    appointment_date: str   # YYYY-MM-DD
    prescription: Optional[List[Union[str, PrescriptionItem, Dict[str, Any]]]] = None
    note: Optional[str] = None


class AppointmentUpdate(BaseModel):
    appointment_date: Optional[str] = None   # YYYY-MM-DD
    status: Optional[StatusEnum] = None              # BOOKED / COMPLETED / CANCELLED
    prescription: Optional[List[Union[str, PrescriptionItem, Dict[str, Any]]]] = None
    note: Optional[str] = None
    
    @field_validator('status', mode='before')
    def validate_status(cls, v):
        if v is None:
            return v
        if isinstance(v, str):
            v = v.upper()
        return v


class AppointmentResponse(BaseModel):
    id: str
    doctor_id: str
    patient_id: str
    appointment_date: str
    token_number: int
    status: str
    prescription: Optional[List[Union[str, Dict[str, Any]]]] = None
    note: Optional[str] = None
