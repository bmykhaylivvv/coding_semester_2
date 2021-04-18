'''
Module for work with points, lines and interactions with them.
'''


class Point:
    '''
    Represents point oncoordinate plane.
    '''

    def __init__(self, x_coord, y_coord):
        self.x_coord = x_coord
        self.y_coord = y_coord

    def __eq__(self, other):
        return self.x_coord == other.x_coord and self.y_coord == other.y_coord


class LineEquation:
    '''
    Class for convenient reaching arguments of the equation.
    '''

    def __init__(self, a_coord, b_coord, c_coord):
        self.a_coord = a_coord
        self.b_coord = b_coord
        self.c_coord = c_coord


class Line:
    '''
    Represents line on the coordinate plane.
    '''

    def __init__(self, points):
        self.points = points
        self.point_1 = points[0]
        self.point_2 = points[1]

    def line_equation(self):
        '''
        Returns coordinates of line equation.
        '''
        self.a_coord = self.point_2.y_coord - self.point_1.y_coord
        self.b_coord = self.point_1.x_coord - self.point_2.x_coord
        self.c_coord = self.point_2.x_coord * self.point_1.y_coord - \
            self.point_1.x_coord * self.point_2.y_coord

        return LineEquation(self.a_coord, self.b_coord, self.c_coord)

    def intersect(self, line):
        '''
        Method which provide an oportunity to find point of intersection.
        '''
        self.line1 = Line(self.points).line_equation()
        self.line2 = line.line_equation()

        try:
            if (self.line2.a_coord * self.line1.b_coord == self.line1.a_coord * self.line2.b_coord
                and self.line2.a_coord * self.line1.c_coord == self.line1.a_coord *
                    self.line2.c_coord):
                return self

            self.x_intersection = (self.line1.b_coord * self.line2.c_coord - self.line2.b_coord *
                                   self.line1.c_coord)/(self.line1.a_coord *
                                                        self.line2.b_coord-self.line2.a_coord * self.line1.b_coord)

            self.y_intersection = (self.line2.a_coord * self.line1.c_coord - self.line1.a_coord *
                                   self.line2.c_coord)/(self.line1.a_coord * self.line2.b_coord -
                                                        self.line2.a_coord * self.line1.b_coord)

        except ZeroDivisionError:
            return None

        # self.intersection_point = (self.x_intersection, self.y_intersection)
        # return self.intersection_point
        return Point(self.x_intersection, self.y_intersection)
