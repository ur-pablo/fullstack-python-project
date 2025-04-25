from fastapi import FastAPI
from .schema import graphql_app
import uvicorn

app = FastAPI()

app.include_router(graphql_app, prefix="/graphql")

@app.get("/")
def root():
    return {"message": "Hello from FastAPI!"}

def start():
    """Start the FastAPI app using uvicorn (reload for dev)."""
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
