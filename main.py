from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel


class Item(BaseModel):
    """
    Represents an item containing text for sentiment analysis.

    Attributes:
        text (str): The text to be analyzed for sentiment.
    """
    text: str


app = FastAPI()
classifier = pipeline("sentiment-analysis")


@app.get("/")
def root():
    """
    Root endpoint to check if the server is running.

    Returns:
        dict: A dictionary containing a welcome message.
    """
    return {"message": "Hello World"}


@app.post("/predict/")
def predict(item: Item):
    """
    Performs sentiment analysis on the provided text.

    Args:
        item (Item): A Pydantic model containing the text to be analyzed.

    Returns:
        dict: The sentiment analysis result from the Transformers pipeline.
              It typically includes labels (e.g., 'POSITIVE', 'NEGATIVE')
              and scores representing the confidence in the prediction.
    """
    return classifier(item.text)[0]
