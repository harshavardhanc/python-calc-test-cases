#test_calculator.py

import unittest
import calculator


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(1, 5), 6)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(5, 1), 4)


if __name__ == '__main__':
    unittest.main()
