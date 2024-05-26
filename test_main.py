from fastapi.testclient import TestClient
from main import app

cl = TestClient(app)


def test_read_main():
    r = cl.get("/")
    assert r.status_code == 200
    assert r.json() == {"message": "World"}


def test_predict_positive():
    r = cl.post("/predict/", json={"text": "I like machine learning!"})
    json_data = r.json()
    assert r.status_code == 200
    assert json_data["label"] == "POSITIVE"


def test_predict_negative():
    r = cl.post("/predict/", json={"text": "I hate machine learning!"})
    json_data = r.json()
    assert r.status_code == 200
    assert json_data["label"] == "NEGATIVE"


def test_predict_positive_weather():
    r = cl.post("/predict/", json={"text": "The weather is beautiful today!"})
    json_data = r.json()
    assert r.status_code == 200
    assert json_data["label"] == "POSITIVE"


def test_predict_negative_weather():
    r = cl.post("/predict/", json={"text": "The weather is terrible!"})
    json_data = r.json()
    assert r.status_code == 200
    assert json_data["label"] == "NEGATIVE"


def test_predict_positive_food():
    r = cl.post("/predict/", json={"text": "This pizza tastes amazing!"})
    json_data = r.json()
    assert r.status_code == 200
    assert json_data["label"] == "POSITIVE"


def test_predict_negative_food():
    r = cl.post("/predict/", json={"text": "This pizza tastes awful!"})
    json_data = r.json()
    assert r.status_code == 200
    assert json_data["label"] == "NEGATIVE"


def test_predict_positive_weather_conditional():
    r = cl.post("/predict/", json={"text": "The weather is nice today."})
    json_data = r.json()
    assert r.status_code == 200
    assert json_data["label"] == "POSITIVE"


def test_predict_negative_weather_sarcasm():
    r = cl.post("/predict/", json={"text": "Oh, another rainy day..."})
    json_data = r.json()
    assert r.status_code == 200
    assert json_data["label"] == "NEGATIVE"
