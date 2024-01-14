import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    def test_init_new_instance(self):
        base = BaseModel()
        self.assertIsInstance(base.id, str)
        self.assertIsInstance(base.created_at, datetime)
        self.assertIsInstance(base.updated_at, datetime)
        self.assertIsNone(base.__dict__.get('__class__'))
        self.assertIsNone(base.__dict__.get('created_at'))
        self.assertIsNone(base.__dict__.get('updated_at'))

    def test_init_from_dict(self):
        data = {
            'id': str(uuid.uuid4()),
            'created_at': '2024-01-14T12:00:00.000000',
            'updated_at': '2024-01-14T13:30:00.000000',
            'custom_attribute': 'some_value'
        }
        base = BaseModel(**data)
        self.assertEqual(base.id, data['id'])
        self.assertAlmostEqual(base.created_at.isoformat(), data['created_at'], delta=datetime.timedelta(seconds=1))
        self.assertEqual(base.updated_at.isoformat(), data['updated_at'])
        self.assertIsNone(base.__dict__.get('__class__'))
        self.assertEqual(base.__dict__.get('custom_attribute'), 'some_value')

    def test_str_representation(self):
        base = BaseModel()
        expected_str = f"[{type(base).__name__}] ({base.id}) {base.__dict__}"
        self.assertEqual(str(base), expected_str)

    def test_save_method(self):
        base = BaseModel()
        prev_updated_at = base.updated_at
        base.save()
        self.assertNotEqual(prev_updated_at, base.updated_at)

    def test_to_dict_method(self):
        base = BaseModel()
        base_dict = base.to_dict()
        self.assertEqual(base_dict['__class__'], type(base).__name__)
        self.assertEqual(base_dict['created_at'], base.created_at.isoformat())
        self.assertEqual(base_dict['updated_at'], base.updated_at.isoformat())
        self.assertIn('id', base_dict)


if __name__ == '__main__':
    unittest.main()
