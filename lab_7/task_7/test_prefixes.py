import unittest
from all_prefixes import all_prefixes


class TestPrefixes(unittest.TestCase):
    '''
    Class for testing flower module.
    '''

    def test_empty_string(self):
        self.assertEqual(all_prefixes(''), set(),
                         'Check how your functions works with empty string')

    def test_all_lowercase(self):
        self.assertEqual(all_prefixes('lead'), {'lead', 'lea', 'l', 'le'}, 'Check how your function\
 works with word in lowercase')

    def test_all_uppercase(self):
        self.assertEqual(all_prefixes('LEAD'), {'lead', 'lea', 'l', 'le'}, 'Check how your function\
 works with word in uppercase')

    def test_lower_upper_case_string(self):
        self.assertEqual(all_prefixes('LeAd'), {'lead', 'lea', 'l', 'le'}, 'Check how your function\
 works with upper and lower case letters in sting at one time')

    def test_integer_string(self):
        self.assertEqual(all_prefixes('1234131'), {'12', '123413', '1234131', '131', '12341',
                                                   '1234', '1', '13', '123'}, 'Check how your function\
 works with integer numbers string')

    def test_integer(self):
        with self.assertRaises(TypeError):
            all_prefixes(123)


if __name__ == '__main__':
    unittest.main()
