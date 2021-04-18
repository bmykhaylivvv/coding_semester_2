"""
Module for Classroom class
"""

from typing import List


class Classroom:
    """
    Class represent classrooms with all properties.
    """

    def __init__(self, number: int, capacity: int, equipment: List[str]):
        self.number = number
        self.capacity = capacity
        self.equipment = equipment

    def __str__(self):
        """
        Function return information about object.
        """
        return f"Classroom {self.number} has a capacity of {self.capacity}\
 persons and has the following equipment: {', '.join(self.equipment)}."

    def __repr__(self):
        """
        Return information depeneded on outer brackets.
        """
        return f"{type(self).__name__}('{self.number}', {self.capacity}, {self.equipment})"

    def is_larger(self, objct):
        """
        Function checks if capacity of the first classroom is bigger than second one.
        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_007 = Classroom('007', 12, ['TV'])
        >>> classroom_016.is_larger(classroom_007)
        True
        """
        if self.capacity > objct.capacity:
            return True
        return False

    def equipment_differences(self, objct):
        """
        Function return equipment in first classroom,
        which doesn`t exist in the second one.
        >>> classroom_016 = Classroom('016', 80, ['PC', 'projector', 'mic'])
        >>> classroom_007 = Classroom('007', 12, ['TV'])
        >>> classroom_016.equipment_differences(classroom_007)
        ['PC', 'projector', 'mic']
        """
        return [x for x in self.equipment if x not in objct.equipment]

import doctest
doctest.testmod()