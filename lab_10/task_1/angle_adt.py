'''
Module for coding encoding string into
'''


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
        >>> AngleADT.to_ascii_list('hello')
        [135.0, 180.0, 135.0, 112.5, 135.0, 270.0, 135.0, 270.0, 135.0, 337.5]
        '''

        move = 22.5

        final_ascii_list = []
        for char in word:
            ascii_list = list(hex(ord(char))[2:])
            res = []

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
        flattened_lst = [
            move*item for sublist in final_ascii_list for item in sublist]
        return flattened_lst

    @staticmethod
    def encode_message(message: str) -> list:
        '''
        Convert string to list with degrees of camera rotation.
        >>> AngleADT.encode_message('hello')
        [135.0, 45.0, -45.0, -22.5, 22.5, 135.0, -135.0, 135.0, -135.0, 202.5]
        '''
        ascii_list = AngleADT.to_ascii_list(message)
        coordinates = []

        coordinates.append(ascii_list[0])

        for position in range(0, len(ascii_list)-1):
            if ascii_list[position+1] - ascii_list[position] == 0.0:
                coordinates.append(360.0)
            else:
                coordinates.append(
                    ascii_list[position+1] - ascii_list[position])

        return coordinates
