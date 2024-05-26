[![Tests](https://github.com/tokarevsas31/ml_fastapi_tests/actions/workflows/python-app.yml/badge.svg)](https://github.com/tokarevsas31/ml_fastapi_tests/actions/workflows/python-app.yml)

# An example of ML Application with the pretrained model and test.

An example of English text tone detection with [Hugging Face](https://huggingface.co/) library.


Tests GitHub Actions

# Объяснение изменений:

# 1. Использование st.session_state:

- Проверяем, есть ли в st.session_state ключ sentences. Если нет, создаем его как пустой список.
- Это позволит сохранять введенные предложения между различными запросами пользователя.
  
# 2. Форма для ввода предложений:

- Используем st.form для создания формы, где пользователь может вводить предложения по одному.
- После ввода и нажатия на кнопку "Submit", предложение добавляется в st.session_state.sentences.
  
# 3. Кнопка для предсказания:

- Кнопка "Predict Emotions" инициирует предсказание на основе всех введенных предложений.
- Если предложений нет, выводится соответствующее сообщение.
  
# 4. Отображение введенных предложений:

- Отображаются все введенные предложения из st.session_state.sentences.

Таким образом, пользователи могут вводить предложения одно за другим, а затем нажать кнопку для получения предсказаний на основе всех введенных предложений.





