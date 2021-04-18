import unittest
from square_preceding import square_preceding


class TestSquare(unittest.TestCase):
    '''
    Class for testing square_preceding function.
    '''

    def setUp(self):
        '''
        Setting values for test.
        '''
        self.empty_list = []
        self.filled_list = [1, 2, 3]

    def test_preceding_empty_list(self):
        '''
        Check how function works with empty list.
        '''
        square_preceding(self.empty_list)
        self.assertEqual(self.empty_list, [], 'Check function logic while \
function works with empty list.')

    def test_preceding_filled_list(self):
        '''
        Check how function works with filled list.
        '''

        square_preceding(self.filled_list)
        self.assertEqual(self.filled_list, [0, 1, 4], 'Check function logic while \
function works with filled list.')


if __name__ == '__main__':
    unittest.main()
