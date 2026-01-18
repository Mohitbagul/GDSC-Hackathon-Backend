from bson import ObjectId
from app.core.database import appointment_collection, doctor_collection
from datetime import datetime


async def get_max_token_for_doctor_date(doctor_id: str, appointment_date: str):
    doc = await appointment_collection.find_one(
        {
            "doctor_id": doctor_id,
            "appointment_date": appointment_date
        },
        sort=[("token_number", -1)]
    )
    return doc["token_number"] if doc else None


async def create_appointment(data: dict) -> str:
    result = await appointment_collection.insert_one(data)
    return str(result.inserted_id)


async def get_appointments_for_doctor_date(
    hospital_id: str,
    doctor_id: str,
    appointment_date: str
):
    # Check if doctor_id is actually a user_id (from doctor login)
    doctor = await doctor_collection.find_one({"user_id": doctor_id})
    if doctor:
        actual_doctor_id = str(doctor["_id"])
    else:
        actual_doctor_id = doctor_id
    
    appointments = []
    cursor = appointment_collection.find(
        {
            "hospital_id": hospital_id,
            "doctor_id": actual_doctor_id,
            "appointment_date": appointment_date
        }
    ).sort("token_number", 1)

    async for appt in cursor:
        appt["id"] = str(appt["_id"])
        del appt["_id"]
        appointments.append(appt)

    return appointments


async def get_all_appointments(hospital_id: str = None):
    """Get all appointments, optionally filtered by hospital"""
    appointments = []
    query = {}
    if hospital_id:
        query["hospital_id"] = hospital_id
    
    cursor = appointment_collection.find(query).sort("appointment_date", -1)
    
    async for appt in cursor:
        appt["id"] = str(appt["_id"])
        del appt["_id"]
        appointments.append(appt)
    
    return appointments


async def get_appointments_by_patient(patient_id: str, hospital_id: str = None):
    """Get all appointments for a specific patient"""
    appointments = []
    query = {"patient_id": patient_id}
    if hospital_id:
        query["hospital_id"] = hospital_id
    
    cursor = appointment_collection.find(query).sort("appointment_date", -1)
    
    async for appt in cursor:
        appt["id"] = str(appt["_id"])
        del appt["_id"]
        appointments.append(appt)
    
    return appointments


async def get_appointments_by_doctor(doctor_id: str, hospital_id: str = None):
    """Get all appointments for a specific doctor"""
    # Check if doctor_id is actually a user_id (from doctor login)
    doctor = await doctor_collection.find_one({"user_id": doctor_id})
    if doctor:
        actual_doctor_id = str(doctor["_id"])
    else:
        actual_doctor_id = doctor_id
    
    appointments = []
    query = {"doctor_id": actual_doctor_id}
    if hospital_id:
        query["hospital_id"] = hospital_id
    
    cursor = appointment_collection.find(query).sort("appointment_date", -1)
    
    async for appt in cursor:
        appt["id"] = str(appt["_id"])
        del appt["_id"]
        appointments.append(appt)
    
    return appointments


async def get_appointments_by_date_range(start_date: str, end_date: str, hospital_id: str = None):
    """Get appointments within a date range"""
    appointments = []
    query = {
        "appointment_date": {
            "$gte": start_date,
            "$lte": end_date
        }
    }
    if hospital_id:
        query["hospital_id"] = hospital_id
    
    cursor = appointment_collection.find(query).sort("appointment_date", 1)
    
    async for appt in cursor:
        appt["id"] = str(appt["_id"])
        del appt["_id"]
        appointments.append(appt)
    
    return appointments


async def update_appointment(appointment_id: str, data: dict):
    """Update appointment with only non-null fields"""
    # Remove None values from the update data
    update_data = {k: v for k, v in data.items() if v is not None}
    
    if not update_data:
        return True
    
    result = await appointment_collection.update_one(
        {"_id": ObjectId(appointment_id)},
        {"$set": update_data}
    )
    return result.modified_count > 0


async def get_appointment_by_id(appointment_id: str):
    """Get a single appointment by ID"""
    appointment = await appointment_collection.find_one(
        {"_id": ObjectId(appointment_id)}
    )
    if appointment:
        appointment["id"] = str(appointment["_id"])
        del appointment["_id"]
    return appointment
