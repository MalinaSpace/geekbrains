def div (a, b):
    a = float(a)
    b = float(b)
    if b != 0:
        return a / b
    else:
        return "Делить на ноль нельзя"

a = input("Введите делимое: ")
b = input("Введите делитель: ")

print(div(a, b))
