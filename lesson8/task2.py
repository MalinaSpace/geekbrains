class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


def div(a, b):
    try:
        if b == 0:
            raise MyError("Произошло деление на ноль, результатом является бесконечность.")
    except MyError as mr:
        print(mr)
    else:
        print(a / b)


div(10, 0)
div(10, 5)
div(0, 10)
