from os import environ

import beanie
import motor
from motor.motor_asyncio import AsyncIOMotorClient

from utils import logger

logger = logger.get_logger(__name__)

async def connect_to_mongo():
    try:
        client = AsyncIOMotorClient(environ.get("MONGO_URI"))
        beanie.init_model(client)
        logger.info("Connected to MongoDB")
    except Exception as e:
        logger.error(f"Error connecting to MongoDB: {e}")
        
async def close_mongo_connection():
    try:
        await beanie.close_connections()
        logger.info("Closed connection to MongoDB")
    except Exception as e:
        logger.error(f"Error closing connection to MongoDB: {e}")