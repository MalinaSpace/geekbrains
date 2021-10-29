def int_func(word):
    word = word.capitalize()
    return word

sentence = input("Enter sentence: ")
temp_list = sentence.split(" ")
new_sentence = ""

for word in temp_list:
    new_sentence = new_sentence + int_func(word) + " "
new_sentence = new_sentence[:-1]

print(new_sentence)
