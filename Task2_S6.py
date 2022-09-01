# Задача 2. Задан массив из случайных цифр на 15 элементов.
# На вход подаётся трёхзначное натуральное число. Напишите программу,
# которая определяет, есть в массиве последовательность из трёх элементов,
# совпадающая с введённым числом.
# [0, 5, 6, 2, 7, 7, 8, 1, 1, 9] - 277 -> да
# [4, 4, 3, 6, 7, 0, 8, 5, 1, 2] - 812 -> нет

import random

n = int(input("Введите число n: "))
my_list = []
for i in range(n):
    my_list.append(random.randint(1,10))
print(my_list)

k = int(input("Введите трехзначное число k: "))
mas = str(k)
length = len(my_list)-2

for i in range(length):
    x1 = str(my_list[i])
    x2 = str(my_list[i+1])
    x3 = str(my_list[i+2])
    num=x1+x2+x3
    if num == mas:
        print("совпадение есть")
