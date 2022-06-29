import unittest
from calculator_pagrindinis import add, subtract, multiply, devide

class Testcalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(4, add(2, 2))
        self.assertEqual(-4, add(-2, -2))


    def test_subtract(self):
        self.assertEqual(10, subtract(20, 10))
        self.assertEqual(40, subtract(45, 5))

    def test_multiply(self):
        self.assertEqual(4, multiply(-2, -2))
        self.assertEqual(9, multiply(3, 3))

    def test_devide(self):
        self.assertEqual(1, devide(-2, -2))
        self.assertEqual(10, devide(100, 10))
        self.assertRaises(ZeroDivisionError, devide, 5, 0)


if __name__ == "__main__":
    unittest.main()