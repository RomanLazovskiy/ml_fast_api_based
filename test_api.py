from fastapi.testclient import TestClient
from api import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_predict_positive():
    response = client.post("/predict/",
                           json={"text": "I like machine learning!"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data[0]['label'] == 'POSITIVE'


def test_predict_negative():
    response = client.post("/predict/",
                           json={"text": "I hate machine learning!"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data[0]['label'] == 'NEGATIVE'


def test_predict_separate():
    response = client.post("/predict/",
                           json={"text": "I like machine learning! "
                                         "I hate neural networks. "
                                         "The weather is good today!",
                                 "sep": True})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data[0]['label'] == 'POSITIVE'
    assert json_data[1]['label'] == 'NEGATIVE'
    assert json_data[2]['label'] == 'POSITIVE'
