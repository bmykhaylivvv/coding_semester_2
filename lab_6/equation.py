from typing import List
class Polynomial:
    def __init__(self, coeffs: List[int]):
        self.coeffs = coeffs

    def __str__(self):
        return f'Polynomial(coeffs={self.coeffs})'
    
    def degree(self):
        return self.coeffs[0]

    def coeff(self, coefficient):
        self.reversed_coeffs = list(reversed(self.coeffs))
        return self.reversed_coeffs[coefficient]

    def evalAt(self, x):
        self.reversed_coeffs = list(reversed(self.coeffs))
        res = 0
        for index, coeff in enumerate(self.reversed_coeffs):
            current_x = coeff * (x**index)
            res += current_x
        return res

    def __eq__(self, other):
        if isinstance(other, Polynomial):
            if self.coeffs == other.coeffs:
                return True

        # if isinstance(other, int):
            # if len(self.coeffs) == 1:
                # if self.coeff[0] == other:
                    # return True
# 
        return False







def testPolynomialEq():
    assert(Polynomial([1,2,3]) == Polynomial([1,2,3]))
    assert(Polynomial([1,2,3]) != Polynomial([1,2,3,0]))
    assert(Polynomial([1,2,3]) != Polynomial([1,2,0,3]))
    assert(Polynomial([1,2,3]) != Polynomial([1,-2,3]))
    assert(Polynomial([1,2,3]) != 42)
    assert(Polynomial([1,2,3]) != "Wahoo!")
    # A polynomial of degree 0 has to equal the same non-Polynomial numeric!
    assert(Polynomial([42]) == 42)


testPolynomialEq()