"""
Module for Triangle class
"""

from typing import List
from numbers import Number
import point

class Triangle:
    """
    Class represent Triangle-object.
    """

    def __init__(self, vertex1: List[point.Point], vertex2: List[point.Point], vertex3:
         List[point.Point]):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.vertex3 = vertex3

    def lines(point1, point2, point3) -> List:
        """
        Function find distances between 3 points.
        """
        dist1 = ((((point2.x - point1.x)**2) + ((point2.y-point1.y)**2))**0.5)
        dist2 = ((((point3.x - point2.x)**2) + ((point3.y-point2.y)**2))**0.5)
        dist3 = ((((point1.x - point3.x)**2) + ((point1.y-point3.y)**2))**0.5)

        return [dist1, dist2, dist3]

    def is_triangle(triangle) -> bool:
        """
        Function checks if it is a triangle from given points.
        >>> triangle = Triangle(point.Point(1,1), point.Point(3,1), point.Point(2,3))
        >>> triangle.is_triangle()
        True
        """
        lines = Triangle.lines(point1=triangle.vertex1,
                               point2=triangle.vertex2, point3=triangle.vertex3)
        if lines[0]+lines[1] > lines[2] and lines[0]+lines[2] > lines[1]\
                and lines[1]+lines[2] > lines[0]:
            return True

        return False

    def perimeter(triangle) -> Number:
        """
        Function returns the perimeter of triangle.
        >>> triangle = Triangle(point.Point(1,1), point.Point(3,1), point.Point(2,3))
        >>> triangle.perimeter()
        6.47213595499958
        """
        lines = Triangle.lines(point1=triangle.vertex1,
                               point2=triangle.vertex2, point3=triangle.vertex3)
        return lines[0] + lines[1] + lines[2]

    def area(triangle) -> Number:
        """
        Function returns the area of triangle.
        >>> triangle = Triangle(point.Point(1,1), point.Point(3,1), point.Point(2,3))
        >>> triangle.area()
        2.0
        """
        lines = Triangle.lines(point1=triangle.vertex1,
                               point2=triangle.vertex2, point3=triangle.vertex3)

        semi_periment = (lines[0] + lines[1] + lines[2])/2
        area = (semi_periment*(semi_periment-lines[0])*(semi_periment-lines[1]) *
                (semi_periment-lines[2]))**0.5

        return area
