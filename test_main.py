# -*- coding: utf-8 -*-
"""Тесты."""

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    """Код ответа страницы."""

    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_predict_positive():
    """Код ответа и ответ модели положительного сообщения."""

    response = client.post("/predict/",
                           json={"text": "I like machine learning!"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['label'] == 'POSITIVE'


def test_predict_negative():
    """Код ответа и ответ модели отрицательного сообщения."""

    response = client.post("/predict/",
                           json={"text": "I hate machine learning!"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['label'] == 'NEGATIVE'


def test_valid_data():
    """Отправляем POST запрос с корректными данными."""

    response = client.post("/predict/", json={"text": "This is a positive sentence."})

    """Проверяем, что статус код ответа равен 200."""

    assert response.status_code == 200

    """Проверяем, что ответ содержит поле "label" с корректным значением."""

    assert "label" in response.json()
    assert response.json()["label"] in ["POSITIVE",
                                        "NEGATIVE"]  # Проверяем, что метка соответствует ожидаемым значениям

    """Проверяем, что ответ содержит поле "score" с корректным значением"""

    assert "score" in response.json()
    assert 0 <= response.json()["score"] <= 1  # Проверяем, что вероятность находится в корректном диапазоне