"""Модель анализа текста."""

from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel


class Item(BaseModel):
    """Опредлеяем тип для класса."""
    text: str


app = FastAPI()
classifier = pipeline("sentiment-analysis", 'distilbert/distilbert-base-uncased-finetuned-sst-2-english')


@app.get("/")
def root():
    """Основная страница с выводом сообщения."""

    return {"message": "Hello World"}


@app.post("/predict/")
def predict(item: Item):
    """Вторая страница с подключенной моделью."""

    return classifier(item.text)[0]
