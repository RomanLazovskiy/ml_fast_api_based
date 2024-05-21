from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    """
    Test case for the root endpoint ("/").

    It verifies that the root endpoint returns the expected message.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Sentiment Analysis API"}


def test_predict_positive():
    """
    Test case for predicting positive sentiment.

    It sends a POST request to the "/predict" endpoint with positive text
    and verifies the response.
    """
    response = client.post(
        "/predict",
        json={"text": "I like machine learning!"}
        )
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['prediction'] == 'POSITIVE'


def test_predict_negative():
    """
    Test case for predicting negative sentiment.

    It sends a POST request to the "/predict" endpoint with negative text
    and verifies the response.
    """
    response = client.post(
        "/predict",
        json={"text": "I hate machine learning!"}
        )
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['prediction'] == 'NEGATIVE'


def test_custom_endpoint():
    """
    Test case for the custom endpoint ("/custom").

    It sends a POST request to the "/custom" endpoint with custom text
    for analysis and verifies the response.
    """
    response = client.post(
        "/custom",
        json={"text": "Custom text for analysis"}
        )
    assert response.status_code == 200
    assert "result" in response.json()
