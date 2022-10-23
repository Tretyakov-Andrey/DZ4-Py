# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint


x = int(input('Enter lenght list>> '))

_list = []
for i in range(x):
    _list.append(randint(1, 20))
print(_list)

_list.sort()
res = []
for i in range(x):
    if i == 1:
        continue
    if _list[i] == _list[i-1]:
        continue
    else: res.append(_list[i])

print(res)