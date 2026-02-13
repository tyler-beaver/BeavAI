from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_ask_endpoint():
    response = client.get("/ask", params={"prompt":"hello"})
    assert response.status_code == 200
    data = response.json()
    assert "answer" in data
    assert isinstance(data["answer"], str)