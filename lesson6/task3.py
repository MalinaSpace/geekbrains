class Worker:
    name = ""
    surname = ""
    position = ""
    _income = {}

    def __init__(self, n, s, p, wage, bonus):
        self.name = n
        self.surname = s
        self.position = p
        self._income["wage"] = wage
        self._income["bonus"] = bonus


class Position(Worker):

    def get_full_name(self):
        return self.name + " " + Worker.surname

    def get_total_income(self):
        return self._income["wage"] + Worker._income["bonus"]


w = Position("Alex", "Rott", "Doctor", 30000, 12000)

print(w.get_full_name())
print(w.position)
print(w.get_total_income())