class User:
    email: str                    # required
    password: str                 # required (hashed)
    role: str                     # required
    hospital_id: str              # required
    is_active: bool = True
