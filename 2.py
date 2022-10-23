# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input("Enter N>> "))

_list = [i for i in range(2,n+1)]

res = [1]

for i in range(len(_list)):
    while n%_list[i] == 0:    
        res.append(_list[i])
        n = n / _list[i]

print(res)

