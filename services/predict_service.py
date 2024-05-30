from transformers import pipeline


def make_sentiment_analysis(text: str):
    classifier = pipeline("sentiment-analysis")

    return classifier(text)[0]
