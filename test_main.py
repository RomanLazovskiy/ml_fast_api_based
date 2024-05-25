from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


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


def test_analytics():
    # Тест для проверки эндпоинта /analytics
    # Этот тест проверяет, правильно ли обновляются аналитические данные после предсказаний
    
    client.get("/")  # Убедимся, что сервер работает
    
    # Сделаем несколько положительных предсказаний
    client.post("/predict/", json={"text": "I love this product!"})
    client.post("/predict/", json={"text": "This is amazing!"})
    
    # Сделаем несколько отрицательных предсказаний
    client.post("/predict/", json={"text": "I hate this product!"})
    client.post("/predict/", json={"text": "This is terrible!"})

    # Получим аналитические данные
    response = client.get("/analytics")
    json_data = response.json()
    
    # Проверим, что статус ответа 200 и данные аналитики корректны
    assert response.status_code == 200
    assert json_data["total_reviews"] == 6
    assert json_data["positive_reviews"] == 3
    assert json_data["negative_reviews"] == 3
    assert json_data["positive_percentage"] == 50.0
    assert json_data["negative_percentage"] == 50.0
