"""
streamlit_api.py
Streamlit based web interface
"""

__author__ = "UrFU team"
__copyright__ = "Copyright 2024, Planet Earth"

import streamlit as sl

import ml_model

sl.title("Определение тональности текста")

text = sl.text_input("Текст для анализа")


def exec_p():
    """
    Button calback. Will check text.
    """
    if text:
        classifier = ml_model.get_classifier()
        response = classifier(text)[0]
        sl.text(
            f"Тональность текста: {response['label']} Достоверность: {response['score']}"
        )
    else:
        sl.text("Пожалуйста, добавьте текст для анализа тональности")


button = sl.button("Проанализируй", on_click=exec_p)
