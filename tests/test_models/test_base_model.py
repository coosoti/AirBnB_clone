#!/usr/bin/python3
""" unittest for BaseModel class"""

import pep8
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for base_model module and BaseModel class"""
    @classmethod
    def setUpClass(cls):
        """ set up base class"""
        base = BaseModel()

    @classmethod
    def teardown(cls):
        del base

    # test pep8 conformation
    def test_pep8_conformance_base_model(self):
        """ Test that base_model.py follows pep8 standardization"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found errors or warnings")

    def test_pep8_conformance_test_base_model(self):
        """ Test that test_base_model.py follows pep8 standardization"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_models/test_base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found errors or warnings")
