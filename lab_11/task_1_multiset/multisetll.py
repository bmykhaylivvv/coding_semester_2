'''
Module for Multiset class.
'''
from node import Node
from math import ceil

# A class implementing Multiset as a linked list.


class Multiset:
    '''
    Represents multiset.
    '''

    def __init__(self):
        """
        Produces a newly constructed empty Multiset.
        __init__: -> Multiset
        Field: _head points to the first node in the linked list
        """
        self._head = None

    def empty(self):
        """
        Checks emptiness of Multiset.
        empty: Multiset -> Bool
        :return: True if Multiset is empty and False otherwise.
        """
        return self._head == None

    def __contains__(self, value):
        """
        Checks existence of value in the Multiset.
        __contains__: Multiset Any -> Bool
        :param value: the value to be check.
        :return: True if Multiset is in the Multiset and False otherwise.
        """
        current = self._head
        while current != None:
            if current.item == value:
                return True
            else:
                current = current.next
        return False

    def add(self, value):
        """
        Adds the value to multiset.

        :param value: the value to be added.
        """
        if self._head is None:
            self._head = Node(value)
        else:
            rest = self._head
            self._head = Node(value)
            self._head.next = rest

    def delete(self, value):
        """

        :param value: value first occurrence of which should be deleted.
        """
        current = self._head
        previous = None
        while current is not None and current.item != value:
            previous = current
            current = current.next
        if current is not None:
            if previous is None:
                self._head = self._head.next
            else:
                previous.next = current.next

    @property
    def length(self):
        '''
        Returns length of linked list.
        '''
        length = 0
        current = self._head
        while current:
            length += 1
            current = current.next

        return length

    def remove_all(self) -> list:
        '''
        Remove all elements in linked list.
        '''
        deleted = []
        current = self._head
        while current:
            deleted.append(current.item)
            self._head = current.next
            current = current.next

        return deleted

    def split_half(self):
        '''
        Splits linked list into to two ones.
        '''
        length_1 = ceil(self.length/2)
        length_2 = self.length - length_1

        multiset_1 = Multiset()
        multiset_2 = Multiset()
        multiset_3 = Multiset()
        multiset_4 = Multiset()

        if self.length == 1:
            return None

        current = self._head

        for _ in range(length_1):

            multiset_1.add(current.item)
            current = current.next

        for _ in range(length_2):

            multiset_2.add(current.item)
            current = current.next

        current_3 = multiset_1._head
        for _ in range(length_1):

            multiset_3.add(current_3.item)
            current_3 = current_3.next

        current_4 = multiset_2._head
        for _ in range(length_2):

            multiset_4.add(current_4.item)
            current_4 = current_4.next

        return multiset_3, multiset_4

    def extend(self, second_list):
        '''
        Extends list with another one.
        '''
        extended_list = Multiset()

        reversed_self = Multiset()
        reversed_second = Multiset()

        current = self._head
        for _ in range(self.length):
            reversed_self.add(current.item)
            current = current.next

        current = second_list._head
        for _ in range(second_list.length):
            reversed_second.add(current.item)
            current = current.next

        current = reversed_self._head
        for _ in range(reversed_self.length):
            extended_list.add(current.item)
            current = current.next

        current = reversed_second._head
        for _ in range(reversed_second.length):
            extended_list.add(current.item)
            current = current.next

        return extended_list
