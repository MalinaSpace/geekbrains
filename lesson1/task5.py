revenue = float(input("Введите сумму выручки: "))
costs = float(input("Введите сумму издержек: "))

if revenue > costs:
    print("Прибыль фирмы составила: ", revenue - costs)
    print("Рентабельность составляет: ", (revenue - costs)/revenue)
    num = int(input("Введите количество сотрудников: "))
    print("Прибыль в расчете на одного сотрудника составила: ", (revenue - costs)/num)
elif revenue < costs:
    print("Убыток фирмы составил: ", costs - revenue)
else:
    print("Фирма работает в ноль")
