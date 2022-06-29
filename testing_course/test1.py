import unittest
from uzduotys import skaiciu_suma

class Testskaiciu_suma(unittest.TestCase):
    def test_skaiciu_suma(self):
        self.assertEqual(10, skaiciu_suma(2,5,3))
        self.assertEqual(-10, skaiciu_suma(-2, -2, -6))
        self.assertEqual(2, skaiciu_suma(-3, 5, 0))

    def test_saraso_suma(self):
        sarasas = [6, 0, 1, 5]
        sarasas1 = [0,-5, 6, 8]
        sarasas2 = []
        self.assertEqual(12, skaiciu_suma(sarasas))
        self.assertEqual(9, skaiciu_suma(sarasas1))
        self.assertEqual(0, skaiciu_suma(sarasas2))


if __name__ == "__main__":
    unittest.main()