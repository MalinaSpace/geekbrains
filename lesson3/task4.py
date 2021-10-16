def my_func(x, y):
    x, y = float(x), int(y)
    return((1 / x) ** abs(y))

def my_func2(x, y):
    x, y = float(x), int(y)
    pow = 1
    for i in range(abs(y)):
        pow = pow * x
    return 1 / pow


print(my_func(2.5, -2))
print(my_func2(2.5, -2))

print(my_func(10, -4))
print(my_func2(10, -4))
