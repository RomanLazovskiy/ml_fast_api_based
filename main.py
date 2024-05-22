from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette import status
from transformers import pipeline
from pydantic import BaseModel, Field


class Item(BaseModel):
    text: str = Field(min_length=1)


app = FastAPI()
classifier = pipeline("sentiment-analysis")


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.post("/predict/")
def predict(item: Item):
    return classifier(item.text)[0]


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request,
                                       exc: RequestValidationError):
    custom = list(
        map(lambda item: {"field": item['loc'][-1], "message": item['msg']},
            exc.errors()))
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder(
            {"validation_errors": custom, "body": exc.body}),
    )
