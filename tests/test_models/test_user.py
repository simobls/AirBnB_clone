import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def test_init(self):
        user = User()
        self.assertIsInstance(user, User)
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)
