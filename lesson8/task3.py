class MyError:

    def __init__(self):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                var = int(input("Enter a value: "))
                self.my_list.append(var)
                print(f"Current list: {self.my_list}\n")
            except:
                print(f'Invalid value - string or boolean value')
                resume = input(f'Try again?(y/n): ')

                if resume == 'y':
                    continue
                else:
                    return f'Input completed'


e = MyError()
print(e.my_input())