class Person():
    def __init__(self):
        self._name = None

    def get_name(self):
        return f'Name: ({self._name})'
    def set_name(self, name):
        self._name = name

class Student(Person):
    def __init__(self):
        super().__init__()
        self._surname = None
    def set_name(self, name, surname):
        # super().set_name(name)
        self._surname = surname

    def get_name(self):
     return f'Name: {self._name}, surname: {self._surname}'


person = Student()
person.set_name('Oleg', 'Misko')
print(person.get_name())
print(person._surname) # bad practice, write getters (get_name)
