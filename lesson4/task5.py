from functools import reduce

def mult(prev_el, el):
    return prev_el * el

list = [i for i in range(100, 1001) if i % 2 == 0]

print(list)
print(reduce(mult, list))
