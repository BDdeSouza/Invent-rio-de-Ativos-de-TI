from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os


load_dotenv()


class MongoDB:
    def __init__(self, uri: str, db_name: str):
        self.client = AsyncIOMotorClient(uri)
        self.db = self.client[db_name]


async def get_database() -> MongoDB:
    uri = os.getenv("MONGODB_URI")
    db_name = os.getenv("DB_NAME")
    return MongoDB(uri, db_name)
