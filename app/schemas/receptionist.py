from pydantic import BaseModel
from typing import Optional


class ReceptionistCreate(BaseModel):
    email: str
    password: str
    full_name: str

    shift_start: Optional[str] = None
    shift_end: Optional[str] = None


class ReceptionistResponse(BaseModel):
    id: str
    full_name: str
    shift_start: Optional[str]
    shift_end: Optional[str]
    is_active: bool
