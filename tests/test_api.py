
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_forecast_endpoint():
    response = client.get("/forecast?date=2024-10-27T12:00:00")
    assert response.status_code == 200
    assert "pv_kw" in response.json()
