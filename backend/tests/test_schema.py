from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_graphql_query():
    query = """
    query {
        items {
            id
            airline
            callsign
        }
    }
    """
    response = client.post("/graphql", json={"query": query})
    assert response.status_code == 200
    assert "data" in response.json()
    assert "items" in response.json()["data"]