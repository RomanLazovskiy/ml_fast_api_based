from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel


class Item(BaseModel):
    text: str


app = FastAPI()
classifier = pipeline("sentiment-analysis")


@app.get("/")
def root():
    """Handler for a GET request to the root URL

    Returns:
        dict: Dictionary with "Hello World"
    """
    return {"message": "Hello World"}


@app.post("/predict/")
def predict(item: Item):
    """Handler for POST request to /predict/

    Args:
        item (Item): Item object containing text for sentiment analysis

    Returns:
        dict: Dictionary with predicted mood of the text
    """
    return classifier(item.text)[0]
