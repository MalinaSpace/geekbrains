file = open("text_files/file3.txt", "r")

str_dict = {}
sum = 0
i = 0
for line in file:
    temp_list = line.split()
    str_dict[temp_list[0]] = temp_list[1]
    sum += float(temp_list[1])
    i += 1

print("Средняя величина дохода сотрудников: {0}\n".format(sum / i))

new_dict = {x: y for x, y in str_dict.items() if float(y) < 20000}

print("Сотрудники имеющие оклад менее 20тыс.:")
for key, values in new_dict.items():
    print(key)