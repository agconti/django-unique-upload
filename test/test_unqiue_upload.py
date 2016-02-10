import unittest
from uuid import UUID

from unique_upload import unique_upload


class TestUniqueUploadMethod(unittest.TestCase):

    def setUp(self):
        self.original_ext = 'jpg'
        self.filename = 'testfile.{}'.format(self.original_ext)

    def test_output_contains_uuid(self):
        new_name = unique_upload({}, self.filename)
        uuid, ext = new_name.split(".")
        validation_uuid = UUID(uuid, version=4)
        self.assertEqual(str(validation_uuid), uuid)

    def test_output_contains_original_extension(self):
        new_name = unique_upload({}, self.filename)
        uuid, ext = new_name.split(".")
        self.assertEqual(ext, self.original_ext)


if __name__ == '__main__':
    unittest.main()
