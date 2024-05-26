from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel
from typing import Dict, Any

class Item(BaseModel):
    text: str

app = FastAPI()
classifier = pipeline("sentiment-analysis")

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.post("/predict/")
def predict(item: Item):
    return classifier(item.text)[0]

@app.post("/predict_proba/")
def predict_proba(item: Item) -> Dict[str, Any]:
    results = classifier(item.text)
    return {
        "label": results[0]['label'],
        "score": results[0]['score'],
        "details": results
    }

@app.get("/docs", include_in_schema=False)
def custom_docs():
    return app.openapi()
