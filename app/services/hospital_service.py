from app.repositories.hospital_repo import create_hospital, get_hospital_by_id


async def create_hospital_service(data: dict):
    return await create_hospital(data)


async def get_hospital_service(hospital_id: str):
    return await get_hospital_by_id(hospital_id)
