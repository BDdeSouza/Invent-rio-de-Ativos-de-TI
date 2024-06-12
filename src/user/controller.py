from fastapi import APIRouter, Depends
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from src.dependencies.get_db import get_database
from src.user.schemas import *
from src.user.repository import db_create_user, db_get_user
from utils.verify_cpf import valida_cpf
from src.dependencies.get_db import MongoDB
from utils.user_null_values import verify_values
from utils.verify_delete import verify_delete_user


async def create_user(user: UserPost, db: MongoDB):
    if not valida_cpf(user.cpf):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid CPF")
    
    collection = db.db['users']
    user_dict = await collection.find_one({"cpf": user.cpf})
    if user_dict:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="CPF already exists\n"+str(user_dict))
    
    verify_values(user)
    
    return await db_create_user(user=user, db=db)


async def get_user_by_id(user_id: str, db: MongoDB):
    collection = db.db["users"]
    user = await collection.find_one({"_id": user_id})
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    return user


async def delete_user(user_id: str, db: MongoDB):
    collection = db.db["users"]
    user = await collection.find_one({"_id": user_id})
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    
    if not verify_delete_user(user):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User has dependencies")
    
    await collection.delete_one({"_id": user_id})
    return {"detail": "User deleted successfully"}


async def update_user(user_id: str, user: UserPost, db: MongoDB):
    collection = db.db["users"]
    user_dict = await collection.find_one({"_id": user_id})
    if not user_dict:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
     
    if not valida_cpf(user.cpf):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid CPF")
    
    user_dict = await collection.find_one({"cpf": user.cpf})
    if user_dict["cpf"] != user.cpf:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="CPF already exists")
    
    verify_values(user)
    
    await collection.update_one({"_id": user_id}, {"$set": user.dict()})
    return {"detail": "User updated successfully"} 