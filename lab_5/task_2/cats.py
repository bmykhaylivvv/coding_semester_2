'''
Module for Animal class and Cat(Animal child) class.
'''


class Animal:
    '''
    Class represents an animal with its classification.
    '''

    def __init__(self, phylum, clas):
        '''
        Init class function.
        '''
        self.phylum = phylum
        self.clas = clas

    def __str__(self):
        '''
        Str class function.
        >>> animal1 = Animal("chordata", "mammalia")
        >>> print(animal1)
        <animal class is mammalia>
        '''
        return f'<animal class is {self.clas}>'

    def __eq__(self, other):
        '''
        Overloaded equality sign.
        >>> animal1 = Animal("chordata", "mammalia")
        >>> animal2 = Animal("chordata", "birds")
        >>> print(animal1 == animal2)
        False
        '''
        if self.phylum == other.phylum and self.clas == other.clas:
            return True
        return False


class Cat(Animal):
    '''
    Module represent a cat with its classification  .
    '''

    def __init__(self, phylum, clas, genus):
        '''
        Init class function.
        '''
        super().__init__(phylum, clas)
        self.genus = genus

    def sound(self):
        """
        Cat sound function.
        >>> cat1 = Cat("chordata", "mammalia", "felis")
        >>> cat1.sound()
        'Meow'
        """
        return "Meow"

    def __str__(self):
        '''
        Str class function.
        >>> cat1 = Cat("chordata", "mammalia", "felis")
        >>> print(cat1)
        <This felis animal class is mammalia>
        '''
        return f'<This {self.genus} animal class is {self.clas}>'

    def __eq__(self, other):
        '''
        Overloaded equality sign.
        >>> cat1 = Cat("chordata", "mammalia", "felis")
        >>> cat2 = Cat("chordata_test", "mammalia_test", "felis_test")
        >>> print(cat1 == cat2)
        False
        >>> cat1 = Cat("chordata", "mammalia", "felis")
        >>> cat2 = Cat("chordata", "mammalia", "felis")
        >>> print(cat1 == cat2)
        True
        '''
        if self.phylum == other.phylum and self.clas == other.clas and self.genus == other.genus:
            return True
        return False
