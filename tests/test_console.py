#!/usr/bin/python3
"""
module for testing console.py
"""

import console
from console import HBNBCommand
import unittest
import pep8
import inspect


class TestConsole(unittest.TestCase):
    """ unittest for console """
    @classmethod
    def setUpClass(cls):
        """set up class for the test"""
        cls.console = HBNBCommand()

    @classmethod
    def teardown(cls):
        """tears down the class at the end of the test"""
        del cls.console

    # testing for pep8 conformance
    def test_pep8_conformance_console(self):
        """ Test that console.py conforms to pep8 standard"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found conformance errors or warnings.")

    def test_pep8_conformance_test_console(self):
        """ Test that tests/test_console.py conforms to pep8 standard"""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_console.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found conformance errors or warnings.")

    # testing for documentation
    def test_module_and_class_and_functions_docstrings(self):
        """ Test for docstrings for module, classes and functions"""
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)

if __name__ == "__main__":
    unittest.main()
