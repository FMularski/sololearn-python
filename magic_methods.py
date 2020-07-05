class ComplexNumber:
    def __init__(self, re, im):
        self.re = re
        self.im = im

    def __repr__(self):
        return f'{self.re} + {self.im}i'

    def __add__(self, other):
        return ComplexNumber(self.re + other.re, self.im + other.im)

    def __sub__(self, other):
        return ComplexNumber(self.re - other.re, self.im - other.im)


n1 = ComplexNumber(2, 3)
print(n1)

n2 = ComplexNumber(5, 1)
print(n1 + n2)
print(n1 - n2)
