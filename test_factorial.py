import unittest
from DZ_Python_20 import factorial

class MyTestFactorial(unittest.TestCase):

    def test_Positive(self):
        self.assertEqual(factorial(5),120)

    def test_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_negative(self):
        self.assertRaises(factorial(-1), ValueError)

    def test_float(self):
        self.assertRaises(factorial(1.25), TypeError)


