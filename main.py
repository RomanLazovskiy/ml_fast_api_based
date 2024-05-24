from fastapi import FastAPI, Query
from transformers import pipeline
from pydantic import BaseModel
from typing import List


class Item(BaseModel):
    text: str


class BatchItem(BaseModel):
    texts: List[str]


app = FastAPI()
classifier = pipeline("sentiment-analysis")


@app.get("/")
def root():
    return {"message": "Welcome to the Sentiment Analysis API"}


@app.post("/predict/")
def predict(item: Item):
    result = classifier(item.text)[0]
    return {"text": item.text, "sentiment": result["label"], "score": result["score"]}

@app.get("/predict/")
def predict_query(text: str = Query(..., min_length=1)):
    result = classifier(text)[0]
    return {"text": text, "sentiment": result["label"], "score": result["score"]}


@app.post("/predict_batch/")
def predict_batch(item: BatchItem):
    results = classifier(item.texts)
    return [{"text": text, "sentiment": result["label"], "score": result["score"]} for text, result in zip(item.texts, results)]

@app.get("/health/")
def health_check():
    return {"status": "OK"}
