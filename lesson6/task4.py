class Car:
    speed = 0
    color = None
    name = None
    is_police = False

    def __init__(self, c, n):
        self.color = c
        self.name = n

    def go(self, s):
        self.speed = s

    def stop(self):
        self.speed = 0

    def turn(self, direction):
        print("Машина повернула {0}".format(direction))

    def show_speed(self):
        print("Текущая скорость: {0}".format(self.speed))


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            print("Скорость превышена!")
        print("Текущая скорость: {0}".format(self.speed))


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            print("Скорость превышена!")
        print("Текущая скорость: {0}".format(self.speed))


class PoliceCar(Car):
    is_police = True

def chek(c):
    print("Машина {0} цвета - {1}, начинает движение".format(c.name, c.color))
    if c.is_police: print("Это полицейская машина")
    c.go(30)
    c.show_speed()
    c.turn("направо")
    c.go(45)
    c.show_speed()
    c.turn("налево")
    c.go(65)
    c.show_speed()
    c.stop()
    c.show_speed()
    print("\n")


chek(Car("черный", "KIA"))
chek(TownCar("желтый", "Lada"))
chek(SportCar("красный", "Chevrolet"))
chek(WorkCar("белый", "Audi"))
chek(PoliceCar("белый", "Ford"))