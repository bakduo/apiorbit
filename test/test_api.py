
from app import app
import json

def test_healht_endpoint():
    with app.test_client() as client:
        resp = client.get("/health")
        data = json.loads(resp.data)
        assert resp.status_code == 200
        assert data["status"] == True
        
def test_orbit_endpoint():
    with app.test_client() as client:
        
        resp = client.post("/api/v1/orbit",json={
        "country":"ARG",
        "sat":"STARLINK-3185"})
        
        data = json.loads(resp.data)
        assert resp.status_code == 200
        assert data is not None
        
def test_sats_endpoint():
    with app.test_client() as client:
        
        resp = client.get("/api/v1/sats")
        data = json.loads(resp.data)
        assert resp.status_code == 200
        assert len(data["sats"]) > 5000