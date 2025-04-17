import strawberry
from typing import List
from .mongo import collection
from strawberry.fastapi import GraphQLRouter

@strawberry.type
class Item:
    id: str
    name: str
    description: str

@strawberry.type
class Query:
    @strawberry.field
    async def items(self) -> List[Item]:
        docs = await collection.find().to_list(100)
        return [Item(id=str(doc["_id"]), name=doc["name"], description=doc["description"]) for doc in docs]

schema = strawberry.Schema(query=Query)
graphql_app = GraphQLRouter(schema)
