from fastapi import FastAPI
from pydantic import BaseModel
from api import classifier


class Item(BaseModel):
    text: str
    sep: bool = True


app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/predict/")
def predict(item: Item):
    result = get_model_result(text=item.text, sep=item.sep)
    return result
