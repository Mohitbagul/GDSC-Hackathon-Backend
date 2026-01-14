from pydantic import BaseModel
from typing import Optional


class DoctorCreate(BaseModel):
    email: str
    password: str
    full_name: str

    specialization: Optional[str] = None
    qualification: Optional[str] = None
    experience_years: Optional[int] = None
    consultation_fee: Optional[float] = None


class DoctorResponse(BaseModel):
    id: str
    full_name: str
    specialization: Optional[str]
    qualification: Optional[str]
    experience_years: Optional[int]
    consultation_fee: Optional[float]
    is_active: bool
