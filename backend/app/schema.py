import strawberry
from typing import List
from .mongo import collection
from strawberry.fastapi import GraphQLRouter

@strawberry.type
class Items:
    id: str
    airline: str
    arrivalTime: str
    callsign: str
    departureTime: str
    destinationAirport: str
    icao24: str
    originAirport: str
    positionHistory: List[str]

@strawberry.type
class Query:
    @strawberry.field
    async def items(self) -> List[Items]:
        docs = await collection.find().to_list(100)
        return [Items(
            id=str(doc["_id"]),
            airline=str(doc["airline"]),
            arrivalTime=str(doc["arrival_time"]),
            callsign=str(doc["callsign"]),
            departureTime=str(doc["departure_time"]),
            destinationAirport=str(doc["destination_airport"]),
            icao24=str(doc["icao24"]),
            originAirport=str(doc["origin_airport"]),
            positionHistory=list(doc["position_history"])) for doc in docs]

schema = strawberry.Schema(query=Query)
graphql_app = GraphQLRouter(schema)
