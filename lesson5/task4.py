file = open("text_files/file4.txt", "r")

trans_num = {
    "One": "Один", "Two": "Два",
    "Three": "Три", "Four": "Четыре"
}

dict_from_file = {}
for line in file:
    dict_from_file[line.split()[0]] = line.split()[2]

print({value: dict_from_file.get(key) for (key, value) in trans_num.items()})