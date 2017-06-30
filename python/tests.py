""" Just run 'python tests.py' here.
"""
import unittest

from task import get_earliest_date, normalize_date


class TestConversion(unittest.TestCase):
    def test_values(self):
        self.assertEqual(normalize_date(2096, 2, 29), (2096, 2, 29))
        self.assertRaises(ValueError, normalize_date, 2096, 32, 39)
        self.assertRaises(ValueError, normalize_date, 2095, 2, 29)


class TestGetEarliestDate(unittest.TestCase):
    """ Test getting the earliest date function """
    def test_valid_values(self):
        """ Tests valid values """
        self.assertEqual(get_earliest_date('01/20/01'), '2001-1-20')
        # a leap year
        self.assertEqual(get_earliest_date('29/2096/02'), '2096-2-29')

    def test_invalid_values(self):
        """ Tests invalid values """
        self.assertRaises(ValueError, get_earliest_date, '1//01')
        self.assertRaises(ValueError, get_earliest_date, '12345/20/01')
        self.assertRaises(ValueError, get_earliest_date, '29/2095/02')
        self.assertRaises(ValueError, get_earliest_date, '2100/2000/01')
        self.assertRaises(ValueError, get_earliest_date, '210/200/01')


if __name__ == '__main__':
    unittest.main()
