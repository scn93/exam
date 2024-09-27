# test_app.py

from fastapi.testclient import TestClient
from main import app

# Créer un client de test
client = TestClient(app)

# Définir un test pour le point de terminaison /status
def test_status():
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json() == {"message": "OK"}

# Définir un test pour le point de terminaison /chat
def test_post_chat():
    response = client.post("/chat", json={"prompt": "Hello, how are you?"})
    assert response.status_code == 200
    assert "response" in response.json()

