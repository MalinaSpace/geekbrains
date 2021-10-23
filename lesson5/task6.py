file = open("text_files/file6.txt", "r")

total = {}
subject = []
classes = []

i = 0
for line in file:
    classes.append(line.split())
    subject.append(classes[i].pop(0)[:-1])
    i += 1

for i in range(len(classes)):
    sum = 0
    for el in classes[i]:
        if el == "-":
            continue
        else:
            sum += int(el.split("(")[0])
    total[subject[i]] = sum

print(total)