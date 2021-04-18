# Method Resolution Order (MRO)

class A: 
    def __init__(self):
        print('A') 

class B(A):
    def __init__(self):
        print('B') 
        super().__init__()

class X(A):
    def __init__(self):
        print('X') 
        super().__init__()

class Forward(B, X):
    def __init__(self):
        print('Forward')
        super().__init__()

class Backward(X, B):
    def __init__(self):
        print('Backward')
        super().__init__()

x = Forward()

