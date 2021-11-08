class Road:
    __length = 0
    __width = 0

    def __init__(self, l, w):
        Road.__length = float(l)
        Road.__width = float(w)

    def weight(self, d, h):
        return Road.__length * Road.__width * float(d) * float(h)

#Road length in meters
length = 20
#Road width in meters
width = 5000

r = Road(length, width)

#The surface density of road per square meter in kilo
surface_density = 25
#The heigth of the road coverage in cm
height = 5

print("The weight of the road is {0} tons.".format(r.weight(surface_density, height) / 1000))