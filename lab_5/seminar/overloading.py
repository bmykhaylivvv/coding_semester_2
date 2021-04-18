class Numbers():
    def __init__(self, nominator, denominator):
        self.nominator = nominator
        self.denominator = denominator

    def add_number(self, another_number:int):
        self.nominator = self.denominator * another_number + self.nominator 

    def __add__(self, another_number):
        self.nominator = self.denominator * another_number + self.nominator

    def __mul__(self, number):
        if isinstance(number, Numbers):
            self.nominator *= number.nominator
            self.denominator *= number.denominator

        if isinstance(number, int):
            self.nominator *= number

    def __str__(self):
        return f'{self.nominator}/{self.denominator}'


number = Numbers(3, 5)
print(number)
# number.add_number(4)
# print(number)

number * 4

print(number)