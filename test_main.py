from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "World"}


def test_predict_positive():
    response = client.post("/predict/", json={"text": "I like machine learning!"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data["label"] == "POSITIVE"


def test_predict_negative():
    response = client.post("/predict/", json={"text": "I hate machine learning!"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data["label"] == "NEGATIVE"


def test_predict_positive_weather():
    response = client.post("/predict/", json={"text": "The weather is beautiful today!"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data["label"] == "POSITIVE"


def test_predict_negative_weather():
    response = client.post("/predict/", json={"text": "The weather is terrible today!"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data["label"] == "NEGATIVE"


def test_predict_positive_food():
    response = client.post("/predict/", json={"text": "This pizza tastes amazing!"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data["label"] == "POSITIVE"


def test_predict_negative_food():
    response = client.post("/predict/", json={"text": "This pizza tastes awful!"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data["label"] == "NEGATIVE"


def test_predict_positive_weather_conditional():
    response = client.post("/predict/", json={"text": "The weather is nice today, if only it could stay like this."})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data["label"] == "POSITIVE"


def test_predict_negative_weather_sarcasm():
    response = client.post("/predict/", json={"text": "Oh, another rainy day..."})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data["label"] == "NEGATIVE"
