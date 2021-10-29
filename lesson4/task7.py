def factorial(num):
    temp = 1
    for i in range(1, num + 1):
        temp *= i
        yield temp

n = 7
i = 1
for el in factorial(n):
    print("{0}! = {1}".format(i, el))
    i += 1