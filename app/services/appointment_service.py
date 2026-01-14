from app.repositories.appointment_repo import (
    create_appointment,
    get_max_token_for_doctor_date,
    get_appointments_for_doctor_date
)


async def create_appointment_service(
    hospital_id: str,
    receptionist_id: str,
    data: dict
):
    max_token = await get_max_token_for_doctor_date(
        doctor_id=data["doctor_id"],
        appointment_date=data["appointment_date"]
    )

    token_number = (max_token or 0) + 1

    appointment_data = {
        "hospital_id": hospital_id,
        "doctor_id": data["doctor_id"],
        "patient_id": data["patient_id"],
        "appointment_date": data["appointment_date"],
        "token_number": token_number,
        "status": "BOOKED",
        "created_by": receptionist_id
    }

    return await create_appointment(appointment_data)


async def get_doctor_appointments_service(
    hospital_id: str,
    doctor_id: str,
    appointment_date: str
):
    return await get_appointments_for_doctor_date(
        hospital_id,
        doctor_id,
        appointment_date
    )
