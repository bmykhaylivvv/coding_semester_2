'''
Module for coding encoding string into
'''

import ctypes


class DynamicArray:
    """A dynamic array class akin to a simplified Python list."""

    def __init__(self):
        """Create an empty array."""
        self._n = 0  # count actual elements
        self._capacity = 1  # default array capacity
        self._llarray = self._make_array(self._capacity)  # low-level array

    def __len__(self):
        """Return number of elements stored in the array."""
        return self._n

    def __getitem__(self, k):
        """Return element at index k."""
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._llarray[k]  # retrieve from array

    def append(self, obj):
        """Add object to end of the array."""
        if self._n == self._capacity:  # not enough room
            self._resize(2 * self._capacity)  # so double capacity
        self._llarray[self._n] = obj
        self._n += 1

    def _resize(self, capac):  # nonpublic utitity
        """Resize internal array to capacity capac."""
        bigger_array = self._make_array(capac)  # new (bigger) array
        for k in range(self._n):  # for each existing value
            bigger_array[k] = self._llarray[k]
        self._llarray = bigger_array  # use the bigger array
        self._capacity = capac

    @staticmethod
    def _make_array(capac):  # nonpublic utility
        """Return new array with capacity capac."""
        return (capac * ctypes.py_object)()  # see ctypes documentation

    def insert(self, k, value):
        """Insert value at index k, shifting subsequent values rightward."""
        # (for simplicity, we assume 0 <= k <= n in this verion)
        if self._n == self._capacity:  # not enough room
            self._resize(2 * self._capacity)  # so double capacity
        for j in range(self._n, k, -1):  # shift rightmost first
            self._llarray[j] = self._llarray[j - 1]
        self._llarray[k] = value  # store newest element
        self._n += 1

    def remove(self, value):
        """Remove first occurrence of value( or  raise ValueError)."""
        # note: we do not consider shrinking the dynamic array in this version
        for k in range(self._n):
            if self._llarray[k] == value:  # found a match!
                for j in range(k, self._n - 1):  # shift others to fill gap
                    self._llarray[j] = self._llarray[j + 1]
                self._llarray[self._n - 1] = None  # help garbage collection
                self._n -= 1  # we have one less item

                return  # exit immediately
        raise ValueError("value not found")  # only reached if no match

    # def __str__(self):
    #     res = ''
    #     for i in list(self):
    #         res += f'{str(i)} '

    #     return res


class AngleADT:
    '''
    Class for representing string into degrees of camera rotation.
    '''

    def __init__(self):
        pass

    @staticmethod
    def to_ascii_list(word: str) -> list:
        '''
        Convert string to list of hex values.
        '''

        move = 22.5

        final_ascii_list = DynamicArray()
        for char in word:
            ascii_list = list(hex(ord(char))[2:])
            res = DynamicArray()

            for num in ascii_list:
                try:
                    res.append(int(num))
                except ValueError:
                    if num == 'a':
                        res.append(10)
                    if num == 'b':
                        res.append(11)
                    if num == 'c':
                        res.append(12)
                    if num == 'd':
                        res.append(13)
                    if num == 'e':
                        res.append(14)
                    if num == 'f':
                        res.append(15)
            final_ascii_list.append(res)

        flattened_lst = DynamicArray()

        for chat_list in final_ascii_list:
            for char in chat_list:
                flattened_lst.append(char*move)
        # flattened_lst = [
        #     move*item for sublist in final_ascii_list for item in sublist]
        return flattened_lst

    @staticmethod
    def encode_message(message: str) -> list:
        '''
        Convert string to list with degrees of camera rotation.
        '''
        ascii_list = AngleADT.to_ascii_list(message)
        coordinates = DynamicArray()

        coordinates.append(ascii_list[0])

        for position in range(0, len(ascii_list)-1):
            if ascii_list[position+1] - ascii_list[position] == 0.0:
                coordinates.append(360.0)
            else:
                coordinates.append(
                    ascii_list[position+1] - ascii_list[position])

        return coordinates
