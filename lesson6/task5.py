class Stationery:
    title = ""

    def __init__(self, t):
        self.title = t

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    title = "Ручка"

    def __init__(self):
        pass

    def draw(self):
        print("{0} рисует".format(self.title))


class Pencil(Stationery):
    title = "Карандаш"

    def __init__(self):
        pass

    def draw(self):
        print("{0} рисует".format(self.title))


class Handle(Stationery):
    title = "Маркер"

    def __init__(self):
        pass

    def draw(self):
        print("{0} рисует".format(self.title))

brush = Stationery("Кисть")
pen = Pen()
pencil = Pencil()
handle = Handle()

print(brush.title)
brush.draw()
pen.draw()
pencil.draw()
handle.draw()

