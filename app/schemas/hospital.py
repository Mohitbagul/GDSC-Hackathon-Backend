from pydantic import BaseModel
from typing import Optional


class HospitalCreate(BaseModel):
    name: str
    address: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None


class HospitalResponse(BaseModel):
    id: str
    name: str
    address: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    is_active: bool
