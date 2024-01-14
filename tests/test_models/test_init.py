import unittest
from models.engine.file_storage import FileStorage


class TestFileStorageInitialization(unittest.TestCase):
    def test_file_storage_instance_creation(self):
        storage = FileStorage()
        self.assertIsInstance(storage, FileStorage)
        self.assertEqual(storage._FileStorage__file_path, "file.json")
        self.assertIsInstance(storage._FileStorage__objects, dict)

    def test_reload_method(self):
        storage = FileStorage()
        # Assuming the file.json does not exist initially
        with self.assertRaises(FileNotFoundError):
            storage.reload()

        # Now create a dummy file.json for testing
        dummy_data = '{"BaseModel.123": {"id": "123", "name": "TestObject"}}'
        with open("file.json", "w") as dummy_file:
            dummy_file.write(dummy_data)

        # Reload after creating the dummy file
        storage.reload()
        self.assertTrue(storage._FileStorage__objects)
        self.assertIn("BaseModel.123", storage._FileStorage__objects)


if __name__ == '__main__':
    unittest.main()
