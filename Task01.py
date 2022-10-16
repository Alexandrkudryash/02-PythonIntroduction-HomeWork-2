# Домашнее задание-2
# Задача-1

# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11
    
n = input('введите число ' )
n2 = n.replace(',', '')
n3 = n2.replace('.', '')
#print(f'print n2 {n2}')
#print(f'print n3 {n3}')
n4 = list(n3)
#print(n4)
n5 = [int(i) for i in n4]
#print(n5)
sum = 0
for i in n5:
    sum = sum+i
print(f' - {n} -> {sum}')



