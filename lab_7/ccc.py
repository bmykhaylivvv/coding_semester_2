class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'Name: {self.name} | Surname: {self.surname}'


person1 = Person('Oleh', 'Tomson')
print(person1)    def __str__(self):
        return f'{self.numerator}/{self.denominator}'