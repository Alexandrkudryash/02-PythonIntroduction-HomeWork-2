# Домашнее задание-2
# Задача-5

# Реализуйте алгоритм перемешивания списка.

import random
list = ['Super', 'puper', 'ROKET', 'POCKET', 48.3, 150]
print(list)
for i in range(len(list)):
    index_a = random.randint(0, len(list) - 1)
    list[i], list[index_a]=list[index_a],list[i]
print(list)