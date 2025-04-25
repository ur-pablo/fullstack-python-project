import typer
import uvicorn
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime, timedelta

app_cli = typer.Typer()

DB_URL = "mongodb://localhost:27017"
client = AsyncIOMotorClient(DB_URL)
db = client["mydatabase"]
flights = db["flights"]

@app_cli.command()
def start():
    """Inicia la aplicación FastAPI en modo desarrollo."""
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)

@app_cli.command()
def seed():
    """Carga datos de prueba en MongoDB."""
    sample_data = [
        {
            "icao24": "a1b2c3",
            "callsign": "LA100",
            "airline": "LATAM",
            "origin_airport": "SCEL",
            "destination_airport": "SPJC",
            "departure_time": datetime.utcnow(),
            "arrival_time": datetime.utcnow() + timedelta(hours=4),
            "position_history": []
        }
    ]

    async def do_seed():
        await flights.delete_many({})
        result = await flights.insert_many(sample_data)
        print(f"Seed completado. IDs insertados: {result.inserted_ids}")

    asyncio.run(do_seed())

@app_cli.command()
def clear_db():
    """Elimina todos los vuelos de la base de datos."""
    async def do_clear():
        result = await flights.delete_many({})
        print(f"Eliminados {result.deleted_count} documentos.")

    asyncio.run(do_clear())

if __name__ == "__main__":
    app_cli()
