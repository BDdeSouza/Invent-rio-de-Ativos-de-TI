from src.dependencies.get_db import get_database, MongoDB
from fastapi import FastAPI, Depends, APIRouter
from src.user.schemas import UserPost
from src.user.controller import create_user, get_user_by_id, delete_user, update_user
from src.user.repository import db_get_user


router = APIRouter(
    prefix="/api/user",
    tags=["user"]
)


@router.post("/")
async def router_create_user(user: UserPost, db: MongoDB = Depends(get_database)):
    return await create_user(user, db)


@router.get("/")
async def router_get_user(db: MongoDB = Depends(get_database)):
    return await db_get_user(db)


@router.get("/{user_id}")
async def router_get_user_by_id(user_id: str, db: MongoDB = Depends(get_database)):
    return await get_user_by_id(user_id, db)


@router.delete("/{user_id}")
async def router_delete_user(user_id: str, db: MongoDB = Depends(get_database)):
    return await delete_user(user_id, db)

@router.put("/{user_id}")
async def router_update_user(user_id: str, user: UserPost, db: MongoDB = Depends(get_database)):
    return await update_user(user_id, user, db)