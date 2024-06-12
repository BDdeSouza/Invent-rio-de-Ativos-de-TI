from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

#print(f"Loaded MONGODB_URI: {os.getenv('MONGODB_URI')}")
#print(f"Loaded DB_NAME: {os.getenv('DB_NAME')}")

class MongoDB:
    def __init__(self, uri: str, db_name: str):
        self.client = AsyncIOMotorClient(uri)
        self.db = self.client[db_name]

async def get_database() -> MongoDB:
    #uri = os.getenv("MONGODB_URI")
    #db_name = os.getenv("DB_NAME")

    uri = "mongodb://localhost:27017"
    db_name = "Inventario"
    
    # Debugging: Print the uri and db_name to verify their values
    print(f"URI: {uri}")
    print(f"DB Name: {db_name}")

    if not uri or not db_name:
        raise ValueError("MONGODB_URI and DB_NAME must be set")
    return MongoDB(uri, db_name)
