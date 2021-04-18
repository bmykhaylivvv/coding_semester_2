import unittest

from line import Point, LineEquation, Line

class TestLine(unittest.TestCase):
    '''
    Class for testing line module.
    '''

    def setUp(self):
        '''
        Setting values for test.
        '''
        self.line1 = Line([Point(0, 0), Point(1, 1)])
        self.line2 = Line([Point(0, 3), Point(2, 3)])

        self.line3 = Line([Point(0, 0), Point(1, 1)])
        self.line4 = Line([Point(0, 1), Point(-1, 0)])

        self.line5 = Line([Point(0, 0), Point(1, 1)])
        self.line6 = Line([Point(0, 0), Point(1, 1)])


    def test_intersection_exist(self):
        self.assertEqual(self.line1.intersect(self.line2), Point(3, 3), 'Check intersect function in case when\
 two lines have intersection point')

    def test_two_parallel(self):
        self.assertEqual(self.line3.intersect(self.line4), None, 'Check intersect function in case when\
 two lines have NO intersection point')

    def test_two_same_line(self):
        self.assertEqual(self.line5.intersect(self.line6), self.line5, 'Check intersect function in case when\
 two lines are the same')



if __name__ == '__main__':
    unittest.main()