from sys import argv

def salary(h, r, p):
    h, r, p = float(h), float(r), float(p)
    return(h * r + p)

if len(argv) == 4 :
    script_name, hours, rate, prize = argv

    print("Имя скрипта:", script_name)
    print("Выработка в часах:", hours)
    print("Ставка в час:", rate)
    print("Премия:", prize)

    print("\nЗарплата:", salary(hours, rate, prize))
else:
    print("Неверное количество аргументов")