class Doctor:
    user_id: str                  # required
    hospital_id: str              # required
    full_name: str                # required

    specialization: str | None = None
    qualification: str | None = None
    experience_years: int | None = None
    consultation_fee: float | None = None
    is_active: bool = True
