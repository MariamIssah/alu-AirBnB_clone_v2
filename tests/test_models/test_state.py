import unittest
from models.state import State

class TestState(unittest.TestCase):
    """ Class to test the State model """

    def test_name_initialization(self):
        """ Test name attribute initialization with default value """
        new = State()
        self.assertEqual(type(new.name), str)
        self.assertEqual(new.name, "")  # Ensure it defaults to an empty string

    def test_name_assignment(self):
        """ Test name attribute when explicitly assigned """
        new = State(name="California")
        self.assertEqual(type(new.name), str)
        self.assertEqual(new.name, "California")  # Check the assigned value

    def test_name_none(self):
        """ Test name attribute when None is assigned """
        new = State(name=None)
        self.assertEqual(type(new.name), str)  # Should still be str
        self.assertEqual(new.name, "")  # Assuming we want None to default to an empty string

# You can add more tests for other attributes and methods
