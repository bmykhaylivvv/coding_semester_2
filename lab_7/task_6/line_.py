class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


point1 = Point(3, 2)
point2 = Point(11, 4)


class Line:
    def __init__(self, points):
        self.points = points
        self.point_1 = points[0]
        self.point_2 = points[1]

    def create_line(self):
        k = (self.point_2.y - self.point_1.y)/(self.point_2.x - self.point_1.x)
        b = self.point_1.y - k*self.point_1.x
        line = (k, b)
        return line

    def intersect(self, line):
        self.line1 = Line(self.points).create_line()
        self.line2 = line.create_line()
        print(self.line1)
        print(self.line2)

        if self.line1[0] == self.line2[0] and self.line1[1] != self.line2[1]:
            return None

        if self.line1 == self.line2:
            return self

        if self.line1[0] != self.line2[0]:
            self.intersection_x = (
                self.line2[1] - self.line1[1])/(self.line1[0] - self.line2[0])
            self.intersection_y = self.line1[0] * \
                self.intersection_x + self.line1[1]
            return Point(self.intersection_x, self.intersection_y)


line1 = Line([Point(1, 3), Point(1, 1)])


# print(line1.intersect([Point(-1, 1), Point(1, 0)]))
a = line1.intersect(Line([Point(0, 1), Point(1, 1)]))
print(a.x)
print(a.y)
