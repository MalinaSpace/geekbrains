class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    def __str__(self):
        return self.day_month_year

    @classmethod
    def convert(cls, day_month_year):
        date_list = []
        for i in day_month_year.split('-'):
            date_list.append(int(i))

        return date_list

    @staticmethod
    def valid(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 0 <= year <= 2020:
                    return "All right"
                else:
                    return "Wrong year"
            else:
                return "Wrong month"
        else:
            return "Wrong day"


date = Data('20-04-1999')
print(date)
print(Data.valid(-1, 22, 2022))
print(Data.valid(1, 22, 2022))
print(date.valid(1, 11, 2020))
print(Data.convert('01-12-2017'))
print(date.convert('20-04-1999'))

