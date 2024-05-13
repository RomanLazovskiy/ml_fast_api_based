from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline


class Item(BaseModel):
    text: str


app = FastAPI()
classifier = pipeline("sentiment-analysis")


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/info/")
def show_info():
    return {
        "message": "This model is designed "
                   "to determine the sentiment of the text"
    }


@app.post("/predict/")
def predict(item: Item):
    return classifier(item.text)[0]
