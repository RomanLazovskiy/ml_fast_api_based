[![Tests](https://github.com/tokarevsas31/ml_fastapi_tests/actions/workflows/python-app.yml/badge.svg)](https://github.com/tokarevsas31/ml_fastapi_tests/actions/workflows/python-app.yml)


# Практическое задание к модулю 2
#### Задание

- Создайте копию репозитория

- Улучшите приложение:

    - разработка новго метода API
    - создание нового теста
    - создание документации
    - исправление стиля кода

- Реализуйте прилодение в новой ветке

### Приложение

Было реализование приложение с помощью fastAPI с методом POST.

#### Запуск
1. Запустить терминал. Зайти в папку, где расположен файл `main.py`
2. Используй в консоли команду python `-m pip install -r requirements.txt` для установки необходимых библиотек
3. У вас дожен быь установлен `uvicorn`. (`pip install uvicorn`)
4. Введите в командной строке `uvicorn main:app`
5. Выведется что открылся на `http://127.0.0.1:8000`
6. Используйте в командной строке `curl -X 'POST' 'http://127.0.0.1:8000/predict/' -H 'Content-Type: application/json' -d '{"text":"I like machine learning!"}'`
"text": "Можно вводит произвольный текст"