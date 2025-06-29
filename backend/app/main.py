from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
import os
import re
from pydantic import BaseModel

#MONGO-FASTAPI sadness
# from pydantic.v1.json import ENCODERS_BY_TYPE
from bson import ObjectId
from fastapi.encoders import ENCODERS_BY_TYPE

ENCODERS_BY_TYPE[ObjectId]=str

app = FastAPI()

# Allow all origins (for development only — lock down in production)
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MongoDB connection variables (you should use environment variables in production)
MONGO_USERNAME = os.getenv("MONGO_INITDB_ROOT_USERNAME")
MONGO_PASSWORD = os.getenv("MONGO_INITDB_ROOT_PASSWORD")
MONGO_HOST = os.getenv("MONGO_HOST")  # matches docker-compose service name
MONGO_PORT = os.getenv("MONGO_PORT")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")

MONGO_URI = f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/?authSource=admin"


# Create MongoDB client
@app.on_event("startup")
async def startup_db_client():
    app.mongodb_client = AsyncIOMotorClient(MONGO_URI)
    app.database = app.mongodb_client[MONGO_DB_NAME]

@app.on_event("shutdown")
async def shutdown_db_client():
    app.mongodb_client.close()

# Example route using MongoDB
@app.get("/")
async def read_root():

    test_collection = app.database.test

    stats = await app.database.command("ping")  # quick check that DB is working
    regex = re.compile("P")
    results = await test_collection.find({"ily":regex}).to_list(length=1)
    value = results[0]["ily"] if results else "Nobody"
    return {"Hello": "World", "value": value}

@app.get("/plusplus")
async def add_to_count():

    test_collection = app.database.test

    result = await test_collection.update_one(
        {"_id": "main_count"},  # filter: update the document with _id = "main_count"
        {"$inc": {"count": 1}},  # update count field
        upsert=True  # create the document if it doesn't exist
    )

    return {
        "message": "Count incremented",
        "matched": result.matched_count,
        "modified": result.modified_count
    }

@app.get("/getcount")
async def get_count():

    test_collection = app.database.test

    doc = await test_collection.find_one({"_id": "main_count"})

    return {
        "count": doc["count"] if doc else 0
    }


