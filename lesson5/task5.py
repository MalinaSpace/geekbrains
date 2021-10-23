import  random

file = open("text_files/file5.txt", "w+")

for _ in range(10):
    file.write(str(random.randint(1, 20)))
    file.write(" ")
file.seek(0)

sum = 0
for el in file.read().split():
    sum += int(el)

print(sum)