class Store:
    storage = []

    @classmethod
    def accept(cls, goods):
        Store.storage.append(goods)


class Equipment:
    name = ''

    def __init__(self, model, price, amount):
        self.model = model
        self.price = price
        self.amount = amount
        self.set = {self.name: model, 'Цена': price, 'Количество': amount}

    def __str__(self):
        return f'{self.model} цена {self.price} количество {self.amount}'

    @classmethod
    def reception(cls):
        try:
            model = input('Введите модель: ')
            price = int(input('Введите цену товара: '))
            amount = int(input('Ведите количество: '))
        except:
            print('Ошибка ввода данных')

        q = input('Хотите продолжить?(д/н): ')
        if q == 'д' or q == 'Д':
            return Equipment.reception()
        else:
            return 'Выход'

    def transfer_to_store(self):
        Store.accept(self.set)

    def take_set(self):
        return self.set


class Printer(Equipment):
    name = 'Принтер'

    def __str__(self):
        return f'Модель принтера: {self.model}. Количество: {self.amount}. Цена: {self.price}'


class Scanner(Equipment):
    name = 'Сканер'

    def __str__(self):
        return f'Модель сканера: {self.model}. Количество: {self.amount}. Цена: {self.price}'


class Xerox(Equipment):
    name = 'Ксерокс'

    def __str__(self):
        return f'Модель ксерокса: {self.model}. Количество: {self.amount}. Цена: {self.price}'


p = Printer('HP', '5000', '15')
s = Scanner('Acer', '4000', '20')
x = Xerox('Samsung', '4500', '10')

store = Store()

for good in p, s, x:
    store.accept(good.take_set())

print(store.storage)
print(Equipment.reception())
