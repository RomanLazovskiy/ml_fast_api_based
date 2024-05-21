import pytest
from fastapi.testclient import TestClient
from main import app
from typing import List

client = TestClient(app)

# Test Data
valid_text = "This is a fantastic product!"
invalid_text = ""  # Empty string for testing validation
keywords = ["fantastic", "great", "amazing"]

# Test Cases

# Root Endpoint Test
def test_read_root():
    """Tests the root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

# Sentiment Prediction Test (Valid Input)
def test_predict_valid_input():
    """Tests sentiment prediction with valid text"""
    response = client.post("/predict/", json={"text": valid_text})
    assert response.status_code == 200
    prediction = response.json()
    assert "label" in prediction
    assert "score" in prediction

# Sentiment Prediction Test (Invalid Input)
def test_predict_invalid_input():
    """Tests sentiment prediction with invalid (empty) text"""
    response = client.post("/predict/", json={"text": invalid_text})
    assert response.status_code == 422  # Expecting a validation error

# Keyword Classification Test (Valid Input)
def test_keyword_classification_valid_input():
    """Tests keyword classification with valid text and keywords"""
    response = client.post(
        "/keyword-classification/", 
        params={"text": valid_text, "keywords": keywords}
    )
    assert response.status_code == 200
    classification = response.json()
    assert "label" in classification
    assert "score" in classification

# Keyword Classification Test (Invalid Input)
@pytest.mark.parametrize("text, keywords", [
    (valid_text, []),  # Empty keywords list
    (invalid_text, keywords)  # Invalid (empty) text
])
def test_keyword_classification_invalid_input(text: str, keywords: List[str]):
    """Tests keyword classification with various invalid inputs"""
    response = client.post(
        "/keyword-classification/", 
        params={"text": text, "keywords": keywords}
    )
    assert response.status_code == 422  # Expecting a validation error

# Model Information Test
def test_model_info():
    """Tests the model information endpoint"""
    response = client.get("/model_info/")
    assert response.status_code == 200
    model_info = response.json()
    assert "model_name" in model_info
    assert "framework" in model_info
    assert "task" in model_info
