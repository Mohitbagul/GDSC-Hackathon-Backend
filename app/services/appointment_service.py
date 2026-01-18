from app.repositories.appointment_repo import (
    create_appointment,
    get_max_token_for_doctor_date,
    get_appointments_for_doctor_date,
    get_all_appointments,
    get_appointments_by_patient,
    get_appointments_by_doctor,
    get_appointments_by_date_range,
    update_appointment,
    get_appointment_by_id
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


async def get_all_appointments_service(hospital_id: str = None):
    """Get all appointments"""
    return await get_all_appointments(hospital_id)


async def get_appointments_by_patient_service(patient_id: str, hospital_id: str = None):
    """Get all appointments for a patient"""
    return await get_appointments_by_patient(patient_id, hospital_id)


async def get_appointments_by_doctor_service(doctor_id: str, hospital_id: str = None):
    """Get all appointments for a doctor"""
    return await get_appointments_by_doctor(doctor_id, hospital_id)


async def get_appointments_by_date_range_service(start_date: str, end_date: str, hospital_id: str = None):
    """Get appointments within a date range"""
    return await get_appointments_by_date_range(start_date, end_date, hospital_id)


async def update_appointment_service(appointment_id: str, data: dict):
    """Update appointment with optional fields"""
    success = await update_appointment(appointment_id, data)
    if success:
        return await get_appointment_by_id(appointment_id)
    return None
