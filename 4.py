# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint


k = int(input("Задайте степень>> "))

_list = []

for i in range(k + 1):
    _list.append(randint(0, 100))
print(_list)

_pow = []

for i in range(k + 1):
    _pow.append(k - i)

str = ""

for i in range(k + 1):
    if _list[i] == 0:
        continue
    elif _pow[i] == 1:
        str += f"{_list[i]}x"
    elif _pow[i] == 0:
        str += f"{_list[i]}"
    else:
        str += f"{_list[i]}x^{_pow[i]}"

    if i - k != 0:
        str += " + "

str += " = 0"
print(str)

file = open("4.txt", "w")
file.write(str)
file.close()
