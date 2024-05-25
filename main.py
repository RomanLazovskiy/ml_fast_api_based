from fastapi import FastAPI, Request
from transformers import pipeline
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

class Item(BaseModel):
    text: str



app = FastAPI()
classifier = pipeline("sentiment-analysis")

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=400,
        content={"detail": "Invalid request body"},
    )

@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/predict/")
def predict(item: Item):
    return classifier(item.text)[0]
