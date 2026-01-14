class Receptionist:
    user_id: str                  # required
    hospital_id: str              # required
    full_name: str                # required

    shift_start: str | None = None
    shift_end: str | None = None
    is_active: bool = True
