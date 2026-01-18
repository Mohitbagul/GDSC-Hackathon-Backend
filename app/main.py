from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.router import router as api_router
import os

app = FastAPI(
    title="Hospital Management System",
    description="FastAPI + MongoDB Atlas Backend",
    version="1.0.0"
)

frontend_url = os.getenv("FRONTEND_URL")

# ✅ ADD THIS BLOCK
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        # "http://localhost:5173",
        # "http://127.0.0.1:5173",
        frontend_url
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)


@app.get("/")
async def root():
    return {"message": "Hospital Management System API is running"}
