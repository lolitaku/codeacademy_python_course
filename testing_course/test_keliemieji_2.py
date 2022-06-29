import unittest
from keliamieji_2 import ar_keliamieji2
class TestKeliamieji(unittest.TestCase):
    def test_ar_keliamieji_2(self):
        self.assertEqual("Keliamieji", ar_keliamieji(2000))
        self.assertEqual("Keliamieji", ar_keliamieji(2020))
        self.assertEqual("Nekeliamieji", ar_keliamieji(2100))


if __name__ == "__main__":
    unittest.main()