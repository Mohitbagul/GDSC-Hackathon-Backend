class Patient:
    hospital_id: str              # required
    full_name: str                # required
    phone: str                    # required

    email: str | None = None
    address: str | None = None
    gender: str | None = None
    date_of_birth: str | None = None
    blood_group: str | None = None
    