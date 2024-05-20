"""
test_unit.py
test ml_model
"""


__author__ = "UrFU team"
__copyright__ = "Copyright 2024, Planet Earth"


import unittest

import ml_model


class TestMlModel(unittest.TestCase):
    def test_positive(self):
        classifier = ml_model.get_classifier()
        response = classifier("I like machine learning!")[0]
        self.assertEqual(response["label"], "POSITIVE")

    def test_negative(self):
        classifier = ml_model.get_classifier()
        response = classifier("I like machine learning!")[0]
        self.assertEqual(response["label"], "NEGATIVE")
