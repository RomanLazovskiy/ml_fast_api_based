[![Tests](https://github.com/tokarevsas31/ml_fastapi_tests/actions/workflows/python-app.yml/badge.svg)](https://github.com/tokarevsas31/ml_fastapi_tests/actions/workflows/python-app.yml)

# An example of ML Application with the pretrained model and test.

An example of English text tone detection with [Hugging Face](https://huggingface.co/) library.

Tests GitHub Actions

# Requirements

To install the necessary libraries to work with the application, run the following command

```sh
pip install -r requirements.txt
```

# Streamlit web application

To run the web application, run the following command

```sh
streamlit run ./streamlit_web.py
```

# API

## API methods
- `root` (simple request to host) method returns "Hello world" string
- `predict` method returns label result of sentiment analisis
- `predict_score` method returns label result of sentiment analisis with score  

## Launch the API

To launch the API, run the command

```sh
uvicorn api:app
```

## Test request to the API 

To check the API functionality, use the command

```sh
curl -X 'POST' 'http://127.0.0.1:8000/predict/' -H 'Content-Type: application/json' -d '{"text": "It is a API predict!"}'
```