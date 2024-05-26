[![Tests](https://github.com/tokarevsas31/ml_fastapi_tests/actions/workflows/python-app.yml/badge.svg)](https://github.com/tokarevsas31/ml_fastapi_tests/actions/workflows/python-app.yml)

# An example of ML Application with the pretrained model and test.

An example of English text tone detection with [Hugging Face](https://huggingface.co/) library.


Tests GitHub Actions

# Объяснение изменений
1. Новый метод API (/predict_proba/):

- Этот метод возвращает полную информацию о классификации, включая вероятности для каждого класса.
  
2. Новый тест (test_predict_proba):

- Проверяет новый метод API, чтобы убедиться, что он возвращает корректные данные.
  
3. Документация:

- Документация для всех методов автоматически генерируется FastAPI и доступна по адресу /docs.
  
4. Исправление стиля кода:

- Обновлены строки документации для методов.
- Классы и функции теперь следуют стандартам PEP 8.

# Заключение
Эти изменения улучшают функциональность приложения, добавляют новый полезный метод, обеспечивают его тестирование и поддерживают документацию, что делает приложение более надежным и удобным для использования.





