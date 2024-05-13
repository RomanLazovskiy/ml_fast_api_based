[![Tests](https://github.com/tokarevsas31/ml_fastapi_tests/actions/workflows/python-app.yml/badge.svg)](https://github.com/tokarevsas31/ml_fastapi_tests/actions/workflows/python-app.yml)

# Project Title: FastAPI Sentiment Analysis

## Description

This project is a simple API for sentiment analysis of text data. It is built using FastAPI, a modern, fast (high-performance), web framework for building APIs with Python, based on standard Python type hints. The sentiment analysis is performed using the Hugging Face's Transformers library, specifically, a pre-trained sentiment analysis model.

## Endpoints

1. `/`: Root endpoint that returns a hello world message.
2. `/info/`: This endpoint provides information about the project.
3. `/predict/`: This is a POST endpoint that takes in a text string and returns the sentiment of the text. The sentiment is classified into 'positive' or 'negative'.

## Usage

To use the sentiment analysis API, you need to send a POST request to the `/predict/` endpoint with the text you want to analyze. The text should be sent in the request body as a JSON object with the key `text`.

## Running the Server

To run the server, use the following command:

`uvicorn main:app`.
