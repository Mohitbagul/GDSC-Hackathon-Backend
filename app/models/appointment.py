class Appointment:
    hospital_id: str              # required
    doctor_id: str                # required
    patient_id: str               # required
    appointment_date: str         # required (YYYY-MM-DD)
    token_number: int             # required

    status: str = "BOOKED"        # BOOKED / COMPLETED / CANCELLED
    created_by: str | None = None
