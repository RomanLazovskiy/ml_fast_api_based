[![Tests](https://github.com/tokarevsas31/ml_fastapi_tests/actions/workflows/python-app.yml/badge.svg)](https://github.com/tokarevsas31/ml_fastapi_tests/actions/workflows/python-app.yml)

# FastAPI Sentiment Analysis using the pretrained model


## Description

An example of English text tone detection. The sentiment analysis is performed using the [Hugging Face](https://huggingface.co/) Transformers library, specifically, a pre-trained sentiment analysis model.

### Launch

1. Clone this repository and navigate to the project folder
2. Install the necessary dependencies
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```
3. Launch the server
```
uvicorn main:app
```
4. The web application will be deployed at ```http://127.0.0.1:8000```
5. Requests:
    - `/`: Root GET-request returns a «Hello World» message
    - `/predict/` A POST-request accepts a text string and returns the sentiment of the text. The sentiment is categorized into "positive" or "negative"
6. Terminal usage
    - To use the sentiment analysis API, you need to send a POST-request to the `/predict/` endpoint with the text you want to analyze. The text must be sent in the request body as a JSON object with the `text` key.
```
curl -X 'POST' 'http://127.0.0.1:8000/predict/' -H 'Content-Type: application/json' -d '{"text":"YOUR TEXT"}
```
