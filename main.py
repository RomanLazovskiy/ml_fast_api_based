from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel
from typing import List

class Item(BaseModel):
    """Item model with a single text field"""
    text: str

class KeywordClassification(BaseModel):
    """Keyword classification result model"""
    label: str
    score: float

def classify_by_keywords(text: str, keywords: List[str]) -> KeywordClassification:
    """
    Classify text by keywords using a custom algorithm (TO DO: implement)

    Args:
        text (str): Input text to classify
        keywords (List[str]): List of keywords to classify by

    Returns:
        KeywordClassification: Classification result with label and score
    """
    # TO DO: implement keyword classification algorithm
    label = "POSITIVE"  # Replace with your classification definition
    score = 0.8  # Replace with your probability score
    return KeywordClassification(label=label, score=score)


app = FastAPI()
classifier = pipeline("sentiment-analysis")


@app.get("/")
def root() -> dict:
    """Root endpoint returning a hello world message"""
    return {"message": "Hello World"}


@app.post("/predict/")
def predict(item: Item) -> dict:
    """Predict sentiment of input text using the sentiment analysis pipeline"""
    return classifier(item.text)[0]


@app.post("/keyword-classification/")
def keyword_classification(text: str, keywords: List[str]) -> KeywordClassification:
    """Classify text by keywords using the custom algorithm"""
    result = classify_by_keywords(text, keywords)
    return result


@app.get("/model_info/")
def model_info() -> dict:
    """Return information about the sentiment analysis model"""
    return {
        "model_name": classifier.model.config._name_or_path,
        "framework": classifier.framework,
        "task": classifier.task,
    }
