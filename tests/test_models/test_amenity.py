import unittest
from models.amenity import Amenity
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """
    Test cases for the Amenity class
    """
    def test_attributes(self):
        """
        Test instantiation and attributes of Amenity class
        """
        amenity = Amenity()
        self.assertIsInstance(amenity.id, str)
        self.assertIsInstance(amenity.created_at, datetime)
        self.assertIsInstance(amenity.updated_at, datetime)
        self.assertEqual(amenity.name, "")

    def test_str(self):
        """
        Test string representation of Amenity class
        """
        amenity = Amenity()
        expected_str = "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__)
        self.assertEqual(str(amenity), expected_str)

    def test_to_dict(self):
        """
        Test to_dict method of Amenity class
        """
        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertEqual(amenity_dict['id'], amenity.id)
        self.assertEqual(amenity_dict['created_at'],
                         amenity.created_at.isoformat())
        self.assertEqual(amenity_dict['updated_at'],
                         amenity.updated_at.isoformat())
        self.assertEqual(amenity_dict['name'], amenity.name)

    def test_save(self):
        """
        Test save method of Amenity class
        """
        amenity = Amenity()
        prev_updated_at = amenity.updated_at
        amenity.save()
        new_updated_at = amenity.updated_at
        self.assertNotEqual(prev_updated_at, new_updated_at)
