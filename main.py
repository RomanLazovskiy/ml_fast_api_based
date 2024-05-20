from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel


class Item(BaseModel):
    text: str

app = FastAPI()
classifier = pipeline("sentiment-analysis")

# Переменные для хранения количества положительных и отрицательных отзывов
positive_reviews_count = 0
negative_reviews_count = 0

@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/predict/")
def predict(item: Item):
    global positive_reviews_count, negative_reviews_count

    prediction = classifier(item.text)[0]
    if prediction['label'] == 'POSITIVE':
        positive_reviews_count += 1
    elif prediction['label'] == 'NEGATIVE':
        negative_reviews_count += 1
    
    return prediction

@app.get("/analytics")
def get_analytics():
    global positive_reviews_count, negative_reviews_count

    analytics_data = {
        "total_reviews": positive_reviews_count + negative_reviews_count,
        "positive_reviews": positive_reviews_count,
        "negative_reviews": negative_reviews_count,
        "positive_percentage": (positive_reviews_count / (positive_reviews_count + negative_reviews_count)) * 100 if positive_reviews_count + negative_reviews_count > 0 else 0,
        "negative_percentage": (negative_reviews_count / (positive_reviews_count + negative_reviews_count)) * 100 if positive_reviews_count + negative_reviews_count > 0 else 0
    }

    return analytics_data
