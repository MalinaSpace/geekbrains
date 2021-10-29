import time

class TrafficLight:
    __color = "red"

    def running(self):
        if TrafficLight.__color == "red":
            print(TrafficLight.__color)
            time.sleep(7)

            TrafficLight.__color = "yellow"
            print(TrafficLight.__color)
            time.sleep(2)

            TrafficLight.__color = "green"
            print(TrafficLight.__color)
            time.sleep(5)
        else:
           print("The color mode is broken! Try again.")

t = TrafficLight()
t.running()