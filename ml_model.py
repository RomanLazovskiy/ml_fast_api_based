"""
ml_mode.py
ml_model for sentiment-analysis
"""

__author__ = "UrFU team"
__copyright__ = "Copyright 2024, Planet Earth"


from transformers import pipeline

classifier = pipeline("sentiment-analysis")


def get_classifier():
    return classifier
