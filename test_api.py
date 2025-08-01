from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bot OK"}

def test_action_endpoint():
    etat = {"ressource_proche": True}
    response = client.request("GET", "/action", json=etat)
    assert response.status_code == 200
    body = response.json()
    assert "move" in body
    assert "action" in body
    assert body["action"] == "COLLECT"