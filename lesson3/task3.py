def my_func(a, b, c):
    a, b, c = float(a), float(b), float(c)
    return a + b + c - min(a, b, c)

print(my_func(1, 3, 7))
