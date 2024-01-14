import unittest
from models.city import City

class TestCity(unittest.TestCase):
    def test_init(self):
        city = City()
        self.assertIsInstance(city, City)
        self.assertIsInstance(city.state_id, str)
        self.assertIsInstance(city.name, str)
