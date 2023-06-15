

import unittest
import math_functions


class TestMathFunctions(unittest.TestCase):

    def test_add(self):
        result = math_functions.add(5, 6)
        self.assertEqual(result, 11)

    def test_subtract(self):
        result = math_functions.subtract(10,6)
        self.assertEqual(result , 4)

    def test_multiply(self):
        result = math_functions.multiply(5,6)
        self.assertEqual(result , 30)

    def test_divide(self):
        result = math_functions.divide(10,2)
        self.assertEqual(result , 5)

    def test_dividebyzero(self):
        with self.assertRaises(ValueError):
            math_functions.divide(1,0)

if __name__ == "__main__":
        unittest.main()






