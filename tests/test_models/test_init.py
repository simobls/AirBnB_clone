import unittest
from models import storage
from models.engine.file_storage import FileStorage

class TestInit(unittest.TestCase):
    def test_storage_instance(self):
        # Create a unique FileStorage instance for your application
        storage_instance = storage._FileStorage__objects

        # Check that the storage instance is of the expected type
        self.assertIsInstance(storage_instance, dict)

        # Check that the storage instance is empty
        self.assertEqual(len(storage_instance), 0)

        # Call the reload() method on the storage instance
        storage.reload()

        # Check that the storage instance is not empty after reloading
        self.assertNotEqual(len(storage_instance), 0)

if __name__ == '__main__':
    unittest.main()
