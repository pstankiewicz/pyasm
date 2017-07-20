import os
import unittest

from scanners import GenericScanner


class TestGenericScanner(unittest.TestCase):

    def setUp(self):
        self.scanner = GenericScanner()
        self.filename = os.path.join(os.path.dirname(__file__), "test_data_input.txt")

    def test_scanner_should_read_file(self):
        # Arrange
        with open(self.filename) as f:
            file_contents = f.read()

        # Act
        self.scanner.read_file(self.filename)

        # Assert
        self.assertEqual(self.scanner.data, file_contents)
