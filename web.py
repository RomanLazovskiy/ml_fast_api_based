import streamlit as st
from transformers import pipeline

st.title('Анализ тональности текста')

classifier = pipeline("sentiment-analysis")

text = st.text_area(label='Введите текст:')

button = st.button('Анализ тональности')

if button:
    result = classifier(text)[0]
    st.write(f"{result.get('label')}: {result.get('score')}")
