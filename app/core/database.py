
from pymongo.mongo_client import MongoClient
# from motor.motor_asyncio import AsyncIOMotorClient


# create database
mongo_details = "mongodb://localhost:27017"
client = MongoClient(mongo_details)
db = client.library_db


# create collection
collection = db["books"]


