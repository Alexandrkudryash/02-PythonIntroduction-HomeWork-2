# Домашнее задание-2
# Задача-4

# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#  Найдите произведение элементов на указанных позициях. 
#  Позиции хранятся в файле file.txt в одной строке одно число. < = данное условие в решении не исполнено (пока)

numN = int(input('Введите число N: '))
list = []
for i in range(-numN,numN+1):
     list.append(i)
print(list)
position1 = int(input('Укажите первую позицию цифры из списка, которую нужно перемножить: '))
position2 = int(input('Укажите вторую позицию цифры из списка, которую нужно перемножить: '))
print(f'Произведение чисел = {list[(position1-1)]*list[(position2-1)]}')
