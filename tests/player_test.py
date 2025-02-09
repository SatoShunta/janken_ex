import unittest
from unittest.mock import patch
from source.player import pon

class TestPonFunction(unittest.TestCase):

    @patch('builtins.input', side_effect=['1'])
    def test_pon_input_1(self, mock_input):
        result = pon()
        self.assertEqual(result, 'グー')

    @patch('builtins.input', side_effect=['2'])
    def test_pon_input_2(self, mock_input):
        result = pon()
        self.assertEqual(result, 'チョキ')

    @patch('builtins.input', side_effect=['3'])
    def test_pon_input_3(self, mock_input):
        result = pon()
        self.assertEqual(result, 'パー')

    @patch('builtins.input', side_effect=['4', '2'])
    def test_pon_invalid_input(self, mock_input):
        result = pon()
        self.assertEqual(result, 'チョキ')

if __name__ == '__main__':
    unittest.main()
