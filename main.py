from fastapi import Body, FastAPI
from transformers import pipeline
from pydantic import BaseModel


class Item(BaseModel):
    text: str = Body(
        embed=True,
        title="Text",
        description="""Text for analysis""",
    )


app = FastAPI()
classifier = pipeline("sentiment-analysis")


@app.get("/", include_in_schema=False)
def root():
    return {"message": "Hello World"}


@app.post(
    "/predict/",
    response_model=Item,
    summary="Make sentiment analysis",
    description="""Make sentiment analysis
         using sentiment-analysis HuggingFace model""",
)
def predict(item: Item):
    return classifier(item.text)[0]
