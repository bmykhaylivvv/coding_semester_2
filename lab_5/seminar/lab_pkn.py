class Person:
    def __init__(self):
        self.__name = None

    @property
    def get_name(self):
        return f'Name: ({self.__name})'

    @get_name.setter
    def set_name(self, name):
        self.__name = name

    name = property(get_name, set_name)


# Point: getter and setter for coordinates

person = Person()
person.name = 'Oleg'
print(person.name)