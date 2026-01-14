from fastapi import FastAPI
from app.api.v1.router import router as api_router

app = FastAPI(
    title="Hospital Management System",
    description="FastAPI + MongoDB Atlas Backend",
    version="1.0.0"
)

app.include_router(api_router)


@app.get("/")
async def root():
    return {"message": "Hospital Management System API is running"}
