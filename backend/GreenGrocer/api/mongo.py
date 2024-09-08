from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

Mongo_url = os.getenv("MONGO_URL")

db_name = os.getenv("DB_NAME")

def get_mongo_client():
    client = MongoClient(Mongo_url)
    db = client[db_name]
    return db
