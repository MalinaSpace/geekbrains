class ComplexNumber:
    def __init__(self, r, i):
        self.re = int(r)
        self.im = int(i)

    def __str__(self):
        if self.im > 0:
            return f'{self.re}+{self.im}i'
        elif self.im == 0:
            return f'{self.re}'
        else:
            return f'{self.re}{self.im}i'

    def __add__(self, other):
        return ComplexNumber(self.re + other.re, self.im + other.im)

    def __mul__(self, other):
        r = self.re * other.re - self.im * other.im
        i = self.re * other.im + self.im * other.re
        return ComplexNumber(r, i)

num1 = ComplexNumber(2, -3)
num2 = ComplexNumber(-1, 3)
print(num1)
print(num2)
print(num1 + num2)
print(num1 * num2)