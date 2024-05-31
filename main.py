from fastapi import FastAPI, Depends
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
from typing import List
from src.dependencies.get_db import get_database, MongoDB
from src.user.router import router as user_router

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}

app.include_router(user_router)

