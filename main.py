from fastapi import Body, FastAPI
from pydantic import BaseModel

from services import predict_service


class Item(BaseModel):
    text: str = Body(
        embed=True,
        title="Text",
        description="""Text for analysis""",
    )


app = FastAPI()


@app.get("/", include_in_schema=False)
def root():
    return {"message": "Hello World"}


@app.post(
    "/predict/",
    summary="Make sentiment analysis",
    description="""Make sentiment analysis
         using sentiment-analysis HuggingFace model""",
)
def predict(item: Item):
    return predict_service.make_sentiment_analysis(item.text)
