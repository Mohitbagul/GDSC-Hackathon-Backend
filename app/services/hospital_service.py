from app.repositories.hospital_repo import create_hospital, get_hospital_by_id, get_all_hospitals


async def create_hospital_service(data: dict):
    return await create_hospital(data)


async def get_hospital_service(hospital_id: str):
    return await get_hospital_by_id(hospital_id)


async def get_all_hospitals_service():
    return await get_all_hospitals()
