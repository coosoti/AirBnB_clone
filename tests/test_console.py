#!/usr/bin/python3
"""
module for testing console.py
"""

import unittest
import console
from console import HBNBCommand


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

    def test_module_class_methods_docstrings(self):
        """Test that module, class and methods have docstrings"""
        self.assertIsNotNone(console.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)

if __name__ == "__main__":
    unittest.main()
