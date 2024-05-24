from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Sentiment Analysis API"}


def test_predict_positive():
    response = client.post("/predict/",
                           json={"text": "I like machine learning!"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['sentiment'] == 'POSITIVE'


def test_predict_negative():
    response = client.post("/predict/",
                           json={"text": "I hate machine learning!"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['sentiment'] == 'NEGATIVE'


def test_predict_batch():
    response = client.post("/predict_batch/",
                           json={"texts": ["I love FastAPI!", "I dislike bugs."]})
    json_data = response.json()
    assert response.status_code == 200
    assert len(json_data) == 2
    assert json_data[0]['sentiment'] == 'POSITIVE'
    assert json_data[1]['sentiment'] == 'NEGATIVE'


def test_predict_query_positive():
    response = client.get("/predict/?text=I+enjoy+coding")
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['sentiment'] == 'POSITIVE'


def test_predict_query_negative():
    response = client.get("/predict/?text=I+hate+bugs")
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['sentiment'] == 'NEGATIVE'


def test_predict_query_invalid():
    response = client.get("/predict/?text=")
    assert response.status_code == 422


def test_health_check():
    response = client.get("/health/")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}
