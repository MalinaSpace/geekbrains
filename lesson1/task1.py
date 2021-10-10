a, b = 4, 5
c = 2.5
str = 'Hello, dude!'

print(str)
print("4 + 5 =", a + b)
print("5 : 2,5 =", 5/2.5)

name = input("What is you name? - ")

print("Hi, %s\n" % name, "Do you want to do some math?")
x1 = float(input("Enter two values, please:\nx1 = "))
x2 = float(input("x2 = "))

print("Remainder of division x1:x2 =", int(x1 % x2))
print("Exponentiation x1^x2 =", x1 ** x2)

if x1 > x2:
    print(x1, ">", x2)
elif x1 < x2:
    print(x1, "<", x2)
else:
    print(x1, "=", x2)
