class Point:
    def __init__(self):
        self._x = None
        self._y = None

    @property
    def coordinates(self):
        return f'Coordinates {(self._x, self._y)}'

    @coordinates.setter
    def coordinates(self, *args):
        x = args[0][0]
        y = args[0][1]
        self._x = x
        self._y = y


point = Point()
point.coordinates = [4, 5]
print(point.coordinates)