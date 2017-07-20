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

    def test_scanner_should_parse_file_to_standard_format(self):

        # Arrange
        parsed_result = [
            [1, 1, 'NEWLINE'],
            [2, 1, 'e'],
            [2, 2, 'x'],
            [2, 3, 'a'],
            [2, 4, 'm'],
            [2, 5, 'p'],
            [2, 6, 'l'],
            [2, 7, 'e'],
            [2, 8, 'NEWLINE'],
            [3, 1, 'SPACE'],
            [3, 2, 'SPACE'],
            [3, 3, 'SPACE'],
            [3, 4, 'SPACE'],
            [3, 5, 'a'],
            [3, 6, 'n'],
            [3, 7, 'o'],
            [3, 8, 't'],
            [3, 9, 'h'],
            [3, 10, 'e'],
            [3, 11, 'r'],
            [3, 12, 'SPACE'],
            [3, 13, 'o'],
            [3, 14, 'n'],
            [3, 15, 'e'],
            [3, 16, 'NEWLINE'],
            [4, 1, 'NEWLINE'],
            [5, 1, 'NEWLINE'],
            [6, 1, 'SPACE'],
            [6, 2, 'e'],
            [6, 3, 'x'],
            [6, 4, 'a'],
            [6, 5, 'm'],
            [6, 6, 'p'],
            [6, 7, 'l'],
            [6, 8, 'e'],
            [6, 9, 'SPACE'],
            [6, 10, '2'],
            [6, 11, 'NEWLINE'],
            [7, 1, 'NEWLINE'],
            [8, 1, 'TAB'],
            [8, 2, 's'],
            [8, 3, 'o'],
            [8, 4, 'm'],
            [8, 5, 'e'],
            [8, 6, 'SPACE'],
            [8, 7, 't'],
            [8, 8, 'a'],
            [8, 9, 'b'],
            [8, 10, 's'],
            [8, 11, 'SPACE'],
            [8, 12, 'TAB'],
            [8, 13, 'NEWLINE'],
            [9, 1, 'EOF'],
        ]

        # Act
        self.scanner.read_file(self.filename)

        # Assert
        self.assertEqual(self.scanner.parsed_data, parsed_result)

    def test_input_normalization(self):
        # Arrange
        check_table = {
            '\n': 'NEWLINE',
            ' ': 'SPACE',
            '\t': 'TAB',
            'a': 'a',
            '9': '9',
        }

        # Act & Assert
        for key, value in check_table.items():
            self.assertEqual(value, self.scanner.normalize(key))

    def test_scanner_should_return_next_element(self):
        # Arrange
        parsed_result = [
            [1, 1, 'NEWLINE'],
            [2, 1, 'e'],
        ]

        # Act
        self.scanner.read_file(self.filename)

        # Assert
        for element in parsed_result:
            self.assertEqual(self.scanner.next(), element)

    def test_scanner_should_return_next_and_prev_element(self):
        # Arrange
        parsed_next_result = [
            [1, 1, 'NEWLINE'],
            [2, 1, 'e'],
        ]

        parsed_prev_result = [
            [1, 1, 'NEWLINE'],
        ]

        # Act
        self.scanner.read_file(self.filename)

        # Assert
        for element in parsed_next_result:
            self.assertEqual(self.scanner.next(), element)

        for element in parsed_prev_result:
            self.assertEqual(self.scanner.prev(), element)
