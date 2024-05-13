[![Tests](https://github.com/tokarevsas31/ml_fastapi_tests/actions/workflows/python-app.yml/badge.svg)](https://github.com/tokarevsas31/ml_fastapi_tests/actions/workflows/python-app.yml)

# An example of ML Application with the pretrained model and test.

An example of English text tone detection with [Hugging Face](https://huggingface.co/) library.


Tests GitHub Actions

# Описание

Данный репозиторий представляет пример создания приложения по определению тональности текста

# Работа с приложением

1. Склонируйте данный репозиторий
2. Установите необходимые зависимости ```pip install -r requirements.txt```
3. Запустите веб-приложение ```uvicorn main:app```
4. Веб приложение будет развернуто по адресу ```http://localhost:8000```
5. Проект имеет две точки доступа:
    - при отправке GET-запроса по адресу ```/``` будет возвращен json с текстом «Hello World»
    - при отправке POST-запроса по адресу ```/predict/``` с передачей параметра «text»
     в теле запроса, в котором передается текст для определения тональности
