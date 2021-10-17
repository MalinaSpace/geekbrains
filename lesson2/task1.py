list = [10, 1.5, True, "string", complex(0, 1)]

i = 1
for val in list:
    print("Типой {0}-го элемента - {1}".format(i, type(val)))
    i += 1