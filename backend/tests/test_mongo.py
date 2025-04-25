import pytest
from motor.motor_asyncio import AsyncIOMotorClient

@pytest.fixture
def mongo_client():
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    yield client
    client.close()

@pytest.mark.asyncio
async def test_mongo_connection(mongo_client):
    db = mongo_client["test_database"]
    collection = db["test_collection"]
    await collection.insert_one({"test_key": "test_value"})
    doc = await collection.find_one({"test_key": "test_value"})
    assert doc["test_key"] == "test_value"
    await collection.drop()