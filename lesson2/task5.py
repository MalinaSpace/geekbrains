rank = [10, 9, 9, 7, 7, 5, 3]

new_el = int(input('Введите новый элемент рейтинга: '))

i = 0
for element in rank:
   if new_el <= element:
      i += 1

rank.insert(i, new_el)
print("Новый рейтинг: ", rank)
