sentence = input("Введите несколько слов: ")

list_s = sentence.split()

i = 1
for element in list_s:
    print("{0}: {1:.10}".format(i, element))
    i += 1
