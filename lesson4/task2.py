list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

new_list = [list[i] for i in range(len(list)) if i > 0 and list[i - 1] < list[i]]

print(new_list)
