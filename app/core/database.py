from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import MONGO_URI

client = AsyncIOMotorClient(MONGO_URI)

db = client.hospital_management_db

# Collections (optional explicit references)
hospital_collection = db.hospitals
user_collection = db.users
doctor_collection = db.doctors
receptionist_collection = db.receptionists
patient_collection = db.patients
appointment_collection = db.appointments
