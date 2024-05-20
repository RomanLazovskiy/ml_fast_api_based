"""
main.py
FastApi based web interface
"""

__author__ = "UrFU team"
__copyright__ = "Copyright 2024, Planet Earth"


from fastapi import FastAPI
from pydantic import BaseModel

import ml_model


class Item(BaseModel):
    text: str


app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/predict/")
def predict(item: Item):
    classifier = ml_model.get_classifier()
    return classifier(item.text)[0]
