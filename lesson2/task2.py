def exchange (list):
    i = 0
    while i < len(list) - len(list) % 2:
        list[i], list[i + 1] = list[i + 1], list[i]
        i += 2
    print(list)

my_list = list(input("Введите через пробел элементы списка: ").replace(" ", ""))
print(my_list)
exchange(my_list)
