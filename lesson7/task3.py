class Cell:

    def __init__(self, n):
        self.number = n

    def __str__(self):
        return "Количество клеток: {0}".format(self.number)

    def __add__(self, other):
        num = self.number + other.number
        return Cell(num)

    def __sub__(self, other):
        if self.number - other.number > 0:
            return Cell(self.number - other.number)
        else:
            return "Разность клеток меньше или равно нулю!"

    def __mul__(self, other):
        return Cell(self.number * other.number)

    def __truediv__(self, other):
        return Cell(round(self.number / other.number))

    def make_order(self, n):
        i = 1
        temp_str = ''
        for j in range(self.number):
            if i < n:
                temp_str += '*'
            else:
                temp_str += '*\n'
                i = 0
            i += 1
        return temp_str


c1 = Cell(100)
c2 = Cell(20)

print(c1 - c2)
print(c2 - c1)
print(c1 + c2)
print(c1 * c2)
print(c1 / c2)
print(c2 / c1)

print(c1.make_order(24))