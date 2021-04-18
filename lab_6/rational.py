'''
Module for work with rational numbers.
'''


class Rational:
    '''
    Represents rational number.
    '''

    def __init__(self, numerator, denominator):
        self.numerator = int(numerator)
        self.denominator = int(denominator)

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'

    def __add__(self, other):
        '''
        Overloading __add__ method for adding two rational numbers.
        '''
        self.common_denominator = int(self.denominator * other.denominator)
        self.common_numerator = int(int(self.numerator*self.common_denominator/self.denominator) + int(
            other.numerator*self.common_denominator/other.denominator))
        return Rational(self.common_numerator, self.common_denominator)

    def __sub__(self, other):
        '''
        Overloading __sub__ method for substracting two rational numbers.
        '''
        self.common_denominator = int(self.denominator * other.denominator)
        self.common_numerator = int(int(self.numerator*self.common_denominator/self.denominator) - int(
            other.numerator*self.common_denominator/other.denominator))
        return Rational(self.common_numerator, self.common_denominator)

    def __mul__(self, other):
        '''
        Overloading __mul__ method for multiplying two rational numbers.
        '''
        self.common_numerator = self.numerator * other.numerator
        self.common_denominator = self.denominator * other.denominator
        return Rational(self.common_numerator, self.common_denominator)

    def __truediv__(self, other):
        '''
        Overloading __truediv__ method for dividing two rational numbers.
        '''
        self.common_numerator = self.numerator * other.denominator
        self.common_denominator = self.denominator * other.numerator
        return Rational(self.common_numerator, self.common_denominator)


def test_rational():
    '''
    Functions for testing rational.py module.
    '''
    print("Testing class Rational ...")
    # This is an implementation of a Rational numbers
    # that consist of 2 parts - nominator and denominator.
    # You can imagine this Ratinal numbers as fractions
    # like 3/4
    rational1 = Rational(1, 4)
    assert (type(rational1) == Rational)
    assert (isinstance(rational1, Rational))
    assert (str(rational1) == "1/4")

    # here you can add two numbers
    rational2 = Rational(2, 5)
    assert (str(rational1 + rational2) == "13/20")

    # here is a substraction
    assert (str(rational1 - rational2) == "-3/20")

    # multiplication
    assert (str(rational1 * rational2) == "2/20")

    # division
    assert (str(rational1 / rational2) == "5/8")

    assert (type(rational1 + rational2) == Rational)
    assert (type(rational1 - rational2) == Rational)
    assert (type(rational1 * rational2) == Rational)
    assert (type(rational1 / rational2) == Rational)

    print("Done!")


if __name__ == '__main__':
    test_rational()
