from pydantic import BaseModel
from typing import Optional


class PatientCreate(BaseModel):
    full_name: str
    phone: str

    email: Optional[str] = None
    address: Optional[str] = None
    gender: Optional[str] = None
    date_of_birth: Optional[str] = None
    blood_group: Optional[str] = None


class PatientResponse(BaseModel):
    id: str
    full_name: str
    phone: str
    email: Optional[str]
    address: Optional[str]
