from itertools import count
from itertools import cycle

def int_num(start, stop):
    i = 1
    list = []
    for el in count(start):
        list.append(el)
        i += 1
        if i > stop - start + 1:
            break
    return list

def rep(list, iter):
    j = 1
    for el in cycle(list):
        print(el)
        j += 1
        if j > iter:
            break

list = int_num(-2, 3)
print(list)

rep(list, 12)