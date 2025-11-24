from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from motor.motor_asyncio import AsyncIOMotorClient

app = FastAPI(title="Storage Service")
MONGO_URL = "mongodb://mongo:27017"
client = AsyncIOMotorClient(MONGO_URL)
db = client.llm_db
collection = db.history

class Record(BaseModel):
    prompt: str
    response: str
    timestamp: datetime = datetime.utcnow()

@app.get("/health")
def health():
    return {"storage": "ok"}

@app.post("/store")
async def store(record: Record):
    await collection.insert_one(record.dict())
    return {"status": "saved"}

@app.get("/records")
async def get_records():
    docs = []
    cursor = collection.find({})
    async for doc in cursor:
        doc["_id"] = str(doc["_id"])
        docs.append(doc)
    return docs
