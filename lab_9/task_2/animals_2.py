'''
Module which represent animals with their properties for ecosystem.
'''
import random


class Animal:
    '''
    Represent an animal.
    '''
    def __init__(self, gender=None, power=None):
        self.gender = random.choice([True, False])
        self.power = random.SystemRandom().uniform(1, 30)


class Fish(Animal):
    '''
    Represents a fish.
    '''

    def __init__(self, gender=None, power=None):
        super().__init__(gender, power)
        self.typo = 'Fish'

    def __str__(self):
        return 'F'


class Bear(Animal):
    '''
    Represents a bear.
    '''

    def __init__(self, gender=None, power=None):
        super().__init__(gender, power)
        self.typo = 'Bear'

    def __str__(self):
        return 'B'
