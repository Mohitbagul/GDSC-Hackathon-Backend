from pydantic import BaseModel


class UserLogin(BaseModel):
    email: str
    password: str


class UserCreate(BaseModel):
    email: str
    password: str
    role: str
    hospital_id: str


class HospitalAdminCreate(BaseModel):
    email: str
    password: str
    hospital_id: str
