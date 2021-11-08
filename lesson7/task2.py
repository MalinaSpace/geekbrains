from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, v):
        self.v = v

    @property
    def consumption(self):
        return self.v / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def consumption(self):
        return 2 * self.h + 0.3

    def sum(self, list_s):
        temp = 0
        for suit in list_s:
            temp += suit.consumption
        return temp

c = Coat(48)
s1 = Suit(1.7)
s2 = Suit(1.65)
s3 = Suit(1.95)
list = [s1, s2, s3]

print(c.consumption)
print(s1.consumption)
print(s1.sum(list))

