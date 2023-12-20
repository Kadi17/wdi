import unittest
from zadanie import number_ascii
from unittest.mock import patch

class TestNumberAscii(unittest.TestCase):
    @patch('builtins.input', return_value='aa0aaaaaa0a')
    def test_number_ascii(self, mock_input):
        result = number_ascii()
        self.assertEqual(result, 97)  # Sprawdzamy, czy zwrócona wartość jest poprawna dla podanego wejścia

if __name__ == '__main__':
    unittest.main()