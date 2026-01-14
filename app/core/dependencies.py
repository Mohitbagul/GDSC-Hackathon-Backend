from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError

from app.core.security import oauth2_scheme
from app.core.config import JWT_SECRET, JWT_ALGORITHM


def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:
    """
    Decodes JWT and returns payload:
    {
        user_id,
        role,
        hospital_id
    }
    """
    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )


def require_roles(*allowed_roles: str):
    """
    Dependency for role-based access
    Usage:
    Depends(require_roles("HOSPITAL_ADMIN", "RECEPTIONIST"))
    """

    def role_checker(current_user: dict = Depends(get_current_user)):
        if current_user.get("role") not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not have permission to perform this action"
            )
        return current_user

    return role_checker
