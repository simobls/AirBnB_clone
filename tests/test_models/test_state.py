import unittest
from models.state import State

class TestState(unittest.TestCase):
    def test_init(self):
        state = State()
        self.assertIsInstance(state, State)
        self.assertIsInstance(state.name, str)
