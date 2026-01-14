from bson import ObjectId
from app.core.database import appointment_collection


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
    appointments = []
    cursor = appointment_collection.find(
        {
            "hospital_id": hospital_id,
            "doctor_id": doctor_id,
            "appointment_date": appointment_date
        }
    ).sort("token_number", 1)

    async for appt in cursor:
        appt["id"] = str(appt["_id"])
        del appt["_id"]
        appointments.append(appt)

    return appointments
