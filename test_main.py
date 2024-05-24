from fastapi.testclient import TestClient
from main import app  # Assuming your FastAPI app is in a file named 'main.py'

client = TestClient(app)


def test_read_main():
    """
    Tests the root ("/") endpoint to ensure it returns a 200 status code and
    the expected JSON message.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}  # Corrected expected message


def test_predict_positive():
    """
    Tests the sentiment prediction endpoint ("/predict/") with positive text
    to ensure it returns a 200 status code and a positive sentiment label.
    """
    response = client.post("/predict/", json={"text": "I like machine learning!"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['label'] == 'POSITIVE'


def test_predict_negative():
    """
    Tests the sentiment prediction endpoint ("/predict/") with negative text
    to ensure it returns a 200 status code and a negative sentiment label.
    """
    response = client.post("/predict/", json={"text": "I hate machine learning!"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['label'] == 'NEGATIVE'
