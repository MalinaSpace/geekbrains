my_file = open("text_files/file2.txt", "r")

list_of_lines = []
for line in my_file:
    list_of_lines.append(line.split(" "))

print("Number of lines: {0}".format(len(list_of_lines)))

i = 1
for string in list_of_lines:
    print("Number of words in {0} line: {1}".format(i, len(string)))
    i += 1
