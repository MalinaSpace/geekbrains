sum = 0
answer = True
while answer == True:
    str = input("Введите числа через пробел: ")
    list = str.split(" ")
    for var in list:
        if var == "n":
            answer = False
            break
        else:
            sum = sum + float(var)

    print(sum)
