class Matrix:
    def __init__(self, l):
        self.value = l

    def __str__(self):
        temp = ''
        for line in self.value:
            for j in line:
                temp = temp + str(j) + ' '
            temp = temp + '\n'
        return temp

    def __add__(self, other):
        new_list = []
        i = 0
        for line in self.value:
            j = 0
            temp = []
            for var in line:
                temp.append(var + other.value[i][j])
                j += 1
            new_list.append(temp)
            i += 1
        return Matrix(new_list)


list_of_lists = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]]
list_of_lists2 = [[10, 10, 10, 10],[10, 10, 10, 10],[10, 10, 10, 10]]

m = Matrix(list_of_lists)
m2 = Matrix(list_of_lists2)
print(m)

print(m + m2)