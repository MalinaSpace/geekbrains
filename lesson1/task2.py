time = float(input("Введите время секундах: "))

h = time // 3600
m = (time - h * 3600) // 60
s = time % 60

print ("Формат вывода: 'часы : минуты : секунды'")
print(int(h), ":", int(m), ":", int(s))
