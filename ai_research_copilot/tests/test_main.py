from fastapi.testclient import TestClient
from ai_research_copilot.app.main import app
from unittest.mock import patch

client = TestClient(app)

def test_ping_endpoint():
    response = client.get("/ping")
    print(response.json())
    assert response.status_code == 200
    assert response.json() == {"status" : "ok"}

def test_ask_endpoint():
    with patch("ai_research_copilot.app.main.ask_gpt", return_value="mocked answer"):
        response = client.get("/ask", params={"prompt":"hello"})
        print(response.json())
        assert response.status_code == 200
        data = response.json()
        assert "answer" in data
        assert data["answer"] == "mocked answer"