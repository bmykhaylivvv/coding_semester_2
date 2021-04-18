"""
Module for AcademicBuilding class
"""

import collections


class AcademicBuilding:
    """
    Class represent classrooms (acamedic buildings) with all properties.
    """

    def __init__(self, address, classrooms):
        self.address = address
        self.classrooms = classrooms

    def __str__(self):
        """
        Function return information about object.
        """
        rooms = []
        for room in self.classrooms:
            rooms.append(str(room))
        rooms_str = "\n".join(rooms)
        return f"{self.address}\n{rooms_str}"

    def total_equipment(self):
        """
        Function return stock of equipment in classrooms.
        >>> classrooms = [classroom_016, classroom_007, classroom_008]
        >>> building = AcademicBuilding('Kozelnytska st. 2a', classrooms)
        >>> building.total_equipment()
        [('PC', 2), ('TV', 1), ('mic', 1), ('projector', 2)]
        """
        extended_lst = []
        stock = []
        for equip_lst in self.classrooms:
            extended_lst.extend(equip_lst.equipment)
        counted_lst = collections.Counter(extended_lst)
        for item in counted_lst.items():
            stock.append(item)

        return sorted(stock)

import doctest
doctest.testmod()
