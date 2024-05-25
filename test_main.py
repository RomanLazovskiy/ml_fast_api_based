from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "World"}


def test_predict_positive():
    response = client.post("/predict/",
                           json={"text": "I like machine learning!"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['label'] == 'POSITIVE'


def test_predict_negative():
    response = client.post("/predict/",
                           json={"text": "I hate machine learning!"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['label'] == 'NEGATIVE'


def test_predict_empty_text():
    response = client.post("/predict/", json={"text": ""})
    assert response.status_code == 200
    result = response.json()
    # Предполагается, что пустой текст может возвращать определённый результат, это можно изменить по необходимости
    assert result["label"] in ["POSITIVE", "NEGATIVE"]
    assert result["score"] > 0.5


def test_predict_long_text():
    long_text = "This is a very long text. " * 100  # Генерируем длинный текст
    response = client.post("/predict/", json={"text": long_text})
    assert response.status_code == 200
    result = response.json()
    assert result["label"] in ["POSITIVE", "NEGATIVE"]
    assert result["score"] > 0.5
