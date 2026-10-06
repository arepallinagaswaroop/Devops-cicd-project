from main import app

client = app.test_client()

def test_home():
    r = client.get("/")
    assert r.status_code == 200
    assert "message" in r.get_json()

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.get_json()["status"] == "ok"

def test_not_found():
    assert client.get("/nope").status_code == 404