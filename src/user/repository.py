from src.dependencies.get_db import get_database, MongoDB
from fastapi import APIRouter, Depends
from src.user.schemas import UserPost
from bson import ObjectId
from utils.null_get import filter_user


async def db_create_user(user: UserPost, db: MongoDB):
    collection = db.db["users"]
    user_dict = user.dict()
    user_id = ObjectId() 
    user_dict['_id'] = str(user_id)  
    result = await collection.insert_one(user_dict)
    inserted_id = result.inserted_id
    inserted_user = await collection.find_one({"_id": inserted_id})
    
    if inserted_user:
        return inserted_user
    else:
        raise ValueError("User not found after insertion")


async def db_get_user(db: MongoDB):
    collection = db.db["users"]
    users = []
    async for user in collection.find():
        
        user = {
            "_id": str(user["_id"]),
            "name": user["name"],
            "cpf": user["cpf"],
            "notebook": {
            "tag_nb": user["tag_nb"],
            "modelo_nb": user["modelo_nb"],
            "num_serie_nb": user["num_serie_nb"],
            "versao_nb": user["versao_nb"],
            "configs_nb": user["configs_nb"],
            "observacao_nb": user["observacao_nb"]},
            "monitor_1": {
                "modelo_m1": user["modelo_m1"],
                "num_serie_m1": user["num_serie_m1"],
                "observacao_m1": user["observacao_m1"]
            },
            "monitor_2": {
                "modelo_m2": user["modelo_m2"],
                "num_serie_m2": user["num_serie_m2"],
                "observacao_m2": user["observacao_m2"]
            },
            "teclado": {
                "modelo_teclado": user["modelo_teclado"],
                "num_serie_teclado": user["num_serie_teclado"],
                "observacao_teclado": user["observacao_teclado"]
            },
            "mouse": {
                "modelo_mouse": user["modelo_mouse"],
                "num_serie_mouse": user["num_serie_mouse"],
                "observacao_mouse": user["observacao_mouse"]
            },
            "desktop": {
                "tag_desktop": user["tag_desktop"],
                "modelo_desktop": user["modelo_desktop"],
                "num_serie_desktop": user["num_serie_desktop"],
                "versao_desktop": user["versao_desktop"],
                "configs_desktop": user["configs_desktop"],
                "observacao_desktop": user["observacao_desktop"]
            },
            "acessorios": user["acessorios"],
            "suporte_notebook": user["suporte_notebook"],
            "mouse_pad": user["mouse_pad"],
            "no_break": {
                "modelo": user["modelo_no"],
                "num_serie": user["num_serie_no"]
            },
            "headset": {
                "modelo_headset": user["modelo_headset"],
                "num_serie_headset": user["num_serie_headset"]
            },
            "celular":{
                "modelo_cel": user["modelo_cel"],
                "imei_celular": user["imei_celular"],
                "numero_celular": user["numero_celular"],
                "observacao_celular": user["observacao_celular"]
            }
        }
        
        filter_user(user)
        
        users.append(user)
    
    return users