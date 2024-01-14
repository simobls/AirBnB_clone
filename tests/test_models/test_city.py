import unittest
from models.city import City
from datetime import datetime
import uuid


class TestCity(unittest.TestCase):
    def test_init_new_instance(self):
        city = City()
        self.assertIsInstance(city.id, str)
        self.assertIsInstance(city.created_at, datetime)
        self.assertIsInstance(city.updated_at, datetime)
        self.assertIsNone(city.__dict__.get('__class__'))
        self.assertIsNone(city.__dict__.get('created_at'))
        self.assertIsNone(city.__dict__.get('updated_at'))
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_init_from_dict(self):
        data = {
            'id': str(uuid.uuid4()),
            'created_at': '2024-01-14T12:00:00.000000',
            'updated_at': '2024-01-14T13:30:00.000000',
            'state_id': 'state123',
            'name': 'City1',
            'custom_attribute': 'some_value'
        }
        city = City(**data)
        self.assertEqual(city.id, data['id'])
        self.assertEqual(city.created_at.isoformat(), data['created_at'])
        self.assertEqual(city.updated_at.isoformat(), data['updated_at'])
        self.assertIsNone(city.__dict__.get('__class__'))
        self.assertEqual(city.state_id, 'state123')
        self.assertEqual(city.name, 'City1')
        self.assertEqual(city.__dict__.get('custom_attribute'), 'some_value')

    def test_str_representation(self):
        city = City()
        expected_str = f"[{type(city).__name__}] ({city.id}) {city.__dict__}"
        self.assertEqual(str(city), expected_str)

    def test_save_method(self):
        city = City()
        prev_updated_at = city.updated_at
        city.save()
        self.assertNotEqual(prev_updated_at, city.updated_at)

    def test_to_dict_method(self):
        city = City()
        city_dict = city.to_dict()
        self.assertEqual(city_dict['__class__'], type(city).__name__)
        self.assertEqual(city_dict['created_at'], city.created_at.isoformat())
        self.assertEqual(city_dict['updated_at'], city.updated_at.isoformat())
        self.assertIsNone(city_dict.get('id'))
        self.assertEqual(city_dict['state_id'], "")
        self.assertEqual(city_dict['name'], "")


if __name__ == '__main__':
    unittest.main()
