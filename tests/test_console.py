#!/usr/bin/python3
"""
module for testing console.py
"""

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

if __name__ == "__main__":
    unittest.main()
