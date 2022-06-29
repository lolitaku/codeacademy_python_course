import unittest
from leap_year import get_leap_year

class TestLeapYear(unittest.TestCase):

    def test_if_leap_year(self):
        self.assert_Equal(True, get_leap_year(2000))
        self.assert_Equal(False, get_leap_year(1985))
