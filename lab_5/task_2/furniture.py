'''
Module for Furniture class and Chair(Furniture child) class.
'''


class Furniture:
    '''
    Class represents furniture with its properties.
    '''

    def __init__(self, style, assign):
        '''
        Init class function.
        '''
        self.style = style
        self.assign = assign

    def __str__(self):
        '''
        Str class function.
        >>> furniture1 = Furniture("empire", "bedroom")
        >>> print(furniture1)
        <furniture style is empire>
        '''
        return f'<furniture style is {self.style}>'

    def __eq__(self, other):
        '''
        Overloaded equality sign.
        >>> furniture1 = Furniture("empire", "bedroom")
        >>> furniture2 = Furniture("modern", "bathroom")
        >>> print(furniture1 == furniture2)
        False
        >>> furniture1 = Furniture("empire", "bedroom")
        >>> furniture2 = Furniture("empire", "bedroom")
        >>> print(furniture1 == furniture2)
        True
        '''
        if self.style == other.style and self.assign == other.assign:
            return True
        return False

    def get_assign(self):
        '''
        Returns assign(one of properties) of class.
        >>> furniture1 = Furniture("empire", "bedroom")
        >>> print(furniture1.get_assign())
        bedroom
        '''
        return self.assign


class Chair(Furniture):
    '''
    Class represent chair with its properties.
    '''

    def __init__(self, style, assign, tipe):
        '''
        Init class function.
        '''
        super().__init__(style, assign)
        self.tipe = tipe

    def __str__(self):
        '''
        Str class function.
        >>> chair1 = Chair("empire", "bedroom", "armchair")
        >>> print(chair1)
        <This armchair furniture style is empire>
        '''
        return f'<This {self.tipe} furniture style is {self.style}>'

    def __eq__(self, other):
        '''
        Overloaded equality sign.
        >>> chair1 = Chair("empire", "bedroom", "armchair")
        >>> chair2 = Chair("modern", "bedroom", "sofa")
        >>> print(chair1 == chair2)
        False
        >>> chair1 = Chair("empire", "bedroom", "armchair")
        >>> chair2 = Chair("empire", "bedroom", "armchair")
        >>> print(chair1 == chair2)
        True
        '''
        if self.style == other.style and self.assign == other.assign and self.tipe == other.tipe:
            return True
        return False
